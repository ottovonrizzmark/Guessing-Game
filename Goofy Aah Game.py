low = 0
high = 100

print("=== Guessing Game ===\n")
print("Please think of a number between 0 and 100!\n") 

while True:
    guess = (high + low) // 2
    print(f"\nIs your secret number {guess}?\n") 
    
    x = input("Enter 'h' to indicate the guess is too high.\n"
              "Enter 'l' to indicate the guess is too low.\n"
              "Enter 'c' to indicate I guessed correctly.\n").lower()

    if x == 'c':
        print(f"\nGame over LOOOOSAAAAAARRRRRR! Your secret number was: {guess}.\n")
        break  

    elif x == 'l':
        low = guess + 1
    elif x == 'h':
        high = guess - 1
    else:
        print("\nSorry, I did not understand your input. Please enter 'h', 'l', or 'c'.\n") 
        continue 

    if low > high:
        print("\nInconsistent input detected. Please check your responses.\n")
        
else:
    print("\nThank you for playing this game :3 Come back soon!\n")
    
        
    
