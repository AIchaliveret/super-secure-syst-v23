"""
SUPER SECURE SYST v23 - SUPER INFRARED
HackGlobal 2026 - 6 Detect in 1 Agent + Bio Healthy Room
Repo: AIchaliveret/super-secure-syst-v23
Main module: app.py - Streamlit Cloud entry point
Vultr: Compute Singapore + Serverless Inference (Llama)
"""
import streamlit as st
import pandas as pd
import numpy as np
import random, time
from datetime import datetime

st.set_page_config(page_title="Super Secure Syst v23 - Super Infrared", page_icon="🛡️", layout="wide")

# --- Header ---
st.title("🛡️ SUPER SECURE SYST v23 - SUPER INFRARED")
st.caption("HackGlobal 2026 | 6 Detect in 1 Agent | Vultr Compute Singapore + Vultr Serverless Inference | 30-Second Safety Observatory + 7-Second IR Lens")
st.markdown("**Live Demo uses simulated sensor data** so judges can test without hardware. Real hardware: ESP32-S3 -> MQTT TLS -> Vultr Compute -> same JSON format.")

# --- Sidebar: controls ---
st.sidebar.header("⚙️ Controls")
mode = st.sidebar.selectbox("Mode", ["Demo - Simulated Sensors", "Live - ESP32 MQTT (coming soon)"])
interval = st.sidebar.slider("Refresh (seconds)", 2, 10, 3)
if st.sidebar.button("🔄 Refresh Now"):
    st.rerun()

# --- Simulated sensor data ---
def get_reading():
    return {
        "CO2_ppm": round(random.uniform(400, 900), 1),
        "CO_ppm": round(random.uniform(0, 45), 1),
        "CH4_ppm": round(random.uniform(0, 8), 2),
        "Naphtol_um": round(random.uniform(3.2, 3.6), 3),
        "H2O_OH": round(random.uniform(3.1, 3.5), 3),
        "Gem_emissivity": round(random.uniform(7.5, 7.9), 3),
        "Temp_C": round(random.uniform(26, 34), 1),
        "Humidity_%": round(random.uniform(55, 88), 1),
        "Thermal_Max_C": round(random.uniform(60, 118), 1),
        "Dust_index": round(random.uniform(10, 95), 1),
    }

data = get_reading()

# --- Top metrics ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("CO2 (4.26um)", f"{data['CO2_ppm']} ppm", "OK" if data['CO2_ppm'] < 800 else "Ventilate")
c2.metric("CO (4.64um)", f"{data['CO_ppm']} ppm", "SAFE" if data['CO_ppm'] < 35 else "⚠️ EVAC ZONE 2")
c3.metric("Thermal Max MLX90640", f"{data['Thermal_Max_C']} °C", "OK" if data['Thermal_Max_C'] < 115 else "🔴 AUTO-STOP")
c4.metric("Humidity SHT41", f"{data['Humidity_%']} %", "OK" if data['Humidity_%'] < 80 else "Mold risk")

# --- Agent suggestion ---
st.subheader("🤖 AI Agent - Action")
if data['CO_ppm'] >= 35:
    st.error("**Action:** CO 40ppm approx - Open damper 30%, evac zone 2, notify tech.")
elif data['Thermal_Max_C'] >= 115:
    st.error("**Action:** Kuali >115°C - Auto-stop Relay COM-NC-NO, check valve Orange SS304.")
elif data['Humidity_%'] >= 80:
    st.warning("**Action:** Humidity >80% - Bio Healthy Room needs ventilation + cleaning schedule. Risk of mold / pests.")
else:
    st.success("**Action:** All safe - Continue monitoring. 30-Second Observatory active.")

# --- Tabs: 6 Detect ---
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🍎 Food", "🏠 Bio Healthy Room", "🧴 Derma", "🎨 Naphtol", "🔍 Forensic Trace", "💎 Gem", "📄 Certificate"
])

with tab1:
    st.header("🍎 Food Detect - IMX219 + NDIR 4.26um")
    st.write(f"CO2: {data['CO2_ppm']} ppm | Temp: {data['Temp_C']}°C | Humidity: {data['Humidity_%']}%")
    st.write("**Result:** Freshness OK" if data['CO2_ppm'] < 800 else "**Result:** Ventilate storage, re-check in 30 sec")
    st.bar_chart(pd.DataFrame({"CO2": [data['CO2_ppm'], 600, 800], "Limit": [800, 800, 800]}))

