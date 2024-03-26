#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("What is the bill: "))
people = int(input("How many people are there: "))
tip = input("How much would you like to tip: ")

tip_percent = float(tip) / 100
total_pay = bill * (1 + tip_percent)
per_person = round(total_pay / people, 2)

print(f"The total bill is {per_person} for each person")
