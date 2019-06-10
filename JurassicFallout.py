import time
import random

heros_weapons = ["pocket knife"]
heros_items = ["island map"]
dinos = ["T-rex", "Alisaurus", "Triceratops", "Stegasaurus", "Velociraptor",
         "Stygimoloch", "Pterodactyl"]

discover_weapons = ["Master Sword", "Boomerang", "slingshot", "butter knife",
                    "bow and arrow", "emergency flare", ]


def print_pause(string, seconds):
    print(string)
    time.sleep(seconds)


def intro():
    print_pause("\nThe year is 2023. Years ago the dinosaurs "
                "were believed to have been destroyed by a "
                "volcanic eruption on Isla Nubar.\n", 3)
    print_pause("You have been sent on a reconnaissance mission \n"
                "to survey the island and recover the t-rex DNA stored\n"
                "in the laboratory before it falls into the wrong hands.\n", 3)
    print_pause("You are equipped with a small pack of supplies - water,\n"
                " food, a tent, and a small pocket knife - for some reason "
                "you forgot to pack your pistol.\n", 3)
    print_pause("Your Lyft driver drops you off from the helicopter at a\n"
                " rendezvous point where you are to meet her again \n"
                "in three days time.\n", 3)
    print_pause("You depart from the launchpad and begin your trek \n"
                "across a once-charred volcanic plain.\n", 3)
    print_pause(". . .\n", 4)


def valid_input(prompt, options):
    response = (input(prompt))
    while True:
        for option in options:
            if str(option) == response:
                return int(response)
            else:
                pass
        print_pause("Sorry, invalid input. Please select from \n"
                    "the given options.", 1.5)
        response = (input(prompt))


def end_game():
    if "T-rex DNA" in heros_items:
        print_pause("Mission complete! You've won the game.", 2)
    else:
        print_pause("Mission failed. You have run out of time.", 2)

    print_pause("GAME OVER.\n", 2)

    decision = valid_input("Would you like to play again? Press 1 \n"
                           "to play again or 2 to exit the game.", [1, 2])

    if decision == 1:
        print_pause("Awesome! Get ready for another adventure.", 2)
        play_game()
    elif decision == 2:
        print_pause("Thanks for playing! See you next time.", 2)
        exit()


def check_for_item(item, list):
    if item in list:
        return True
    else:
        return False


def dino_encounter():
    print_pause("Suddenly, you hear an ominous \n"
                "rustling sound to your right.", 2)
    print_pause(f"You whirl around to find a(n) {random.choice(dinos)}\n"
                " staring back at you.", 2)
    print_pause("Your weapons: ", 2)
    print(*heros_weapons, sep=", ")
    action = valid_input("Press 1 to fight or 2 to run for it.\n", [1, 2])
    if action == 1:
        if "emergency flare" in heros_weapons:
            print_pause("You pull out an emergency flare and the dino is\n"
                        " scared off by the fire.\n"
                        "You make a narrow escape and return \n"
                        "to the field", 1.5)
        elif "Master Sword" in heros_weapons:
            print_pause("You make a valiant effort to fight off \n"
                        "the dino with your Master Sword.\n", 1.5)
            print_pause("You give the dino an owie and buy yourself \n"
                        "enough time to make an escape.", 2)
        elif "boomerang" in heros_weapons:
            print_pause("You make a valiant effort to fight off the \n"
                        "dino with your boomerang.\n", 1.5)
            print_pause("You give the dino an owie and buy yourself \n"
                        "enough time to make an escape.", 2)
        elif "slingshot" or "bow and arrow" in heros_weapons:
            print_pause("Shots fired! Unfortunately, your aim's \n"
                        "not great.\n", 1.5)
            print_pause("You are badly hurt, but make it back to the\n"
                        " launchpad in one piece.\n", 1.5)
            print_pause("You wait on the helipad for your \n"
                        "Lyft driver to return.\n", 2)
        else:
            print_pause("You attempt to fight off the dino, but you're \n"
                        "not properly armed. You are badly hurt,\n"
                        " but make it back to the \n"
                        "launchpad in one piece.", 1.5)
            print_pause("You wait on the helipad for your\n"
                        " Lyft driver to return.\n", 2)
            end_game()
    elif action == 2:
        print_pause("You make a break for it and barely escape.", 1.5)


