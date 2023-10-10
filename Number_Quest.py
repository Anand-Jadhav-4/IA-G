# 1. The program takes the first 4-digit integer input from the user and stores it in `user_input1`.
# 2. It converts `user_input1` to an integer and subtracts 2, storing the result in `result_integer1`.
# 3. "2" is added as a prefix to `result_integer1`, and the final result is stored in `result_string1`.
# 4. It then takes a second 4-digit integer input from the user and stores it in `user_input2`.
# 5. For `user_input2`, it iterates through each digit, subtracts it from 9, and stores the result as a string in `result2`.
# 6. The program prompts the user to enter a third 4-digit integer (`user_input3`) and stores it.
# 7. Similar to step 5, it iterates through each digit in `user_input3`, subtracts it from 9, and stores the result as a string in `result3`.
# 8. Finally, the program prints a summary line that includes the original `user_input1`, `user_input2`, `result2`, `user_input3`, `result3`, and `result_string1`. It also displays an ASCII art representation.
# 9. If the user enters an invalid input (not a 4-digit integer) for any of the three inputs, the program prints an error message accordingly.
# This code takes three 4-digit integer inputs, performs operations on them, and provides a final summary of the inputs and results, including an ASCII art representation.



# Get the first integer input from the user
user_input1 = input("Please enter a 4-digit integer: ")

# Check if the input has exactly 4 digits
if len(user_input1) == 4 and user_input1.isdigit():
    # Convert the input to an integer
    user_integer1 = int(user_input1)

    # Subtract 2 from the first input
    result_integer1 = user_integer1 - 2

    # Add "2" in front of the result
    result_string1 = "2" + str(result_integer1)

    print(f"My guess of Final answer: {result_string1}")
    
    # Get the second 4-digit integer input from the user
    user_input2 = input("Enter another 4-digit integer: ")
    
    # Check if the second input has exactly 4 digits
    if len(user_input2) == 4 and user_input2.isdigit():
        # Subtract each digit separately from 9 for the second input
        result2 = ""
        for digit in user_input2:
            result2 += str(9 - int(digit))
        
        print(f"My selection: {result2}")
    else:
        print("Invalid second input. Please enter a 4-digit integer.")
    
    # Get the third 4-digit integer input from the user
    user_input3 = input("Enter one more 4-digit integer: ")
    
    # Check if the third input has exactly 4 digits
    if len(user_input3) == 4 and user_input3.isdigit():
        # Subtract each digit separately from 9 for the third input
        result3 = ""
        for digit in user_input3:
            result3 += str(9 - int(digit))
        
        print(f"My selection: {result3}")
    else:
        print("Invalid third input. Please enter a 4-digit integer.")

    # Display the desired message
    print(f"{user_input1} + {user_input2} + {result2} + {user_input3} + {result3} = {result_string1} which was the final answer")
    print("""
.__  __ /\                               .__        
|__|/  |)/ ______   _____ _____     ____ |__| ____  
|  \   __\/  ___/  /     \\__  \   / ___\|  |/ ___\ 
|  ||  |  \___ \  |  Y Y  \/ __ \_/ /_/  >  \  \___ 
|__||__| /____  > |__|_|  (____  /\___  /|__|\___  >
              \/        \/     \//_____/         \/ 
""")
else:
    print("Invalid first input. Please enter a 4-digit integer.")
