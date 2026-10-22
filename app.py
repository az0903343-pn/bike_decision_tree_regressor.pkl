import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Load the trained Decision Tree model
model = joblib.load('bike_decision_tree_regressor.pkl')

# 2. App Interface Configuration
st.set_page_config(page_title="Bike Fuel Estimator", page_icon="🏍️", layout="centered")
st.title("🏍️ Automated Bike Petrol Consumption Estimator")
st.write("Enter your journey distance below, and the machine learning model will automatically calculate fuel metrics for all standard engine categories (70cc to 250cc).")

st.markdown("---")

# 3. User Input (Travel Distance Slider)
st.subheader("🗺️ Journey Distance Selection")
safar_km = st.slider("Select Travel Distance (KM)", min_value=1, max_value=150, value=20, step=1)

st.markdown("---")

# 4. Automation and Prediction Logic
if st.button("⛽ Run Automated Petrol Estimation", type="primary"):
    # Array containing the standard target motorcycle displacement sizes
    cc_array = np.array([70, 100, 125, 150, 200, 225, 250])
    
    # Structuring the structured table configuration for the model batch inputs
    input_dict = {
        'Engine_CC': cc_array,
        'Distance_KM': np.full(len(cc_array), safar_km)
    }
    test_df = pd.DataFrame(input_dict)
    
    # Generating predictive matrix outputs using the model reference parameters
    predicted_petrol = model.predict(test_df)
    
    # Building a highly optimized analytical summary grid for evaluation metrics
    results_df = pd.DataFrame({
        'Engine Capacity': [f"{int(cc)} cc" for cc in cc_array],
        'Total Distance': [f"{safar_km} KM" for _ in cc_array],
        'Estimated Petrol Needed': [f"{petrol:.2f} Liters" for petrol in predicted_petrol],
        'Calculated Efficiency (KPL)': [f"{(safar_km / petrol):.1f} KM/L" for petrol in predicted_petrol]
    })
    
    # Rendering visual layout elements on successful predictive output sequence
    st.balloons()
    st.subheader(f"📊 Projected Performance Matrix for {safar_km} KM")
    st.dataframe(results_df, use_container_width=True)