def where_to():
    print_pause("You pull out a map of the island \n"
                "to decide where you'll head next.\n", 3)
    choice = valid_input("Press 1 to head towards \n"
                         "the thicket, 2 to visit the waterfall, \n"
                         "3 to journey to the volcano, or 4 to check\n"
                         " out the lab.\n", [1, 2, 3, 4])
    if choice == 1:
        thicket()
        where_to()
    if choice == 2:
        waterfall()
        where_to()
    if choice == 3:
        volcano()
        where_to()
    if choice == 4:
        lab()
        where_to()


def thicket():
    print_pause("As you're walking you come upon a thicket of trees.", 1.5)
    print_pause("Would you like to explore or turn around?", 1.5)
    decision = valid_input("Press 1 to enter the thicket or\n"
                           " 2 to turn around.\n", [1, 2])
    if decision == 1:
        print_pause("You enter the thicket and tangled among\n"
                    " the jungly vines, you find some climbing rope.\n"
                    "You use your pocket knife to cut some down.", 2)
        heros_items.append("climbing rope")
        dino_encounter()
    elif decision == 2:
        print_pause("Unsure of what you'll find and whether you're prepared\n"
                    " , you turn back and return to the plains.", 2)
        dino_encounter()


def volcano():
    print_pause("You continue on your way and soon enough you reach\n"
                " the volcano that everyone's been talking about", 2)
    found_weapon = random.choice(discover_weapons)
    print_pause(f"A bit randomly, you happen upon a(n) {found_weapon}\n"
                " just lying on the ground. Score!", 2)
    heros_weapons.append(found_weapon)
    print_pause("There's not much to do here, so you better \n"
                "get going before something eventful happens.", 4)
    dino_encounter()


def waterfall():
    print_pause("You continue walking until you discover a waterfall.", 2)
    print_pause(f"You have the following items in your pack:", 2)
    print(*heros_items, sep=", ")
    decision = valid_input("Enter 1 to climb the waterfall\n"
                           " or 2 to turn around and leave.\n", [1, 2])
    if decision == 1:
        if "climbing rope" in heros_items:
            print_pause("You use your climbing rope to \n"
                        "scale the slippery waterfall.", 2)
            print_pause("When you reach the top, you find a rather large \n"
                        "and important looking key just lying there \n"
                        "inconspicuously. Better add that to your\n"
                        " pack, just in case.", 2)
            heros_items.append("important key")
        else:
            print_pause("You attempt to climb the waterfall, but its \n"
                        "steep and slippery face proves insurmountable.", 2)
            print_pause("If you're really going to climb this thing, \n"
                        "you might need some proper equipment.", 2)
            print_pause("You shake the mud off your \n"
                        "boots and continue back to the field.", 2)
            thicket()
    elif decision == 2:
            print_pause("Rather than risk a nasty fall, you\n"
                        " turn back and head towards the field.", 2)
            print_pause("Hopefully there's nothing you missed at the top.", 2)


def lab():
    print_pause("After still more walking, you come\n"
                " across an abandoned lab.", 2)
    print_pause("Remembering your mission, you approach \n"
                "and attempt to open the old rusty door.", 2)
    if ("important key") in heros_items:
        print_pause("You try the key you found before, \n"
                    "and it works! The door creaks open\n"
                    " and you slowly enter the lab.", 2)
        print_pause("After a bit of poking around, you find a\n"
                    " small vial amid many broken tools and beakers.", 3)
        print_pause("You've found the T-rex DNA you came for!!\n", 3)
        print_pause(". . . . .\n", 4)
        heros_items.append("T-rex DNA")
        dino_encounter()
        end_game()
    else:
        print_pause("You try the door, but it's locked.", 1.5)
        print_pause("There has to be a key around here somewhere.", 1.5)
        print_pause("You head back to the field to see what you can find.", 2)
        dino_encounter()
        where_to()


def play_game():
    intro()
    where_to()


play_game()
