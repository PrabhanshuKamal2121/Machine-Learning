import streamlit as st
import pandas as pd 
import joblib

st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS with warm color palette
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Main app background with warm gradient */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a0f0a 25%, #2a1a0f 50%, #1a0f0a 75%, #0a0a0a 100%);
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
        min-height: 100vh;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1000px;
        background: rgba(10, 10, 10, 0.4);
        border-radius: 30px;
        backdrop-filter: blur(15px);
        border: 2px solid rgba(247, 181, 56, 0.2);
        box-shadow: 
            0 0 60px rgba(247, 181, 56, 0.1),
            0 20px 40px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .main .block-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #780116, #F7B538, #DB7C26, #D8572A, #C32F27);
        opacity: 0.8;
    }
    
    /* Enhanced title styling with warm gradient */
    .main-title {
        font-size: 2.8rem;  /* Reduced from 3.5rem */
        font-weight: 800;
        text-align: center;
        background: linear-gradient(135deg, #F7B538, #DB7C26, #D8572A, #C32F27);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        animation: warm-glow 4s ease-in-out infinite alternate;
        letter-spacing: -2px;
        text-shadow: 0 0 40px rgba(247, 181, 56, 0.3);
    }
    
    @keyframes warm-glow {
        from { 
            filter: drop-shadow(0 0 20px rgba(247, 181, 56, 0.4));
            transform: scale(1);
        }
        to { 
            filter: drop-shadow(0 0 40px rgba(219, 124, 38, 0.6));
            transform: scale(1.02);
        }
    }
    
    /* Subtitle styling */
    .subtitle {
        font-size: 1.6rem;  /* Increased from 1.2rem */
        font-weight: 600;   /* Increased from 400 */
        text-align: center;
        color: #E8E8E8;
        margin-bottom: 3rem;
        letter-spacing: 1px;
        opacity: 0.9;
    }
    
    /* Card container styling with warm accents */
    .input-card {
        background: linear-gradient(145deg, 
            rgba(120, 1, 22, 0.1), 
            rgba(26, 15, 10, 0.8), 
            rgba(42, 26, 15, 0.6)
        );
        border: 2px solid rgba(247, 181, 56, 0.3);
        border-radius: 25px;
        padding: 30px;
        margin: 25px 0;
        box-shadow: 
            0 10px 40px rgba(0, 0, 0, 0.4),
            0 0 30px rgba(247, 181, 56, 0.1),
            inset 0 1px 0 rgba(247, 181, 56, 0.1);
        backdrop-filter: blur(15px);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .input-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(247, 181, 56, 0.05), 
            transparent
        );
        transition: left 0.6s ease;
    }
    
    .input-card:hover::before {
        left: 100%;
    }
    
    .input-card:hover {
        border-color: rgba(247, 181, 56, 0.5);
        box-shadow: 
            0 15px 50px rgba(0, 0, 0, 0.5),
            0 0 40px rgba(247, 181, 56, 0.2),
            inset 0 1px 0 rgba(247, 181, 56, 0.2);
        transform: translateY(-5px);
    }
    
    /* Section headers with warm gradient underline */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 2rem;
        text-align: center;
        position: relative;
        padding-bottom: 15px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 3px;
        background: linear-gradient(90deg, #F7B538, #DB7C26, #D8572A);
        border-radius: 2px;
        box-shadow: 0 0 15px rgba(247, 181, 56, 0.5);
    }
    
    /* Enhanced input field styling */
    .stSelectbox > div > div {
        background: linear-gradient(145deg, 
            rgba(15, 15, 15, 0.9), 
            rgba(25, 20, 15, 0.8)
        );
        border: 2px solid rgba(219, 124, 38, 0.4);
        border-radius: 15px;
        box-shadow: 
            0 5px 20px rgba(0, 0, 0, 0.3),
            0 0 15px rgba(219, 124, 38, 0.1);
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .stSelectbox > div > div:hover {
        border-color: rgba(247, 181, 56, 0.6);
        box-shadow: 
            0 8px 25px rgba(0, 0, 0, 0.4),
            0 0 25px rgba(247, 181, 56, 0.2);
        transform: translateY(-2px);
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #F7B538;
        box-shadow: 
            0 8px 25px rgba(0, 0, 0, 0.4),
            0 0 30px rgba(247, 181, 56, 0.3);
    }
    
    .stNumberInput > div > div > input {
        background: linear-gradient(145deg, 
            rgba(15, 15, 15, 0.9), 
            rgba(25, 20, 15, 0.8)
        );
        border: 2px solid rgba(219, 124, 38, 0.4);
        border-radius: 15px;
        color: #FFFFFF;
        box-shadow: 
            0 5px 20px rgba(0, 0, 0, 0.3),
            0 0 15px rgba(219, 124, 38, 0.1);
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        font-weight: 500;
        font-size: 1rem;
    }
    
    .stNumberInput > div > div > input:hover {
        border-color: rgba(247, 181, 56, 0.6);
        box-shadow: 
            0 8px 25px rgba(0, 0, 0, 0.4),
            0 0 25px rgba(247, 181, 56, 0.2);
        transform: translateY(-2px);
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #F7B538;
        box-shadow: 
            0 8px 25px rgba(0, 0, 0, 0.4),
            0 0 30px rgba(247, 181, 56, 0.3);
        outline: none;
    }
    
    /* Enhanced Slider styling with warm colors */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #DB7C26, #F7B538);
        box-shadow: 0 0 20px rgba(219, 124, 38, 0.3);
        height: 6px;
    }
    
   
    
    /* Spectacular button styling */
    .stButton > button {
        color: #FFFFFF !important;
        background: linear-gradient(135deg, #780116, #C32F27, #D8572A, #F7B538);
        border: none;
        border-radius: 25px;
        padding: 20px 60px;
        font-size: 1.4rem;
        font-weight: 700;
        box-shadow: 
            0 10px 30px rgba(120, 1, 22, 0.4),
            0 0 40px rgba(247, 181, 56, 0.2);
        transition: all 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
        overflow: hidden;
        font-family: 'Inter', sans-serif;
        cursor: pointer;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255, 255, 255, 0.3), 
            transparent
        );
        transition: left 0.6s ease;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        color: #FFFFFF !important;
        background: linear-gradient(135deg, #C32F27, #D8572A, #F7B538, #DB7C26);
        box-shadow: 
            0 15px 40px rgba(120, 1, 22, 0.6),
            0 0 50px rgba(247, 181, 56, 0.4);
        transform: translateY(-5px) scale(1.05);
    }
    
    .stButton > button:active {
        transform: translateY(-2px) scale(1.02);
    }
    
    /* Enhanced Success and error message styling */
    .stSuccess {
        background: linear-gradient(135deg, 
            rgba(34, 197, 94, 0.2), 
            rgba(22, 163, 74, 0.1)
        );
        border: 2px solid #22C55E;
        border-radius: 20px;
        box-shadow: 
            0 10px 30px rgba(34, 197, 94, 0.2),
            0 0 40px rgba(34, 197, 94, 0.1);
        backdrop-filter: blur(15px);
        padding: 25px;
        margin: 25px 0;
        font-weight: 500;
    }
    
    .stError {
        background: linear-gradient(135deg, 
            rgba(239, 68, 68, 0.2), 
            rgba(220, 38, 38, 0.1)
        );
        border: 2px solid #EF4444;
        border-radius: 20px;
        box-shadow: 
            0 10px 30px rgba(239, 68, 68, 0.2),
            0 0 40px rgba(239, 68, 68, 0.1);
        backdrop-filter: blur(15px);
        padding: 25px;
        margin: 25px 0;
        font-weight: 500;
    }
    
    /* Enhanced label styling */
    .stSelectbox label, .stNumberInput label, .stSlider label {
        color: #F0F0F0;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 10px;
        text-shadow: 0 0 15px rgba(247, 181, 56, 0.2);
        letter-spacing: 0.5px;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.8rem;
            letter-spacing: -1px;
        }
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            margin: 1rem;
            border-radius: 20px;
        }
        .input-card {
            padding: 20px;
            margin: 20px 0;
            border-radius: 20px;
        }
        .stButton > button {
            padding: 18px 45px;
            font-size: 1.2rem;
            letter-spacing: 1px;
        }
        .section-header {
            font-size: 1.3rem;
            letter-spacing: 1px;
        }
    }
    
    /* Loading animation with warm colors */
    @keyframes warm-loading {
        0% { 
            transform: rotate(0deg);
            border-top-color: #F7B538;
        }
        25% { 
            border-top-color: #DB7C26;
        }
        50% { 
            border-top-color: #D8572A;
        }
        75% { 
            border-top-color: #C32F27;
        }
        100% { 
            transform: rotate(360deg);
            border-top-color: #F7B538;
        }
    }
    
    .loading {
        border: 4px solid rgba(247, 181, 56, 0.3);
        border-top: 4px solid #F7B538;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: warm-loading 1.5s linear infinite;
        margin: 20px auto;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, 0.3);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #F7B538, #DB7C26);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #DB7C26, #D8572A);
    }
