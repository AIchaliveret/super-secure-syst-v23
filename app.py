"""
SUPER SECURE SPACE GUARDIAN - FINAL JURI DIGITHOOK - 3 JAM REVISI
STATUS: SIMULATOR TEORI UNTUK JUDGING - BUKAN ALAT AKTUAL
Fix: FileNotFoundError + Disclaimer Hukum + Tidak klaim NDIR aktual
"""

import streamlit as st
import random
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path

st.set_page_config(page_title="SUPER SECURE SPACE GUARDIAN - JURI SIMULATOR", layout="wide", page_icon="🛡️")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700;800&display=swap');
.hud-top {font-family:'JetBrains Mono', monospace; font-size:16px; font-weight:800; color:white; background: rgba(200,0,0,0.85); padding:12px; border:2px solid #ff0;}
.hud-sub {font-family:'JetBrains Mono', monospace; font-size:12px; color:#ff0; background: rgba(0,0,0,0.9); padding:8px; border:1px solid #ff0;}
.hotspot {font-family:'JetBrains Mono', monospace; font-size:28px; font-weight:900; color:white; text-align:center; text-shadow: 3px 3px 0px black; margin:15px 0; background: rgba(0,0,0,0.6); padding:10px; border:1px solid red;}
.panel {background: rgba(20,20,31,0.95); border:1px solid #19AC57; border-radius:12px; padding:14px; margin:10px 0; color:white;}
.disclaimer {background: rgba(255,255,0,0.9); color:black; font-weight:800; padding:10px; border:2px solid red; text-align:center;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hud-top">🛡️ SUPER SECURE SPACE GUARDIAN - SIMULATOR TEORI UNTUK JURI DIGITHOOK | JUDGING IN PROGRESS | LOC: JAKARTA WAREHOUSE -6.2088°S, 106.8456°E</div>', unsafe_allow_html=True)
st.markdown('<div class="hud-sub">⚠️ DISCLAIMER: INI ADALAH SIMULATOR DASHBOARD UNTUK PENILAIAN TEORI 01-02-03. DATA GAS DI BAWAH INI ADALAH DATA SIMULASI UI UNTUK DEMO, BUKAN DATA SENSOR NDIR AKTUAL. ALAT AKTUAL ROBOTIK DIKEMBANGKAN TERPISAH DI RUANG TEDUH.</div>', unsafe_allow_html=True)
st.markdown('<div class="disclaimer">SIMULATOR - BUKAN ALAT DETEKSI KEBAKARAN AKTUAL - UNTUK BELAJAR TEORI & OBSERVASI JURI</div>', unsafe_allow_html=True)

col_img, col_side = st.columns([2.5,1])

img_path = Path("gallery/image_20261015_163716.webp")
img_path_alt = Path("image_20261015_163716.webp")

with col_img:
    if img_path.exists():
        st.image(str(img_path), use_container_width=True, caption="HMDS-35 85% TRANSP - SIMULATOR VISUAL - THE BEST FINAL")
    elif img_path_alt.exists():
        st.image(str(img_path_alt), use_container_width=True)
    else:
        st.warning("⚠️ Upload file gallery/image_20261015_163716.webp ke GitHub untuk HUD. Saat ini pakai placeholder simulator.")
        st.markdown('<div style="background: linear-gradient(to bottom, #333, #111); height:380px; display:flex; align-items:center; justify-content:center; border:1px solid #19AC57; color:white; font-family:monospace; text-align:center;">GUDANG JAKARTA — AREA C12 — SIMULATOR<br>HOTSPOT 612°C WHITE HOT (SIMULASI UI)<br>UPLOAD image_20261015_163716.webp TO gallery/</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="hotspot">→ HOTSPOT DETECTED SIMULASI — WHITE HOT 612°C — THERMAL ANOMALY (UI DEMO)</div>', unsafe_allow_html=True)

with col_side:
    st.markdown("### 🛡️ F-21 SYSTEM SIMULATOR v3.0 JURI")
    st.metric("Cycle", "5:00", "30s DETECT / 270s STANDBY SIMULASI")
    st.metric("System", "4-NDIR SIMULATOR", "CH4 3.33, CO2 4.26, CO 4.64, Ref 3.91 - SIMULASI")
    st.metric("Status", "JUDGING", "Disithook - Teori & Observasi")

    mode = st.radio("PILIH MODE SIMULATOR", ["MODE 1 - EARLY GUARD (SIMULASI)", "MODE 2 - HEALTH ROOM IDEAL (SIMULASI)"], index=0)

    if mode == "MODE 1 - EARLY GUARD (SIMULASI)":
        st.info("**Safety Simulator:** MLX90640 32x24 White Hot + IMX219 + 850nm IR Fusion + Gas NDIR - DATA SIMULASI UNTUK TEORI JURI")
    else:
        st.success("**Ruangan Ideal Simulator:** SHT41 22-26°C, RH 40-60%, CO2<1000ppm - SIMULASI")

    st.divider()
    t1, t2, t3 = st.tabs(["01 THEORY (JURI)", "02 OBSERVATION 30s (SIMULASI)", "03 OPINION AI (TEORI)"])

    with t1:
        st.markdown('<div class="panel"><b>01 — THEORY UNTUK JURI:</b><br>Fire risk theory: Jika thermal anomaly >600°C + HC >10% LEL, risiko pembakaran meningkat. NDIR 4-channel: 3.33um HC (BBM/LPG/Ethanol 45C), 4.26um CO2, 4.64um CO, 3.91um Ref. O2 drop >0.5% indikasi LPG berat di bawah. Di mall/plaza/DPR, power WAJIB kabel, data bisa WiFi atau kabel LAN untuk stabilitas. ESP32 sebagai otak + koneksi WiFi include.<br><br><b>AKTUAL vs SIMULATOR:</b> Simulator ini pakai data random untuk demo UI teori. Alat aktual robotik baca voltase NDIR beneran di ruang teduh (ESP32).</div>', unsafe_allow_html=True)
    with t2:
        st.markdown('<div class="panel"><b>02 — OBSERVATION PBB 30s/270s (SIMULASI UI UNTUK JURI):</b><br>Data di bawah adalah SIMULASI untuk menunjukkan cara kerja dashboard. Sample 1x per 5 menit, 24 jam nonstop, 90 hari circular reset - KONSEP TEORI.<br><br>CO2 852ppm (SIM) • TEMP 28.3°C (SIM) • HUMIDITY 62% (SIM) • AIRFLOW 0.4 m/s (SIM)</div>', unsafe_allow_html=True)
        if st.button("▶ Jalankan Observasi 30s DETECT (SIMULASI)"):
            with st.spinner("DETECTING 30s SIMULASI..."):
                import time; time.sleep(1)
            st.success("SIMULASI: 612°C White Hot terdeteksi (DEMO UI)")
            
            # SIMULASI DENGAN LABEL JELAS - TIDAK KLAIM AKTUAL
            st.warning("⚠️ DATA DI BAWAH INI SIMULASI UI - BUKAN DATA SENSOR AKTUAL")
            hc_sim = random.randint(2, 8)  # SIMULASI RENDAH - TIDAK BAHAYA
            temp_sim = 28.3 + random.random()*2
            
            # JANGAN TAMPILKAN ALERT BAHAYA PALSU - HANYA INFO TEORI
            st.info(f"SIMULASI UI: HC {hc_sim}% LEL (simulasi) | TEMP {temp_sim:.1f}°C (simulasi) - Jika aktual >10% LEL + thermal >600°C = teori bahaya kebakaran")
            
            data = []
            now = datetime.now()
            for i in range(12):
                data.append({"time": now - timedelta(minutes=5*i), "CO2_SIM": 850+random.randint(-10,15), "TEMP_SIM": 28.3+random.random(), "HOTSPOT_SIM": 610+random.randint(0,5)})
            df = pd.DataFrame(data)
            st.line_chart(df.set_index("time")[["CO2_SIM","TEMP_SIM"]])
            st.dataframe(df, use_container_width=True)
            st.caption("Grafik di atas adalah SIMULASI untuk demo cara kerja observasi 5 menit - bukan data aktual")
            
    with t3:
        st.markdown('<div class="panel"><b>03 — OPINION AI (TEORI UNTUK JURI):</b><br>Jika sistem aktual robotik (ESP32 + NDIR 4 + thermal + CCTV) mendeteksi:<br>- HC >10% LEL AKTUAL + thermal >600°C AKTUAL = Confirmed heat source + flammable vapor<br>- O2 drop >0.5% = LPG bocor berat di bawah<br>- Temp 40-50°C + HC naik = Ethanol 45°C / spiritus menguap<br><br>Rekomendasi teori: Suppress fire, isolate section, ventilasi paksa, cut gas valve otomatis via relay. Pompa 350mL ON 24 jam. Power WAJIB kabel untuk enterprise mall/plaza/DPR/Polri/TNI.<br><br>OPINI INI ADALAH TEORI - ALAT AKTUAL DIUJI DI RUANG TEDUH TERPISAH.</div>', unsafe_allow_html=True)
        if st.button("🚨 Simulasi Signal Pro (TEORI)"):
            st.error("🚨 SIMULASI ALARM TEORI: Buzzer + Strobo Merah + Laser pointer - Ini simulasi UI untuk juri, bukan alarm aktual")

st.success("✅ FINAL JURI DIGITHOOK - SIMULATOR TEORI SIAP DEPLOY - AMAN HUKUM - TIDAK KLAIM AKTUAL")
st.caption("File ini untuk juri Digithook only. Data gas adalah SIMULASI UI. Alat aktual robotik NDIR 4 + thermal + CCTV dikembangkan terpisah di ruang teduh dengan ESP32. Power WAJIB kabel, data WiFi/kabel LAN.")
