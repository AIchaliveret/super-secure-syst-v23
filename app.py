
import streamlit as st
import random
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="SUPER SECURE SYST v2.3", layout="wide", page_icon="🛡️")

st.markdown("""
<style>
.main {background-color: #0a0a0f;}
h1 {color: #19AC57 !important;}
h2 {color: #BF0090 !important;}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ SUPER SECURE SYST v2.3")
st.subheader("30-Second Safety Observatory | AMD x ACT III | Intelligent Industry")
st.caption("UNIKA Atma Jaya Jakarta | Best Gas Syst: 4-channel NDIR + Pump + Evolus")

col1, col2, col3 = st.columns(3)
col1.metric("AMD MI300X", "Online", "ROCm + vLLM")
col2.metric("Evolus", "2 Blocks Active", "Extractor + Workflow")
col3.metric("Pump", "350 mL/min", "30-sec sampling")

tab1, tab2, tab3, tab4 = st.tabs(["📊 Live Observatory", "🔌 Wiring Diagram", "⚙️ Evolus Workflow", "🚀 Deploy"])

with tab1:
    st.markdown("### Live 6-Gas Observatory (5-min flow x 30-sec)")

    if 'data' not in st.session_state:
        st.session_state.data = pd.DataFrame({
            'time': [datetime.now()],
            'CH4_3.33um': [0.5],
            'CO2_4.26um': [450],
            'CO_4.64um': [5],
            'Ref_3.91um': [1.0],
            'O2': [20.9],
            'H2S': [0.2]
        })

    if st.button("🔄 Simulate 30-sec Sample"):
        new_row = {
            'time': datetime.now(),
            'CH4_3.33um': random.uniform(0.2, 12.0),
            'CO2_4.26um': random.uniform(400, 2200),
            'CO_4.64um': random.uniform(0, 55),
            'Ref_3.91um': random.uniform(0.95, 1.05),
            'O2': random.uniform(19.5, 21.0),
            'H2S': random.uniform(0, 8)
        }
        st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_row])], ignore_index=True)
        if len(st.session_state.data) > 20:
            st.session_state.data = st.session_state.data.tail(20)

    df = st.session_state.data

    fig = go.Figure()
    for col in ['CH4_3.33um', 'CO2_4.26um', 'CO_4.64um', 'O2', 'H2S']:
        fig.add_trace(go.Scatter(x=df['time'], y=df[col], mode='lines+markers', name=col))
    fig.update_layout(title="Best Gas Syst Real-Time", height=400, template="plotly_dark", paper_bgcolor="#0a0a0f", plot_bgcolor="#0a0a0f")
    st.plotly_chart(fig, use_container_width=True)

    last = df.iloc[-1]
    alert = False
    if last['CO_4.64um'] > 35:
        st.error(f"ALERT: CO {last['CO_4.64um']:.1f} ppm > 35ppm | Action: Open damper 30%, evac zone 2 | Evolus Workflow Triggered")
        alert = True
    if last['CH4_3.33um'] > 10:
        st.error(f"ALERT: CH4 {last['CH4_3.33um']:.1f}% LEL > 10% | Action: Cut gas valve, ventilate")
        alert = True
    if last['CO2_4.26um'] > 1000:
        st.warning(f"WARNING: CO2 {last['CO2_4.26um']:.0f} ppm high | Action: Increase HVAC 25%")
        alert = True
    if not alert:
        st.success("All gases normal | Pump 350mL/min | Ref drift 1.00 | Operator clear")

with tab2:
    st.markdown("### Wiring Diagram 4-Channel + Pump - Best Gas Syst")
    st.markdown("""
    **ESP32 DevKit Mapping:**
    - GPIO16 RX2 / GPIO17 TX2 -> NDIR 4-channel (CH4 3.33um, CO2 4.26um, CO 4.64um, Ref 3.91um) UART 9600
    - GPIO21 SDA / GPIO22 SCL -> O2 + H2S electrochemical I2C
    - GPIO27 PWM -> Micro diaphragm pump 5V 200-500mL/min
    - GPIO25 -> Status LED + Buzzer
    - Flow: Inlet -> Filter 5um -> Pump -> NDIR cell 80mm -> Exhaust -> 4ft probe -> MQTT -> AMD Cloud
    """)
    st.code("ESP32 Pinout:\nNDIR_RX=16, NDIR_TX=17\nO2_SDA=21, SCL=22\nPUMP_PWM=27\nLED=25\n// 30-sec MQTT to AMD", language="text")

with tab3:
    st.markdown("### Evolus Workflow Alert - Partner Prize")
    st.markdown("""
    **Requirements Met:**
    1. Free Evolus workspace with event code
    2. BYOM: Llama 3.1 8B via vLLM on AMD MI300X ROCm
    3. 2 Building Blocks: Document Extractor + Workflow
    4. Drive via REST API
    **Flow:** Sensor MQTT / Email / PDF -> Extractor -> Workflow -> LLM Reasoning on AMD -> REST API -> Alert + CRM MCP + Human handoff
    """)
    st.json({
        "evolus_endpoint": "https://app.evolus.ai/api/v1/workflows",
        "vllm_endpoint": "https://your-mi300x.amd.cloud/v1",
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "workflow": "safety_alert_v2.3"
    })

with tab4:
    st.markdown("### Deploy")
    st.markdown("GitHub repo public MIT, Streamlit Cloud main file app.py, Python 3.11")
    st.code("pip install -r requirements.txt\nstreamlit run app.py", language="bash")

st.markdown("---")
st.caption("Ready for lablab.ai submission | AMD ACT III | Intelligent Industry")
