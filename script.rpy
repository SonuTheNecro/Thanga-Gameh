# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Thanga")
define k = Character("Kody")
define jj = Character("PillowR")


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

        $ raise Exception(" youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape % youらは逃canれなnot%影escape  you影か%らcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  %youらは逃canれなnot影escape%  you影からcanい %影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape%  youらは逃canれなnot影%escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは%逃canれなnot影escape  you影か%らcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape % youらは逃canれなnot影escape % you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape %you影からcanい 影notなたはescape")
        t "I hope you die"
        jj "what... This reminds me of a time in Africa"
        return

    label scene2:
        scene thanga7
        with fade
        t "woah is that my smash bros top 1 in the entire universe thanks to me and not zade"
        jj "Kill yourself NOW MULTIVERSUS WAS BETTER"
        show kody:
            xalign 0.0
            linear 0.05 xalign 1.0
            repeat
        k "WAIT THANG I NEED CHICKEN NUGGETS PLZ"

        show jj1
        jj "KILL YOURSELF"

        t "oof"

    # This ends the game.

    return