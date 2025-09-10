import random
fun_factor = random.randint(0,1000)

def askchoice(choice1, choice2):
    choice = input(f"Do you want to {[1]} {choice1} or {[2]} {choice2}")
    print()

    if choice == "1" or choice == "2":
        return choice

    else: 
        raise ValueError("You mistyped something and caused an error haha now you have to restart. ERROR ENDING")

def triplechoice(choice1, choice2, choice3):
    choice = input(f"Do you want to {[1]} {choice1}, {[2]} {choice2}, or {[3]} {choice3}")
    print()

    if choice == "1" or choice == "2" or choice == "3":
        return choice

    else: 
        raise ValueError("You mistyped something and caused an error haha now you have to restart. ERROR ENDING")

def quadchoice(choice1, choice2, choice3, choice4):
    choice = input(f"Do you want to {[1]} {choice1}, {[2]} {choice2}, {[3]} {choice3}, or {[4]} {choice4}")
    print()

    if choice == "1" or choice == "2" or choice == "3" or choice == "4":
        return choice
    else: 
        raise ValueError("You mistyped something and caused an error haha now you have to restart. ERROR ENDING")

def fivechoice(choice1, choice2, choice3, choice4,choice5):
    choice = input(f"Do you want to {[1]} {choice1}, {[2]} {choice2}, {[3]} {choice3}, {[4]} {choice4}, or {[5]} {choice5}")
    print()

    if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
        return choice
    else: 
        raise ValueError("You mistyped something and caused an error haha now you have to restart. ERROR ENDING")
        
def violence():
    print("You attack brother julian, and he grabs your arm and flips you over.")
    ans = askchoice("apologize","keep fighting")
    if ans == "1":
        print("Brother Julian forgives you, but it is too late, since he already broke your arm. It heals in 3 months. NEUTRAL ENDING")
    if ans == "2":
        evenmoreviolence()

def evenmoreviolence():
    print("You stun Brother Julian with a punch to the gut, and run away")
    print()
    print("You find yourself in the wilds of middle school, alone and afraid")
    ans = askchoice("Hide underneath a bus", "Explore the school")
    if ans == "1":
        bus()
    elif ans == "2":
        wilds()

def bus():
    print("You hide underneath the bus. Suddenly, the bus turns on and starts driving. It runs over you and you are squished into a pancake. Why would you even try to kick your kind brother anyways? BAD ENDING")

def wilds():
    print("You enter the main hallway of the school. It is abandoned, and overgrown with wildlife. You look out the window to see a foggy field.")
    if fun_factor <= 250:
        ans = triplechoice("Enter Library", "Enter Tech Room", "Enter Science Lab")
        if ans == ("1"):
            library()
        if ans == ("2"):
            tech()
        if ans == ("3"):
            science()
    if fun_factor > 250 and fun_factor <= 650:
        ans = quadchoice("Enter Library", "Enter Tech Room", "Enter Science Lab", "Enter Washroom")
        if ans == ("1"):
            library()
        if ans == ("2"):
            tech()
        if ans == ("3"):
            science()
        if ans == "4":
            toilet()
    if fun_factor > 650 and fun_factor <= 999:
        ans = fivechoice("Enter Library", "Enter Tech Room", "Enter Science Lab", "Enter Washroom", "Enter Office")
        if ans == ("1"):
            library()
        if ans == ("2"):
            tech()
        if ans == ("3"):
            science()
        if ans == "4":
            toilet()
        if ans == "5":
            richard()
    if fun_factor == 1000:
        print("CONNNNNNNNNNGRATULATIONS!!! YOU ARE OFFICIALLY SPECIAL! Why, you ask? Well, your fun factor is 1000! What's a fun factor? Well, it's a random number from 1 - 1000 that generates at the start of the game, which can unlock all new paths, rooms, and more! There's only a 0.1% chance of getting here! Wow! Woohoo! Uhh... Screenshot this and send it to your friends or something. Actually scratch that they'll think you're a no life.")
        print("...")
        print("... uh")
        print("juuuuust the two of us, we can make it if we try, just the two of us (just the two of us)")
        print("ok, well. i'm sure you have places to be. don't worry about me. i'll just stay here... alone again, naturally... :(")
        print("...")
        print("SPECIAL ENDING")
