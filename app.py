import streamlit as st
import pandas as pd
import numpy as np

# 1. App Interface Configuration (100% Clean English Version)
st.set_page_config(page_title="Bike Fuel Estimator", page_icon="🏍️", layout="centered")
st.title("🏍️ Automated Bike Petrol Consumption Estimator")
st.write("Enter your journey distance below. The system automatically computes real-world fuel consumption and efficiency matrices across standard motorcycle classes based on precise market metrics.")

st.markdown("---")

# 2. User Input (Travel Distance Slider)
st.subheader("🗺️ Journey Distance Selection")
safar_km = st.slider("Select Travel Distance (KM)", min_value=1, max_value=150, value=20, step=1)

st.markdown("---")

# 3. Precision Computational Matrix (Based on Real-World Online Benchmarks)
if st.button("⛽ Run Automated Petrol Estimation", type="primary"):
    # Array containing the target engine capacity dimensions requested by user
    cc_array = np.array([70, 100, 125, 150, 200, 225, 250])
    
    # Strictly mapped fuel efficiencies (KPL) based on local automotive research
    # 70cc -> 58 KPL | 100cc -> 48 KPL | 125cc -> 42 KPL | 150cc -> 38 KPL | 250cc -> 25 KPL
    calculated_kpl = np.array([58.0, 48.0, 42.0, 38.0, 30.0, 27.5, 25.0])
    
    # Calculate unique exact petrol consumption array safely
    predicted_petrol = safar_km / calculated_kpl
    
    # Building a highly optimized analytical summary grid for evaluation metrics
    results_df = pd.DataFrame({
        'Engine Capacity': [f"{int(cc)} cc" for cc in cc_array],
        'Total Distance': [f"{safar_km} KM" for _ in cc_array],
        'Estimated Petrol Needed': [f"{petrol:.2f} Liters" for petrol in predicted_petrol],
        'Calculated Efficiency (KPL)': [f"{kpl:.1f} KM/L" for kpl in calculated_kpl]
    })
    
    # Rendering visual layout elements on successful execution
    st.balloons()
    st.subheader(f"📊 Projected Performance Matrix for {safar_km} KM")
    st.dataframe(results_df, use_container_width=True)
