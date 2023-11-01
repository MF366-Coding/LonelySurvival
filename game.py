# pylint: disable=W0603

from colorama import Fore
import save_system as saves
import sys, os, time, keyboard
from pygame import mixer

mixer.init()

y = saves.load()

script_path = os.path.abspath(__file__)
script_dir = os.path.abspath(os.path.dirname(script_path))
sounds_dir = os.path.join(script_dir, "sounds")

loads_gun = mixer.Sound(os.path.join(sounds_dir, "load_gun.mp3"))
uses_gun = mixer.Sound(os.path.join(sounds_dir, "gun.mp3"))

def read_event(suppress: bool = False) -> keyboard.KeyboardEvent:
    time.sleep(1.0)
    return keyboard.read_event(suppress=suppress)

def clear():
    if sys.platform == 'win32':
        os.system("cls")
    else:
        os.system('clear')

def output(speaker: str, mainStr: str):
    print(speaker, Fore.RESET)
    time.sleep(0.3)
    input(mainStr + '\n')


def start_point():
    global y

    saves.save(y[0], y[1])

    y = saves.load()

    clear()
    start_game()


def break_point():
    y[0]["day"] += 1
    start_point()


death_ends = ("te", "me", "woe", "bete")

def death(death_msg: str):
    print(f"""{Fore.RED}
██    ██  ██████  ██    ██     ██████  ██ ███████ ██████  ██ 
 ██  ██  ██    ██ ██    ██     ██   ██ ██ ██      ██   ██ ██ 
  ████   ██    ██ ██    ██     ██   ██ ██ █████   ██   ██ ██ 
   ██    ██    ██ ██    ██     ██   ██ ██ ██      ██   ██    
   ██     ██████   ██████      ██████  ██ ███████ ██████  ██ 
                                                             
                              """)

    input(f"Mistakes were made{Fore.RESET}\n{death_msg}\n...\nI'll restart for you, buddy!")
    start_game()


