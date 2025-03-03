import streamlit as st

st.title("🎯 Unit Converter App")
st.markdown("### Converts Lenght,Weight,Time and Temperature instantly.")
st.write("Welcome! select a category,enter a value and get the converted result.")

# Conversion factors
Lenght_units = {
    "Meter": 1,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Mile": 1609.34,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254
}

weight_units = {
    "Kilogram": 1,
    "Gram": 0.001,
    "Milligram": 0.000001,
    "Pound": 0.453592,
    "Ounce": 0.0283495
}

time_units = {
    "Second": 1,
    "Minute": 60,
    "Hour": 3600,
    "Day": 86400
}

temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

def convert_Lenght(value, from_unit, to_unit):
    return value * Lenght_units[from_unit] / Lenght_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    return value * weight_units[from_unit] / weight_units[to_unit]

def convert_time(value, from_unit, to_unit):
    return value * time_units[from_unit] / time_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32


category = st.selectbox("Select Category", ["Lenght", "Weight", "Time", "Temperature"])

value = st.number_input("Enter Value", value=0.0)

if category == "Lenght":
    from_unit = st.selectbox("From", Lenght_units.keys())
    to_unit = st.selectbox("To", Lenght_units.keys())
    result = convert_Lenght(value, from_unit, to_unit)
elif category == "Weight":
    from_unit = st.selectbox("From", weight_units.keys())
    to_unit = st.selectbox("To", weight_units.keys())
    result = convert_weight(value, from_unit, to_unit)
elif category == "Time":
    from_unit = st.selectbox("From", time_units.keys())
    to_unit = st.selectbox("To", time_units.keys())
    result = convert_time(value, from_unit, to_unit)
else:
    from_unit = st.selectbox("From", temperature_units)
    to_unit = st.selectbox("To", temperature_units)
    result = convert_temperature(value, from_unit, to_unit)

if st.button("Convert"):
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