def library():
    print("You enter the main library. You find a really good and interesting book that you would like to read.")
    ans = triplechoice("read it", "leave library", "keep exploring the library")
    if ans == ("1"):
        print("You read the book. It's pretty interesting. Fufilled, you go and get some ice cream. BOOKWORM ENDING")
    if ans == ("2"):
        wilds()
    if ans == ("3"):
        lore()

def lore():
    print("You find yourself in a deep and unknown part of the library. A leaflet on a shelf nearby catches your attention.")
    ans = triplechoice("leave unknown areas","read ancient books", "read leaflet")
    if ans == ("1"):
        library()
    if ans == "2":
        print("The books compell you... You read them all. They contain the deep secrets of the universe. Unknown and Forbidden knowledge. You put away the ancient tomes, forever changed. LOREKEEPER ENDING")
    if ans == "3":
        print('''

        Presenting: The Truth and Recon Initiative!
        The Truth and Recon Initiative is a cutting edge reasearch project, helmed by researchers hailing straight from Japan!
        Truth and Recon aims to study the physical, mental, and spiritual limits of humanity! Subjects are placed
        in our risk-free Surround Sound System™ where they are blasted by frequencies that envoke an interesting reaction.
        Testing is quick and easy! Apply for the Truth and Recon Initiative today!
        Contact us at: 555-0100

        ''')
        print("That was... quite something.")
        lore()

def tech():
    print("You enter the tech room to see old computers and electronics.")
    ans = triplechoice("play games", "explore", "leave the tech room")
    if ans == ("1"):
        print("You find this SUPER FUN GAME: https://replit.com/@EliasSayed1/Tower-Of-Doom. Even if it is a little buggy, you play for hours. SHAMELESS PROMOTION ENDING")
    if ans == ("2"):
        electric()
    if ans == ("3"):
        wilds()

def electric():
    print("You find outdated tech like the Nintendo Wii... Hey, wait, that isn't outdated! It's only... oh... 20... years old... Hm, there's a piece of paper that catches your eye.")
    ans = triplechoice("keep exploring", "go back", "read the paper")
    if ans == ("2"):
        tech()
    if ans == ("1"):
        email()
    if ans == "3":
        print('''
        
        ---the top half of the paper seems to be ripped off---


        T&R PHASE 2 RESULTS: ST█DE██ NUM█E█ 012524 █EA█TED A██ER█E█Y TO TE█T██G
                             012524 RELEASED A POWERFUL █A█E OF TH█OA█C██O█E
                             012524 F█ED ██ M█IN ██LL, A██OR█TI█S ARE I█ C█RREN█ P██SUI█

        ''')
        print()
        print("That was... ominous, to be sure. What could T&R be?")
        electric()
        
                             

def email():
    print("The deeper you explore, the older the technology seems to get. You reach the end of the tech room to find a giant, house sized computer. You also notice a tunnel behind some overgrown weeds")
    ans = triplechoice("go back", "destroy computer", "enter tunnel")
    if ans == ("1"):
        electric()
    if ans == ("2"):
        print("You destroy the ancient tech, and a part of history along with it. You pull out the vacuum tubes of the ENIAC, crushing them under your feet. AMISH ENDING")
    if ans == ("3"):
        secret()

