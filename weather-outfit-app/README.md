# 🌤️ WeatherFit — AI Outfit Suggester

> **What should I wear today?** — Just enter your city and let AI decide.

A full-stack web app that fetches **live weather data** and uses an **AI engine** to recommend the perfect outfit based on temperature, humidity, wind speed, and weather conditions.

---

## 🔥 Live Demo

> Clone the repo, run locally, and try cities like **Mumbai, Delhi, Bangalore, Chennai, Jaipur** in demo mode — no API key needed!

---

## ✨ Features

- 🌍 **Live weather** via OpenWeatherMap API
- 🤖 **AI outfit engine** — recommends top, bottom, footwear & accessories
- 🎨 **Color palette suggestions** matched to the weather vibe
- 💡 **Smart tips** — accounts for rain, wind, humidity, and extreme heat/cold
- 🇮🇳 **Demo mode** — works without an API key for 8 Indian cities
- 📱 **Fully responsive** — works on mobile and desktop
- 🌈 **Dynamic UI** — weather card changes tint based on conditions

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3 (Glassmorphism), Vanilla JavaScript |
| Backend | Python, Flask |
| Weather Data | OpenWeatherMap API |
| AI Logic | Rule-based outfit engine (Python) |

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/the-sparsh-shukla/weather-outfit-app.git
cd weather-outfit-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask app
```bash
python app.py
```

### 4. Open in browser
```
http://127.0.0.1:5000
```

### 5. Try it!
- **No API key?** Just type a city like `Mumbai` or `Delhi` — demo mode works!
- **Want live data?** Get a free API key at [openweathermap.org](https://openweathermap.org/api) and paste it in the key field.

---

## 🧠 How the AI Works

The outfit engine takes 4 inputs:

```
Temperature + Weather Condition + Humidity + Wind Speed
        ↓
  Rule-based Decision Tree
        ↓
  Outfit (Top + Bottom + Footwear + Accessories + Colors + Tip)
```

**Temperature zones:**
| Range | Recommendation |
|-------|---------------|
| ≥ 35°C | Sleeveless / Ultra Light |
| 28–35°C | Cotton T-shirt / Casual |
| 20–28°C | Light jacket layer |
| 10–20°C | Sweater + Closed shoes |
| < 10°C | Full winter outfit |

**Condition overrides:**
- 🌧️ Rain → Waterproof shoes + umbrella
- 💨 Windy → Windbreaker
- 💧 High humidity → Moisture-wicking fabrics

---

## 📁 Project Structure

```
weather-outfit-app/
│
├── app.py                  # Flask backend + AI outfit engine
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html          # Main webpage
│
└── static/
    ├── css/
    │   └── style.css       # Glassmorphism UI styling
    └── js/
        └── main.js         # Fetch API + dynamic rendering
```

---

## 🔮 Future Improvements

- [ ] Add 5-day forecast with outfit plan for the week
- [ ] Integrate Gemini / OpenAI API for smarter suggestions
- [ ] User preference settings (formal / casual / sporty)
- [ ] Deploy to Render or Railway for public access
- [ ] Add geolocation to auto-detect city

---

## 👤 Author

**SPARSH SHUKLA**
📧 reachme.sparshshukla.com
🔗 [LinkedIn](https://linkedin.com/in/sparsh-shukla) · [GitHub](https://github.com/the-sparsh-shukla)

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

⭐ **If you found this useful, drop a star on GitHub!**
