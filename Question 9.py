bday = input("Enter your birthday (DD-MM-YYYY): ") #Asking for bday
def days_since_birthday(birthday): #Finding days since bday
    year = int(birthday[6:])  #Extracting BDay
    current_year = int(input("Enter the current year: ")) #Here i am enetering the year of bday

    whole_years = current_year - year - 1   #Getting rid of birthyear
    leap_years = whole_years // 4  # Approximate leap years (1 every 4 years)

    days = whole_years * 365 + leap_years #Adding all

    print("Days passed:", days) #Printing

days_since_birthday(bday)


