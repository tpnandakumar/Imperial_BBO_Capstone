(function () {
  "use strict";

  const tracks = {
    "Cover": ["01_welcome_and_project_purpose.m4a", "Welcome and project purpose"],
    "Imperial BBO": ["02_imperial_bbo_journey.m4a", "The Imperial BBO journey"],
    "README": ["01_welcome_and_project_purpose.m4a", "Welcome and project purpose"],
    "Read by Week": ["02_imperial_bbo_journey.m4a", "The Imperial BBO journey"],
    "Read by Function": ["03_results_and_interpretation.m4a", "Results and interpretation"],
    "Scientific Atlas": ["03_results_and_interpretation.m4a", "Results and interpretation"],
    "Repository": ["03_results_and_interpretation.m4a", "Results and interpretation"],
    "Above and Beyond": ["05_black_box_resolution.m4a", "Black Box Resolution"],
    "Resolution": ["05_black_box_resolution.m4a", "Black Box Resolution"],
    "Beyond BBO": ["04_delta_signature_of_change.m4a", "Delta and the Signature of Change"],
    "Evidence": ["03_results_and_interpretation.m4a", "Results and interpretation"]
  };

  const pdhisResearchViews = new Set(["model", "advanced", "flicker", "atlas"]);
  const audio = new Audio();
  let currentSource = "";

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
    if (section === "Beyond BBO" && pdhisResearchViews.has(selectedValue("pdhis_view"))) {
      return ["06_pdhis_and_conclusion.m4a", "PDHIS and conclusion"];
    }
    return tracks[section] || tracks.Cover;
  }
  function stopNarration(message) {
    audio.pause();
    audio.currentTime = 0;
    currentSource = "";
    setMainLabel("HEAR ME");
    setStatus(message || "Narration stopped.");
  }
  async function startNarration() {
    const track = selectedTrack();
    const source = "/narration/" + track[0];
    if (currentSource !== source) {
      audio.src = source;
      currentSource = source;
      audio.currentTime = 0;
    }
    try {
      await audio.play();
      setMainLabel("PAUSE");
      setStatus(track[1] + " narration started.");
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
    currentSource = "";
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
