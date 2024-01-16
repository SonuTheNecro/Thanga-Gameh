# Thanga Gamea (Thang Game) is a creation of SonuTheNecro & TacticalVortex
# Current Verison 1.3

define t = Character("Thanga")
define k = Character("Kody")
define jj = Character("PillowR")
define c = Character("Cody")
define b = Character("B-Bop")
define stn = Character("SonuTheNecro")
define tv = Character("TacticalVortex")




label start:


    # The Prologue Scene
    scene carontheroad:
        xzoom 1.8
        yzoom 1.3
    k "Holy shit Thang. I am so excited for this"
    k "You actually made my day with this trip I am so excited!"

    t "I am only doing this because Papi is making me because you are a fatass..."
    t "You eat everything on spot like Kirby bro"

    k "Ayo man, that is not fair."
    k "I am trying to gain some muscle and I need that protein"

    t "..."
    t "..."
    t "You realize it is really hard to gain muscle while also trying to lose weight..."
    t "You are actually a dumb fuck, shut up so we can get there without me getting a headache"

    scene mcdonalds_outside

    show thanag2
    show kody

    t "well alright"
    t "here we are... the worst place in America"

    k "OMG YES I LOVE YOU THANG YOU ARE THE BEST!"

    t "What the fuck?"
    t "Are you like gay or something?"

    k "BRO I AIN'T GAY I JUST LOVE MCDONALDS NOW LETS GO I AM HUNGRY"

    scene mcdonalds_inside
    t "Alright what do you even want to eat?"

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