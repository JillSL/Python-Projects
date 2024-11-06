#SAN LUIS, Jillian Joy C.
#Project: Temperature Converter

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
        elif to_unit == "rankine":
            return (value + 273.15) * 9/5
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
        elif to_unit == "rankine":
            return value + 459.67
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
        elif to_unit == "rankine":
            return value * 9/5
    elif from_unit == "rankine":
        if to_unit == "celsius":
            return (value - 491.67) * 5/9
        elif to_unit == "fahrenheit":
            return value - 459.67
        elif to_unit == "kelvin":
            return value * 5/9
    else:
        raise ValueError("Invalid unit entered. Please enter a valid unit: Celsius, Fahrenheit, Kelvin, or Rankine.")

while True:
    try:
        value = float(input("Enter the temperature value: "))
        from_unit = input("Enter the current unit (Celsius, Fahrenheit, Kelvin, Rankine): ").lower()
        to_unit = input("Enter the unit to convert to (Celsius, Fahrenheit, Kelvin, Rankine): ").lower()

        result = convert_temperature(value, from_unit, to_unit)
        print(value, " ", from_unit, " is equal to ", result, " ", to_unit, ".")
        
        while True:
            user_response = input("Do you want to try again? (yes/no) \n")
            
            if user_response.lower() == "yes" or user_response.lower() == "yes.":
                break
            elif user_response.lower() == "no" or user_response.lower() == "no.":
                print("Goodbye!")
                exit()
            else:
                print("ERROR! Invalid response. Please type 'yes' or 'no'.")
    
    except ValueError as e:
        print(e)
        while True:
            user_response = input("Do you want to try again? (yes/no) \n")
            
            if user_response.lower() == "yes" or user_response.lower() == "yes.":
                break
            elif user_response.lower() == "no" or user_response.lower() == "no.":
                print("Goodbye!")
                exit()
            else:
                print("ERROR! Invalid response. Please type 'yes' or 'no'.")