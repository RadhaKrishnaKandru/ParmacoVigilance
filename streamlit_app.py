import streamlit as st
import requests


st.set_page_config(
    page_title="PharmacoVigilance AI",
    page_icon="💊",
    layout="wide"
)

st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #F7F9FB;
}

/* Title */
h1 {
    color: #1F3A5F;
    text-align: center;
    font-weight: 700;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #6B7280;
    font-size: 15px;
    margin-bottom: 10px;
}

/* Input */
textarea {
    background-color: #FFFFFF !important;
    border-radius: 10px !important;
    border: 1px solid #D1D5DB !important;
}

/* Button */
.stButton > button {
    background-color: #2563EB;
    color: white;
    border-radius: 8px;
    height: 45px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #1D4ED8;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border-radius: 12px;
    padding: 18px;
    border: 1px solid #E5E7EB;
}

/* Narrative */
.stAlert {
    background-color: #EFF6FF;
    border-left: 4px solid #2563EB;
}

</style>
""", unsafe_allow_html=True)


st.markdown("<h1>PharmacoVigilance 💊 Safety System</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>AI-powered adverse event analysis & signal detection</p>", unsafe_allow_html=True)

st.divider()


st.subheader("📝 Case Input")

user_input = st.text_area(
    "Enter patient case description",
    height=120,
    placeholder="e.g., I started DrugX last week and now I have severe headache and nausea. I went to hospital."
)

analyze_btn = st.button("Analyze Case", use_container_width=True)

st.divider()

def color_text(text, color):
    return f"<span style='color:{color}; font-weight:600'>{text}</span>"

# 🔹 Processing
if analyze_btn:
    if not user_input.strip():
        st.warning("Please enter a case description.")
    else:
        with st.spinner("Analyzing case..."):

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    json={"text": user_input}
                )

                result = response.json()

                st.success("Analysis Complete")

                
                col1, col2, col3, col4 = st.columns(4)

                seriousness = result["seriousness"]["label"]
                causality = result["causality"]["causality"]
                signal_flag = result["signal"][0]["signal"]
                hospitalization = result["data"].get("hospitalization", False)

                serious_color = "#DC2626" if seriousness == "SERIOUS" else "#059669"
                signal_color = "#DC2626" if signal_flag else "#059669"
                hospital_color = "#DC2626" if hospitalization else "#059669"
                causal_color = "#2563EB"

                with col1:
                    st.markdown(
                        f"**Seriousness**<br>{color_text(seriousness, serious_color)}",
                        unsafe_allow_html=True
                    )

                with col2:
                    st.markdown(
                        f"**Causality**<br>{color_text(causality.upper(), causal_color)}",
                        unsafe_allow_html=True
                    )

                with col3:
                    st.markdown(
                        f"**Signal**<br>{color_text('YES' if signal_flag else 'NO', signal_color)}",
                        unsafe_allow_html=True
                    )

                with col4:
                    st.markdown(
                        f"**Hospitalization**<br>{color_text('YES' if hospitalization else 'NO', hospital_color)}",
                        unsafe_allow_html=True
                    )

                st.divider()

                
                st.subheader("📝 Clinical Narrative")
                st.info(result["narrative"])

                st.divider()

               
                with st.expander("Structured Data"):
                    st.json(result["data"])

                with st.expander("Seriousness Details"):
                    st.json(result["seriousness"])

                with st.expander("Causality Details"):
                    st.json(result["causality"])

                with st.expander("Signal Details"):
                    st.json(result["signal"])

            except Exception as e:
                st.error(f"Error: {e}")
