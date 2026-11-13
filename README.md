SUPER SECURE SYST v23 - SUPER INFRARED
HackGlobal 2026 | 6 Detect in 1 Agent + Bio Healthy Room

One agent with 6 multispectral detection tools in one dashboard.
Built for HackGlobal 2026 on Vultr.

What It Does
6 Detect Tools
Food - RGB IMX219 + NDIR 4.26um CO2 for freshness / air quality
Bio Healthy Room - SHT41 + NDIR + Thermal for dust, humidity, dirty area monitoring
Status: Clean / Needs Cleaning / Risk
Monitoring + prevention prototype, NOT a medical sterilization claim
Derma - Multispectral skin check preview
Naphtol - NDIR 3.4um Naphtol + 3.3um H2O/OH for dye quality
Forensic Trace - Trace detection preview
Gem Authenticity - 7.7um emissivity + RGB for gem check
Safety - 30-Second Safety Observatory
CH4 3.33um - explosion risk
CO2 4.26um - air quality
CO 4.64um - toxicity
3.91um - auto-calibration
O2 / H2S via I2C pump 350 mL/min
Agent converts raw values to actions, e.g.:

CO 40ppm -> Open damper 30%, evac zone 2, notify tech

Fast Check - 7-Second IR Lens
Quick 7-second infrared lens check for fast screening.

Architecture
[NDIR 4-CH + IMX219 + MLX90640 + SHT41 + O2/H2S]
        |
        v
[ESP32-S3 + Pump]
  UART2 GPIO16/17 -> NDIR
  I2C GPIO21/22 -> O2 / H2S
  GPIO27 PWM -> Pump
        |
        v
[MQTT TLS - JSON Telemetry]
        |
        v
[Vultr Compute Singapore + Vultr Serverless Inference]
  AI Agent - 6 Detect Reasoning
  RAG Vector Search
        |
        v
[Streamlit Observatory Dashboard + ESC/POS Certificate]
How Vultr Is Used
Vultr Compute (Singapore) - Closest to Jakarta for low latency. Hosts Streamlit app, MQTT broker, RAG search, certificate generator.
Vultr Serverless Inference - Runs the 6 Detect reasoning agent.
How To Run
git clone https://github.com/AIchaliveret/super-secure-syst-v23.git
cd super-secure-syst-v23
pip install -r requirements.txt
streamlit run app.py
Open: http://localhost:8501

Live demo: https://super-secure-syst-v23.streamlit.app

Files In This Repo
app.py - Streamlit dashboard, 6 Detect + Bio Healthy Room + Certificate
requirements.txt - Python dependencies
room air quality.jpg - Room air quality reference image
index.html - Static landing page
Supporting Repos
super-infrared - IR core
ir-7detik-lensa-infra - Fast 7-sec IR lens detection
Honest Notes
Live demo uses simulated sensor data so anyone can test without hardware.
Real hardware uses the same MQTT JSON format as the demo.
Bio Healthy Room is a monitoring + prevention prototype.
Track
HackGlobal 2026 - Civic and real-world impact + Agentic and GenAI apps

---

## Vision: Ruang Teduh for All Cities

One box per city: Power Wajib Kabel 12V + AQI Monitoring ON.
Same Super Infrared agent in every city: NDIR + Thermal + RGB -> MQTT -> Vultr Compute -> Dashboard.

Start: Serpong, Tangsel, PIK 1, PIK 2
Next: Bandung, Bogor, Semarang, Medan, Batam

Automatic from Jupiter: 1x Run in Jupiter = all cities filled automatically.

Proof in gallery: Jakarta Warehouse hotspot 612°C detected, CO2 852ppm, AI action: suppress fire, isolate section.

Full list in file: Ruang_teduh_for_all_Cities.txt
