(function () {
  "use strict";

  const tracks = {
    "Cover": [
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/30_cover_page.m4a?version=1",
      "Cover page"
    ],
    "Imperial BBO": [
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/31_imperial_bbo_page.m4a?version=1",
      "Imperial BBO page"
    ],
    "README": [
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/25_readme_page.m4a?version=1",
      "README page"
    ],
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
    "Repository": [
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/26_repository_page.m4a?version=1",
      "Repository page"
    ],
    "Above and Beyond": [
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/27_above_and_beyond_page.m4a?version=1",
      "Above and Beyond page"
    ],
    "Resolution": [
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/28_resolution_home_page.m4a?version=1",
      "Resolution home page"
    ],
    "Beyond BBO": [
      "https://github.com/tpnandakumar/Imperial_BBO_Capstone/releases/download/executive-summary-narration-v1/29_beyond_bbo_home_page.m4a?version=1",
      "Beyond BBO home page"
    ],
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
    if (!deepLinkOpened && ["executive-summary", "bbr"].includes(requestedPage) && window.Shiny) {
      deepLinkOpened = true;
      window.Shiny.setInputValue("deep_link_page", requestedPage, { priority: "event" });
    }
  }

  function positionNarrationControls() {
    const controls = document.querySelector(".hear-me-controls");
    const executiveTab = document.querySelector('.navbar-nav .nav-link[data-value="Executive Summary"]');
    if (!controls) return;

    if (executiveTab && executiveTab.getClientRects().length) {
      const tabRect = executiveTab.getBoundingClientRect();
      controls.style.left = (tabRect.left + tabRect.width / 2) + "px";
      controls.style.top = (tabRect.bottom + 5) + "px";
      return;
    }

    controls.style.left = "50%";
    controls.style.top = "3.65rem";
  }

  document.addEventListener("shiny:connected", function () {
    openRequestedPage();
    window.setTimeout(positionNarrationControls, 100);
  });
  window.addEventListener("load", function () {
    window.setTimeout(openRequestedPage, 500);
    window.setTimeout(positionNarrationControls, 100);
  });
  window.addEventListener("resize", positionNarrationControls);
  window.setTimeout(openRequestedPage, 1200);
  window.setTimeout(positionNarrationControls, 1200);

  function mainButton() { return document.getElementById("hear_me"); }
  function setStatus(message) {
    const node = document.getElementById("hear_me_status");
    if (node) node.textContent = message;
  }
  function setMainLabel(label) {
    const button = mainButton();
    if (button) {
      button.textContent = label;
      button.dataset.state = label.toLowerCase().replace(/\s+/g, "-");
    }
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
  function resumeKey() {
    return "imperial-bbo-narration:" + activeSection();
  }
  function savePosition() {
    if (!currentSources.length || !Number.isFinite(audio.currentTime)) return;
    try {
      localStorage.setItem(resumeKey(), JSON.stringify({ part: currentPart, time: audio.currentTime }));
    } catch (error) {}
  }
  function savedPosition() {
    try {
      return JSON.parse(localStorage.getItem(resumeKey()) || "null");
    } catch (error) {
      return null;
    }
  }
  function updateSeekControl() {
    const seek = document.getElementById("narration_seek");
    const label = document.getElementById("narration_time");
    if (seek && Number.isFinite(audio.duration) && audio.duration > 0) {
      seek.value = String((audio.currentTime / audio.duration) * 100);
    }
    if (label) {
      const seconds = Math.max(0, Math.floor(audio.currentTime || 0));
      label.textContent = Math.floor(seconds / 60) + ":" + String(seconds % 60).padStart(2, "0");
    }
  }
  async function startNarration() {
    const track = selectedTrack();
    const sources = Array.isArray(track[0]) ? track[0] : [track[0]];
    const source = sourceUrl(sources[0]);
    if (currentSources.join("|") !== sources.join("|")) {
      currentSources = sources;
      currentTitle = track[1];
      const saved = savedPosition();
      currentPart = saved && Number.isInteger(saved.part) && saved.part < sources.length ? saved.part : 0;
      currentSource = sourceUrl(sources[currentPart]);
      audio.src = currentSource;
      audio.addEventListener("loadedmetadata", function restoreSavedPosition() {
        if (saved && Number.isFinite(saved.time) && saved.time < audio.duration) audio.currentTime = saved.time;
        updateSeekControl();
      }, { once: true });
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
    const partButton = event.target.closest("[data-audio-part]");
    if (partButton) {
      event.preventDefault();
      const track = selectedTrack();
      const sources = Array.isArray(track[0]) ? track[0] : [track[0]];
      const requestedPart = Number(partButton.dataset.audioPart);
      if (!Number.isInteger(requestedPart) || requestedPart < 0 || requestedPart >= sources.length) return;
      currentSources = sources;
      currentPart = requestedPart;
      currentTitle = track[1];
      currentSource = sourceUrl(sources[currentPart]);
      audio.src = currentSource;
      audio.currentTime = 0;
      audio.play().then(function () {
        setMainLabel("PAUSE");
        partStatus("started");
      }).catch(function () {
        setMainLabel("HEAR ME");
        setStatus("This narration part could not start. Please try again.");
      });
      return;
    }
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

  document.addEventListener("input", function (event) {
    if (!(event.target instanceof HTMLInputElement) || event.target.id !== "narration_seek") return;
    if (Number.isFinite(audio.duration) && audio.duration > 0) {
      audio.currentTime = (Number(event.target.value) / 100) * audio.duration;
      savePosition();
      updateSeekControl();
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
    positionNarrationControls();
  });
  audio.addEventListener("timeupdate", function () {
    updateSeekControl();
    savePosition();
  });
  audio.addEventListener("loadedmetadata", updateSeekControl);
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