def start_game():
    if not y[1]["start"]:
        y[1]["start"] = True
        saves.save(y[0], y[1])
        input(f"{Fore.CYAN}Achievment Unlocked: {Fore.YELLOW}The Start of a New Adventure{Fore.RESET}\nStart Day 1 for the very first time.\n")
    
    # [i] Day 1
    if y[0]["day"] == 1:
        print(f'''{Fore.GREEN}
██████   █████  ██    ██      ██ 
██   ██ ██   ██  ██  ██      ███ 
██   ██ ███████   ████        ██ 
██   ██ ██   ██    ██         ██ 
██████  ██   ██    ██         ██ 
                                 
                                            ''')
        input(f"{Fore.CYAN}As you go home after school, you notice your parents haven't arrived yet. Looks like you'll be alone for 2 hours.\n")
        output(f"{Fore.MAGENTA}You", "Finally, some time for myself. What should I do first?")
        print("""1) Watch YouTube
2) Study
3) Sleep
        """)

        read_event()

        if keyboard.is_pressed("1"):
            output(f"{Fore.MAGENTA}You", "I'm gonna watch my favorite youtuber...")

        if keyboard.is_pressed("2"):
            output(f"{Fore.MAGENTA}You", "I don't want to disappoint my parents so I guess I'll study...")

        if keyboard.is_pressed("3"):
            output(f"{Fore.MAGENTA}You", "Who doesn't love a quick nap?")

        input(f"{Fore.BLUE}1 HOUR AND 45 MINUTES LATER{Fore.RESET}\n")

        input(f"{Fore.GREEN}The phone is ringing. You decide to pick it up.\n")

        output(f"{Fore.MAGENTA}You", "Hello. Who am I talking to?")
        output(f"{Fore.RED}???", "Hello this is... uh... a Police information, yes.")
        output(f"{Fore.MAGENTA}You", "What's the information?")
        output(f"{Fore.RED}Police Officer???", "We are questioning children if they're home alone and if they are, we'd like to know if they're fine.")
        output(f"{Fore.MAGENTA}You", "I shouldn't speak to strangers...")
        output(f"{Fore.RED}Police Officer???", "B-But I am a Police Officer! You can trust me.")
        output(f"{Fore.MAGENTA}You", "Fine. Yes, I am alone... at home... And yes, I'm quite fine.")
        output(f"{Fore.MAGENTA}You", "It's also something that happens every Monday and-")
        output(f"{Fore.RED}Police Officer???", "Stop right there. As soon as I track this call, you're a little dead boy.")
        output(f"{Fore.MAGENTA}You", "E-E-E-Exc-Excuse me??")
        output(f"{Fore.RED}Mad Person (Killer???)", "Get ready! 'Cause I'm coming for ya...")

        if y[1]["last-end"] in death_ends:
            output(f"{Fore.RED}Killer", "(Last time I did this, things didn't go according to the plan...)")

        if y[1]["last-end"] == "we":
            output(f"{Fore.RED}Killer", "Fun Fact: the last kid I tortured ended up teaming with me.\nBye, kiddo!")

        if y[1]["last-end"] == "se":
            output(f"{Fore.RED}Killer", "I hope you don't take your own life just like the previous kid...\nThat's cheating and it ruins the fun!!")

        if y[1]["last-end"] == "ne":
            output(f"{Fore.RED}Killer", "Also... er... all Mondays? Home alone?")
            output(f"{Fore.MAGENTA}You", "I'm in shock!")
            output(f"{Fore.RED}Killer", "So it's a yes! See you next Monday kiddo...")

        input(f"{Fore.RED}The other side hang up.\n")

        output(f"{Fore.MAGENTA}You", ".")

        for i in range(6):
            time.sleep(1.3)
            print(".\n")

        input("Please help!\n")

        print(f"""{Fore.YELLOW}
██    ██  ██████  ██    ██     ███████ ██    ██ ██████  ██    ██ ██ ██    ██ ███████ ██████  ██ 
 ██  ██  ██    ██ ██    ██     ██      ██    ██ ██   ██ ██    ██ ██ ██    ██ ██      ██   ██ ██ 
  ████   ██    ██ ██    ██     ███████ ██    ██ ██████  ██    ██ ██ ██    ██ █████   ██   ██ ██ 
   ██    ██    ██ ██    ██          ██ ██    ██ ██   ██  ██  ██  ██  ██  ██  ██      ██   ██    
   ██     ██████   ██████      ███████  ██████  ██   ██   ████   ██   ████   ███████ ██████  ██ 
                                                                                                
                                                                                                {Fore.RESET}""")

        print("Do you wish to leave or do you want to keep playing?\n")
        print("""1) Keep playing
2) Leave
    """)

        read_event()

        if keyboard.is_pressed("1"):
            break_point()

        if keyboard.is_pressed('2'):
            time.sleep(1.7)
            sys.exit()

    # [i] Day 2
    if y[0]["day"] == 2:
        print(f'''{Fore.GREEN}
██████   █████  ██    ██     ██████ 
██   ██ ██   ██  ██  ██           ██ 
██   ██ ███████   ████        █████  
██   ██ ██   ██    ██        ██     
██████  ██   ██    ██        ███████ 
                                     
                                            ''')
        input(f"{Fore.CYAN}As you go home after school, you notice your parents haven't arrived yet. Looks like you'll be alone for 2 hours.\n")
        output(f"{Fore.MAGENTA}You", "Oh no, another day alone! What should I do to relax?")
        print("""1) Watch YouTube
2) Study
3) Sleep
        """)


        read_event()

        if keyboard.is_pressed("1"):
            output(f"{Fore.MAGENTA}You", "I'm gonna watch my favorite youtuber...")

        if keyboard.is_pressed("2"):
            output(f"{Fore.MAGENTA}You", "I don't want to disappoint my parents so I guess I'll study...")

        if keyboard.is_pressed("3"):
            output(f"{Fore.MAGENTA}You", "Who doesn't love a quick nap?\nHowever, with this killer out there I should be ready for action I guess...")

        input(f"{Fore.BLUE}1 HOUR AND 35 MINUTES LATER{Fore.RESET}\n")

        input(f"{Fore.GREEN}The phone is ringing. You're shaking, but still decide to pick it up.\n")

        output(f"{Fore.MAGENTA}You", "H-Hey... Who am I t-t-talking to?")
        output(f"{Fore.RED}???", "Hey boy! We meet again...")
        output(f"{Fore.MAGENTA}You", "Not you again! Go to bloody hell!")
        output(f"{Fore.RED}Killer", "First, yes, 'me' again. And second, shut it! I'm the one who talks.")
        output(f"{Fore.RED}Killer", "You are quite aware I know where you live.")
        output(f"{Fore.RED}Killer", "Oh it's the mailman!... Hey sir! Are you delivering the mail?")
        output(f"{Fore.RED}Killer", "You are? Not for long!...")

        loads_gun.play()
        time.sleep(0.25)
        uses_gun.play()
        time.sleep(2)

        output(f"{Fore.RED}Killer", "Now you know I'm not f***ing around anymore.")
        output(f"{Fore.MAGENTA}You", "You're sick!")
        output(f"{Fore.RED}Killer", "It was nice knowing you kiddo...")

        input(f"{Fore.RED}The other side hang up.\n")

        output(f"{Fore.MAGENTA}You", "If he thinks I'll just stand here not doing anything, he's wrong!")
        output(f"{Fore.MAGENTA}You", "However I probably need some sort of Weapon or Armor.")
        output(f"{Fore.MAGENTA}You", "I was able to gather some stuff but what should I use?")
        print("""1) Pillow [Not a weapon but can be used to block the killer for a short while.]
2) Chair [Can be used both as weapon and as a shield. It can also block doors from inside.]
3) Oil [It makes the floor slippery.]
        """)

        weap = None

        read_event()

        if keyboard.is_pressed("1"):
            output(f"{Fore.MAGENTA}You", "I guess I'll take... a pillow? Yeah, I guess...")
            weap = "pillow"

        if keyboard.is_pressed("2"):
            output(f"{Fore.MAGENTA}You", "Now this is hard to handle.")

            print("""1) Use the chair as a weapon by throwing it
2) Use it to block attacks
3) Use it to lock the door from inside
""")

            read_event()

            if keyboard.is_pressed("1"):
                output(f"{Fore.MAGENTA}You", "Alright... Hope I stay alive...")
                weap =  "chair-attack"
                y[0]["weapons"] += 1

            if keyboard.is_pressed("2"):
                output(f"{Fore.MAGENTA}You", "Let's do this then...")
                weap = "chair-shield"

            if keyboard.is_pressed("3"):
                output(f"{Fore.MAGENTA}You", "I should play defensive so I'm locking the door.")
                weap = "chair-lock"


        if keyboard.is_pressed("3"):
            output(f"{Fore.MAGENTA}You", "I should probably spread this on the floor...\nThere, it's done!")
            weap = "oil"

        if weap == "chair-attack":
            output(f"{Fore.MAGENTA}You", "I really don't want to do this...")
            output(f"{Fore.MAGENTA}You", "Uh... Here goes nothing...")
            output(f"{Fore.RED}Killer", "I honestly thought you'd never show up.\nI thought you were going to lock yourself and hide like the cry baby you are.")
            output(f"{Fore.RED}Killer", "You can't do anything.\nYou're all alone.\nDaddy, mommy, come help me before I get shot 20 times on the head.\nScream, boy...\nI'll be outta here faster that my dad getting milk.")
            output(f"{Fore.MAGENTA}You", "I'm no ordinary kid. You shall be punished for what you're trying to do to me.")
            output(f"{Fore.RED}Killer", f"Don't make me laugh, kiddo. You can't win this fight...\nThe fight against {Fore.RED}death{Fore.RESET}.\nEnjoy your death, bastard.")
            output(f"{Fore.MAGENTA}You", "You asked for it.")
            input(f"{Fore.BLUE}Like a master, you grabbed the chair and threw it at the killer.\nWhile falling down the stairs, he cursed at you. Several times.{Fore.RESET}")
            output(f"{Fore.MAGENTA}You", "Get the freak outta here, you nasty piece of s***! No wonder your dad left you.")

        if weap == "chair-lock":
            output(f"{Fore.MAGENTA}You", "I'll be safe if I lock the door, right?")
            output(f"{Fore.MAGENTA}You", "Alright there we go!")
            output(f"{Fore.RED}Killer", "I thought so. I knew you were going to lock yourself and hide like the cry baby you are.")
            output(f"{Fore.RED}Killer", "You can't do anything.\nYou're all alone.\nDaddy, mommy, come help me before I get shot 20 times on the head.\nScream, boy...\nI'll be outta here faster that my dad getting milk.")
            output(f"{Fore.MAGENTA}You", "Well, good luck unlocking the door weirdo.")
            output(f"{Fore.RED}Killer", "(This situation sucks, I need to learn how to break into a locked house. Lonelingo has math, languages and robbing stuff so I guess it could work.)")
            output(f"{Fore.RED}Killer", "I'll come back with the needed info to finish the job.")
            output(f"{Fore.MAGENTA}You", "That's right, loser! Get outta here, you nasty piece of s***! No wonder your dad left you.")

        if weap == "chair-shield":
            output(f"{Fore.MAGENTA}You", "I literally have a shield. His bullets will be stopped.")
            output(f"{Fore.MAGENTA}You", "Alright here I go!")
            output(f"{Fore.RED}Killer", "Look who it is. The kid I need to kill... and he's holding a chair.")
            output(f"{Fore.MAGENTA}You", "You can't do anything.\nMy shield stops your bullets.")
            output(f"{Fore.RED}Killer", "Then I guess we can test that!")

            loads_gun.play()
            time.sleep(0.25)
            uses_gun.play()
            time.sleep(2)

            output(f"{Fore.RED}Killer", "Uh...\nWell, that was easy!")

            death("If chairs were shields, I'd be equipped for war.")

        if weap == "pillow":
            output(f"{Fore.MAGENTA}You", "I'm not sure how a pillow will protect me but whatever...")
            output(f"{Fore.MAGENTA}You", "Alright here goes nothing...")
            output(f"{Fore.RED}Killer", "So we meet... FINALLY! I wanted to kill you so badly!")
            output(f"{Fore.RED}Killer", "You can't do anything.\nYou're all alone.\nDaddy, mommy, come help me before I get shot 20 times on the head.\nScream, boy...\nI'll be outta here faster that my dad getting milk.")
            output(f"{Fore.MAGENTA}You", "Well, good luck shooting through this pillow.")

            for i in range(20):
                loads_gun.play()
                time.sleep(0.25)
                uses_gun.play()
                time.sleep(2.2)

            death("First, WHADAHELL IS WRONG WITH YOU?!\nSecond, no way bro actually shot you 20 times")

        if weap == "oil":
            output(f"{Fore.MAGENTA}You", "HEY STUPID KILLER! COME! THE DOOR ISN'T LOCKED!")
            output(f"{Fore.RED}Killer", "Fine... There, I'm in!")
            output(f"{Fore.RED}Killer", "There you are. Oh crap! There's oil in the floor...")
            output(f"{Fore.RED}Killer", "I guess I should shoot you from here then!")

            loads_gun.play()
            time.sleep(0.25)
            uses_gun.play()
            time.sleep(2)
            death("I quit.")

        print(f"""{Fore.YELLOW}
██    ██  ██████  ██    ██     ███████ ██    ██ ██████  ██    ██ ██ ██    ██ ███████ ██████  ██ 
 ██  ██  ██    ██ ██    ██     ██      ██    ██ ██   ██ ██    ██ ██ ██    ██ ██      ██   ██ ██ 
  ████   ██    ██ ██    ██     ███████ ██    ██ ██████  ██    ██ ██ ██    ██ █████   ██   ██ ██ 
   ██    ██    ██ ██    ██          ██ ██    ██ ██   ██  ██  ██  ██  ██  ██  ██      ██   ██    
   ██     ██████   ██████      ███████  ██████  ██   ██   ████   ██   ████   ███████ ██████  ██ 
                                                                                                
                                                                                                {Fore.RESET}""")

        print("Do you wish to leave or do you want to keep playing?\n")
        print("""1) Keep playing
2) Leave
    """)

        read_event()

        if keyboard.is_pressed("1"):
            break_point()

        if keyboard.is_pressed('2'):
            time.sleep(1.7)
            sys.exit()

    # [i] Day 3
    if y[0]["day"] == 3:
        print(f'''{Fore.GREEN}
██████   █████  ██    ██     ██████ 
██   ██ ██   ██  ██  ██           ██ 
██   ██ ███████   ████        █████  
██   ██ ██   ██    ██             ██ 
██████  ██   ██    ██        ██████  
                                    
                                            ''')
        input(f"{Fore.CYAN}As you go home after school, you notice your parents haven't arrived yet. Looks like you'll be alone for 2 hours.\n")
        output(f"{Fore.MAGENTA}You", "Yet another day alone! What should I do to relax?")
        print("""1) Finish the homework
2) Play videogames
3) Watch YouTube
        """)

        read_event()

        if keyboard.is_pressed("3"):
            output(f"{Fore.MAGENTA}You", "I guess I'll watch my favorite youtuber...")

        if keyboard.is_pressed("1"):
            output(f"{Fore.MAGENTA}You", "I don't want to disappoint my parents so I'll do my homework...")

        if keyboard.is_pressed("2"):
            output(f"{Fore.MAGENTA}You", "Imma play this new game!\nAlthrought it might be the last time I play it.")

        input(f"{Fore.BLUE}1 HOUR LATER{Fore.RESET}\n")

        input(f"{Fore.GREEN}The phone is ringing. As usual, you decide to pick it up.\n")

        output(f"{Fore.MAGENTA}You", "It's you again, loser.")
        output(f"{Fore.BLUE}Officer Lotus", "It's Police Officer Helena Lotus over here, kiddo! Show some respect for the people who are better than you!")
        output(f"{Fore.MAGENTA}You", "Oh, I see...")
        
        print("""1) Did I ask?
2) Still a loser
3) Why are you calling me anyway?
""")

        read_event()

        if keyboard.is_pressed("1") or keyboard.is_pressed("2"):
            output(f"{Fore.BLUE}Lotus", "(Just breathe and imagine yourself killing children, Lotus...)\nWhatever, idiot.")
            
            if not y[1]["mean"]:
                y[1]["mean"] = True
                saves.save(y[0], y[1])
                input(f"{Fore.CYAN}Achievment Unlocked: {Fore.YELLOW}Meanie{Fore.RESET}\nBe mean to Officer Lotus.\n")

        if keyboard.is_pressed("3"):
            output(f"{Fore.BLUE}Lotus", "Don't you think I'll explain it, weirdo?")
            output(f"{Fore.MAGENTA}You", "Honestly, I don't.")
        
        output(f"{Fore.BLUE}Lotus", "I'm calling you for a survey.")
        output(f"{Fore.MAGENTA}You", "'No' to everything.")
        output(f"{Fore.BLUE}Lotus", "Lemme explain it! I'll come to your house (yes, I tracked the call) and you'll take the survey there.")
        output(f"{Fore.MAGENTA}You", "Ok, traffic officer...")
        output(f"{Fore.BLUE}Lotus", "One of these days, I swear I'll shoot someone!")

        input(f"{Fore.RED}You hang up.\n")

        # [!!] TO BE CHANGED TOMORROW VERY URGENT
        raise NotImplementedError

        output(f"{Fore.MAGENTA}You", "If he thinks I'll just stand here not doing anything, he's wrong!")
        output(f"{Fore.MAGENTA}You", "However I probably need some sort of Weapon or Armor.")
        output(f"{Fore.MAGENTA}You", "I was able to gather some stuff but what should I use?")
        print("""1) Pillow [Not a weapon but can be used to block the killer for a short while.]
2) Chair [Can be used both as weapon and as a shield. It can also block doors from inside.]
3) Oil [It makes the floor slippery.]
        """)

        weap = None

        read_event()

        if keyboard.is_pressed("1"):
            output(f"{Fore.MAGENTA}You", "I guess I'll take... a pillow? Yeah, I guess...")
            weap = "pillow"

        if keyboard.is_pressed("2"):
            output(f"{Fore.MAGENTA}You", "Now this is hard to handle.")

            print("""1) Use the chair as a weapon by throwing it
2) Use it to block attacks
3) Use it to lock the door from inside
""")

            read_event()

            if keyboard.is_pressed("1"):
                output(f"{Fore.MAGENTA}You", "Alright... Hope I stay alive...")
                weap =  "chair-attack"
                y[0]["weapons"] += 1

            if keyboard.is_pressed("2"):
                output(f"{Fore.MAGENTA}You", "Let's do this then...")
                weap = "chair-shield"

            if keyboard.is_pressed("3"):
                output(f"{Fore.MAGENTA}You", "I should play defensive so I'm locking the door.")
                weap = "chair-lock"


        if keyboard.is_pressed("3"):
            output(f"{Fore.MAGENTA}You", "I should probably spread this on the floor...\nThere, it's done!")
            weap = "oil"

        if weap == "chair-attack":
            output(f"{Fore.MAGENTA}You", "I really don't want to do this...")
            output(f"{Fore.MAGENTA}You", "Uh... Here goes nothing...")
            output(f"{Fore.RED}Killer", "I honestly thought you'd never show up.\nI thought you were going to lock yourself and hide like the cry baby you are.")
            output(f"{Fore.RED}Killer", "You can't do anything.\nYou're all alone.\nDaddy, mommy, come help me before I get shot 20 times on the head.\nScream, boy...\nI'll be outta here faster that my dad getting milk.")
            output(f"{Fore.MAGENTA}You", "I'm no ordinary kid. You shall be punished for what you're trying to do to me.")
            output(f"{Fore.RED}Killer", f"Don't make me laugh, kiddo. You can't win this fight...\nThe fight against {Fore.RED}death{Fore.RESET}.\nEnjoy your death, bastard.")
            output(f"{Fore.MAGENTA}You", "You asked for it.")
            input(f"{Fore.BLUE}Like a master, you grabbed the chair and threw it at the killer.\nWhile falling down the stairs, he cursed at you. Several times.{Fore.RESET}")
            output(f"{Fore.MAGENTA}You", "Get the freak outta here, you nasty piece of s***! No wonder your dad left you.")

        if weap == "chair-lock":
            output(f"{Fore.MAGENTA}You", "I'll be safe if I lock the door, right?")
            output(f"{Fore.MAGENTA}You", "Alright there we go!")
            output(f"{Fore.RED}Killer", "I thought so. I knew you were going to lock yourself and hide like the cry baby you are.")
            output(f"{Fore.RED}Killer", "You can't do anything.\nYou're all alone.\nDaddy, mommy, come help me before I get shot 20 times on the head.\nScream, boy...\nI'll be outta here faster that my dad getting milk.")
            output(f"{Fore.MAGENTA}You", "Well, good luck unlocking the door weirdo.")
            output(f"{Fore.RED}Killer", "(This situation sucks, I need to learn how to break into a locked house. Lonelingo has math, languages and robbing stuff so I guess it could work.)")
            output(f"{Fore.RED}Killer", "I'll come back with the needed info to finish the job.")
            output(f"{Fore.MAGENTA}You", "That's right, loser! Get outta here, you nasty piece of s***! No wonder your dad left you.")

        if weap == "chair-shield":
            output(f"{Fore.MAGENTA}You", "I literally have a shield. His bullets will be stopped.")
            output(f"{Fore.MAGENTA}You", "Alright here I go!")
            output(f"{Fore.RED}Killer", "Look who it is. The kid I need to kill... and he's holding a chair.")
            output(f"{Fore.MAGENTA}You", "You can't do anything.\nMy shield stops your bullets.")
            output(f"{Fore.RED}Killer", "Then I guess we can test that!")

            loads_gun.play()
            time.sleep(0.25)
            uses_gun.play()
            time.sleep(2)

            output(f"{Fore.RED}Killer", "Uh...\nWell, that was easy!")

            death("If chairs were shields, I'd be equipped for war.")

        if weap == "pillow":
            output(f"{Fore.MAGENTA}You", "I'm not sure how a pillow will protect me but whatever...")
            output(f"{Fore.MAGENTA}You", "Alright here goes nothing...")
            output(f"{Fore.RED}Killer", "So we meet... FINALLY! I wanted to kill you so badly!")
            output(f"{Fore.RED}Killer", "You can't do anything.\nYou're all alone.\nDaddy, mommy, come help me before I get shot 20 times on the head.\nScream, boy...\nI'll be outta here faster that my dad getting milk.")
            output(f"{Fore.MAGENTA}You", "Well, good luck shooting through this pillow.")

            for i in range(20):
                loads_gun.play()
                time.sleep(0.25)
                uses_gun.play()
                time.sleep(2.2)

            death("First, WHADAHELL IS WRONG WITH YOU?!\nSecond, no way bro actually shot you 20 times")

        if weap == "oil":
            output(f"{Fore.MAGENTA}You", "HEY STUPID KILLER! COME! THE DOOR ISN'T LOCKED!")
            output(f"{Fore.RED}Killer", "Fine... There, I'm in!")
            output(f"{Fore.RED}Killer", "There you are. Oh crap! There's oil in the floor...")
            output(f"{Fore.RED}Killer", "I guess I should shoot you from here then!")

            loads_gun.play()
            time.sleep(0.25)
            uses_gun.play()
            time.sleep(2)
            death("I quit.")

        print(f"""{Fore.YELLOW}
██    ██  ██████  ██    ██     ███████ ██    ██ ██████  ██    ██ ██ ██    ██ ███████ ██████  ██ 
 ██  ██  ██    ██ ██    ██     ██      ██    ██ ██   ██ ██    ██ ██ ██    ██ ██      ██   ██ ██ 
  ████   ██    ██ ██    ██     ███████ ██    ██ ██████  ██    ██ ██ ██    ██ █████   ██   ██ ██ 
   ██    ██    ██ ██    ██          ██ ██    ██ ██   ██  ██  ██  ██  ██  ██  ██      ██   ██    
   ██     ██████   ██████      ███████  ██████  ██   ██   ████   ██   ████   ███████ ██████  ██ 
                                                                                                
                                                                                                {Fore.RESET}""")

        print("Do you wish to leave or do you want to keep playing?\n")
        print("""1) Keep playing
2) Leave
    """)

        read_event()

        if keyboard.is_pressed("1"):
            break_point()

        if keyboard.is_pressed('2'):
            time.sleep(1.7)
            sys.exit()