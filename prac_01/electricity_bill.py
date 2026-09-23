print("Electricity bill estimator")
TARIFF_11 = 0.244618  # This "tariff" number represents the cost per kWh in cents
TARIFF_31 = 0.136928
tariff_number = int(input("Which tariff? 11 or 31: "))

while tariff_number != 11 and tariff_number != 31:
    print("Invalid Tariff Number!")
    tariff_number = int(input("Which tariff? 11 or 31: "))

Daily_energy_use_kwh = int(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))

if tariff_number == 11:
    estimated_bill = TARIFF_11 * 10 ** -2 * Daily_energy_use_kwh * number_of_days
else:
    estimated_bill = TARIFF_31 * 10 ** -2 * Daily_energy_use_kwh * number_of_days

print(f"Estimated bill: ${estimated_bill}")
                  

