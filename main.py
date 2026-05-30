import json
from datetime import datetime

# Load JSON data
with open("tips.json", "r") as file:
    data = json.load(file)

name = input("Enter your name: ")

print(f"\nHello, {name}! Welcome to Smart Student Assistant.")

while True:
    print("\nMenu")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Choose an option: ")

    result = ""

    if choice == "1":
        result = data["study_tips"][0]
        print("\nStudy Tip:")
        print(result)

    elif choice == "2":
        result = data["quotes"][0]
        print("\nMotivation Quote:")
        print(result)

    elif choice == "3":
        result = str(datetime.now())
        print("\nCurrent Date & Time:")
        print(result)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
        continue

    with open("output.txt", "a") as out:
        out.write(result + "\n")