def science():
    print("You reach a science room full of moldy chemical flasks and crumpled up trifold poster boards.")
    print()
    print("You turn around to see a giant monster made of sludge or something, pushing it's chest out to seem larger. It smells horrible. It suddenly smashes a table and destroys several poster boards")
    ans = triplechoice("go back", "throw a flask at it", "fight it with a poster board")
    if ans == ("1"):
        print("As you try to leave the science room, the monster grabs you and eats you. In it's stomach, you find several rubrics. Out of curiosity, you try to read them. Hmmm, they seem awfully unspecific. DIGESTIVE ENDING")
    if ans == "2":
        print("You throw a flask at the creature. The chemicals seem to make it stronger. The monster throws a whiteboard at you, and you die. WHITEBOARD ENDING")
    if ans == ("3"):
        print("You use a poster board to stab the heart of the beast. It lets down a deafening roar before dissolving into a puddle of goop. Since the puddle of goop is right in front of the door, there's no way to go but forward...")
        secret()

def secret():
    print("You find yourself in a pretty spooky chamber of the science room. You look through a crack in the wall to see the main science room.")
    print("The puddle of goop turns into a monster...")
    print("You also see a tunnel covered by overgrown weeds, along with another path")
    ans = askchoice("go in the tunnel", "continue onwards")
    if ans == "1":
        email()
    if ans == "2":
        chamber()

def chamber():
    print("You find a path to the main hall of the school.")
    ans = askchoice("go to the main hall", "continue on")
    if ans == "1":
        wilds()
    if ans == "2":
        final()

def final():
    print("You stumble upon an ancient and abandoned room.")
    print()
    print()
    print("An ominous mood fills the room.")
    print()
    print()
    print("The carvings on the wall appear to move...")
    print()
    print()
    print("You move forwards and see a giant, ominous statue. It's similar to the sludge monster you saw, except much more human like, although with a horribly disfigured face, with a gem encrusted in it's forehead.")
    print()
    print()
    print("The statue seems to beckon you to come closer, with trancelike whispering.")
    print()
    print()
    boompus()
def boompus():
    ans = askchoice("touch the statue", "leave")
    if ans == "2":
        print("You escape quickly, retreating to the main hall.")
        wilds()
    if ans == "1":
        sher()

def sher():
    print("You suddenly have a vision")
    print()
    print("You have remarkable power... You must destroy everything to create it anew... Others shun your for this power... You go to the main hall of your school... You utter sacred verses to unleash this power... The power leaked out. The extinction event has begun.")
    print()
    print("The school is destroyed. Those who shunned you have paid dearly. You are about to finish off the world, when someone, or something stops you. They seal you away for thousands of years.")
    print("In the thousands of years, you lose all humanity, and become an embodiment of pure rage. The seal is weakening. You will be freed.")
    print("...")
    print("...")
    print("...")
    print("...")
    print("...")
    print("...")
    print("...")
    print("'ʰᵉʸ.. ʰᵉʸʸʸ... ʷᵃᵏᵉ ᵘᵖ... ʷᵃᵏᵉ ᵘᵖ...'")
    print("...")
    print("...")
    print("...")
    print("'ʸᵒᵘ ᵒᵏˀˀˀ'")
    print("...")
    print("You snap back to reality")
    print("You realize what this means... You want nothing more than to destroy the statue, but doing so would free that... thing... inside. It wouldn't matter anyways, the seal will break soon. You can't fix it. There is nothing you can do.")
    print("Shocked, you go to the main hall. You can see the spot where the power was first released...")
    wilds()
    


def toilet():
    print("You enter the bathroom.")
    ans = triplechoice("enter stall", "leave", "go in closet")
    if ans == "2":
        wilds()
    if ans == "1":
        stall()
    if ans == "3":
        closet()

def stall():
    print("You enter the stall and see a security camera behind the toilet. Maybe you don't need to use the bathroom after all...")
    ans = askchoice("leave stall", "use the bathroom anyways")
    if ans == "1":
        toilet()
    if ans == "2":
        print("Disgusting. The camera is on, y'know. I'm gonna have to end the game on you out of my own distaste. GROSS ENDING")

def closet():
    print("You go in the closet and see 4 men playing cards.")
    ans = quadchoice("attack them", "ask to play with them", "cry", "go back")
    if ans == "4":
        toilet()
    if ans == "3":
        print("They look at you oddly, causing you to cry even more. JUDGEMENTAL ENDING")
    if ans == "1":
        battle()
    if ans == "2":
        cards()

