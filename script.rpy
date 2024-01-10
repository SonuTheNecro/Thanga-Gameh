# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Thanga")


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

    e "live thang reaction"

    e "my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend! my favorite anime is rent a girlfriend!"
    menu:

        "rent a girlfriend is awesome":
            jump good

        "rent a girlfriend sucks":
            jump bad

    label good:

        e "LETS GOOOO"

        scene black
        with fade
        "you now like rent a girlfriend"

        "the bad end"

        return

    label bad:

        e "KILL YOURSELF NOW"

        scene black
        with fade
        "you kill yourself"

        "the good end"

        $ raise Exception(" youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape % youらは逃canれなnot%影escape  you影か%らcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  %youらは逃canれなnot影escape%  you影からcanい %影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape%  youらは逃canれなnot影%escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは%逃canれなnot影escape  you影か%らcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape % youらは逃canれなnot影escape % you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape  you影からcanい 影notなたはescape  youらは逃canれなnot影escape %you影からcanい 影notなたはescape")

        return

    # This ends the game.

    return
