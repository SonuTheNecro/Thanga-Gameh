# Thanga Gamea (Thang Game) is a creation of SonuTheNecro & TacticalVortex
# Current Verison 1.6.0.1



default location = -1
default rngint = -1
default rngint1 = -1
default choice = -1
default count = -1
default count2 = -1
default time = 0
default check = False

default persistent.player_name = "Kody"
# Flags for all Secret Endings Secret0 = Prologue
default persistent.secret0 = False
default persistent.secret1 = False
default persistent.secret2 = False
default persistent.secret3 = False
default persistent.secret4 = False
default persistent.secret5 = False

#Temp Flag Clears
default persistent.intro = False
default persistent.ch00 = False
default persistent.ch01 = False
default persistent.ch02 = False
default persistent.ch03 = False
default persistent.ch04 = False
default persistent.ch05 = False

default camera_speed = 0
#
default persistent.play_time = 0
default temp_playtime = 0
label main_menu:
    return

label quit:
    if check != "bloxwich": #When you reset data, this stops a crash when you close the game
        $ persistent.play_time += renpy.get_game_runtime() - temp_playtime
    return
label start:
    if persistent.intro == False:
        $ discord.set(state = "Signing a Contract", details = "In The Prologue", large_image = "prologue", buttons = [dict(label = "SonuTheNecro's Free Promo", url = "https://github.com/SonuTheNecro/Thanga-Gameh")])
        label intro:
        play music "audio/music/prologue/aria_of_the_soul.ogg"
        scene velvet room with fade:
            subpixel True pos (-0.08, 0.0)  yzoom 1.12 zoom 1.22 
        questionmark "This story is a work of fiction"
        questionmark "Similarities between characters or events to persons living or dead in your world are purely coincidental"
        questionmark "Only those who have agreed to the above have the privilege of partaking in this game"
        questionmark "The world is not as it should be"
        questionmark "It's filled with distortion, and ruin can no longer be avoided"
        questionmark "those who oppose fate and desire change... From time to time, they were referred to as the light"
        questionmark "now is the time to rise against the abyss of distortion"
        questionmark "Do you accept?"

        menu:
            "yes":
                label intro_yes:
                    questionmark "That is good. Now sign the contract with your name."
                    $ player_name = renpy.input("What is your name?", length = 8)
                    "Remember this one hint"
                    "Leave no stone unturned"
                    stop music
                    $ persistent.intro = True
                    jump prologue
            "no":
                questionmark "Wait Really?"
                questionmark "So according to you chucklenuts, this is not a work of fiction but all of this is simply real?"
                show igor with dissolve:
                    subpixel True pos (0.21, 0.57) yoffset -585.0 xzoom 1.0 zoom 4.2
                igor "Like are you serious?"
                igor "Let's try this again..."
                menu:
                    "yes":
                        igor "That is What I thought!"
                        jump intro_yes
                    "no":
                        igor "Fuck off you bitch ass"
                        $ renpy.quit()

    else:
        play music "audio/music/prologue/phantom.ogg" loop
        scene main_menu_bg3
        $ discord.set(details = "In The Main Menu.", large_image = "main_menu", buttons = [dict(label = "SonuTheNecro's Free Promo", url = "https://github.com/SonuTheNecro/Thanga-Gameh")])
        label main_menu_chapter_select:
        show screen clickable_main_menu_clock
        show screen clickable_main_menu_trash_can
        show screen clickable_main_menu_trophy
        show screen clickable_main_menu_ch00 #1
        show screen clickable_main_menu_minigames
        if persistent.ch00:#2
            show screen clickable_main_menu_ch01
        else:#2
            show screen clickable_main_menu_question_screen1(768,13)
        if persistent.secret0:
            show screen clickable_chapter_secret_one
        if persistent.ch01:#3
            show screen clickable_main_menu_ch02
        else:#3
            show screen clickable_main_menu_question_screen2(1444,13)
        if persistent.ch02:#4
            show screen clickable_main_menu_ch03
        else:#4
            show screen clickable_main_menu_question_screen3(140,541)
        if persistent.ch03:#5
            show screen clickable_main_menu_ch04
        else:
            show screen clickable_main_menu_question_screen4(768,541)
    #if not persistent.ch04:#6
        show question_screen:
            subpixel True pos(1444,541) zoom 0.62
        call screen clickable_main_menu_question_screen5(1444,541)
        