/* Main client-side logic for WeatherFit */

const COLOR_MAP = {
  "White":         "#f8fafc", "Beige":          "#f5f0e8", "Light blue":     "#bae6fd",
  "Pastel yellow": "#fef9c3", "Sky blue":       "#7dd3fc", "Mint green":     "#6ee7b7",
  "Coral":         "#fca5a5", "Navy":           "#1e3a5f", "Olive green":    "#65a30d",
  "Grey":          "#9ca3af", "Terracotta":     "#c2663c", "Burgundy":       "#881337",
  "Forest green":  "#166534", "Camel":          "#c49a6c", "Charcoal":       "#374151",
  "Deep navy":     "#0f2d4a", "Black":          "#1f2937", "Dark olive":     "#3d4a1e",
};

const $ = id => document.getElementById(id);

async function fetchWeather() {
  const city   = $("cityInput").value.trim();
  const apiKey = $("apiKey").value.trim();

  if (!city) { showError("Enter a city name."); return; }

  hideError();
  showLoader(true);
  hideResult();

  try {
    const res  = await fetch("/weather", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ city, api_key: apiKey }),
    });
    const data = await res.json();

    if (!res.ok) { showError(data.error || "Something went wrong."); return; }

    renderWeather(data);
    renderOutfit(data.outfit);
    showResult();
  } catch (e) {
    showError("Network error — check your connection or the server.");
  } finally {
    showLoader(false);
  }
}

function renderWeather(d) {
  $("cityName").textContent    = `${d.city}, ${d.country}`;
  $("weatherDesc").textContent = d.desc;
  $("tempVal").textContent     = `${d.temp}°C`;
  $("feelsVal").textContent    = `${d.feels}°C`;
  $("humidVal").textContent    = `${d.humidity}%`;
  $("windVal").textContent     = `${d.wind} km/h`;
  $("weatherIcon").src         = `https://openweathermap.org/img/wn/${d.icon}@2x.png`;
  $("weatherIcon").alt         = d.desc;

  if (d.demo_mode) {
    $("demoTag").classList.remove("hidden");
  } else {
    $("demoTag").classList.add("hidden");
  }

  // Color-tint the weather card based on condition
  const card  = $("weatherCard");
  const tints = {
    Clear:        "rgba(255,213,79,0.06)",
    Rain:         "rgba(79,195,247,0.08)",
    Drizzle:      "rgba(79,195,247,0.06)",
    Thunderstorm: "rgba(179,136,255,0.08)",
    Snow:         "rgba(220,240,255,0.08)",
    Clouds:       "rgba(144,164,174,0.06)",
    Haze:         "rgba(255,204,128,0.06)",
    Mist:         "rgba(176,190,197,0.06)",
  };
  card.style.background = tints[d.main] || "rgba(255,255,255,0.06)";
}

function renderOutfit(o) {
  $("outfitEmoji").textContent       = o.emoji;
  $("outfitVibe").textContent        = o.vibe;
  $("outfitTop").textContent         = o.top;
  $("outfitBottom").textContent      = o.bottom;
  $("outfitFootwear").textContent    = o.footwear;
  $("outfitAccessories").textContent = o.accessories.join(" · ") || "None needed";
  $("outfitTip").textContent         = o.tip;

  // Render color chips
  const chips = $("colorChips");
  chips.innerHTML = "";
  o.colors.forEach(c => {
    const hex  = COLOR_MAP[c] || "#94a3b8";
    const chip = document.createElement("div");
    chip.className = "color-chip";
    chip.innerHTML = `<div class="chip-dot" style="background:${hex};border:1px solid rgba(255,255,255,0.2)"></div>${c}`;
    chips.appendChild(chip);
  });
}

// Helpers
function showError(msg) {
  $("errorMsg").textContent = msg;
  $("errorBox").classList.remove("hidden");
}
function hideError() { $("errorBox").classList.add("hidden"); }
function showLoader(on) { $("loader").classList.toggle("hidden", !on); }
function showResult() { $("resultSection").classList.remove("hidden"); }
function hideResult() { $("resultSection").classList.add("hidden"); }

// Events
$("searchBtn").addEventListener("click", fetchWeather);
$("cityInput").addEventListener("keydown", e => { if (e.key === "Enter") fetchWeather(); });
