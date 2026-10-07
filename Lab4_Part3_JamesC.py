salary= float(input("Enter your annual salary:"))
yearsworked= int(input("Enter the number of years employed:"))


if salary < 30000:
    print('you must earn at least 30000 per  year to qualify')
elif yearsworked < 2:
    print('you must have been on your current job for at least 2 years to qualify')
else:
    print('you qualify for the loan')

