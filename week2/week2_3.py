height = float(input("Enter your height (cm): "))
weight = float(input("Enter your weight (kg): "))
BMI = weight/pow((height/100),2)
print(f"You BMI is {BMI}")

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
else:
    print("You are severely over weight.")
