# Useless Trivia
#
# Gets personal information from the user and then
# prints true but useless information about him or her
#
# Customization
# I added in a loop that ran until the user inputed
# what gender they are.  Then I added a line that
# says if ee cummings would formally call them
# Mr. (name) or Miss or Mrs. (name).
# I also added in code that calculated and told them
# how much they weigh on ounces.

name = input("Hi. What's your name?\n")

sex = ""
while sex not in ("male", "female"):
    sex = input("Are you a male or female? Type 'male' or 'female'.\n").lower()

age = input("How old are you?\n")
age = int(age)

weight = int(input("Okay, last question.  How many pounds do you weigh? \n"))

print("\nIf poet ee cummings were to email you, he'd address you as",
      name.lower())
print("But if ee were mad, he'd call you", name.upper())
if sex == "male":
    print("More formally, he might say Mr.", name)
else:
    print("More formally, he might say Miss or Mrs.", name)

called = name * 5
print("\nIf a small child were trying to get your attention",)
print("your name would become:")
print(called)

seconds = age * 365 * 24 * 60 * 60
print("\nYou're over", seconds, "seconds old")

print("\nNow some facts about how much you weigh!")
ounces = weight * 16
print("You weigh", ounces, "ounces, or", weight, "pounds")
moon_weight = weight / 6
print("\nOn the moon, you would only weigh", moon_weight, "pounds!")
sun_weight = weight * 27.1
print("On the sun, you'd weigh", sun_weight, "(but, ah... not for long).")

input("\n\nPress the enter key to exit.")

