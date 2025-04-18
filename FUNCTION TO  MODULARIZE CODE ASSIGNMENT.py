def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def get_user_choice():
    """Gets the conversion choice from the user."""
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice (1 or 2): ")
    return choice

def get_temperature():
    """Gets the temperature value from the user."""
    temp = float(input("Enter the temperature: "))
    return temp

def main():
    choice = get_user_choice()
    
    if choice == "1":
        temp = get_temperature()
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {result:.2f}°F")
    elif choice == "2":
        temp = get_temperature()
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {result:.2f}°C")
    else:
        print("Invalid choice. Please run the program again.")

# Run the main function
main()

