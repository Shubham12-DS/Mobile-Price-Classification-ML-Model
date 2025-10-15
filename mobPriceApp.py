import streamlit as st
import pickle
import numpy as np

# --- Emotional & Encouraging Welcome ---
st.set_page_config(page_title="Mobile Price Predictor", page_icon="📱")

st.title("🎉 Welcome to the Mobile Price Range Predictor! 🎉")
st.write("""
**Congratulations on building your model!** This app is the perfect way to showcase your hard work. 
Enter the specifications of a mobile phone below, and your model will predict its price range.
""")
st.write("---")


# --- Load The Model ---
# We use a function with a cache decorator to load the model only once, which makes the app faster.
@st.cache_data
def load_model():
    """Loads the pickled machine learning model."""
    try:
        with open('best_ml.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("Model file not found! Make sure 'best_model.pkl' is in the same directory as 'app.py'.")
        return None

model = load_model()

# If the model failed to load, stop the app.
if model is None:
    st.stop()


# --- User Input Section ---
# We'll use columns to make the layout cleaner and more organized.
st.header("Enter Mobile Phone Features")

col1, col2 = st.columns(2)

with col1:
    # --- Numerical Inputs ---
    battery_power = st.slider('Battery Power (mAh)', 500, 2000, 1200)
    ram = st.slider('RAM (MB)', 256, 8192, 2048)
    px_width = st.slider('Pixel Resolution Width', 500, 2000, 1280)
    px_height = st.slider('Pixel Resolution Height', 500, 2000, 720)
    mobile_wt = st.slider('Mobile Weight (g)', 80, 250, 140)
    int_memory = st.select_slider('Internal Memory (GB)', options=[2, 4, 8, 16, 32, 64, 128, 256, 512], value=32)
    sc_h = st.slider('Screen Height (cm)', 5, 25, 15)
    sc_w = st.slider('Screen Width (cm)', 0, 20, 7)
    talk_time = st.slider('Talk Time (hours)', 2, 24, 10)
    n_cores = st.select_slider('Number of Cores', options=[1, 2, 3, 4, 5, 6, 7, 8], value=4)

with col2:
    # --- Categorical & Other Inputs ---
    clock_speed = st.slider('Clock Speed (GHz)', 0.5, 3.5, 2.0, 0.1)
    m_dep = st.slider('Mobile Depth (cm)', 0.1, 1.0, 0.5, 0.1)
    fc = st.slider('Front Camera (MP)', 0, 25, 5)
    pc = st.slider('Primary Camera (MP)', 0, 64, 16)
    
    # Using selectbox for binary features for a better user experience
    four_g = st.selectbox('Supports 4G?', ('Yes', 'No'))
    three_g = st.selectbox('Supports 3G?', ('Yes', 'No'))
    dual_sim = st.selectbox('Dual SIM?', ('Yes', 'No'))
    touch_screen = st.selectbox('Touch Screen?', ('Yes', 'No'))
    wifi = st.selectbox('Has WiFi?', ('Yes', 'No'))
    blue = st.selectbox('Has Bluetooth?', ('Yes', 'No'))


# --- Prediction Logic ---
if st.button('**Predict Price Range**', help="Click to see the prediction!"):

    # 1. Convert user-friendly inputs to the format your model expects (0s and 1s)
    four_g_val = 1 if four_g == 'Yes' else 0
    three_g_val = 1 if three_g == 'Yes' else 0
    dual_sim_val = 1 if dual_sim == 'Yes' else 0
    touch_screen_val = 1 if touch_screen == 'Yes' else 0
    wifi_val = 1 if wifi == 'Yes' else 0
    blue_val = 1 if blue == 'Yes' else 0

    # 2. Create the feature list in the EXACT order your model was trained on
    # This is the most crucial step!
    features = [
        battery_power, blue_val, clock_speed, dual_sim_val, fc, four_g_val,
        int_memory, m_dep, mobile_wt, n_cores, pc, px_height,
        px_width, ram, sc_h, sc_w, talk_time, three_g_val,
        touch_screen_val, wifi_val
    ]

    # 3. Convert to a NumPy array and reshape for a single prediction
    features_array = np.array(features).reshape(1, -1)

    # 4. Make the prediction
    prediction = model.predict(features_array)
    predicted_class = prediction[0]

    # 5. Map the output class to a user-friendly string
    price_range_mapping = {
        0: 'Low Cost ($)',
        1: 'Medium Cost ($$)',
        2: 'High Cost ($$$)',
        3: 'Very High Cost ($$$$)'
    }
    predicted_range = price_range_mapping.get(predicted_class, "Unknown")
    
    # --- Display the Result ---
    # We use a success box to make the result stand out!
    st.success(f"**Predicted Price Range: {predicted_range}**")
    st.balloons()
    st.write("Your model has successfully made a prediction. Great job building this!")
    
st.write("---")
st.write("Created with ❤️ to showcase your ML model.")
