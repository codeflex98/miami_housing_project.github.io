import streamlit as st
import joblib
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), 'miami_housing_model')
model = joblib.load(model_path)

def main():
    st.title("Miami Housing Prediction by Manvanth")

    p1 = st.number_input("LATITUDE",min_value=-90.0, max_value=90.0)
    p2 = st.number_input('LONGITUDE',min_value=-180.0, max_value=180.0)

    p3 = st.number_input("LND_SQFOOT")
    p4 = st.number_input("TOT_LVG_AREA")
    p5 = st.number_input("SPEC_FEAT_VAL")

    p6 = st.number_input("RAIL_DIST")
    p7 = st.number_input("OCEAN_DIST")
    p8 = st.number_input("WATER_DIST")
    p9 = st.number_input("CNTR_DIST")
    p10 = st.number_input("SUBCNTR_DI")
    
    p11 = st.number_input("HWY_DIST")
    p12 = st.number_input("age")
    p13 = st.number_input("avno60plus")
    p14 = st.number_input("month_sold")
    p15 = st.number_input("structure_quality")
    
    # Debugging statements
    print(f"Inputs: {p1}, {p2}, {p3}, {p4}, {p5}, {p6}, {p7}, {p8}, {p9}, {p10}, {p11}, {p12} {p13}, {p14}, {p15}")
    input_data = np.array([[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15]])
    print(f"Input data shape: {input_data.shape}")

    # Example result (replace with your prediction logic)
    if st.button("Predict Price"):
        try:
            prediction = model.predict(input_data)
            st.snow()
            st.success(f"Best Price for your home {round(prediction[0], 2)} US Dollars")
        except Exception as e:
            st.error(f"Error in prediction: {e}")

if __name__ == "__main__":
    main()