with tab2:
    st.header("🏠 Bio Healthy Room - NEW for HackGlobal")
    st.write("Dust, Humidity, Dirty Area monitoring. Prevention prototype, NOT medical sterilization.")
    # Bio Healthy Room logic
    if data['Dust_index'] > 70 or data['Humidity_%'] >= 80:
        status = "🔴 RISK - Needs Cleaning"
    elif data['Dust_index'] > 40:
        status = "🟡 NEEDS CLEANING"
    else:
        status = "🟢 CLEAN"
    st.subheader(f"Status: {status}")
    colA, colB, colC = st.columns(3)
    colA.metric("Dust Index", f"{data['Dust_index']}")
    colB.metric("Humidity", f"{data['Humidity_%']} %")
    colC.metric("Thermal", f"{data['Thermal_Max_C']} °C")
    st.write("**AI Suggestion:**")
    if "RISK" in status:
        st.write("- Turn on ventilation, schedule cleaning now, check for mold / pests / bacteria risk area.")
    elif "NEEDS" in status:
        st.write("- Clean dusty area, dry wet area, re-check in 1 hour.")
    else:
        st.write("- Room is clean. Keep monitoring every 30 seconds.")
    # Checklist
    st.checkbox("Ventilation ON", value=True)
    st.checkbox("Cleaning scheduled")
    st.checkbox("Filter checked")

with tab3:
    st.header("🧴 Derma Detect - Multispectral Preview")
    st.write(f"RGB IMX219 + NDIR: H2O/OH {data['H2O_OH']} um | Temp {data['Temp_C']}°C")
    st.write("Preview only - not a medical diagnosis.")

with tab4:
    st.header("🎨 Naphtol Detect - Dye Quality")
    st.write(f"Naphtol 3.4um: {data['Naphtol_um']} um | H2O/OH 3.3um: {data['H2O_OH']}")
    st.write("**Result:** Dye lot consistent" if 3.3 <= data['Naphtol_um'] <= 3.5 else "**Result:** Re-check dye lot")

with tab5:
    st.header("🔍 Forensic Trace")
    st.write("Trace detection preview - IMX219 + NDIR pattern check.")
    st.write(f"Signal strength: {round(random.uniform(60, 99),1)}%")

with tab6:
    st.header("💎 Gem Authenticity - 7.7um Emissivity")
    st.write(f"Emissivity 7.7um: {data['Gem_emissivity']}")
    st.write("**Result:** Likely genuine pattern" if 7.6 <= data['Gem_emissivity'] <= 7.8 else "**Result:** Need re-scan")

with tab7:
    st.header("📄 Certificate - ESC/POS")
    st.write(f"**Certificate ID:** SSS-v23-{datetime.now().strftime('%Y%m%d-%H%M%S')}")
    st.write(f"**Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S WIB')}")
    st.write(f"**Checks:** CO2 {data['CO2_ppm']} ppm | CO {data['CO_ppm']} ppm | Thermal {data['Thermal_Max_C']}°C | Bio Room: {status if 'status' in locals() else 'Checked'}")
    st.write("**Verdict:** PASS - Safe to proceed" if data['CO_ppm'] < 35 and data['Thermal_Max_C'] < 115 else "**Verdict:** HOLD - Fix action above first")
    if st.button("🖨️ Generate Certificate (ESC/POS)"):
        st.success("Certificate generated - ready to print via ESC/POS printer.")

# --- Architecture ---
st.divider()
st.subheader("🏗️ Architecture")
st.code("[NDIR 4-CH + IMX219 + MLX90640] -> [ESP32-S3 + Pump] -> [MQTT TLS] -> [Vultr Compute + Vultr Serverless Inference] -> [Streamlit + ESC/POS]", language="text")
st.caption("Repo: github.com/AIchaliveret/super-secure-syst-v23 | Supporting: super-infrared (IR core) + ir-7detik-lensa-infra (7-sec IR lens)")

# --- History table ---
st.subheader("📊 Recent Log (Simulated)")
hist = pd.DataFrame([get_reading() for _ in range(5)])
st.dataframe(hist, width="stretch")
