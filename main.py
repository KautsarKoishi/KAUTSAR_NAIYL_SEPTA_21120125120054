import tkinter as tk
import sys
import threading
import queue
import pygame
import time
from PIL import Image, ImageTk
from tkinter import font
import json
import ast
import os
import shelve
import pickle

print("")
print(">>>>> TERRA LEGENDS: MYTHOS <<<<<")
print("version : Pre-Alpha Test 1.1")
print("")

# PYGAME MIXER

pygame.mixer.init()
pygame.init()

ambient_forest = pygame.mixer.Sound("Audio/Forest.mp3")
sound_1 = pygame.mixer.Sound("Audio/BONUS.wav")
attack_1 = pygame.mixer.Sound("Audio/SFX/ATTACK5.wav")
effect_1 = pygame.mixer.Sound("Audio/SFX/TWINKLE2.wav")

# PRINT

class TkinterConsole:
    def __init__(self, text_widget, queue):
        self.text_widget = text_widget
        self.queue = queue

    def write(self, message):
        self.queue.put(message)

    def flush(self):
        pass

# INPUT

class InputManager:
    def __init__(self):
        self.queue = queue.Queue()

    def get_input(self, prompt=""):
        print(prompt)
        return self.queue.get()  # BLOCKS safely in thread

input_manager = InputManager()

def input(prompt=""):
    return input_manager.get_input(prompt)

# GUI

root = tk.Tk()
root.title("Terra Mythos")
root.geometry("800x600")
root.iconbitmap("Terra.ico")

text_area = tk.Text(root, wrap=tk.WORD, font=("Times New Roman", 14), bg="#222", fg="#fff", height=25, width=70, state="disabled")
text_area.pack(padx=10, pady=10)

entry = tk.Entry(root, width=100)
entry.pack(side="left", padx=50)

def submit_input():
    text = entry.get()
    entry.delete(0, tk.END)
    input_manager.queue.put(text)

submit_btn = tk.Button(root, text="Submit", command=submit_input)
submit_btn.pack(side="left")

# CUSTOMIZATION

bg_image_path = None  # Change to your image path
if not bg_image_path:
    pass
