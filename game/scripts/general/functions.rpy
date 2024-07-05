#Generic Functions intended to be used for the whole project

#Python Code
init python:
    import random
    from renpy.display import im
    from enum import Enum
    renpy.music.register_channel("sound2", "sound", loop = False) # second sound track for dual sound effects

    #A confirm menu for important decisions, Paramater is the str for the menu label, jump decision is where you would go if you choose yes
    def confirm_menu_jump(original_menu, jump_decision):
        renpy.say(None, "This is an Important Decision that will affect your future gameplay, are you sure about this?")
        check = renpy.display_menu([("Yes", "yes"), ("No", "no")])
        if check == "yes":
            renpy.say(None, "Good luck on your decision")
            renpy.jump(str(jump_decision))
        else:
            renpy.say(None, "Good luck on your decision")
            renpy.jump(str(original_menu))
    #A confirm menu for important decisions, Paramater is the str for the menu label
    def confirm_menu_no_jump(original_menu):
        renpy.say(None, "This is an Important Decision that will affect your future gameplay, are you sure about this?")
        check = renpy.display_menu([("Yes", "yes"), ("No", "no")])
        if check == "no":
            renpy.say(None, "Good luck on your decision")
            renpy.jump(str(original_menu))
        else:
            renpy.say(None, "Good luck on your decision")
    class ItemState(Enum):
        NOT_OBTAINED = 0
        OBTAINED = 1
#Renpy Code
image blood_red = Solid("#790000")

#A game over screen for general use, why is Master Igor shit talking so hard
label game_over:
    stop sound
    stop music
    pause 5.0
    play music "audio/music/prologue/aria_of_the_soul.ogg"
    scene velvet room with fade:
        subpixel True pos (-0.08, 0.0) yzoom 1.12 zoom 1.22 
    "You have fallen and lost thy life!"
    show igor with dissolve:
        subpixel True pos (0.21, 0.57) yoffset -585.0 xzoom 1.0 zoom 4.2
    
    igor "But honestly you suck at the game!"
    igor "Like how do you mess up these basic mechanics"
    igor "I got no legs and I coulda walked further and made it further than you you absolute shitter"
    igor "This is a baby-easy visual novel made for stupid people!"
    igor "play a real visual novel made for adults!"
    igor "You fucking suck, use some common sense"
    igor "Straight up bozo!"
    igor "Goodbye forever (Or not)"
    $ renpy.quit()

label dio_time_stop():
    $ rngint = renpy.random.randint(0,1)
    if rngint == 0:
        play sound "audio/sound/general/dio1.ogg"
    else:
        play sound "audio/sound/general/dio2.ogg"
    return
label stab_blood_screen():
    window auto hide
    play sound "audio/sound/general/stab_die1.ogg"
    pause .4
    show blood_red at Transform(alpha = 0.5) with Dissolve(1.5)
    return
label gun_blood_screen():
    window auto hide
    play sound "audio/sound/general/gun_die1.ogg"
    pause .4
    show blood_red at Transform(alpha = 0.5) with Dissolve(1.5)
    return
# Code for auto advance as a Pseudo-Function, 1 = Starting it, 0 for Ending it
label auto_advance(value):
    if value == 1:
        $ _preferences.afm_enable = True
        $ _preferences.afm_time = 5
    elif value == 0:
        $ _preferences.afm_enable = False
        $ _preferences.afm_time = 15
    return