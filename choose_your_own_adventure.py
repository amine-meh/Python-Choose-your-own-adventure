name = input("Enter your name: ")
print("Welcome",name,"to this epic adventure!")

print("You wake up in a small, dimly lit room. The sound of dripping water echoes around you.")
print("You notice two doors: one made of sturdy oak and the other a rusted iron gate.")

answer = input("Which door will you choose to explore? (oak/iron): ").lower()

if answer == "oak":
    print("\nThe oak door creaks open, and you step into a serene forest bathed in golden sunlight.")
    answer = input(
        "You see a narrow path leading deeper into the forest and a small cabin nearby. Where will you go? (path/cabin): "
    ).lower()

    if answer == "path":
        print(
            "You follow the path and find a shimmering lake with a mysterious figure standing by the shore."
        )
        answer = input("Do you approach the figure or stay hidden? (approach/hide): ").lower()

        if answer == "approach":
            print(
                "The figure turns out to be a kind old wizard who grants you a magical map. You are now equipped to find hidden treasures!"
            )
        elif answer == "hide":
            print(
                "You remain hidden, but the figure disappears into the mist. You feel a pang of regret but continue your journey."
            )
        else:
            print("Invalid option. You lose!")

    elif answer == "cabin":
        print(
            "You enter the cabin and find it filled with strange artifacts. A journal on the table catches your eye."
        )
        answer = input(
            "Do you read the journal or explore the rest of the cabin? (read/explore): "
        ).lower()

        if answer == "read":
            print(
                "The journal reveals the secrets of the forest, including a hidden portal to another world!"
            )
        elif answer == "explore":
            print(
                "You find a hidden trapdoor that leads to a network of underground tunnels. Adventure awaits!"
            )
        else:
            print("Invalid option. You lose!")

    else:
        print("Invalid option. You lose!")

elif answer == "iron":
    print(
        "\nThe iron gate screeches as you push it open, revealing a dark corridor lit by flickering torches."
    )
    answer = input(
        "You hear faint whispers ahead and see a staircase leading down. Do you follow the whispers or descend the staircase? (whispers/staircase): "
    ).lower()

    if answer == "whispers":
        print(
            "You find a hidden chamber where ghostly figures are gathered. They offer you a choice: knowledge of the past or power for the future."
        )
        answer = input("Which do you choose? (knowledge/power): ").lower()

        if answer == "knowledge":
            print(
                "The ghosts reveal ancient secrets that could change the course of history. You are now a keeper of knowledge."
            )
        elif answer == "power":
            print(
                "You are imbued with incredible strength and abilities. The world is yours to shape as you wish!"
            )
        else:
            print("Invalid option. You lose!")

    elif answer == "staircase":
        print(
            "You descend into a vast cavern filled with glowing crystals. A strange creature approaches you."
        )
        answer = input(
            "Do you greet the creature or run back up the stairs? (greet/run): "
        ).lower()

        if answer == "greet":
            print(
                "The creature turns out to be a guardian of the crystals. It gifts you a shard with mysterious powers."
            )
        elif answer == "run":
            print(
                "You escape unscathed, but you wonder what might have happened if you had stayed."
            )
        else:
            print("Invalid option. You lose!")

    else:
        print("Invalid option. You lose!")

else:
    print("Invalid option. You lose!")
