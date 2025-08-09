print("Welcome to A Day In My Life")
print("\n __________________________")

mood_score = 0
input1 = input("1. Hit the Gym 🏋️‍♂️? OR 2. Do a Yoga session 🧘‍♀️? ")

if input1 == "1":
    mood_score += 2
    print("You hit the gym 🏋️‍♂️ and feel refreshed.")
    next_choice = input("Do you 1. drink a coke 🥤 OR 2. have oatmeal🥣? ")
    if next_choice == "1":
        mood_score -= 1
        print("You drink a coke 🥤 and gain calories.")
    elif next_choice == "2":
        mood_score += 2
        print("You have oatmeal🥣 and feel satisfied.")
    else:
        print("U fasting I think...")
elif input1 == "2":
    mood_score += 1
    print("You do a yoga session 🧘‍♀️ and feel relaxed.")
    next_choice = input("Do you want to 1. have promogrante juice🍹 OR 2. watch television📺? ")
    if next_choice == "1":
        mood_score += 1
        print("You drink promogrante juice🍹 and feel refreshed.")
    elif next_choice == "2":
        mood_score -= 1
        print("You watch television📺 and lounge in the sofa.")
    else:
        print("U fasting I think...")
else:
    print("Hmm, that wasn't one of the options.")
print("\n __________________________")

if mood_score >= 4:
    print("🎉 What a fantastic day! You feel energized and happy.")
elif 2 <= mood_score < 4:
    print("🙂 A pretty good day overall. You feel calm and content.")
else:
    print("😴 You feel a bit tired and could use more self-care tomorrow.")

