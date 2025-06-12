import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset with location, cost, household size, and salary range
data = pd.DataFrame({
    "Location": ["Kuala Lumpur", "Penang", "Selangor", "Johor", "Sarawak"],
    "Average Monthly Cost (RM)": [6000, 4500, 5000, 4800, 4000],
    "Household Size": [1, 2, 3, 4, 5],
    "Salary Numeric": [2000, 5000, 10000, 15000, 20000]  # Numeric representation
})

# Train ML model
X = data[["Average Monthly Cost (RM)", "Household Size", "Salary Numeric"]]
y = data["Average Monthly Cost (RM)"]
model = LinearRegression()
model.fit(X, y)

# Car brands in Malaysia with recommended salaries
car_options = {
    "Perodua Axia": {"Comfortable Salary": 2000, "Reason": "Affordable and fuel-efficient."},
    "Proton Saga": {"Comfortable Salary": 4000, "Reason": "Balanced price and features."},
    "Honda City": {"Comfortable Salary": 7000, "Reason": "Good resale value & comfort."},
    "Toyota Corolla": {"Comfortable Salary": 9000, "Reason": "Reliable with strong market demand."},
    "Mercedes-Benz A-Class": {"Comfortable Salary": 15000, "Reason": "Premium comfort & status."},
}

# Streamlit UI
st.title("Malaysia Lifestyle & Car Recommendation App for Youngsters")

# Step 1: User Inputs
location = st.selectbox("Select your location:", data["Location"].unique())
household_size = st.slider("Household size:", 1, 5, 2)
salary_range = st.selectbox("Select your salary range:", data["Salary Numeric"])
car_choice = st.selectbox("Which car do you want to buy?", list(car_options.keys()))

# Step 2: Salary Prediction
selected_location_cost = data.loc[data["Location"] == location, "Average Monthly Cost (RM)"].iloc[0]
predicted_salary = model.predict(np.array([[selected_location_cost, household_size, salary_range]]).reshape(1, -1))[0]

# Step 3: Car Comfortability Check
comfortable_salary_for_car = car_options[car_choice]["Comfortable Salary"]

# Display results
st.write(f"### Estimated Salary Needed in {location}: RM{round(predicted_salary, 2)} per month")
st.write(f"You need approximately RM{round(predicted_salary * 12, 2)} annually for a comfortable life.")

st.write(f"### Recommended Car Based on Your Salary: {car_choice}")
st.write(f"Comfortable Salary Needed: RM{comfortable_salary_for_car} per month")
st.write(f"Why? {car_options[car_choice]['Reason']}")

# Final Conclusion
if predicted_salary >= comfortable_salary_for_car:
    st.write(f"✅ You can comfortably afford the {car_choice} with your estimated salary!")
else:
    st.write(f"⚠️ You might need a higher salary to afford the {car_choice} comfortably.")

st.write("### Final Conclusion")
st.write(f"Based on your location, household size, salary range, and expected salary, we estimate that living comfortably in {location} requires approximately RM{round(predicted_salary, 2)} per month.")
st.write("Your car recommendation aligns with affordability and lifestyle expectations.")

