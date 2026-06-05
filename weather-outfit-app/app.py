 """WeatherFit Flask app — outfit suggestions based on current weather."""

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Outfit suggestion engine
def get_outfit_suggestion(temp_c, weather_main, humidity, wind_speed, is_day):
    """Simple rule-based outfit suggestions. Returns items, colors and a short tip."""
    outfit = {
        "top": "", "bottom": "", "footwear": "",
        "accessories": [], "colors": [], "tip": "",
        "vibe": "", "emoji": ""
    }

    rain = weather_main.lower() in ["rain", "drizzle", "thunderstorm"]
    snow = weather_main.lower() in ["snow", "sleet"]
    windy = wind_speed > 6   # m/s
    humid = humidity > 75

    # Temperature-based core outfit
    if temp_c >= 35:
        outfit.update({
            "top": "Sleeveless top or light linen shirt",
            "bottom": "Shorts or loose cotton trousers",
            "footwear": "Sandals or open-toe slippers",
            "colors": ["White", "Beige", "Light blue", "Pastel yellow"],
            "vibe": "Ultra Light & Breezy",
            "emoji": "🌞"
        })
        outfit["accessories"].append("Sunglasses 🕶️")
        outfit["accessories"].append("Wide-brim hat 🧢")
        outfit["tip"] = "Wear loose, breathable fabrics. Stay hydrated and avoid dark colors that absorb heat."

    elif 28 <= temp_c < 35:
        outfit.update({
            "top": "Cotton t-shirt or short-sleeve shirt",
            "bottom": "Chinos, jeans, or light trousers",
            "footwear": "Sneakers or loafers",
            "colors": ["Sky blue", "White", "Mint green", "Coral"],
            "vibe": "Casual & Fresh",
            "emoji": "☀️"
        })
        outfit["accessories"].append("Sunglasses 🕶️")
        outfit["tip"] = "Light cotton works best. A small backpack is handy for carrying extras."

    elif 20 <= temp_c < 28:
        outfit.update({
            "top": "T-shirt with a light jacket or hoodie",
            "bottom": "Jeans or chinos",
            "footwear": "Sneakers or casual boots",
            "colors": ["Navy", "Olive green", "Grey", "Terracotta"],
            "vibe": "Smart Casual",
            "emoji": "🌤️"
        })
        outfit["accessories"].append("Light scarf (optional) 🧣")
        outfit["tip"] = "Layer up! A light jacket you can remove mid-day is perfect for this weather."

    elif 10 <= temp_c < 20:
        outfit.update({
            "top": "Full-sleeve shirt + sweater or sweatshirt",
            "bottom": "Jeans or warm trousers",
            "footwear": "Closed shoes or ankle boots",
            "colors": ["Burgundy", "Forest green", "Camel", "Charcoal"],
            "vibe": "Cozy Layered",
            "emoji": "🌥️"
        })
        outfit["accessories"].append("Light scarf 🧣")
        outfit["accessories"].append("Jacket or blazer 🧥")
        outfit["tip"] = "Layering is key. Start warm and peel off as the day heats up."

    else:  # below 10
        outfit.update({
            "top": "Thermal inner + heavy sweater or fleece",
            "bottom": "Thick jeans or warm joggers",
            "footwear": "Boots or insulated closed shoes",
            "colors": ["Charcoal", "Deep navy", "Black", "Dark olive"],
            "vibe": "Full Winter Mode",
            "emoji": "❄️"
        })
        outfit["accessories"].append("Warm scarf 🧣")
        outfit["accessories"].append("Beanie or cap 🧢")
        outfit["accessories"].append("Gloves 🧤")
        outfit["tip"] = "Bundle up! Keep extremities warm — hands, neck, and ears lose heat fastest."

    # Weather condition overrides
    if rain:
        outfit["footwear"] = "Waterproof shoes or rain boots"
        outfit["accessories"].append("Umbrella ☂️")
        outfit["accessories"].append("Waterproof bag cover")
        outfit["tip"] += " Rain expected — carry an umbrella and avoid suede or leather shoes."

    if snow:
        outfit["footwear"] = "Insulated waterproof snow boots"
        outfit["accessories"].append("Waterproof gloves 🧤")
        outfit["tip"] += " Snow forecast — layer up and wear waterproof outer layers."

    if windy:
        outfit["accessories"].append("Windbreaker jacket 🌬️")
        outfit["tip"] += " It's windy — a windbreaker over your outfit will help a lot."

    if humid and temp_c > 25:
        outfit["top"] = "Moisture-wicking or breathable fabric top"
        outfit["tip"] += " High humidity today — moisture-wicking fabrics will keep you comfortable."

    return outfit


