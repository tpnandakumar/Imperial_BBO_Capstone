(function () {
  "use strict";

  const tracks = {
    "Cover": ["01_welcome_and_project_purpose.m4a", "Welcome and project purpose"],
    "Imperial BBO": ["02_imperial_bbo_journey.m4a", "The Imperial BBO journey"],
    "README": ["01_welcome_and_project_purpose.m4a", "Project overview and README"],
    "Read by Week": [
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/24_read_by_week_page.m4a?version=4",
      "Read by Week page"
    ],
    "Read by Function": [
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/23_read_by_function_page.m4a?version=1",
      "Read by Function page"
    ],
    "Scientific Atlas": [
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/22_scientific_atlas_page.m4a?version=1",
      "Scientific Atlas page"
    ],
    "Executive Summary": [[
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/07_executive_summary_part_1.m4a?version=2",
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/08_executive_summary_part_2.m4a",
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/09_executive_summary_part_3.m4a"
    ], "Full Executive Summary"],
    "Repository": ["01_welcome_and_project_purpose.m4a", "Repository overview"],
    "Above and Beyond": ["05_black_box_resolution.m4a", "Black Box Resolution"],
    "Resolution": ["05_black_box_resolution.m4a", "Black Box Resolution"],
    "Beyond BBO": ["04_delta_signature_of_change.m4a", "Delta and the Signature of Change"],
    "Evidence": [
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/21_verified_evidence_page.m4a?version=1",
      "Verified Evidence page"
    ]
  };

  const pdhisResearchViews = new Set(["model", "advanced", "flicker", "atlas"]);
  const audio = new Audio();
  let currentSource = "";
  let currentSources = [];
  let currentPart = 0;
  let currentTitle = "";
  let deepLinkOpened = false;

  function openRequestedPage() {
    const requestedPage = new URLSearchParams(window.location.search).get("page");
    if (!deepLinkOpened && requestedPage === "executive-summary" && window.Shiny) {
      deepLinkOpened = true;
      window.Shiny.setInputValue("deep_link_page", "executive-summary", { priority: "event" });
    }
  }

  document.addEventListener("shiny:connected", openRequestedPage);
  window.addEventListener("load", function () { window.setTimeout(openRequestedPage, 500); });
  window.setTimeout(openRequestedPage, 1200);

  function mainButton() { return document.getElementById("hear_me"); }
  function setStatus(message) {
    const node = document.getElementById("hear_me_status");
    if (node) node.textContent = message;
  }
  function setMainLabel(label) {
    const button = mainButton();
    if (button) button.textContent = label;
  }
  function activeSection() {
    const active = document.querySelector(".navbar-nav .nav-link.active, .nav-tabs .nav-link.active");
    return active ? active.textContent.trim() : "Cover";
  }
  function selectedValue(name) {
    const selected = document.querySelector('input[name="' + name + '"]:checked');
    return selected ? selected.value : "";
  }
  function selectedTrack() {
    const section = activeSection();
    if (section === "Resolution" && selectedValue("resolution_section") === "bbr") {
      return [
        "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/10_bbr_method_page.m4a?version=1",
        "BBR method page"
      ];
    }
    if (section === "Beyond BBO" && selectedValue("pdhis_view") === "model") {
      return [
        "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/11_pdhis_mathematical_model.m4a?version=1",
        "PDHIS mathematical model page"
      ];
    }
    if (section === "Beyond BBO" && selectedValue("pdhis_view") === "meanings") {
      return [
        "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/15_pdhis_delta_meanings.m4a?version=1",
        "PDHIS Delta meanings page"
      ];
    }
    if (section === "Beyond BBO" && selectedValue("pdhis_view") === "hierarchy") {
      return [
        "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/16_pdhis_lotus_hierarchy.m4a?version=1",
        "PDHIS Lotus hierarchy page"
      ];
    }
    if (section === "Beyond BBO" && selectedValue("pdhis_view") === "trajectory") {
      return [
        "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/17_pdhis_delta_trajectory.m4a?version=1",
        "PDHIS Delta trajectory page"
      ];
    }
    if (section === "Beyond BBO" && selectedValue("pdhis_view") === "orders") {
      return [
        "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/18_pdhis_predictability.m4a?version=1",
        "PDHIS Predictability page"
      ];
    }
    if (section === "Beyond BBO" && selectedValue("pdhis_view") === "functions") {
      return [
        "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/19_pdhis_f1_to_f8_relationships.m4a?version=1",
        "PDHIS F1 to F8 relationship page"
      ];
    }
    if (section === "Beyond BBO" && selectedValue("pdhis_view") === "evidence") {
      return [
        "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/20_pdhis_evidence_boundary.m4a?version=1",
        "PDHIS Evidence boundary page"
      ];
    }
    if (section === "Beyond BBO" && selectedValue("pdhis_view") === "advanced") {
      return [
        "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/12_pdhis_advanced_model.m4a?version=1",
        "PDHIS advanced model page"
      ];
    }
    if (section === "Beyond BBO" && selectedValue("pdhis_view") === "flicker") {
      return [
        "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/13_pdhis_event_locked_flicker.m4a?version=1",
        "PDHIS event-locked flicker study page"
      ];
    }
    if (section === "Beyond BBO" && selectedValue("pdhis_view") === "atlas") {
      return [
        "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/14_pdhis_matched_event_atlas.m4a?version=1",
        "PDHIS matched event atlas page"
      ];
    }
    if (section === "Beyond BBO" && pdhisResearchViews.has(selectedValue("pdhis_view"))) {
      return ["06_pdhis_and_conclusion.m4a", "PDHIS and conclusion"];
    }
    return tracks[section] || tracks.Cover;
  }
  function stopNarration(message) {
    audio.pause();
    audio.currentTime = 0;
    currentSource = "";
    currentSources = [];
    currentPart = 0;
    currentTitle = "";
    setMainLabel("HEAR ME");
    setStatus(message || "Narration stopped.");
  }
  function sourceUrl(source) {
    return source.startsWith("http://") || source.startsWith("https://") ? source : "/narration/" + source;
  }
  function partStatus(action) {
    const part = currentSources.length > 1 ? ", part " + (currentPart + 1) + " of " + currentSources.length : "";
    setStatus(currentTitle + part + " narration " + action + ".");
  }
  async function startNarration() {
    const track = selectedTrack();
    const sources = Array.isArray(track[0]) ? track[0] : [track[0]];
    const source = sourceUrl(sources[0]);
    if (currentSources.join("|") !== sources.join("|")) {
      currentSources = sources;
      currentPart = 0;
      currentTitle = track[1];
      audio.src = source;
      currentSource = source;
      audio.currentTime = 0;
    }
    try {
      await audio.play();
      setMainLabel("PAUSE");
      partStatus("started");
    } catch (error) {
      setMainLabel("HEAR ME");
      setStatus("Narration could not start. Please try again.");
    }
  }

  document.addEventListener("click", function (event) {
    if (!(event.target instanceof Element)) return;
    const hear = event.target.closest("#hear_me");
    const stop = event.target.closest("#hear_stop");
    if (stop) {
      event.preventDefault();
      stopNarration();
      return;
    }
    if (!hear) return;
    event.preventDefault();
    if (!currentSource || audio.ended) {
      startNarration();
    } else if (audio.paused) {
      audio.play().then(function () {
        setMainLabel("PAUSE");
        setStatus("Narration continued.");
      });
    } else {
      audio.pause();
      setMainLabel("CONTINUE");
      setStatus("Narration paused.");
    }
  });

  document.addEventListener("change", function (event) {
    if (!(event.target instanceof HTMLInputElement)) return;
    if (event.target.name === "pdhis_view" || event.target.name === "resolution_section") {
      stopNarration("Narration reset for the selected section.");
    }
  });
  document.addEventListener("shown.bs.tab", function () {
    stopNarration("Narration reset for the selected page.");
  });
  audio.addEventListener("ended", function () {
    if (currentPart < currentSources.length - 1) {
      currentPart += 1;
      currentSource = sourceUrl(currentSources[currentPart]);
      audio.src = currentSource;
      audio.currentTime = 0;
      audio.play().then(function () {
        setMainLabel("PAUSE");
        partStatus("started");
      }).catch(function () {
        setMainLabel("HEAR ME");
        setStatus("The next narration part could not start. Please try again.");
      });
      return;
    }
    currentSource = "";
    currentSources = [];
    currentPart = 0;
    currentTitle = "";
    setMainLabel("HEAR ME");
    setStatus("Narration complete.");
  });
  audio.addEventListener("error", function () {
    currentSource = "";
    setMainLabel("HEAR ME");
    setStatus("This narration file could not be loaded.");
  });
  document.addEventListener("visibilitychange", function () {
    if (document.hidden && !audio.paused) {
      audio.pause();
      setMainLabel("CONTINUE");
      setStatus("Narration paused because the page is no longer visible.");
    }
  });
  window.addEventListener("beforeunload", function () { audio.pause(); });
})();

