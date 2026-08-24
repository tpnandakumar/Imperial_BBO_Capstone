from decimal import Decimal, getcontext

getcontext().prec = 40

# Verified late-round evidence used for the counterfactual extension.
# No outputs beyond Round 13 are created or inferred.

F2_X = [Decimal('0.695000'), Decimal('0.690000'), Decimal('0.685000')]
F2_Y = [
    Decimal('0.5848554940277205'),
    Decimal('0.7335252043269003'),
    Decimal('0.6413430885133908'),
]


def quadratic_vertex_from_three_points(xs, ys):
    """Return the vertex x-coordinate for the unique quadratic through three points."""
    x1, x2, x3 = xs
    y1, y2, y3 = ys

    # Divided differences preserve the calculation in Decimal arithmetic.
    d12 = (y2 - y1) / (x2 - x1)
    d23 = (y3 - y2) / (x3 - x2)
    a = (d23 - d12) / (x3 - x1)
    b = d12 - a * (x1 + x2)

    if a == 0:
        return None
    return -b / (Decimal('2') * a)


f2_vertex = quadratic_vertex_from_three_points(F2_X, F2_Y)

candidates = {
    'F1': '0.600000-0.600000',
    'F2': f'{f2_vertex.quantize(Decimal("0.000001"))}-0.950000',
    'F3': '0.860000-0.140000-0.860000',
    'F4': '0.600000-0.430000-0.420000-0.250000',
    'F5': '0.080000-1.000000-1.000000-1.000000',
    'F6': '0.700000-0.200000-0.700000-0.700000-0.200000',
    'F7': '0.040000-0.480000-0.260000-0.220000-0.420000-0.740000',
    'F8': '0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000',
}

continuation = {
    'F1': False,
    'F2': True,
    'F3': True,
    'F4': False,
    'F5': True,
    'F6': True,
    'F7': False,
    'F8': False,
}

if __name__ == '__main__':
    print('Counterfactual extension only. No Round 14 outputs exist.')
    print(f'F2 local quadratic stationary point: {f2_vertex}')
    print()
    for function in sorted(candidates):
        decision = 'continue' if continuation[function] else 'retain best point'
        print(f'{function}: {decision}: {candidates[function]}')