def get_weather(city, api_key):
    """Fetch current weather from OpenWeatherMap."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    resp = requests.get(url, timeout=8)
    return resp.json()


def get_demo_weather(city):
    """Return demo weather for testing without an API key."""
    demo_data = {
        "mumbai":    {"temp": 32, "feels": 36, "desc": "Humid and hazy",      "main": "Haze",   "humidity": 85, "wind": 4.2, "icon": "50d"},
        "delhi":     {"temp": 38, "feels": 42, "desc": "Sunny and hot",        "main": "Clear",  "humidity": 35, "wind": 3.1, "icon": "01d"},
        "bangalore": {"temp": 24, "feels": 24, "desc": "Pleasant and cloudy",  "main": "Clouds", "humidity": 65, "wind": 2.8, "icon": "03d"},
        "kolkata":   {"temp": 30, "feels": 34, "desc": "Partly cloudy",        "main": "Clouds", "humidity": 78, "wind": 3.5, "icon": "04d"},
        "chennai":   {"temp": 34, "feels": 39, "desc": "Hot and sunny",        "main": "Clear",  "humidity": 72, "wind": 5.1, "icon": "01d"},
        "pune":      {"temp": 27, "feels": 28, "desc": "Mostly clear",         "main": "Clear",  "humidity": 55, "wind": 2.2, "icon": "02d"},
        "hyderabad": {"temp": 33, "feels": 36, "desc": "Partly sunny",         "main": "Clear",  "humidity": 42, "wind": 3.8, "icon": "01d"},
        "jaipur":    {"temp": 40, "feels": 44, "desc": "Very hot and dry",     "main": "Clear",  "humidity": 20, "wind": 4.5, "icon": "01d"},
    }
    key = city.lower().strip()
    d = demo_data.get(key, {"temp": 28, "feels": 30, "desc": "Partly cloudy", "main": "Clouds", "humidity": 60, "wind": 3.0, "icon": "03d"})
    return {
        "name": city.title(),
        "sys": {"country": "IN"},
        "main": {"temp": d["temp"], "feels_like": d["feels"], "humidity": d["humidity"]},
        "weather": [{"description": d["desc"], "main": d["main"], "icon": d["icon"]}],
        "wind": {"speed": d["wind"]},
        "cod": 200
    }


# Routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather", methods=["POST"])
def weather():
    data    = request.get_json()
    city    = data.get("city", "").strip()
    api_key = data.get("api_key", "").strip()

    if not city:
        return jsonify({"error": "Please enter a city name."}), 400

    # Use live API if an API key is provided; otherwise use demo data
    if api_key:
        try:
            w = get_weather(city, api_key)
            if w.get("cod") != 200:
                return jsonify({"error": f"City not found: {city}"}), 404
        except Exception as e:
            return jsonify({"error": "Could not fetch weather. Check your API key."}), 500
    else:
        w = get_demo_weather(city)

    temp_c    = round(w["main"]["temp"])
    feels     = round(w["main"]["feels_like"])
    humidity  = w["main"]["humidity"]
    wind      = w["wind"]["speed"]
    desc      = w["weather"][0]["description"].title()
    main      = w["weather"][0]["main"]
    icon_code = w["weather"][0]["icon"]
    is_day    = icon_code.endswith("d")
    country   = w["sys"]["country"]

    outfit = get_outfit_suggestion(temp_c, main, humidity, wind, is_day)

    return jsonify({
        "city":      w["name"],
        "country":   country,
        "temp":      temp_c,
        "feels":     feels,
        "humidity":  humidity,
        "wind":      round(wind * 3.6, 1),   # m/s → km/h
        "desc":      desc,
        "main":      main,
        "icon":      icon_code,
        "demo_mode": not bool(api_key),
        "outfit":    outfit
    })


if __name__ == "__main__":
    print("WeatherFit running on http://127.0.0.1:5000")
    app.run(debug=True)