def battle():
    print("The men suddenly merge to become a giant robot. The robot enters attack mode.")
    ans = askchoice("go for the jugular", "apologize")
    if ans == "2":
        print("It doesn't care, and eat you. TERMINATOR ENDING")
    if ans == "1":
        print("Yu strike the robot's julular vein (wait do robots even have veins??) and it collapses and explodes.")
        ans = askchoice("vow war against all robots", "sleep")
        if ans == "1":
            print("You waged war against all the robots. You go outside, and see every human on Earth standing before you. Suddenly, they all turn into robots. Oh no! Everyone was a robot the whole time!")
            if fun_factor > 700:
                print("Well, you waged war against them, so you pull a gun out of your pocket (you had that the whole time) and brutally kill the 8 billion robots, including Brother Julian-bot. GENOCIDE ENDING")
            else:
                print("The robots beat you. They put a machine in your brain. Now you are a robot too. Ṫ̵̬ẖ̶̽é̵̹y̵̯̿ ̵͈͑p̸̳̀ǘ̶̘n̵͔͂i̵͈͋s̷͉̉h̸̜̊ ̷̩͑y̷͖̆ȍ̷̬u̵͓̾.̷̗͋. They install a v̷̨̛͒i̸̦͚͔̎̑͝ŕ̸̢̌ụ̶̉͌ṣ̶̳͐̓̈́ ̴̻̩̾̑̈ḯ̶̤̤̖̂̄ṇ̵̌̅̚ͅs̷͈͈̋ḭ̶̏d̷̰͉́̒̕ẻ̴̲̎ ̸̫̰̗͗͝y̷͉̥̋̇͌ō̸̩͊̾ư̴͕͂̉. You feel i̶̠̩̦͂̅t̵̝̰̞̄ ẗ̷̳̪͉͎́̓̑̂ę̴̺̔́á̴̩̲̲͋ŕ̵̞̰̻ì̵̙̣͗͋̌̎ń̵̼̗͕̻̞̉̿̏g̴̡̜̓̈ ̶͉̹̬̥̿̅͝͠ẙ̴̺̏̌͝o̵̲̻͓̯̗͆̑ǔ̴̗͛̐͂ ̸͔̓͋a̴̼͓̳͛͊̈p̵̧̢͙̯̙̃̀̉̕͘ạ̵̢͕̐̓̓ŗ̵̲̹̄͝ͅt̶̜͍̒̄͘. Y̷͕̍ȯ̶̖͎ů̴̯͆̌ ̵̧̧̜̔̂̈́͠l̶͔̍ó̸̈s̵̢̪̀ë̴̤̦́̅̋̎ c̷̘̻̤͖͒o̵͈̱͕̬͒͝m̴̞̠͍͇̩͊̋̓̚͜͝p̸̞̗̝̺̻̉̐͑͒͠r̶̞͓͉͖̿͑ę̷̭͕͎͉̳͗̅͊̈́̑͜͝h̵̫̪̭̼͈̦̪͆͆͐̀̌̊̽ȅ̵̠͆̀̍n̷͕͈͈̅̀̑ͅs̷̰̹̜̃ï̴̺͉̲̭̲̬o̸̟̣̥͈̠̫͎̓͌͐̓̕͜ņ̵̡͎̙͈̰͔̝̑͒͌̍́͑́... Ỳ̷̡͉̰̱̭͚̟̮̲̲̰͔̦̟̯ơ̷̢̛̘̱̹̫̳̅͐̀͒̄̌̑͑͛́̅̌̈̄̄͆͛̚̕̕ů̶̧̩̯̞̜̟͓͒́̔͛̾̒̿ ớ̶̢̨̛̝̣̖͈̤̞̣̟̥̙̞̲̞̲͉͈̯̘͎̘̭͍̬̗̘͇̖̪̲̟̫̳͕̀̃̾͌͊̈́̂̌͘͜͠ͅv̴̢̝͙͎͇͎̥̩̜͇͇̤͈̖͆́̉̾̽̏͂̀̑̀̋̽̆͊͒̔̄̂̏̍̿́́̏̆̄̉̌͛̚̚̚̕͘͜͝͝ë̴̟͇̩̀ŕ̵̢̙̙̖̲̠̟̠͙͓̙̠͙̳̰̠̖̰̭̯̹͚̥̮̦͙̹͚̞̤͗͛̌͜l̵͖̝͚͎̝̱̼͎͕̯̈͜ǫ̷̦̥̲̙̩̤̼̫̪̙͓̣̞͔̬̑̓̐̉̃̄͝͝͠ͅa̷̡̡̡͙͈̱̭͓̹͎͍̦͚̰͔̖̗̗̲͎̬͇͊̍̈͗̒̊̽͗͜͜d̵͇͎͑̍͌̾̔͂͋̀̈͋̆͋̆̃̔͑͒̒̆̋̂̈́̿́͊͘͘̕͠.̴̛̜̘̤̼̦͕͙̣̀̊̈́͐͊̿͛̇͛̈́̂̾́̊̂̓͆͛̕͝")
                print()
                for i in range(25):
                    print(" ̷̡̛̗̫̮̼͙̣͖̩̟͙̞̆̈́̾̌̑͠ ̶̡͚̜̳̘̿͊̋͆̍͌ ̸̖̭̲͂̓̇̂̒̀̄̔͘ ̴̝͎̯̱͔͉̫̫̾ͅ ̴̤̪͓̙͕̉̋̌̽̍̄̊ ̴̥̲̠̜̤͕̤͐̌̿̈́͐͘ ̶̖̝͎̦̘͌͊͜ ̵̧̨̠̺̤̰͖͓̝͈̪͒̔̅ ̵̛͉͙̯̙͉͔̯̠͍̞̉ ̶̺̠͙̳̗̬̠̾͋̀̎ ̷̧̠͙̳̻̻̹͓̰̰̣̭̈̍̍́͆ ̷̛̹̻͔̼̞̭̫̟̰̤̍͐̐͗̓̄͒̽͗̕̕͜͠ ̴̞̯̌̿͊̅͠ ̵̫̉̏̍̇͋̕ ̶͚̝̯̳̲̲̱͚͓͕̲͎͑͜͝ ̸̨̢̞͗̈́̒̊̔̇͘ ̴͎̫͇̙̖̮̜̙̯̀̿̏͊̈̊͆͘͜͝ͅ ̸̖͎͇͛̆̂̏̇̓̅̏ ̴̟̣͔̻͆͋̈́̌͋͌̌̐͝ ̶̫͔̔͛́͌̇͜͝͝ͅ ̶̳̹͉̙̻̳̖̗̻̊́̽̕̕ͅ ̴̢̛̟͈̳̠̥̞̺̼̜̖̋̅̎̓̄̽̒̍͐̇̓̍ ̶̨̨̨̧̫̞̝̰̭̼͆͌̃̎͘͜͝ ̶̯͉̤̱͇̣̪͕͎͗́͐̽͗̔̋̏͠͠ ̸̢̡̬̲̝̱̱̙̮̯̜̿͗͛͘ ̶̨̣̟̠̫͗́̿̎̀̇̂̌̀̓̄ ̸̗͖̖̀̆̍̾̃͘͝͠ ̶̨̟̘̫̳̘̹̫̙͌͑́͊̇́̃͗͜͠ ̶̨̹̫̬̙̙̲͇̟̣̊͗̃̎̐͗̒́́̉ ̵̧̡̮̻̖̭̱̩͉͔̤̳̹̏̽̅̅̂̏ ̴̺̺͔̝͉̏̽̆̈́̉̀̌͛́͂̕ ̶̳̘̋̈́͋͘ ̵̛̪̣͓̼̌̐́̊̍̐̏̎̍͝͝ ̸̻̝͖͎̟̿̈̀̑̇̕ ̴͚͕̺͆̅͛̔̓̌̽̈́͠ͅ ̸̧͍̦͚̣͎̩̺̔ͅ ̶̮̞̣̦͌͌͑͗̇ ̷͇̭̱̫͉̝͉͈̣̲̓̉̽͂̈́̈̿ ̶̨̲̬̰̾̓͑̓̓̄̎͒̕͠ ̵̨̛̭̦͚̩͈̈́̿͒̌͒̿̽̐̓̎̿͠ͅ ̶̪̱͉̘̼̭͑̈́͆͊͐͝͝ ̷̘͍͖̀̈́̅̓̓̃̃̈́̿ ̴̛̖̘̹̲͍͔͖̩̟̳͉̟̬̀̐͑̃̊̈́̆̀͗̐͝͠ ̸̡͚̪̟̠͍̻̻͍̦̋́͑̄̓̓̋́̀͝ ̷̭͊͛̒̄̀͗ ̶̛̤̩̤̦̀̈́͋̒͛̅ ̷̡̡̢̨͙̺͕̦̮͔͎̝͇̇̉͒͒͐͛͝ ̴̡̡̧̩̣̬̏̊͛̐̚ ̶̯̭͇̠̲̮͍͔̳̺͈͎͑͌̈́̕̕ ̴̡̨͓̞͍͎̬̘̩̜̫̟̣̐̽̓̿̀́͊͠͝ ̶̣̽̊̍̒̓́̓̅͆̎̇̿ ̵̢̛̹̩̤͓̰̤̙̻͈̓̏̅̈́͒̐͆̏̅̓̉̋ ̴̢̨͙̥͍̩͙̭͉̙̱̫̓̉̌͐͋̏ ̴̧̯̮̜̖͖̰̠͊̀̇͝ͅ ̷̢͔̬͍̩̯͐̅͗̃̄͂̈͗̈̀́̋ ̵̟̣͆̐̏̂͑͋́̂̕ ̵̹͙̱̙͍̞̱͕͈̥̣̾̉ ̶͈͔̦͔̳̩͈̘̥͉̍̐͊̎̿̒̎͆͊͘̕ͅ ̴̡̢͓̟̦͚̲̳͚͔̟̠̅̉̓ ̵̣̜̦̈́͘ ̵̢̛͔͇̰̣̖̘̠̄͛̿͜͝ ̶̨̛̖̖̬̲̹͔̖̪̬͆͗́̑͆͜ ̶̻͈͕͚̏̀̅̃̚͝ ̷̘̺̥͍͚̞͈͌͐ ̷̛̛͔̗͆̈́̾̒͐͒͂̓̋͑ ̸̺̭͕̂̓͒̑̓̀̔̔̌̀ͅ ̵̖̖̱̳̪͙͔̘̓̑̽͋̈́̇̿́̿̕͘ ̶̢͓͍͚̠̙̝̺̗̤̑͂̅̉ ̷̡͙̒̒̆̿̀ ̸̨̯̝̱̰̱̮̩͈̟͎̪̃̌̅͝ ̸̬̼̈́̊́̉̓̀̏̈́͑͊̆ ̷̧̛̞̯͎̠̰̱͈̘̞͎̼̿̈́̃̇̃̓̈͘͠͠ͅ ̶̙̲͋̏̿̊̀̚͜ ̴̨̝̫̘̘͔͋͊̐̈͊ͅ ̶͔̣̹̪̗̪̩̠̱̱̭͕͛̓̍͒͘ ̷̡̘͔̮̟̞͉̩̥̣̗͒͜ͅ ̶͔̩͓͈̰̘̭͑́͋̄͑̓ ̸̧̻̱̠̹͔̠̬̝̉̈́̽̎͊̕͜͜͝ ̵̧̡̧͙̥͎͓͇̊ ̴̼̻͙̞͈͇̖͈̺͐̊̓́̓̓̍́̓͊͊́͊͜͜ ̵̛̰̼̿̊̽́̋̾̊̽͋͝ ̴̨̧̨͕̤̬̠̱̺̰͕̬̜̀͒̓͗͐̉͘ ̵̛̞̫̏̔̒̌̏̀̓̅͜͠͠͝ ̸̟̺̝͚̤͚͓̪̱̯̥̈͐̆̋̋̽̒̒̀̚ ̶̡̮̲̯̳̲͖̹͙̯͎͂̃̈́̈́͘͜ͅ ̶̢̧̢̤̦̯̼̘̞̹͉͖̖̾͒̈́̀̽͌̆͝ ̸̥̤͇̈̇͑ ̵̡͍̞̝͎͔̤̺̖̊̀̓̿̔̚ ̵̱̲͊͗̈́̈̈́̆̃͒̿̈̌͌͠")
                raise ValueError("CORRUPTED ENDING")
        if ans == "2":
            print("You sleep :). SLEEPY ENDING")

