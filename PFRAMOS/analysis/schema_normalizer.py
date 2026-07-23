"""Normalise historical Imperial BBO CSV schema variants.

Supported input forms:
- packed coordinates in Input, Query, Coordinates or input_values
- split coordinates in Input_1 to Input_8
- function labels such as F1 or Function 1
- leading blank lines before CSV headers

The module never invents missing observations.
"""

from __future__ import annotations

import csv
import io
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Dict, List, Sequence


EXPECTED_DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}


def normalise_function(value: str) -> int:
    cleaned = value.strip().lower().replace("function", "").replace("f", "").strip()
    number = int(cleaned)
    if number not in EXPECTED_DIMENSIONS:
        raise ValueError(f"Unsupported function label: {value}")
    return number


def _read_nonblank_csv(path: Path) -> tuple[Sequence[str], List[Dict[str, str]]]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    reader = csv.DictReader(io.StringIO("\n".join(lines)))
    return tuple(reader.fieldnames or ()), list(reader)


def _column_map(fieldnames: Sequence[str]) -> Dict[str, str]:
    return {name.strip().lower(): name for name in fieldnames if name is not None}


def _normalise_number(value: str) -> str:
    try:
        return format(Decimal(value.strip()), "f")
    except InvalidOperation as error:
        raise ValueError(f"Invalid numeric value: {value}") from error


def _normalise_coordinates(values: Sequence[str], expected: int) -> List[str]:
    cleaned = [value.strip() for value in values if value is not None and value.strip()]
    if len(cleaned) != expected:
        raise ValueError(f"Expected {expected} coordinates, found {len(cleaned)}")
    result: List[str] = []
    for value in cleaned:
        number = Decimal(value)
        if number < 0 or number > 1:
            raise ValueError(f"Coordinate outside [0,1]: {value}")
        result.append(f"{number:.6f}")
    return result


def load_inputs(path: Path) -> Dict[int, List[str]]:
    fieldnames, rows = _read_nonblank_csv(path)
    mapping = _column_map(fieldnames)
    function_column = next(
        (mapping[name] for name in ("function", "function_id", "objective") if name in mapping),
        None,
    )
    if function_column is None:
        raise ValueError(f"No recognised function column in {path}: {fieldnames}")

    packed_column = next(
        (
            mapping[name]
            for name in ("input", "query", "coordinates", "input_values")
            if name in mapping
        ),
        None,
    )
    split_columns = [
        mapping[f"input_{index}"]
        for index in range(1, 9)
        if f"input_{index}" in mapping
    ]

    if packed_column is None and not split_columns:
        raise ValueError(f"No recognised input coordinate columns in {path}: {fieldnames}")

    result: Dict[int, List[str]] = {}
    for row in rows:
        function = normalise_function(row[function_column])
        if function in result:
            raise ValueError(f"Duplicate Function {function} in {path}")
        if packed_column is not None:
            packed = row.get(packed_column, "").strip().strip('"')
            separator = "," if "," in packed else "-"
            values = packed.split(separator)
        else:
            values = [row.get(column, "") for column in split_columns]
        result[function] = _normalise_coordinates(values, EXPECTED_DIMENSIONS[function])

    if set(result) != set(EXPECTED_DIMENSIONS):
        raise ValueError(f"Incomplete input data in {path}")
    return result


def load_results(path: Path) -> Dict[int, str]:
    fieldnames, rows = _read_nonblank_csv(path)
    mapping = _column_map(fieldnames)
    function_column = next(
        (mapping[name] for name in ("function", "function_id", "objective") if name in mapping),
        None,
    )
    value_column = next(
        (mapping[name] for name in ("output", "result", "value") if name in mapping),
        None,
    )
    if function_column is None or value_column is None:
        raise ValueError(f"Unrecognised result schema in {path}: {fieldnames}")

    result: Dict[int, str] = {}
    for row in rows:
        function = normalise_function(row[function_column])
        if function in result:
            raise ValueError(f"Duplicate Function {function} in {path}")
        result[function] = _normalise_number(row[value_column])

    if set(result) != set(EXPECTED_DIMENSIONS):
        raise ValueError(f"Incomplete result data in {path}")
    return result
