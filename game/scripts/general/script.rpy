﻿# Thanga Gamea (Thang Game) is a creation of SonuTheNecro & TacticalVortex
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
default player_name = "Kody"
default check = False

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



label start:
    if persistent.intro == False:
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
        menu:
            "Chapter_0":
                jump prologue
            "Chapter_1" if persistent.ch00 == True:
                jump chapter_one
            "Chapter_3" if persistent.ch01 == True:
                #jump chapter_two
                jump chapter_three
            "Chapter_3_fnaf_start" if persistent.ch01 == True:
                jump chapter_three_fnaf_start
            "Chapter_3_fnaf_secret" if persistent.ch01 == True:
                jump chapter_three_secret
            "Erase all Data":
                $ renpy.delete_persistent()
                "All persistent Data has been deleted"
                jump intro

            




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