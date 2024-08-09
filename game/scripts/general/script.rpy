# Thanga Gamea (Thang Game) is a creation of SonuTheNecro & TacticalVortex
# Current Verison 1.3.5


define questionmark = Character("???")
define t = Character("Thanga")
define k = Character("Kody")
define jj = Character("PillowR")
define c = Character("Cody")
define b = Character("B-Bop")
define stn = Character("SonuTheNecro")
define tv = Character("TacticalVortex")
define igor = Character("Master Igor")

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

#
default persistent.play_time = 0
default temp_playtime = 0
label main_menu:
    return

label quit:
    if check != "bloxwich":
        $ persistent.play_time += renpy.get_game_runtime()
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
        

label hide_clickable_menus:
    hide screen clickable_main_menu_ch00
    hide screen clickable_main_menu_ch01
    hide screen clickable_main_menu_ch02
    hide screen clickable_main_menu_ch03
    hide screen clickable_main_menu_ch04
    hide screen clickable_main_menu_question_screen1
    hide screen clickable_main_menu_question_screen2
    hide screen clickable_main_menu_question_screen3
    hide screen clickable_main_menu_question_screen4
    hide screen clickable_main_menu_question_screen5
    hide screen clickable_main_menu_trash_can
    hide screen clickable_main_menu_trophy
    hide screen clickable_main_menu_clock
    hide screen clickable_main_menu_minigames
    hide screen clickable_chapter_secret_one
    return
            
