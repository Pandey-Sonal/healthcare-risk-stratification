import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Healthcare Risk Stratification",
    page_icon="🏥",
    layout="wide"
)


# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("Risk_model1.pkl")


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
<style>

.stApp {
    background-color: #f5f7fb;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Header */
.main-header {
    background: linear-gradient(135deg, #173f5f, #20639b);
    padding: 30px 35px;
    border-radius: 18px;
    color: white;
    margin-bottom: 30px;
}

.main-header h1 {
    font-size: 34px;
    margin-bottom: 8px;
}

.main-header p {
    font-size: 16px;
    margin-bottom: 0;
    opacity: 0.9;
}

/* Section title */
.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #1f2937;
    margin-top: 15px;
    margin-bottom: 15px;
}

/* Metric cards */
.metric-card {
    background-color: white;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.05);
    text-align: center;
}

.metric-label {
    font-size: 13px;
    color: #6b7280;
    margin-bottom: 8px;
    font-weight: 600;
}

.metric-value {
    font-size: 25px;
    font-weight: 700;
    color: #173f5f;
}

/* Risk cards */
.risk-card {
    padding: 35px;
    border-radius: 18px;
    text-align: center;
    min-height: 170px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.high-risk {
    background-color: #fff1f2;
    border: 2px solid #ef4444;
}

.low-risk {
    background-color: #f0fdf4;
    border: 2px solid #22c55e;
}

.risk-title {
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 12px;
}

.high-risk-title {
    color: #dc2626;
}

.low-risk-title {
    color: #16a34a;
}

.risk-description {
    color: #4b5563;
    font-size: 15px;
}

/* Probability card */
.probability-card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.05);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #eef3f8;
}

/* Footer */
.footer {
    text-align: center;
    color: #6b7280;
    font-size: 13px;
    margin-top: 30px;
}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-header">'
    '<h1>🏥 Healthcare Risk Stratification</h1>'
    '<p>Machine learning powered patient risk assessment dashboard</p>'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("👤 Patient Information")

st.sidebar.write(
    "Enter patient details to generate a risk prediction."
)

st.sidebar.divider()


age = st.sidebar.number_input(
    "Age",
    min_value=0,
    max_value=120,
    value=50,
    step=1
)


length_of_stay = st.sidebar.number_input(
    "Length of Stay (days)",
    min_value=0,
    value=5,
    step=1
)


treatment_cost = st.sidebar.number_input(
    "Treatment Cost",
    min_value=0.0,
    value=5000.0,
    step=500.0
)


st.sidebar.divider()


predict_button = st.sidebar.button(
    "🔍 Generate Risk Prediction",
    use_container_width=True
)


# =========================================================
# PATIENT OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-title">📊 Patient Overview</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        f'<div class="metric-card">'
        f'<div class="metric-label">PATIENT AGE</div>'
        f'<div class="metric-value">{age} years</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f'<div class="metric-card">'
        f'<div class="metric-label">LENGTH OF STAY</div>'
        f'<div class="metric-value">{length_of_stay} days</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f'<div class="metric-card">'
        f'<div class="metric-label">TREATMENT COST</div>'
        f'<div class="metric-value">${treatment_cost:,.0f}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


st.write("")


# =========================================================
# RISK PREDICTION
# =========================================================

if predict_button:

    # Create model input
    input_data = pd.DataFrame(
        [[age, length_of_stay, treatment_cost]],
        columns=[
            "Age",
            "LengthOfStay",
            "TreatmentCost"
        ]
    )


    # Make prediction
    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    probability_percent = probability * 100


    # -----------------------------------------------------
    # Risk Assessment
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">🎯 Risk Assessment</div>',
        unsafe_allow_html=True
    )


    result_col, probability_col = st.columns([1.3, 1])


    # =====================================================
    # RISK RESULT
    # =====================================================

    with result_col:

        if prediction == 1:

            st.markdown(
                '<div class="risk-card high-risk">'
                '<div class="risk-title high-risk-title">'
                '🔴 HIGH RISK'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

            st.write(
                "The model predicts a higher probability "
                "of an adverse patient outcome."
            )

        else:

            st.markdown(
                '<div class="risk-card low-risk">'
                '<div class="risk-title low-risk-title">'
                '🟢 LOW RISK'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

            st.write(
                "The model predicts a lower probability "
                "of an adverse patient outcome."
            )


    # =====================================================
    # RISK PROBABILITY
    # =====================================================

    with probability_col:

        st.markdown(
            '<div class="probability-card">'
            '<h3>Risk Probability</h3>'
            '</div>',
            unsafe_allow_html=True
        )

        st.metric(
            "Predicted Probability",
            f"{probability_percent:.1f}%"
        )

        st.progress(probability)

        st.caption(
            f"Probability of adverse outcome: "
            f"{probability_percent:.1f}%"
        )


else:

    st.info(
        "👈 Enter patient information in the sidebar "
        "and click **Generate Risk Prediction**."
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    '<div class="footer">'
    'Healthcare Analytics • Machine Learning Risk Stratification'
    '<br><br>'
    'This application is a predictive analytics demonstration '
    'and should not be used as a medical diagnosis.'
    '</div>',
    unsafe_allow_html=True
)