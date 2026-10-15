
"""
SUPER SECURE SYST v3.0 - AMD ACT III FINAL
Track: Intelligent Industry - Monitor safety conditions
THE BEST - F-21 / HMDS-35 85% TRANSP BOLD LARGE FONT

Koreksi Final:
- OBSERVATION: 30s DETECT + 270s STANDBY = 5 menit cycle (PBB Standard)
- Cuma 2 MODE: MODE 1 Early Guard (Heat+Gas), MODE 2 Health Room (Suhu ideal + banjir)
- HUD 85% transparent ultra, font besar kontras tebal putih + outline hitam
- Best Gas Syst: 4-channel NDIR (CH4 3.33um, CO2 4.26um, CO 4.64um, Ref 3.91um) + O2/H2S + Pump 350mL/min
"""

import streamlit as st
import time
import random
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="SUPER SECURE SYST v3.0 - HMDS-35", layout="wide", page_icon="🛩️")

# CSS F-21 HMDS Style - 85% TRANSP BOLD
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700;800&display=swap');
.hud-top {font-family:'JetBrains Mono', monospace; font-size:22px; font-weight:800; color:white; text-shadow: 2px 2px 0px black, 0 0 8px black; letter-spacing:1px; background: rgba(0,0,0,0.4); padding:8px; border:1px solid rgba(255,255,255,0.3);}
.hotspot {font-family:'JetBrains Mono', monospace; font-size:36px; font-weight:900; color:white; text-align:center; text-shadow: 3px 3px 0px black, 0 0 12px black; margin:20px 0;}
.panel {background: rgba(0,0,0,0.45); border:1px solid rgba(255,255,255,0.25); padding:14px; backdrop-filter: blur(3px);}
.panel b {font-family:'JetBrains Mono', monospace; font-size:18px; font-weight:800; color:white; text-shadow: 2px 2px 0 black;}
.panel p {font-family:'JetBrains Mono', monospace; font-size:15px; color:white; text-shadow: 1px 1px 0 black; line-height:1.4;}
.badge {background: rgba(255,0,0,0.2); border:1px solid red; color:white; padding:4px 8px; font-weight:800;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hud-top">HMDS-35 | PILOT-ASR | FUSED THERMAL+RGB | 85% TRANSP &nbsp;&nbsp;&nbsp;&nbsp; LOC: JAKARTA WAREHOUSE • -6.2088°S, 106.8456°E • 07:42Z 2024-11-22</div>', unsafe_allow_html=True)

col_img, col_side = st.columns([2.5,1])

with col_img:
    st.image("/mnt/data/gallery/image_20261015_163716.webp", use_container_width=True)
    st.markdown('<div class="hotspot">→ HOTSPOT DETECTED — WHITE HOT<br>612°C — THERMAL ANOMALY</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; color:#aaa; font-family:monospace;'>
    GUDANG JAKARTA — AREA C12 — BAHAYA KEBAKARAN | LOGISTIK • JAKARTA • FRAGILE
    </div>
    """, unsafe_allow_html=True)

with col_side:
    st.markdown("### ✈️ F-21 SYSTEM")
    st.metric("Cycle", "5:00", "30s DETECT / 270s STANDBY")
    st.metric("Best Gas Syst", "4-NDIR Active", "CH4 3.33um, CO2 4.26um, CO 4.64um, Ref 3.91um")
    st.metric("Pump", "350 mL/min", "O2/H2S Enabled")

    mode = st.radio("PILIH MODE (CUMA 2)", ["MODE 1 - EARLY GUARD", "MODE 2 - HEALTH ROOM / IDEAL"], index=0)

    if mode == "MODE 1 - EARLY GUARD":
        st.info("**Safety:** MLX90640 32x24 White Hot 612C + IMX219 + 850nm IR Fusion + Gas NDIR + O2/H2S")
    else:
        st.success("**Ruangan Ideal:** SHT41 22-26°C, RH 40-60%, CO2<1000ppm | Bocor cair/banjir = QR Cert ESC/POS")

    st.divider()
    t1, t2, t3 = st.tabs(["01 THEORY", "02 OBSERVATION", "03 OPINION"])

    with t1:
        st.markdown('<div class="panel"><b>01 — THEORY:</b><p>Fire risk: ELEVATED. Thermal anomaly >600°C exceeds safe limit. Risk of combustion on nearby combustibles. Best Gas Syst 4-channel NDIR monitoring continuous.</p></div>', unsafe_allow_html=True)
    with t2:
        st.markdown('<div class="panel"><b>02 — OBSERVATION: PBB 30s/270s</b><p>CO2 852ppm • TEMP 28.3°C • HUMIDITY 62% • AIRFLOW 0.4 m/s<br>Sample 1x per 5 menit, 24 jam nonstop, 90 hari circular reset. Hemat memory & daya.</p></div>', unsafe_allow_html=True)
        if st.button("▶️ Jalankan Observasi 30s DETECT"):
            with st.spinner("DETECTING 30s... MLX90640 scanning..."):
                time.sleep(2)
            st.success("DETECTED: 612°C White Hot confirmed")
            # Generate dummy rolling data
            data = []
            now = datetime.now()
            for i in range(12):
                data.append({"time": now - timedelta(minutes=5*i), "CO2": 850+random.randint(-10,15), "TEMP": 28.3+random.random(), "HOTSPOT": 610+random.randint(0,5)})
            df = pd.DataFrame(data)
            st.line_chart(df.set_index("time")[["CO2","TEMP"]])
            st.dataframe(df, use_container_width=True)
            st.caption("Grafik rolling: 1 titik per 5 menit (30s DETECT) - Sesuai PBB")

    with t3:
        st.markdown('<div class="panel"><b>03 — OPINION:</b><p>AI CONCLUSION: Confirmed heat source.<br>Recommendation: Suppress fire immediately; isolate section; continue monitoring.</p></div>', unsafe_allow_html=True)
        if st.button("🚨 Aktifkan Signal Pro Robotik"):
            st.error("🚨 ALARM PROFESIONAL AKTIF")
            st.markdown("""
            - **Night Vision Fused:** RGB + Thermal White Hot auto ON saat terdeteksi
            - **Signal Bahaya:** Buzzer 85dB + Lampu Strobo Merah + Relay Auto Shutdown
            - **Titik Bocor:** Ditunjuk laser pointer + BBOX HUD + Koordinat -6.2088,106.8456
            - **Area Kontaminasi:** Heatmap overlay + QR Cert 'Ruangan Tidak Ideal' ESC/POS
            - **Aktivasi:** Profesional - sesuai standar industri safety
            """)

st.divider()
st.markdown("### 📦 GitHub Deploy - SUPER SECURE SYST v2.3 → v3.0 THE BEST")
st.code("""
git add app.py README.md
git commit -m "v3.0 THE BEST - F-21 HMDS 85% TRANSP BOLD LARGE FONT - PBB 30s/270s - 2 Modes Only"
git push origin main
""", language="bash")
st.success("Siap push ke https://github.com/Alchaliveret/super-secure-syst-v23 - AMD ACT III FINAL CORRECTED")
