def days_since_birthday(birthday):
    year = int(birthday[6:])  # Gets the year

    current_year = int(input("Enter the current year: "))  # Ask for the current year

    whole_years = current_year - year - 1  # GEt rid of this year and birth
    days = whole_years * 365  # *365

    print("Days passed:", days)

bday = input("Enter your birthday (DD-MM-YYYY): ") #Here we are asking for bday
days_since_birthday(bday)
