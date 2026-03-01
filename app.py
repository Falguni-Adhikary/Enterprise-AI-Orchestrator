import time
import streamlit as st
from orchestrator import generate_executive_brief

st.set_page_config(page_title="Enterprise AI Orchestrator", layout="wide")

st.title("🏗️ Enterprise AI Orchestration System")

st.markdown("""
### 🧠 Internal Automation Prototype

This system simulates a multi-agent AI orchestration layer used inside enterprise environments.
It routes business updates through specialized intelligence agents and produces a structured executive brief.
""")

st.markdown("### 🧩 Agent Status Panel")

colA, colB, colC = st.columns(3)

with colA:
    st.success("Summary Agent: Active")

with colB:
    st.success("Risk Agent: Active")

with colC:
    st.success("Strategy Agent: Active")


st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    text = st.text_area(
        "📥 Enter Business Update / Operational Report",
        height=250,
        placeholder="Paste business update here..."
    )

with col2:
    st.markdown("### 🔎 Active Agents")
    st.markdown("""
    - Summary Agent  
    - Risk Detection Agent  
    - Strategy Intelligence Agent  
    """)

    st.markdown("### ⚙ System Mode")
    st.success("Rule-Based Orchestration (LLM-Ready Architecture)")

st.divider()

if st.button("🚀 Generate Executive Brief"):
    if text.strip() == "":
        st.warning("Please enter content before generating report.")
    else:
        st.markdown("### 🛰 Agent Execution Log")

        with st.spinner("Orchestrating multi-agent analysis..."):
    
            log = st.empty()

            log.markdown("**[1/4] Routing to Summary Agent...**")
            time.sleep(0.7)

            log.markdown("**[2/4] Running Risk Detection Agent...**")
            time.sleep(0.7)

            log.markdown("**[3/4] Executing Strategy Intelligence Agent...**")
            time.sleep(0.7)

            log.markdown("**[4/4] Aggregating outputs...**")
            time.sleep(0.7)

            result = generate_executive_brief(text)

            # 📊 Intelligence Metrics Panel
            st.markdown("### 📊 Intelligence Metrics")

            m1, m2, m3 = st.columns(3)

            m1.metric("Risks Detected", len(result["risks"]))
            m2.metric("Strategic Signals", len(result["strategies"]))
            m3.metric("Summary Length", len(result["summary"].split()))

            st.subheader("📄 Executive Output")

            with st.expander("🧾 Executive Overview", expanded=True):
                st.info(result["summary"])

            with st.expander("⚠ Key Risks Identified"):
                if result["risks"]:
                    for r in result["risks"]:
                        st.error(r)
                else:
                    st.success("No significant risks detected.")

            with st.expander("📈 Strategic Recommendations"):
                if result["strategies"]:
                    for s in result["strategies"]:
                        st.success(s)
                else:
                    st.info("No strategic signals identified.")

            report_text = f"""
            #EXECUTIVE BRIEF

            Summary:
            {result['summary']}

            Risks:
            {chr(10).join(result['risks']) if result['risks'] else 'None'}

            Strategies:
            {chr(10).join(result['strategies']) if result['strategies'] else 'None'}
            """

            st.download_button(
                label="📥 Download Executive Brief",
                data=report_text,
                file_name="executive_brief.txt",
                mime="text/plain"
            )
st.divider()

st.markdown("""
### 🏗 Architecture Overview

User Input  
↓  
Orchestrator Layer  
↓  
Multiple Specialized Agents  
↓  
Aggregated Executive Brief  

Future versions will integrate Claude API for semantic reasoning and advanced orchestration.
""")