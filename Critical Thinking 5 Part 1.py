#Calculate average rainfall over a period of years

#ask for the number of years
years = 0
while years <= 0:
    try:
        years = int(input('Please enter the number of years: '))
        if years <= 0:
            print('The number of years must be 1 or more')
    except ValueError:
        print("Invalid input pease enter an integer.")

total_rainfall = 0
total_months = years*12


#Loop for the years
for year in  range (1, years + 1):
    print('Year {}:'.format(year))
    #Loop for the months
    for month in range (1,13):
        while True:
            try:
                rainfall= float(input('Please enter the inches of rainfall for month {}: '.format(month)))
                if rainfall<0:
                    print('Rainfall must be a positive number, please re-enter the inches of rainfall.')
                    continue
                break
            except ValueError:
                print('Rainfall must be a number, please re-enter the inches of rainfall.')

        total_rainfall = rainfall + total_rainfall


#Calculate the average rainfall per month
average_rainfall=total_rainfall/total_months

#output
print('The number of months is', total_months)
print('There were {:.2f} inches of rainfall throughout {} months.'.format(total_rainfall, total_months))
print('The average rainfall per month was {:.2f}'.format(average_rainfall))
print('Thank you for your input.')

#Terminate the program
input('Press enter to end the program')
