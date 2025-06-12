import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset with location, cost, household size, salary range, and income groups
data = pd.DataFrame({
    "Location": ["Kuala Lumpur", "Penang", "Selangor", "Johor", "Sarawak"],
    "Average Monthly Cost (RM)": [6000, 4500, 5000, 4800, 4000],
    "Household Size": [1, 2, 3, 4, 5],
    "Salary Numeric": [2000, 5000, 10000, 15000, 20000],
    "Income Group": ["B40", "M40", "T20", "T15", "T5"]
})

# Car brands in Malaysia with recommended salaries
car_options = {
    "Perodua Axia": {"Comfortable Salary": 2000, "Income Group": "B40", "Reason": "Affordable and fuel-efficient."},
    "Proton Saga": {"Comfortable Salary": 4000, "Income Group": "B40-M40", "Reason": "Balanced price and features."},
    "Honda City": {"Comfortable Salary": 7000, "Income Group": "M40-T20", "Reason": "Good resale value & comfort."},
    "Toyota Corolla": {"Comfortable Salary": 9000, "Income Group": "T20-T15", "Reason": "Reliable with strong market demand."},
    "Mercedes-Benz A-Class": {"Comfortable Salary": 15000, "Income Group": "T15-T5", "Reason": "Premium comfort & status."}
}

# Train ML model
X = data[["Average Monthly Cost (RM)", "Household Size", "Salary Numeric"]]
y = data["Average Monthly Cost (RM)"]
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("Stresformance Identification Apps 🚗💰")
st.markdown ("by Norasibah Abdul Jalil")

# Step 1: User Inputs
location = st.selectbox("📍 Select your location:", data["Location"].unique())
household_size = st.slider("👨‍👩‍👧‍👦 Household size:", 1, 10, 3)
salary = st.number_input("💵 Enter your salary (RM):", min_value=1000, max_value=50000, value=5000, step=500)
married = st.radio("💍 Are you married?", ["Yes", "No"])
dependents = st.multiselect("👥 Select dependents:", ["Wife", "Children", "Parents", "Siblings"])
income_group = st.selectbox("🏠 Select your income group:", data["Income Group"].unique())
car_choice = st.selectbox("🚘 Which car do you want to buy?", list(car_options.keys()))

# Step 2: Salary Prediction
selected_location_cost = data.loc[data["Location"] == location, "Average Monthly Cost (RM)"].iloc[0]
predicted_salary = model.predict(np.array([[selected_location_cost, household_size, salary]]).reshape(1, -1))[0]

# Step 3: Car Comfortability Check
comfortable_salary_for_car = car_options[car_choice]["Comfortable Salary"]

# Display results
st.subheader("📊 Estimated Financial Analysis")
st.write(f"💰 Estimated Salary Needed in {location}: RM{round(predicted_salary, 2)} per month")
st.write(f"🏡 Annual Comfortable Living Cost: RM{round(predicted_salary * 12, 2)}")

st.subheader("🚗 Recommended Car Based on Your Financial Profile")
st.write(f"🔹 Selected Car: {car_choice}")
st.write(f"💵 Comfortable Salary Needed: RM{comfortable_salary_for_car} per month")
st.write(f"📌 Income Group Match: {car_options[car_choice]['Income Group']}")
st.write(f"🔎 Reason: {car_options[car_choice]['Reason']}")

# Step 4: Budgeting Suggestions
if predicted_salary < comfortable_salary_for_car:
    st.warning(f"⚠️ You might need a higher salary to afford the {car_choice} comfortably.")
    st.subheader("💡 Budgeting Tips")
    st.write("- Consider increasing household income by freelancing or side businesses.")
    st.write("- Reduce monthly expenses in non-essential areas.")
    st.write("- Look for financial aid options if applicable.")
    st.write("- Consider a more budget-friendly alternative, like:")
    alternative_car = [car for car, details in car_options.items() if details["Comfortable Salary"] <= predicted_salary]
    if alternative_car:
        st.write(f"✅ Suggested Alternative: {alternative_car[0]} (Comfortable Salary: RM{car_options[alternative_car[0]]['Comfortable Salary']})")
else:
    st.success(f"✅ You can comfortably afford the {car_choice} with your estimated salary!")
    st.subheader("🔎 Final Conclusion")
st.write(f"Based on your location, household size, salary, dependents, and marital status, we estimate that living comfortably in {location} requires approximately RM{round(predicted_salary, 2)} per month.")
st.write("Your car recommendation aligns with affordability and lifestyle expectations.")

