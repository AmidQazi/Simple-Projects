print("Welcome to the tip calculator.")
total = input("What was the total bill? ")
tip_percent = input("What percent tip would you like to give? 10, 15, or 20? ")
int_tip = int(tip_percent)
if (int_tip == 15):
    x = (0.15 * float(total)) + float(total)
    int_x = float(x)

elif (int_tip == 10):
    x = (0.1 * float(total)) + float(total)
    int_x = float(x)

elif (int_tip == 20):
    x = (0.2 * float(total)) + float(total)
    int_x = float(x)
  
else:
    print("Wrong value entered...")

split = input("How many people to split the bill? ")
int_split = int(split)


each_person_price = (int_x/int_split)
each_person_price_rounded = round(each_person_price, 2)
print("Each person should pay: $", each_person_price_rounded)

