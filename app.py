import streamlit as st
import pandas as pd
import numpy as np

# 1. App Interface Configuration (English Clean Version)
st.set_page_config(page_title="Bike Fuel Estimator", page_icon="🏍️", layout="centered")
st.title("🏍️ Automated Bike Petrol Consumption Estimator")
st.write("Enter your journey distance below, and the automated logic will instantly calculate real-world fuel metrics for all standard engine categories (70cc to 250cc).")

st.markdown("---")

# 2. User Input (Travel Distance Slider)
st.subheader("🗺️ Journey Distance Selection")
safar_km = st.slider("Select Travel Distance (KM)", min_value=1, max_value=150, value=20, step=1)

st.markdown("---")

# 3. Dynamic Precision Computation Logic
if st.button("⛽ Run Automated Petrol Estimation", type="primary"):
    # Array containing the standard target motorcycle displacement sizes
    cc_array = np.array([70, 100, 125, 150, 200, 225, 250])
    
    # Real-world dynamic evaluation logic:
    # 70cc offers ~55 KM/L, while 250cc drops down to ~25 KM/L linearly
    calculated_kpl = 65.0 - (cc_array * 0.16)
    predicted_petrol = safar_km / calculated_kpl
    
    # Building a highly optimized analytical summary grid for evaluation metrics
    results_df = pd.DataFrame({
        'Engine Capacity': [f"{int(cc)} cc" for cc in cc_array],
        'Total Distance': [f"{safar_km} KM" for _ in cc_array],
        'Estimated Petrol Needed': [f"{petrol:.2f} Liters" for petrol in predicted_petrol],
        'Calculated Efficiency (KPL)': [f"{kpl:.1f} KM/L" for kpl in calculated_kpl]
    })
    
    # Rendering visual layout elements on successful predictive output sequence
    st.balloons()
    st.subheader(f"📊 Projected Performance Matrix for {safar_km} KM")
    st.dataframe(results_df, use_container_width=True)
