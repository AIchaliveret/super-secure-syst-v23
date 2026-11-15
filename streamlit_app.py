
# SUPER-SECURE SYST v23 - AUTO-ACTIVE + PAUSE + KREDIT
# Repo: https://github.com/AIchaliveret/super-secure-syst-v23
# Sama seperti Super-Infrared AUTO: AUTO gerak sendiri, bisa PAUSE, ada limit kredit

import streamlit as st
import random, time, pandas as pd
from datetime import datetime

st.set_page_config(page_title="SUPER-SECURE SYST v23 - AUTO", layout="wide")

if "paused" not in st.session_state: st.session_state.paused = False
if "credit" not in st.session_state: st.session_state.credit = 98
if "log" not in st.session_state: st.session_state.log = []
if "auto" not in st.session_state: st.session_state.auto = True

st.markdown("""
<div style="background:linear-gradient(90deg,#0F1B3D,#DC2626);padding:16px 20px;border-radius:12px;color:white">
<h1 style="margin:0">SUPER-SECURE SYST v23 — AUTO-ACTIVE</h1>
<p style="margin:4px 0 0 0">SENSE → DECIDE → ACT &nbsp;|&nbsp; <b>DIGIT HUB SUPER SECURE</b> — Sensor Aktif 24 Jam &nbsp;|&nbsp; PAUSE / RESUME Tersedia</p>
</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns([1,1,1,2])
with c1:
    if st.button("⏸️ PAUSE" if not st.session_state.paused else "▶️ RESUME"):
        st.session_state.paused = not st.session_state.paused
        st.rerun()
with c2:
    if st.button("🔄 AUTO: ON" if st.session_state.auto else "🔄 AUTO: OFF"):
        st.session_state.auto = not st.session_state.auto
        st.rerun()
with c3:
    st.metric("💳 Sisa Kredit", f"{st.session_state.credit} / 100", "FREE CORE")
with c4:
    st.info("PAUSE = Baca pelan-pelan. AUTO = Gerak sendiri tiap 5 detik untuk video. Kredit habis = Berhenti otomatis.")

if st.session_state.paused:
    st.warning("⏸️ SUPER-SECURE DI-PAUSE — Sensor berhenti. Klik RESUME untuk jalan lagi.")
    st.stop()

if st.session_state.auto:
    if st.session_state.credit > 0:
        st.session_state.credit -= 1
    else:
        st.error("⚠️ KREDIT HABIS — FREE CORE 100 scan/hari. Upgrade PAID untuk unlimited.")
        if st.button("🔁 Reset Kredit Demo"):
            st.session_state.credit = 100
            st.rerun()
        st.stop()

# Sensor Super Secure - 4 kartu Digit Hub
co2 = random.randint(410, 1150)
voc = round(random.uniform(0.4, 3.8), 1)
suhu = round(random.uniform(25.0, 32.5), 1)
humid = round(random.uniform(55.0, 75.0), 1)
api = round(random.uniform(28.0, 42.0), 1)
csi = random.choice(["ADA ORANG - Normal", "RUANGAN KOSONG", "ADA ORANG - Diam"])
secure_action = "AUTO: Filter HEPA + Fan ON - Udara perlu dibersihkan" if co2>1000 else "AUTO: Semua aman, filter normal, sensor standby waspada"

a1,a2,a3,a4 = st.columns(4)
with a1: st.metric("CO2", f"{co2} ppm", "AUTO • Live")
with a2: st.metric("VOC / Bau", f"{voc} ppm", "AUTO • Live")
with a3: st.metric("Suhu Ruangan", f"{suhu} °C", "AUTO • Live")
with a4: st.metric("Kelembaban", f"{humid} %", "AUTO • Live")
st.markdown(f"**AI Agent Action:** `{secure_action}` | **Suhu Api:** {api}°C Aman | **WiFi-CSI:** {csi}")

st.markdown(f'<div style="background:#FEF3C7;padding:14px;border-radius:10px"><h3>🛡️ Super Secure — Digit Hub</h3><p><b>{secure_action}</b></p><p style="font-size:13px">Super Secure bukan hanya monitor. Kalau udara kotor, dia bertindak sendiri. Kalau api terdeteksi, buzzer + matikan listrik OTOMATIS. Kalau orang jatuh, WiFi-CSI kirim ALERT DARURAT.</p></div>', unsafe_allow_html=True)

st.markdown("### 6 Filter Agent — Semua AUTO")
x1,x2,x3 = st.columns(3)
with x1: st.info("1. Api / Panas — MLX90640 — AMAN")
with x2: st.info("2. Asap / Gas — MQ-2 + NDIR — AMAN")
with x3: st.info("3. Udara / Debu — PMS5003 — AUTO")
y1,y2,y3 = st.columns(3)
with y1: st.info(f"4. Gerak Manusia — WiFi-CSI — {csi}")
with y2: st.info("5. Bau / VOC — ENS160 — AUTO")
with y3: st.info("6. RAG Decision — Vultr — AKTIF")

now = datetime.now().strftime("%H:%M:%S")
st.session_state.log.insert(0, {"Waktu": now, "CO2": co2, "Suhu": suhu, "WiFi-CSI": csi, "Aksi AUTO": secure_action, "Kredit Sisa": st.session_state.credit})
st.markdown("### Recent Log — Sensor Aktif (Demo Live)")
st.dataframe(pd.DataFrame(st.session_state.log[:6]), use_container_width=True)
st.caption("Super Secure Syst v23 - AUTO-ACTIVE. PAUSE untuk baca, RESUME untuk jalan lagi. Kredit FREE CORE 100/hari.")

if st.session_state.auto and not st.session_state.paused:
    st.caption("🎥 MODE VIDEO: Demo refresh sendiri tiap 5 detik. Tinggal rekam layar.")
    time.sleep(5)
    st.rerun()
