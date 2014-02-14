# This program recieves a message from the user and prints it out backwards

message = input("Enter a message: ")
length = len(message)
print("\nYour message has length:", length)

print("Your message reversed is:")
reversed_message = ""
i = length - 1
for j in range(length):
    reversed_message += (message[i])
    i = i - 1 

print(reversed_message)
input("\n\nPress the enter key to exit.")