def cards():
    if fun_factor > 251 and fun_factor < 700:
        print("They let you play. You become great friends with the men, and play cards with them forever. Eventually you die of old age. ELDERLY ENDING")
    else:
        print("They don't let you play, and shun you.")
        toilet()

def richard():
    print("You enter the office. It reeks of unfinished paperwork and broken promises.")
    ans = triplechoice("go back", "go to secretary desk", "enter back room")
    if ans == "1":
        wilds()
    if ans == "2":
        print("The desk is full of scattered paperwork. One student log catches your eye.")
        ans = askchoice("read it", "put it away")
        if ans == "2":
            richard()
        if ans == "1":
            print('''
             STUDENT ID: 012524
             STUDENT NAME: █████████████
             EXCEPTIONALITIES: GI█T█D, H█PE██MO█I█NAL, IM██ES███NAB█E, ██GM█
             CAPABILITIES OF NOTE: ABLE TO L██K ██T OF T█E EM███HU█E, W██TE█ █NGR█ EM█I█S, A█SF
             T&R PHASE ONE RESULTS: DEMONSTRATED AN UNUSUAL ABILITY TO CREATE T██OAC█T█N█
             T&R PHASE TWO STATUS: A█PR█V█D - N█T Y██ C██PL█TE
             
             ---the bottom half of the paper seems to be ripped off---''')
            print()
            print()
            print("Huh, odd. What could T&R be...?")
            richard()  
    if ans == "3":
        back()