</style>
""", unsafe_allow_html=True)

# Load model with error handling
@st.cache_resource
def load_model():
    try:
        model = joblib.load('logistic_regression_heart.pkl')
        scaler = joblib.load('scaler.pkl')
        expected_columns = joblib.load('columns.pkl')
        return model, scaler, expected_columns
    except FileNotFoundError:
        st.error("⚠️ Model files not found. Please ensure the model files are in the correct directory.")
        return None, None, None

# Main application
def main():
    # Enhanced title and subtitle
    st.markdown('<h1 class="main-title">❤ Heart Disease Predictor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">by Prabhanshu Kamal </p>', unsafe_allow_html=True)
    
    # Load model
    model, scaler, expected_columns = load_model()
    
    if model is None:
        st.stop()
    
    st.markdown('<p style="text-align: center; color: #E8E8E8; font-size: 1.1rem; margin-bottom: 3rem; font-weight: 500;">Please provide the following details for accurate prediction</p>', unsafe_allow_html=True)
    
    # Personal Information Section
    st.markdown('''
    <div class="input-card">
        <h3 class="section-header">👤 Personal Information</h3>
    ''', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age", 18, 100, 40, help="Your current age in years")
    with col2:
        sex = st.selectbox("Sex", ["M", "F"], help="Biological sex")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Clinical Assessment Section
    st.markdown('''
    <div class="input-card">
        <h3 class="section-header">🩺 Clinical Assessment</h3>
    ''', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"], 
                                help="ATA: Atypical Angina, NAP: Non-Anginal Pain, TA: Typical Angina, ASY: Asymptomatic")
        resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"],
                                 help="Normal: Normal, ST: ST-T wave abnormality, LVH: Left ventricular hypertrophy")
    with col2:
        exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"],
                                     help="Does exercise induce chest pain?")
        st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"],
                              help="Slope of the peak exercise ST segment")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Vital Signs Section
    st.markdown('''
    <div class="input-card">
        <h3 class="section-header">📊 Vital Signs & Lab Results</h3>
    ''', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        resting_bp = st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120,
                            help="Resting blood pressure measurement")
        cholesterol = st.slider("Cholesterol (mg/dL)", 100, 600, 200,
                            help="Serum cholesterol level")
        fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1],
                                help="0: No, 1: Yes")
    with col2:
        max_hr = st.slider("Max Heart Rate", 60, 220, 150,
                         help="Maximum heart rate achieved during exercise")
        oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0,
                          help="ST depression induced by exercise relative to rest")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Prediction Section
    st.markdown('<div style="text-align: center; margin: 4rem 0;">', unsafe_allow_html=True)
    
    if st.button("🔮 Predict Heart Disease Risk"):
        with st.spinner("🧠 Analyzing your health data..."):
            import time
            time.sleep(1)  # Simulate processing time
            
            # Create a raw input dictionary
            raw_input = {
                'Age': age,
                'RestingBP': resting_bp,
                'Cholesterol': cholesterol,
                'FastingBS': fasting_bs,
                'MaxHR': max_hr,
                'Oldpeak': oldpeak,
                'Sex_' + sex: 1,
                'ChestPainType_' + chest_pain: 1,
                'RestingECG_' + resting_ecg: 1,
                'ExerciseAngina_' + exercise_angina: 1,
                'ST_Slope_' + st_slope: 1
            }
            
            input_df = pd.DataFrame([raw_input])
            
            for col in expected_columns:
                if col not in input_df.columns:
                    input_df[col] = 0
            
            input_df = input_df[expected_columns]
            scaled_input = scaler.transform(input_df)
            prediction = model.predict(scaled_input)[0]
            
            # Display results
            if prediction == 1:
                st.error("⚠️ **HIGH RISK** of Heart Disease\n\n**Recommendation:** Please consult with a healthcare professional immediately for further evaluation and appropriate medical care.")
            else:
                st.success("✅ **LOW RISK** of Heart Disease\n\n**Recommendation:** Continue maintaining a healthy lifestyle with regular exercise, balanced diet, and routine medical check-ups.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced Medical disclaimer
    st.markdown("""
    <div style="background: linear-gradient(135deg, 
                    rgba(120, 1, 22, 0.2), 
                    rgba(26, 15, 10, 0.8), 
                    rgba(42, 26, 15, 0.6)
                ); 
                border: 2px solid rgba(247, 181, 56, 0.3); 
                border-radius: 20px; 
                padding: 25px; 
                margin-top: 4rem;
                text-align: center;
                backdrop-filter: blur(15px);
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);">
        <h4 style="color: #F7B538; margin-bottom: 15px; font-weight: 700; font-size: 1.2rem;">⚕️ Medical Disclaimer</h4>
        <p style="color: #E8E8E8; font-size: 1rem; line-height: 1.7; margin: 0; font-weight: 400;">
            This tool is for educational and informational purposes only. It should not be used as a substitute 
            for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare 
            professionals for accurate medical assessment and personalized treatment recommendations.
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
