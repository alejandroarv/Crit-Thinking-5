#Book club awards code

#A function to calculate the ponts the user earns
def calculate_points(books_purchased):
    if books_purchased >= 8:
        return 60
    elif books_purchased >= 6:
        return 30
    elif books_purchased >= 4:
        return 15
    elif books_purchased >= 2:
        return 5
    else:
        return 0

#Loop to get the input and print output
while True:
    try:
        books_purchased = int(input('Please enter the number of books purchased this month: '))
        if books_purchased < 0:
            print('Invalid input, the  number of books must be positive.')
        else:
            points = calculate_points(books_purchased)
            print('You have earned', points, 'points.')
            break
    except ValueError:
        print('Invalid input, enter a valid number.')

#End the program
print('Thank you for your purchases!')
input('Press enter to end the program.')
