user_input = input("Enter a number: ")


try:
    num = int(user_input)
    if num%2 == 1:
        print("The number is odd")
    else: 
        print("The number is even")
except ValueError:
    print("Your input was not a number. Please try again.")
    