def back():
    print("The back room smells like decay. There is a strange machine in the middle. It says 'Surround Sound System™'. Weird...")
    ans = askchoice("investigate machine", "go back")
    if ans == "2":
        richard()
    if ans == "1":
        print("It has a speaker system in all directions. It's covered in moldy stains. Gross... ")
        ans = askchoice("lick the mold", "go back")
        if ans == "1":
            if fun_factor > 800:
                print("You know what? I'm not gonna let you. I can't in good faith let you lick the spooky mold.")
                ans = askchoice("lick the mold anyways", "make a wise decision")
                if ans == "1":
                    print("bruh. You lick the mold anyways, disgusting freak. You see weird hallucinations of trees and the wilderness. You feel at peace. And then you die painfully. What did you expect? Remember kids, don't do drugs, or this could be you. PSA ENDING")
                if ans == 2:
                    back()
            else:
                 print("Disgusting freak. You lick it and you see weird hallucinations of trees and the wilderness. You feel at peace. And then you die painfully. What did you expect? Remember kids, don't do drugs, or this could be you. PSA ENDING")
        if ans == "2":
             richard()
        

def startgame():
    print("Welcome to the cool game! In the cool game you can do cool things! You are at the house of your dear Brother Julian")
    ans = askchoice("kick brother julian", "hug brother julian")
    if ans == ("1"):
        violence()
    if ans == ("2"):
        print("Brother Julian makes you some cookies")
        ans = askchoice("eat them", "deny the cookies")
        if ans == "1":
            print("You eat them. They're pretty good, actually. GOOD ENDING")
        if ans == "2":
            print("Brother Julian cries. TEARS ENDING")

startgame()