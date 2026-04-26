import random
age = 0
health = 100
happiness = 0
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
events_categories = [
    neutral_events,
    minor_damage_events,
    major_damage_events
]
def health_cats():
    health_damage = random.choice(events_categories)
    helth_event = random.choice(health_damage)
    if health_damage == minor_damage_events:
        Global.health -= 10
    elif health_damage == major_damage_events:
        Global.health -= 90
    return helth_event
name = input("hello what is your name: ")
print("hey " + name + " ready to play a game?")
answer = input(' type "y" for yes and "n" for no: ')
if answer == "y" or answer == "Y" or answer == "yes" or answer == "YES":
    print("lets get started")
else:
    input("well, if you have a change of heart, just type y: ")