label clickable_menus:
    screen clickable_main_menu_ch00:
        imagebutton:
            pos (140, 13) at Transform(zoom=0.62)
            idle "images/chapter_zero_screen.png"
            hover "images/chapter_zero_screen.png"
            action Jump("chapter_start0")
    screen clickable_main_menu_ch01:
        imagebutton:
            pos (768, 13) at Transform(zoom=0.62)
            idle "images/chapter_one_screen.png"
            hover "images/chapter_one_screen.png"
            action Jump("chapter_start1")
    screen clickable_main_menu_ch02:
        imagebutton:
            pos (1444, 13) at Transform(zoom=0.62)
            idle "images/chapter_two_screen.png"
            hover "images/chapter_two_screen.png"
            action Jump("chapter_start2")
    screen clickable_main_menu_ch03:
        imagebutton:
            pos (140, 541) at Transform(zoom=0.62)
            idle "images/chapter_three_screen.png"
            hover "images/chapter_three_screen.png"
            action Jump("chapter_start3")
    screen clickable_main_menu_ch04:
        imagebutton:
            pos (768, 541) at Transform(zoom=0.62)
            idle "images/question_screen.png"
            hover "images/question_screen.png"
            action Jump("chapter_start4")
    screen clickable_main_menu_question_screen1(xpos,ypos):
        imagebutton:
            pos (xpos, ypos) at Transform(zoom=0.62)
            idle "images/question_screen.png"
            hover "images/question_screen.png"
            action Jump("chapter_start_question")
    screen clickable_main_menu_question_screen2(xpos,ypos):
        imagebutton:
            pos (xpos, ypos) at Transform(zoom=0.62)
            idle "images/question_screen.png"
            hover "images/question_screen.png"
            action Jump("chapter_start_question")
    screen clickable_main_menu_question_screen3(xpos,ypos):
        imagebutton:
            pos (xpos, ypos) at Transform(zoom=0.62)
            idle "images/question_screen.png"
            hover "images/question_screen.png"
            action Jump("chapter_start_question")
    screen clickable_main_menu_question_screen4(xpos,ypos):
        imagebutton:
            pos (xpos, ypos) at Transform(zoom=0.62)
            idle "images/question_screen.png"
            hover "images/question_screen.png"
            action Jump("chapter_start_question")
    screen clickable_main_menu_question_screen5(xpos,ypos):
        imagebutton:
            pos (xpos, ypos) at Transform(zoom=0.62)
            idle "images/question_screen.png"
            hover "images/question_screen.png"
            action Jump("chapter_start_question")
    label chapter_start0():
        "Do you want to start the Prologue?"
        menu:
            "Yes":
                call hide_clickable_menus
                jump prologue
            "No":
                jump main_menu_chapter_select
    label chapter_start1():
        "Do you want to start Chapter One?"
        menu:
            "Yes":
                call hide_clickable_menus
                jump chapter_one
            "No":
                jump main_menu_chapter_select
    label chapter_start2():
        "Do you want to start Chapter Two?"
        menu:
            "Yes":
                call hide_clickable_menus
                jump chapter_two
            "No":
                jump main_menu_chapter_select
    label chapter_start3():
        "Do you want to start the Chapter Three?"
        menu:
            "Yes":
                call hide_clickable_menus
                jump chapter_three
            "No":
                jump main_menu_chapter_select
    label chapter_start4():
        "Do you want to start the Chapter Four?"
        menu:
            "Yes":
                call hide_clickable_menus
                jump chapter_four
            "No":
                jump main_menu_chapter_select

    label chapter_start_question:
        "That chapter is currently locked/unavailable!"
        "Please select another chapter!"
        jump main_menu_chapter_select
    screen clickable_main_menu_trash_can:
        imagebutton:
            pos((0, 1020))
            idle "images/main_menu_delete.png"
            hover "images/main_menu_delete.png"
            action Jump("main_menu_delete")
    label main_menu_delete:
        "Do you want to delete all of your Save Data"
        "This includes your Chapter Completions, Secrets Found, and the player name!"
        "This is an IRREVERSIBLE ACTION!"
        "Would you like to continue?"
        menu:
            "Yes, delete my DATA":
                $ check = "bloxwich"
                $ reset_data()
                jump main_menu_chapter_select
            "No, Don't Do That":
                jump main_menu_chapter_select
            "Max Save File!":
                $ persistent.ch00 = True
                $ persistent.ch01 = True
                $ persistent.ch02 = True
                $ persistent.ch03 = True
                $ persistent.ch04 = True
                $ persistent.secret0 = True
                $ persistent.secret1 = True
                $ persistent.secret2 = True
                $ persistent.secret3 = True
                jump main_menu_chapter_select
    screen clickable_main_menu_trophy:
        imagebutton:
            pos(60,1020)
            idle "images/main_menu_trophy.png"
            hover "images/main_menu_trophy.png"
            action Jump("main_menu_stats")
    label main_menu_stats:
        if persistent.ch00:
            "Prologue has been Completed!"
            if persistent.secret0:
                "Prologue's Secret has been Found!"
        if persistent.ch01:
            "Chapter One has been Completed!"
            if persistent.secret1:
                "The secret of Kody has been Found!"
        if persistent.ch02:
            "Chapter two has been Completed!"
            if persistent.secret2:
                "Chapter Two's Secret has been Found!"
        if persistent.ch03:
            "Chapter Three has been Completed!"
            if persistent.secret3:
                "The SpringTrap has been Formed!"
        jump main_menu_chapter_select
    screen clickable_main_menu_clock:
        imagebutton:
            pos(0,960)
            idle "images/main_menu_clock.png"
            hover "images/main_menu_clock.png"
            action Jump("main_menu_playtime")
    label main_menu_playtime:
        $ persistent.play_time -= temp_playtime
        $ temp_playtime = renpy.get_game_runtime()
        $ persistent.play_time += temp_playtime
        $ hours = int(persistent.play_time // 3600)
        $ minutes = int((persistent.play_time % 3600) // 60)
        $ seconds = int(persistent.play_time % 60)
        $ formatted_time = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
        "Playtime: [formatted_time]"
        jump main_menu_chapter_select
    screen clickable_main_menu_minigames:
        imagebutton:
            pos(60,960)
            idle "images/main_menu_minigames.png"
            hover "images/main_menu_minigames.png"
            action Jump("main_menu_minigames")
    label main_menu_minigames:
        menu:
            "Cody's Roshambo":
                jump minigame_rps
            "Baldi's Mathmatical Madness":
                jump minigame_math
            "Puppet's Paradoxical Plight (idk man)":
                jump minigame_puppet
            "debug":
                jump debug_menu
            "Return to Main Menu":
                jump main_menu_chapter_select
    
    screen clickable_chapter_secret_one:
        imagebutton:
            pos (549, 210)
            idle "images/slender_man.png"
            hover At("images/slender_man.png", animated_outline)
            action Jump("chapter_start_secret1")
    label chapter_start_secret1:
        "Do you want to start the Secret Chapter?"
        menu:
            "Yes":
                call hide_clickable_menus
                jump chapter_secret_one_start
            "No":
                jump main_menu_chapter_select
    label debug_menu:
        call hide_clickable_menus
        menu:
            "Chapter Three Secret":
                jump chapter_three_secret

label test1:
    scene bg room


    t "live thang reaction"

    t "my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend!"
    default learned = False
    menu:

        "rent a girlfriend is awesome!":
            jump good

        "rent a girlfriend sucks!":
            jump bad

label good:

    t "LETS GOOOO!!!!"

    scene black
    with fade
    "you now like rent a girlfriend..."

    "The Bad Ending..."
    jump scene2
    return

label bad:

    t "KILL YOURSELF NOW!"

    scene black
    with fade
    "you have ended your own life..."

    "The Good Ending"

    t "I hope you die RIGHT NOW!"
    jj "what... This reminds me of a time in Africa"
    $ learned = True
    jump start

label scene2:
    scene thanga7
    with fade
    t "woah is that my Smash Bros top 1 in the entire universe thanks to me and not zaiyde"
    jj "Kill yourself NOW!"
    jj "MULTIVERSUS WAS BETTER"
    show kody:
        xalign 0.0
        linear 10000 xalign 1.0
        repeat
    k "WAIT THANG I NEED CHICKEN NUGGETS PLEASE"
    t "Fine here is your nuggets you fatass."
    hide kody

    show kody:
        xalign 0.5
        linear 0.01 xalign 1.0
        repeat
    k "YIPPIE!!!!!!"
    "lead metal pipe.mp4"
    show jj1
    jj "KILL YOURSELF NOW!"

    t "oof"

    show cody:
        xalign 1.0
        yalign 0.5
    c "YOU SHOULD KILL YOURSELF NOW!" 

    hide jj1
    with fade
    hide Kody

    show brian1:
        xalign 0.0
        yalign 0.5
    b "Where is the pokemon :("

    show jj1
    show lopunny1:
        yalign 0.7
        xalign 0.4
    jj "Here is your pokemon :D"

    b "Damn girl, you small"

    scene thanga4
    with fade

    t "wow guys... we did it"

    k "COMIN IN HOT"

    show kody with hpunch:
        yalign 0.5

    k "hello ThangaMangaLangaDangaShangaRangaYangaPangaBanga"

    show cody with easeintop:
        yalign 0.5
        xalign 1.0
    
    c "you're not escaping from me!"

    scene final1 with Swing(5.0)

    show thanga2:
        xzoom 0.5
        yzoom 0.5
        yalign 0.5
        xalign 0.5

    t "IN THE LEFT CORNER WE HAVE KODY!!"

    show kody with fade:
        xzoom 0.5
        yzoom 0.5
        yalign 0.6
        xalign 0.25

    k "YAY"

    t "AND IN THE RIGHT CORNER WE HAVE CODY!!"

    show cody with blinds:
        xzoom 1.5
        yzoom 1.5
        yalign 0
        xalign 0.75

    c "⅄∀⅄"

    t "alright buddy I don't see how this is fair..."

    c "okay"

    show cody with dissolve:
        xzoom 0.5
        yzoom 0.5
        yalign 0.6
        xalign 0.75

    c "this better?"

    t "yes, so LET'S GET THIS BATTLE STARTED."

    menu: 
        "Dodge Left":
            jump left

        "Dodge Right":
            jump right

        "Duck":
            jump duck

    label left:
        show sword1:
            xzoom 0.2
            yzoom 0.2
            yalign 0.6
            xalign 0.75
            linear 0.1 xalign 0.0


        hide kody with dissolve
        hide sword1

        t "NO KODY"

        return

    label right:
        show sword1:
            xzoom 0.2
            yzoom 0.2
            yalign 0.6
            xalign 0.75
            linear 0.1 xalign 0.0

        hide kody with dissolve
        hide sword1

        t "NO KODY"

        return

    label duck:
        if learned:
            "You have learned the ways of Africa"
            jump finish
        else:
            "You have not learned the ways of Africa"
            show sword1:
                xzoom 0.2
                yzoom 0.2
                yalign 0.6
                xalign 0.75
                linear 0.1 xalign 0.0

            hide kody with dissolve
            hide sword1

            t "NO KODY"
            return
            

    label finish:
        show kody:
            xzoom 0.5
            yzoom 0.2
            yalign 0.65
            xalign 0.25
        show sword1:
            xzoom 0.2
            yzoom 0.2
            yalign 0.5
            xalign 0.75
            linear 0.1 xalign 0.0


        c "WHAT!"
        c "IMPOSSIBLE!!"
        hide sword1

        show kody:
            xzoom 0.5
            yzoom 0.5
            yalign 0.6
            xalign 0.25

        k "im straight up better"
        jump sonuhenryreaction
    
    label sonuhenryreaction:
        scene fireplace with Pixellate(8.0, 10):
            xzoom 1.9
            yzoom 1.75

        show henry:
            xzoom 0.75
            yzoom 0.75
            xalign 0.1
            yalign 0.8
            linear 0.1 xoffset -2 yoffset 2 
            linear 0.1 xoffset 3 yoffset -3 
            linear 0.1 xoffset 2 yoffset -2
            linear 0.1 xoffset -3 yoffset 3
            linear 0.1 xoffset 0 yoffset 0
            repeat

        show sonuthenecro:
            xzoom 0.6
            yzoom 0.6
            yalign 0.6
            xalign 0.95
            linear 0.1 xoffset -2 yoffset 2 
            linear 0.1 xoffset 3 yoffset -3 
            linear 0.1 xoffset 2 yoffset -2
            linear 0.1 xoffset -3 yoffset 3
            linear 0.1 xoffset 0 yoffset 0
            repeat


        stn "WHAT THE HELL WAS THAT?!!"
        tv "I thought you said this was a GOOD story..."
        stn "I DID NOT SAY THAT"
        stn "I said it was a story."
        stn "THESE CHARACTERS SUCK, especially kodydaboss"
        tv "wtf are these animations"
        tv "whoever made them is straight up a noob"
        stn "..."
        tv "..."
        tv "why are you moving like that?"
        "FIN"
        


    # This ends the game.

    return