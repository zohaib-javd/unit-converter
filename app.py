import streamlit as st

def convert_length(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "meter_centimeter": 100,
        "centimeter_meter": 0.01,
        "meter_millimeter": 1000,
        "millimeter_meter": 0.001,
        "kilometer_centimeter": 100000,
        "centimeter_kilometer": 1 / 100000,
        "kilometer_millimeter": 1e6,
        "millimeter_kilometer": 1e-6,
        "centimeter_millimeter": 10,
        "millimeter_centimeter": 0.1
    }
    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        return value * conversions[key]
    else:
        return "Conversion not available"

def convert_mass(value, unit_from, unit_to):
    conversions = {
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
        "gram_milligram": 1000,
        "milligram_gram": 0.001,
        "kilogram_milligram": 1e6,
        "milligram_kilogram": 1e-6
    }
    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        return value * conversions[key]
    else:
        return "Conversion not available"

def convert_temperature(value, unit_from, unit_to):
    # Temperature conversion formulas
    if unit_from == unit_to:
        return value
    if unit_from == "Celsius" and unit_to == "Fahrenheit":
        return value * 9 / 5 + 32
    elif unit_from == "Fahrenheit" and unit_to == "Celsius":
        return (value - 32) * 5 / 9
    elif unit_from == "Celsius" and unit_to == "Kelvin":
        return value + 273.15
    elif unit_from == "Kelvin" and unit_to == "Celsius":
        return value - 273.15
    elif unit_from == "Fahrenheit" and unit_to == "Kelvin":
        return (value - 32) * 5 / 9 + 273.15
    elif unit_from == "Kelvin" and unit_to == "Fahrenheit":
        return (value - 273.15) * 9 / 5 + 32
    else:
        return "Conversion not available"

def main():
    # Title bar icon and layout
    st.set_page_config(page_title="Enhanced Unit Converter", page_icon="📐", layout="wide")
    st.title("📐Enhanced Unit Converter by ZeeJay🙅‍♂️")
    st.markdown("### Choose your conversion category from the sidebar and get started!")

    # Sidebar selection for conversion category
    category = st.sidebar.radio("Conversion Category", ("Length", "Mass", "Temperature"))
    
    # Set available units based on the selected category
    if category == "Length":
        units = ["meter", "kilometer", "centimeter", "millimeter"]
    elif category == "Mass":
        units = ["gram", "kilogram", "milligram"]
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]

    st.header(f"{category} Conversion")
    value = st.number_input("Enter the value you want to convert", value=0.0)
    unit_from = st.selectbox("Convert from", units, key="unit_from")
    unit_to = st.selectbox("Convert to", units, key="unit_to")
    
    if st.button("Convert"):
        if category == "Length":
            result = convert_length(value, unit_from, unit_to)
        elif category == "Mass":
            result = convert_mass(value, unit_from, unit_to)
        elif category == "Temperature":
            result = convert_temperature(value, unit_from, unit_to)
            
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"{value} {unit_from} is equal to {result} {unit_to}")

    # Sidebar info and about section

    st.sidebar.markdown("## About This App")
    st.sidebar.info("A simple and powerful unit converter built with Streamlit. Choose a category, enter a value, and convert instantly! ⚖️🌡️📏")

    # Additional sidebar information in dropdowns using expanders
    with st.sidebar.expander("📲 Connect with me:"):
        st.markdown("""
- 🔗 [LinkedIn](https://www.linkedin.com/in/zohaib-javd)
- 👨‍💻 [GitHub](https://www.github.com/zohaib-javd)
- 📧 Email: zohaibjaved@gmail.com
        """)

    with st.sidebar.expander("🧑‍🏫 Special thanks to all my teachers:"):
        st.markdown("""
- Sir Zia Khan  
- Sir Daniyal Nagori  
- Sir Muhammad Qasim  
- Sir Ameen Alam  
- Sir Aneeq Khatri  
- Sir Okasha Aijaz  
- Sir Muhammad Osama  
- Sir Mubashir Ali  
- Sir Amjad Ali  
- Sir Naeem Hussain  
- Sir Fahad Ghouri  
- Sir Saleem Raza  
- Sir Shaikh Abdul Sami  
- Sir Abdullah arain
        """)

if __name__ == "__main__":
    main()
