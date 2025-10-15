# Mobile-Price-Classification-ML-Model

# 📱 Mobile Price Range Classification

This is a simple web application built with Streamlit to predict the price range of a mobile phone based on its specifications. The prediction is powered by a machine learning model.

---

### ## 🚀 Live Demo

https://mobile-price-classification-ml-model-byshu.streamlit.app/

---

### ## 🛠️ How to Run This Project Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Shubham12-DS/Mobile-Price-Classification-ML-Model
    cd Mobile-Price-Classification-ML-Model
    ```

2.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    The app should now be open in your web browser!

---

### ## ✨ Features Used for Prediction

The model takes the following 20 features as input to predict the price range [0, 1, 2, 3]:
- `battery_power`
- `blue` (Bluetooth)
- `clock_speed`
- `dual_sim`
- `fc` (Front Camera megapixels)
- `four_g`
- `int_memory` (Internal Memory)
- `m_dep` (Mobile Depth)
- `mobile_wt` (Mobile Weight)
- `n_cores` (Number of Cores)
- `pc` (Primary Camera megapixels)
- `px_height` (Pixel Height)
- `px_width` (Pixel Width)
- `ram`
- `sc_h` (Screen Height)
- `sc_w` (Screen Width)
- `talk_time`
- `three_g`
- `touch_screen`
- `wifi`
