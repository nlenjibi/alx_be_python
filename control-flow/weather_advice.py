temperature = int(input("Enter the temperature in Celsius: "))

if temperature < 10:
    print("Wear a heavy jacket.")
elif 10 <= temperature < 20:
    print("Wear a light jacket or sweater.")
elif 20 <= temperature < 30:
    print("Wear a t-shirt and jeans.")
else:
    print("It's hot! Wear shorts and a tank top.")
