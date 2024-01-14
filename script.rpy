# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Thanga")
define k = Character("Kody")
define jj = Character("PillowR")
define c = Character("Cody")
define b = Character("B-Bop")
define stn = Character("SonuTheNecro")
define tv = Character("TacticalVortex")


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
        
        show cody at right:
        c "YOU SHOULD KILL YOURSELF NOW!" 

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

            jump sonuhenryreaction

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

            jump sonuhenryreaction

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
                jump sonuhenryreaction
                

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


            stn "WHAT THE HELL WAS THAT?"
            tv "I thought you said this was a GOOD story..."
            stn "I DID NOT SAY THAT"
            stn "I said it was a story."
            stn "THESE CHARACTERS SUCK, especially kody"
            tv "wtf are these animations"
            tv "whoever made them is straight up a noob"
            stn "..."
            tv "..."
            tv "why are you moving like that?"
            "FIN"
        


    # This ends the game.

    return