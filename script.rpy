# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Thanga")
define k = Character("Kody")
define jj = Character("PillowR")
define c = Character("Cody")
define b = Character("B-Bop")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    t "live thang reaction"

    t "my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend!"
    default learned = False
    menu:

        "rent a girlfriend is awesome":
            jump good

        "rent a girlfriend sucks":
            jump bad

    label good:

        t "LETS GOOOO"

        scene black
        with fade
        "you now like rent a girlfriend"

        "the bad end"
        jump scene2
        return

    label bad:

        t "KILL YOURSELF NOW"

        scene black
        with fade
        "you kill yourself"

        "the good end"

        t "I hope you die"
        jj "what... This reminds me of a time in Africa"
        $ learned = True
        jump start

    label scene2:
        scene thanga7
        with fade
        t "woah is that my smash bros top 1 in the entire universe thanks to me and not zade"
        jj "Kill yourself NOW MULTIVERSUS WAS BETTER"
        show kody:
            xalign 0.0
            linear 10000 xalign 1.0
            repeat
        k "WAIT THANG I NEED CHICKEN NUGGETS PLZ"
        t "Fine here is your nuggets you fatass"
        hide kody

        show kody:
            xalign 0.5
            linear 0.01 xalign 1.0
            repeat
        show jj1
        jj "KILL YOURSELF"

        t "oof"
        
        show cody at right:
        c "YOU SHOULD KILL YOURSELF NOW" 

        hide jj1
        with fade
        hide Kody

        show brian1 at left:
        b "Where is the pokemon :("

        show jj1
        show lopunny1:
            yalign 0.7
            xalign 0.4
        jj "Here is your pokemon :D"

        b "OMG THANK YOU"

        scene thanga4
        with fade

        t "wow guys... we did it"

        k "COMIN IN HOT"

        show kody with hpunch:
            yalign 0.5

        k "hello thang"

        show cody with easeintop:
            yalign 0.5
            xalign 1.0
        
        c "you're not escaping from me"

        scene final1 with Swing(5.0)

        show thanga2:
            xzoom 0.5
            yzoom 0.5
            yalign 0.5
            xalign 0.5

        t "IN THE LEFT CORNER WE HAVE KODY"

        show kody with fade:
            xzoom 0.5
            yzoom 0.5
            yalign 0.6
            xalign 0.25

        k "YAY"

        t "AND IN THE RIGHT CORNER WE HAVE CODY"

        show cody with blinds:
            xzoom 1.5
            yzoom 1.5
            yalign 0
            xalign 0.75

        c "⅄∀⅄"

        t "alright buddy I don't see how this is fair"

        c "okay"

        show cody with dissolve:
            xzoom 0.5
            yzoom 0.5
            yalign 0.6
            xalign 0.75

        c "this better?"

        t "yes, so LET'S GET THIS BATTLE STARTED"

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


            c "WHAT"
            hide sword1

            show kody:
                xzoom 0.5
                yzoom 0.5
                yalign 0.6
                xalign 0.25

            k "im better"

    # This ends the game.

    return