else:
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((800, 600), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def change_colors(bg="#000", fg="#fff"):
    text_area.config(bg=bg, fg=fg)

def change_bg_image(path):
    img = Image.open(path)
    img = img.resize((800, 600), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(img)
    bg_label.config(image=new_image)

#text_area = tk.Text(root, wrap=tk.WORD, font=("Courier", 14), bg="#222", fg="#fff")
#text_area.pack(expand=True, fill=tk.BOTH)
#text_area.config(state=tk.DISABLED)

#input_field = tk.Entry(root, font=("Courier", 14))
#input_field.pack(fill=tk.X)

#bg_image_path = "Background.png"  # Change to your image path
#bg_image = Image.open(bg_image_path)
#bg_image = bg_image.resize((800, 600), Image.ANTIALIAS)
#bg_photo = ImageTk.PhotoImage(bg_image)

#bg_label = tk.Label(root, image=bg_photo)
#bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# QUEUE

print_queue = queue.Queue()
sys.stdout = TkinterConsole(text_area, print_queue)

# UPDATE TEXT

def process_print_queue():
    while not print_queue.empty():
        msg = print_queue.get()
        text_area.config(state="normal")
        text_area.insert(tk.END, msg)
        text_area.see(tk.END)
        text_area.config(state="disabled")
    root.after(50, process_print_queue)

process_print_queue()

# LOOP FIX

def run_game_function(func, *args, **kwargs):
    thread = threading.Thread(target=func, args=args, kwargs=kwargs)
    thread.daemon = True
    thread.start()

# SAVING SYSTEM


def saving(data):
    print("Saving Progress...")
    with open (save_file, "w") as f:
        json.dump(data, f, indent=4)

def loading():
    print("Loading progress...")
    if not os.path.exists(save_file):
        print("No save file found. Starting with empty save.")
        return []

    with open(save_file, "r") as f:
        data = json.load(f)

    print("Save loaded!")
    return data

save_file = "save_file.json"

save = loading()
print("Current save : ", save)

# MISC FUNCTION

def shared_function():

    def fast_print(text, delay=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
        return fast_print

    def normal_print(text, delay=0.1):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
        return normal_print

    def slow_print(text, delay=0.3):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
        return slow_print
    
    return fast_print, normal_print, slow_print

fast_print, normal_print, slow_print = shared_function()

# MAIN GAME 
def TerraMythos():

    print("")
    print(">>>>> TERRA LEGENDS: MYTHOS <<<<<")
    print("version : Pre-Alpha Test 1.1")
    print("")

    def testing():
        print("Hi")
        time.sleep(2)
        print("Need to test something first. Please hold on tight.")
        time.sleep(1)
        fast_print("testing one two three four five")
        time.sleep(1)
        normal_print("testing one two three four five")
        time.sleep(1)
        slow_print("testing testing.")
        time.sleep(1)
        print("Thank you for waiting... Have fun!")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")

    testing()

    progress1 = False

    def opening():


        def opening1():
            text_area.config(font=("Courier", 14))
            change_colors(bg="#002404", fg="#00D719")

            pygame.mixer.music.load("Audio/Exomyth.mp3")
            pygame.mixer.music.play(-1)

            print("-----Terra Legends : mythos------")
            time.sleep(1)
            normal_print("I've been awaiting for your arrival....")
            time.sleep(1)
            normal_print("You must have some kind of interest perhaps I thought?")
            time.sleep(1)
            normal_print("Quite particular.....")
            time.sleep(1)
            normal_print("If I may....    You could experience my magnum opus....")
            time.sleep(1)
            normal_print("How shall it? My Terra Legends.... ")
            time.sleep(2)
            print(".")
            time.sleep(2)
            print("..")
            time.sleep(2)
            print("...")
            time.sleep(3)
            normal_print("If you are interested in my creation.... I shall gladly make you see it through your eye.....")
            time.sleep(1)
            normal_print("Well then.... Why not I tell you everything about this?")
            time.sleep(1)
            normal_print("Four heroes....")
            time.sleep(1)
            normal_print("Four of a kind....")
            time.sleep(1)
            normal_print("Four option to choose....")
            time.sleep(1)
            normal_print("Four.... Characters.....")
            time.sleep(1)
            slow_print("Four Actors.")
            time.sleep(1)
            normal_print("---Actor one : The elf---")
            time.sleep(1)
            normal_print("Her name is Mary Hartmann.")
            time.sleep(1)
            normal_print("She is a hunter....")
            time.sleep(1)
            normal_print("A blood of the monarchy...")
            time.sleep(1)
            normal_print("The last lineage of the royal family....")
            time.sleep(1)
            normal_print("Soon.... She shall become the arrowhead of her people....")
            time.sleep(3)
            normal_print("---Actor two : The Dragon.---")
            time.sleep(1)
            normal_print("His name is Xue Yunlong.")
            time.sleep(1)
            normal_print("The warrior.")
            time.sleep(1)
            normal_print("A dragon once banished from the royal dynasty.")
            time.sleep(1)
            normal_print("He aimed the goal of guardianship.")
            time.sleep(1)
            normal_print("And by then.... The Son of Dragon will rise from below.")
            time.sleep(3)
            normal_print("---Actor three : The Cat---")
            time.sleep(1)
            normal_print("Her name is Qitat Anaya.")
            time.sleep(1)
            normal_print("A cat with magic.")
            time.sleep(1)
            normal_print("A travelling magician abroad.")
            time.sleep(1)
            normal_print("She wanted to use her power to help others.")
            time.sleep(1)
            normal_print("And once that done.... Her promises will eventually respond....")
            time.sleep(3)
            normal_print("---Actor Four : The Human.---")
            time.sleep(1)
            normal_print("Her name is Chie Satoru")
            time.sleep(1)
            normal_print("Brilliant maiden of science.")
            time.sleep(1)
            normal_print("A peerless prodigy. Yet, empty as all she felt.")
            time.sleep(1)
            normal_print("She searched for something meaningful to her.")
            time.sleep(1)
            normal_print("The one that she searching for.... Is the way for her expression....")
            time.sleep(3)
            normal_print("Four Variables has been presented....")
            time.sleep(1)
            normal_print("Choose your variables on the input box below... (1, 2, 3, 4)")

            def option():

                mary_path = False
                xue_path = False
                anaya_path = False
                chie_path = False
                while True:
                    characters_choices = input()
                    print("Your option : ", characters_choices)

                    if characters_choices.isdigit():
                        if characters_choices == "1":
                            mary_path = True
                            break

                        elif characters_choices == "2":
                            xue_path = True
                            break
    
                        elif characters_choices == "3":
                            anaya_path = True
                            break
                            
                        elif characters_choices == "4":
                            chie_path = True
                            break
                            
                        else:
                            normal_print("That is not the right input... Try it again....")
                            continue
                    else:
                        normal_print("That is not the right input... Try again.")
                        continue
                    
                if mary_path:
                    sound_1.play()
                    print("<<< You have chosen The Hunt Path! >>>")
                    return "mary"
                if xue_path:
                    sound_1.play()
                    print("<<< You have chosen The Resilience Path! >>>")
                    return "xue"
                if anaya_path:
                    sound_1.play()
                    print("<<< You have chosen The Harmony Path! >>>")
                    return "anaya"
                if chie_path:
                    sound_1.play()
                    print("<<< You have chosen The Interval Path! >>>")
                    return "chie"

            route = option()

            normal_print("Excellent choice")
            time.sleep(1)
            normal_print(route)
            time.sleep(1)
            normal_print("Thank you for entering the show...")
            time.sleep(1)
            normal_print("Now.... Go ahead....")
            time.sleep(1)
            normal_print("Experience the story itself....")
            time.sleep(1)
            slow_print("My... Terra Legends....")

            pygame.mixer.music.fadeout(2000)
            pygame.time.delay(2000)

            text_area.config(font=("Times New Roman", 14))
            change_colors(bg="#202020", fg="#B4FF28")

            print("")
            time.sleep(1)
            print("")

            pygame.mixer.music.load("Audio/Heroes.mp3")
            pygame.mixer.music.play(1)

            time.sleep(1)
            normal_print("At the early era of everything...")
            time.sleep(1)
            normal_print("A thing began to exist....")
            time.sleep(1)
            normal_print("Alass... Born a being of abstraction.")
            time.sleep(1)
            normal_print("'Primordials' is what they called.")
            time.sleep(1)
            normal_print("An embodiements of it's own concept.")
            time.sleep(1)
            normal_print("A cosmic being that define reality itself.")
            time.sleep(1)
            normal_print("Yet one such primordials of Equilibrium, thrive in the world where balance met.")
            time.sleep(1)
            normal_print("Terra, a planet where everything lived in a harmonic equilibrium.")
            time.sleep(1)
            normal_print("Where life thrive, as mortal born and advanced.")
            time.sleep(1)
            normal_print("It's nectar like life forces attracts various kind of Primordials that bestowed the land with it's blessing.")
            time.sleep(1)
            normal_print("Yet none all were safe.")
            time.sleep(1)
            normal_print("As Khaos, the Primordials of Terror set it's gaze on Terra.")
            time.sleep(1)
            normal_print("A land once was in balance has been disrupted by the Terror.")
            time.sleep(1)
            normal_print("Chaos breaks in this time, as many calamity event unfold, the living being scream for answer.")
            time.sleep(1)
            normal_print("As hope stray to lost, the primordials respond it's mortal's prayers.")
            time.sleep(1)
            normal_print("And so, heroes arise...")
            time.sleep(1)
            change_colors(bg="#797716", fg="#EAFF28")
            normal_print("Thus born the saintess, Theresa Lorellei.")
            time.sleep(1)
            normal_print("With her divine kindness, she shall bring the light to this world.")
            time.sleep(1)
            change_colors(bg="#250101", fg="#FF6161")
            normal_print("At the moonlit flower's bloom, one lies the samurai of beauty.")
            time.sleep(1)
            normal_print("Mitsuki Komurasama, as her name, forseen the meaning itself.")
            time.sleep(1)
            change_colors(bg="#1B1B1B", fg="#FFFFFF")
            normal_print("The daughter of tengoku family, the art of caligraphy.")
            time.sleep(1)
            normal_print("One such speak, Minato Miko.")
            time.sleep(1)
            change_colors(bg="#3F1700", fg="#FFB835")
            normal_print("And so, the son of dragon have risen from below.")
            time.sleep(1)
            normal_print("Xue Yunlong, his gallantful roar pierce through the battle.")
            time.sleep(1)
            change_colors(bg="#005A35", fg="#4AFFC3")
            normal_print("Soar high, the arrow of the wind.")
            time.sleep(1)
            normal_print("Mary Hartmann, the last lieanage of the monarchy.")
            time.sleep(1)
            change_colors(bg="#310212", fg="#FF3762")
            normal_print("Yet, why bring destruction? They may asked.")
            time.sleep(1)
            normal_print("But for the sake of Recreation, Calliopee answered.")
            time.sleep(1)
            change_colors(bg="#222222", fg="#DAFF56")
            normal_print("Chie Satoru, a maiden of science.")
            time.sleep(1)
            normal_print("Beside her, Takeshi Kenshi, the brilliant gunsmith.")
            time.sleep(1)
            normal_print("And with this, the heroes rise from the slumber of equilibrium.")
            time.sleep(1)
            normal_print("And by then, the Terror shall be answered with Primus Vertex.")
            time.sleep(1)
            normal_print("And to finally repel chaos from this very world.")
            time.sleep(1)
            normal_print("But for this, it may be just the beginning.")
            time.sleep(1)
            normal_print("But for what it may seems. Our journey had not been over yet.")
            time.sleep(1)
            normal_print("Countless heroes, countless journey, and countless possibility.")
            time.sleep(1)
            normal_print("Come forth, the heroes of Terra, the legends that was promised.")
            time.sleep(1)
            normal_print("The one that the prophecy has revealed.")
            time.sleep(1)
            normal_print("To bring back the equilibrium that we had hoped for...")
            time.sleep(3)

            pygame.mixer.music.fadeout(5000)
            pygame.time.delay(5000)

            opening_done = True
            return opening_done, route
        progress1, route = opening1()

        return progress1, route
    
    if any(item.get("progress1") == True for item in save):
        progress1 = True

    if progress1:
        print("Skipping...")
        route_path = save[0]['route']
        pass
    else:
        progress1, route = opening()
        entry1 = {
        "progress1" : progress1,
        "route" : route
    }
        save.append(entry1)
        saving(save)
        print("Saving complete, current save : ", save)
        route_path = save[0]['route']

    def chapter1():
        def the_hunt():
            text_area.config(font=("Times New Roman", 14))
            change_colors(bg="#163A14", fg="#FFFFFF")
            ambient_forest.play(-1)
            ambient_forest.set_volume(0.8)
            
            time.sleep(1)
            slow_print("...")
            time.sleep(1)
            fast_print("On the peaceful day of the forest.")
            time.sleep(1)
            fast_print("There's a figure, all in hunting gear, relaxed on the grassy floor")
            time.sleep(1)
            fast_print("That is you, the one you've chossen.")
            time.sleep(1)
            fast_print("The elf with turqoise hair, and a particular looking purple tiara, decorated by a gems of the blue sky.")
            time.sleep(1)
            fast_print("It was a peaceful time.")
            time.sleep(1)
            fast_print("You are lying down on the shade of the forest.")
            time.sleep(1)
            fast_print("Shielding you from the sun rays.")
            time.sleep(1)
            fast_print(".")
            time.sleep(1)
            fast_print(".")
            time.sleep(1)
            fast_print(".")
            time.sleep(1)
            fast_print("It's too quiet, and you forgot what you're doing.")
            time.sleep(1)
            normal_print("...")
            time.sleep(1)
            fast_print("You woke up, and you jolted upwards.")
            time.sleep(1)
            fast_print("'The boar!'")
            time.sleep(1)
            fast_print("You muttered.")
            time.sleep(1)
            fast_print("And now you stand up and walk...")
            time.sleep(1)

            pygame.mixer.music.load("Audio/Day.mp3")
            pygame.mixer.music.play(-1)
            print("")
            print("-----Volume 1 : Chapter 1 : Interwoven Story (The Hunt)-----")
            print("")

            time.sleep(1)
            fast_print("Mary : 'The boar should be here somewhere....'")
            time.sleep(1)
            fast_print("Mary : 'Maybe right around the corner.'")
            time.sleep(1)
            fast_print("You looked around the forest trying to find your prey.")
            time.sleep(1)
            fast_print("Your long ears, adjusting itself to locate your prey.")
            time.sleep(1)
            fast_print("You goes silence to listen the surrounding.")
            time.sleep(1)
            slow_print(".....")
            time.sleep(1)
            fast_print("Mary: 'Found it!'")
            time.sleep(1)
            fast_print("You walked through the bushes in stealth.")
            time.sleep(1)
            fast_print("Mary: 'There you are!'")
            time.sleep(1)
            fast_print("You ready your bow for an imenante battle...")
            time.sleep(1)
            pygame.mixer.music.fadeout(1000)
            pygame.time.delay(1000)
            pygame.mixer.music.load("Audio/Battle.mp3")
            pygame.mixer.music.play(-1)
            print("")
            print("-----BATTLE SCENE-----")
            print("")
            time.sleep(1)
            fast_print("This is the battle scene.")
            time.sleep(1)
            fast_print("You don't need to worry about your equipment and setup.")
            time.sleep(1)
            fast_print("This battle is predetermined.")
            time.sleep(1)
            fast_print("Choose your action that fits with the scene itself.")
            time.sleep(1)

            def battle_scene0():

                boar = 100
                if boar < 0:
                    boar = 0
                if boar != 100:
                    print("The boar got scared!")

                while True:

                    if boar != 100:
                        print("The boar got scared!")

                    print("Choose your action!")
                    print("1. Aim and shoot.")
                    print("2. Stealthly get closer.")
                    print("3. Run (not possible currently.)")
                    user_action = input()
                    if user_action.isdigit():
                        if user_action == "1":
                            print("You aim your shoots and hit a boar!")
                            attack_1.play()
                            time.sleep(1)
                            boar -= 50
                            print("Boar HP : ", boar)
                        elif user_action == "2" and boar != 100:
                            print("You tried stealthly get closer to the boar, the boar knows what you're doing!")
                            time.sleep(1)
                            print("Action Failed!")
                        elif user_action == "2" and boar == 100:
                            print("You've successfully get closer to the boar and initiate your surprise attack!")
                            attack_1.play()
                            boar -= 70
                            time.sleep(1)
                            print("Boar HP : ", boar)
                        elif user_action == "3":
                            print("Action currently unavailable!")
                            time.sleep(1)
                        else:
                            print("Invalid action! Please try again!")
                            continue

                    if boar <= 0:
                        print("The boar is defeated!")
                        print("-----BATTLE VICTORY-----")
                        battle1 = True
                        break
            
            battle1 = battle_scene0()
            
            time.sleep(1)
            pygame.mixer.music.fadeout(1000)
            pygame.time.delay(1000)
            pygame.mixer.music.load("Audio/Day.mp3")
            pygame.mixer.music.play(-1)
            time.sleep(1)
            print("Mary : 'That's some real meat over here...'")
            time.sleep(1)

        def the_resilience():
            print("Sorry, the path is under development, please choose the hunt path first.")

        def the_harmony():
            print("Sorry, the path is under development, please choose the hunt path first.")

        def the_interval():
            print("Sorry, the path is under development, please choose the hunt path first.")

        if route_path == "mary":
            the_hunt()
        elif route_path == "xue":
            the_resilience()
        elif route_path == "anaya":
            the_harmony()
        elif route_path == "chie":
            the_interval()
        else:
            print("Warning! Invalid 'route' returned value! Please check the code again!")

    if progress1:
        chapter1()
            


# START

run_game_function(TerraMythos)

root.mainloop()
