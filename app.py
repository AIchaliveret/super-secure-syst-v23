"""
SUPER SECURE SYST v3.0 - FIXED FOR STREAMLIT CLOUD
Fix FileNotFoundError line 40: use relative path gallery/image_20261015_163716.webp
"""

import streamlit as st
import random
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path

st.set_page_config(page_title="SUPER SECURE SYST v3.0 - HMDS-35", layout="wide", page_icon="🛩")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700;800&family=Chakra+Petch:wght@700&display=swap');
.hud-top {font-family:'JetBrains Mono', monospace; font-size:20px; font-weight:800; color:white; text-shadow: 2px 2px 0px black, 0 0 8px black; letter-spacing:1px; background: rgba(30,30,30,0.9); padding:10px; border:1px solid rgba(255,255,255,0.3);}
.hotspot {font-family:'JetBrains Mono', monospace; font-size:34px; font-weight:900; color:white; text-align:center; text-shadow: 3px 3px 0px black, 0 0 12px black; margin:20px 0; background: rgba(0,0,0,0.5); padding:10px;}
.panel {background: rgba(20,20,31,0.9); border:1px solid #19AC57; border-radius:12px; padding:14px; margin:10px 0;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hud-top">HMDS-35 | PILOT-ASR | FUSED THERMAL+RGB | 85% TRANSP &nbsp;&nbsp; LOC: JAKARTA WAREHOUSE • -6.2088°S, 106.8456°E • 07:42Z 2024-11-22</div>', unsafe_allow_html=True)

col_img, col_side = st.columns([2.5,1])

# FIXED IMAGE LOADING - relative path for Streamlit Cloud
img_path = Path("gallery/image_20261015_163716.webp")
img_path_alt = Path("image_20261015_163716.webp")

with col_img:
    if img_path.exists():
        st.image(str(img_path), use_container_width=True, caption="HMDS-35 85% TRANSP - THE BEST FINAL")
    elif img_path_alt.exists():
        st.image(str(img_path_alt), use_container_width=True)
    else:
        st.warning("⚠ Upload file gallery/image_20261015_163716.webp ke GitHub repo untuk HUD THE BEST")
        st.markdown('<div style="background: linear-gradient(to bottom, #333, #111); height:400px; display:flex; align-items:center; justify-content:center; border:1px solid #19AC57; color:white; font-family:monospace;">GUDANG JAKARTA — AREA C12 — BAHAYA KEBAKARAN<br>UPLOAD image_20261015_163716.webp TO gallery/</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="hotspot">→ HOTSPOT DETECTED — WHITE HOT<br>612°C — THERMAL ANOMALY</div>', unsafe_allow_html=True)

with col_side:
    st.markdown("### ✈ F-21 SYSTEM v3.0 FIXED")
    st.metric("Cycle", "5:00", "30s DETECT / 270s STANDBY")
    st.metric("Best Gas Syst", "4-NDIR Active", "CH4 3.33um, CO2 4.26um, CO 4.64um, Ref 3.91um")
    st.metric("Status", "FIXED", "FileNotFoundError Patched")

    mode = st.radio("PILIH MODE (CUMA 2)", ["MODE 1 - EARLY GUARD", "MODE 2 - HEALTH ROOM / IDEAL"], index=0)

    if mode == "MODE 1 - EARLY GUARD":
        st.info("**Safety:** MLX90640 32x24 White Hot 612C + IMX219 + 850nm IR Fusion + Gas NDIR + O2/H2S")
    else:
        st.success("**Ruangan Ideal:** SHT41 22-26°C, RH 40-60%, CO2<1000ppm | Bocor cair/banjir = QR Cert ESC/POS")

    st.divider()
    t1, t2, t3 = st.tabs(["01 THEORY", "02 OBSERVATION", "03 OPINION"])

    with t1:
        st.markdown('<div class="panel"><b>01 — THEORY:</b><br>Fire risk: ELEVATED. Thermal anomaly >600°C exceeds safe limit. Risk of combustion on nearby combustibles. Best Gas Syst 4-channel NDIR monitoring continuous.</div>', unsafe_allow_html=True)
    with t2:
        st.markdown('<div class="panel"><b>02 — OBSERVATION: PBB 30s/270s</b><br>CO2 852ppm • TEMP 28.3°C • HUMIDITY 62% • AIRFLOW 0.4 m/s<br>Sample 1x per 5 menit, 24 jam nonstop, 90 hari circular reset.</div>', unsafe_allow_html=True)
        if st.button("▶ Jalankan Observasi 30s DETECT"):
            with st.spinner("DETECTING 30s..."):
                import time; time.sleep(1)
            st.success("DETECTED: 612°C White Hot confirmed")

            # --- BARIS 68 - TAMBAHAN PERSONAL NDIR4 THERMAL SPECTRAL ---
            # Untuk gas mudah terbakar: LPG, BBM, solar, spiritus, ethanol 45% menguap
            hc_333 = random.randint(11, 18)  # simulasi %LEL dari NDIR 3.33um
            o2_drop = random.random()  # simulasi O2 turun
            co2_rise = random.choice([True, False])

            if hc_333 > 10:  # %LEL
                if o2_drop > 0.5:
                    gas_type = "LPG Bocor - berat di bawah!"
                elif co2_rise:
                    gas_type = "BBM/Solar Menguap - ventilate!"
                else:
                    gas_type = "Ethanol 45% / Spiritus / CH4"
                st.error(f"🚨 ALERT: {gas_type} {hc_333}% LEL | Thermal plume detected CCTV")
            # --- END TAMBAHAN ---

            data = []
            now = datetime.now()
            for i in range(12):
                data.append({"time": now - timedelta(minutes=5*i), "CO2": 850+random.randint(-10,15), "TEMP": 28.3+random.random(), "HOTSPOT": 610+random.randint(0,5)})
            df = pd.DataFrame(data)
            st.line_chart(df.set_index("time")[["CO2","TEMP"]])
            st.dataframe(df, use_container_width=True)
    with t3:
        st.markdown('<div class="panel"><b>03 — OPINION:</b><br>AI CONCLUSION: Confirmed heat source.<br>Recommendation: Suppress fire immediately; isolate section; continue monitoring.</div>', unsafe_allow_html=True)
        if st.button("🚨 Aktifkan Signal Pro"):
            st.error("🚨 ALARM PROFESIONAL AKTIF - Night Vision Fused + Buzzer + Strobo Merah + Laser pointer titik bocor")

st.success("v3.0 FIXED - Ready Streamlit Cloud - Upload gallery/ image dan push!")
