import random
import os
os.system("title Kernel Bit Life")
ageing = 0
health = 100
neutral_events = [
    "Nothing interesting happened today.",
    "You scrolled on your phone for hours.",
    "You watched the clouds pass by.",
    "You stayed home and relaxed.",
    "A quiet day with no surprises.",
    "You took a long nap.",
    "You spaced out for a while.",
    "You daydreamed about the future.",
    "You listened to music all day.",
    "You wandered around aimlessly."
]
minor_damage_events = [
    "You tripped on the sidewalk. -10 health.",
    "You caught a cold. -10 health.",
    "You stubbed your toe really hard. -10 health.",
    "You slipped in the shower. -10 health.",
    "You ate something questionable. -10 health.",
    "You stayed up way too late. -10 health.",
    "You pulled a muscle. -10 health.",
    "You got a headache. -10 health.",
    "You got lightly injured while exercising. -10 health.",
    "You twisted your ankle. -10 health."
]
major_damage_events = [
    "A piano fell from the sky and almost crushed you. -90 health.",
    "You got chased by a bear. You barely escaped. -90 health.",
    "You fell down a massive flight of stairs. -90 health.",
    "You got struck by lightning. -90 health.",
    "You were hit by a rogue shopping cart at full speed. -90 health.",
    "You got into a serious accident. -90 health.",
    "You angered a goose. It did not go well. -90 health.",
    "You slipped on a banana peel cartoon-style. -90 health.",
    "You tried parkour. It was a mistake. -90 health.",
    "You fought gravity and gravity won. -90 health."
]
health_gain_events = [
    "You drank plenty of water today. +10 health.",
    "You ate a healthy meal. +10 health.",
    "You took a refreshing walk outside. +10 health.",
    "You stretched your body and felt better. +10 health.",
    "You went to bed early and slept well. +10 health.",
    "You meditated and felt calmer. +10 health.",
    "You took your vitamins. +10 health.",
    "You avoided junk food today. +10 health.",
    "You did some light exercise. +10 health.",
    "You had a relaxing bath. +10 health."
]

events_categories = [
    health_gain_events,
    neutral_events,
    minor_damage_events,
    major_damage_events
]
neutral_happy = [
    "You scrolled social media for a while.",
    "You stared at the ceiling thinking about life.",
    "You listened to music but didn’t feel much.",
    "You walked around the house aimlessly.",
    "You watched random YouTube videos.",
    "You zoned out for a bit.",
    "You sat outside and did nothing.",
    "You played with your hands like a bored toddler.",
    "You laid in bed thinking about the universe.",
    "You vibed quietly in your room."
]

def health_cats():
    global health 
    health_damage = random.choice(events_categories)
    health_event = random.choice(health_damage)
    if health_damage == health_gain_events:
        if health < 100:
            health += 10
        else:
            health = 100
    if health_damage == minor_damage_events:
        health -= 10
    elif health_damage == major_damage_events:
        health -= 90
    return health_event
name = input("hello what is your name: ")
print("hey " + name + " ready to play a game?")
answer = input(' type "y" for yes and "n" for no: ')
if answer == "y" or answer == "Y" or answer == "yes" or answer == "YES":
    print("lets get started")
else:
    input("well, if you have a change of heart, just type y: ")

print(' "a" is to age, "h" is to do happy things, "n" is to quit')
ageing = 0
health = 100
while ageing < 100 and health > 0:
    age = input(' "a" or "h" or "n": ')
    if age == "a" or age == "A":
        ageing += 1
        event = health_cats()
        print("Age: " + str(ageing), event, " Health: " + str(health))
    elif age == "h" or age == "H":
        print(random.choice(neutral_happy))
    elif age == "n" or age == "N":
        print("Thanks for playing! Restart the program to play again.")
        break
if ageing >= 100:
    print("You have beat the game, but now died at 100 years old. Congrats!")
else:
    print("You have died at the age of " + str(ageing))
play = input('do you want to play again? "y" for yes: ')
while play.lower() == "y":
    ageing = 0
    health = 100
    while ageing < 100 and health > 0:
        age = input(' "a" or "h" or "n": ')
        if age == "a" or age == "A":
            ageing += 1
            event = health_cats()
            print("Age: " + str(ageing), event, " Health: " + str(health))
        elif age == "h" or age == "H":
            print(random.choice(neutral_happy))
        elif age == "n" or age == "N":
            print("Thanks for playing! Restart the program to play again.")
            break
    if ageing >= 100:
        print("You have beat the game, but now died at 100 years old. Congrats!")
    else:
        print("You have died at the age of " + str(ageing))
    play = input('do you want to play again? "y" for yes: ')