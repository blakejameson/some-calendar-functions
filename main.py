def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
month_names={
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}
first_day_month=1
first_day_date=1
first_day_year=1900
first_day_day_of_week=7

days={
    1:"Sunday",
    2:"Monday",
    3:"Tuesday",
    4:"Wednesday",
    5:"Thursday",
    6:"Friday",
    7:"Saturday"
}

# The function below prompts the user to input a date and calculates how many days it comes after January 1, 1900
# January 1, 1900 occurred on a Monday
def days_after_1_1_1900():
    first_day_month = 1
    first_day_date = 1
    first_day_year = 1900
    first_day_day_of_week = 7

    while True:
        print("Enter the year: ")
        year = input()
        try:
            year = int(year)
        except:
            print("Please enter an integer. \n")
            continue
        else:
            if year<1900:
                print("You must enter a year greater than or equal to 1900. \n")
            else:
                break

    while True:
        print("Enter the month: ")
        month = input()
        try:
            month = int(month)
        except:
            print("You must enter an integer. \n")
            continue
        else:
            if month<=0 or month>12:
                print("You must enter a value between 1 and 12.")
                continue
            else:
                break

    while True:
        print("Enter the day: ")
        day = input()
        try:
            day = int(day)
        except:
            print("You must enter an integer.\n")
            continue
        else:
            legal_limit=months[month]
            if is_leap_year(year) and month==2:
                legal_limit = 29
            if day > legal_limit or day<=0:
                print(f"That is an invalid day. You must enter a value between 1 and {legal_limit}")
                continue
            else:
                break

    day_counter = 0
    while first_day_year < year:
        first_day_month = 1
        while first_day_month <= 12:
            if first_day_month == 2:
                if is_leap_year(first_day_year):
                    day_counter += 29
                else:
                    day_counter += 28
            else:
                day_counter += months[first_day_month]
            first_day_month += 1
        first_day_year += 1

    first_day_month=1
    while first_day_month < month:
        if first_day_month == 2:
            if is_leap_year(year):
                day_counter += 29
            else:
                day_counter += 28
        else:
            day_counter += months[first_day_month]
        first_day_month += 1
        if first_day_month == 13:
            first_day_month=1

    if month == first_day_month:
        difference = day - first_day_date
        day_counter += difference

    day_of_week=calculate_day_of_week_for_given_value(day_counter)
    return day_counter

# This function calculates how many days are between the two inputted dates
def difference_between_two_dates():
    value1=days_after_1_1_1900()
    value2=days_after_1_1_1900()
    difference = value2 - value1


    print(f"There are {difference} days between the two dates. ")

# The user enters a day and the weekday name is returned.
def calculate_day_a_date_fell_on():
    value = days_after_1_1_1900()
    day_of_week= calculate_day_of_week_for_given_value(value)
    print(f"This date occured on a {day_of_week}.")

# The function below is a helper function to some of the above functions.
# Given a number of days after January 1, 1900, the function uses the modulo operation to find the day of the week the date fell on
def calculate_day_of_week_for_given_value(value):

    # Because Monday is the day for January 1, 1900, modulo is used in relation to Monday.
    days = {
        6: "Sunday",
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday"
    }
    modulo = value % 7
    return days[modulo]



#result= days_after_1_1_1900()
#print(result)




#result2 = calculate_day_a_date_fell_on()



#result3 = difference_between_two_dates()



#result4 = is_leap_year(2016)
print(result4)