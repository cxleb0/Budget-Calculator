
def calculate_percentage(number):
    necesities = round(number * .50, 2)
    wants = round(number * .30, 2)
    savings = round(number * .20, 2)
    print(f"Allocated amount for necesities is ${necesities:.2f}")
    print(f"Allocated amount for wants is ${wants:.2f}")
    print(f"Allocated amount for saving is ${savings:.2f}")

print("Automatic Budget Calculator")
biweeklypay = float(input("Enter the amount you were paid: "))
calculate_percentage(biweeklypay)