# Code for the functions in Chapter Four


init python:
    from random import randint
    from enum import Enum



label chapter_four_early_ending_1:
    #TODO: Clock speed effect
    scene ch04_lab with dissolve:
        subpixel True zoom 1.2 
    show matt2:
        subpixel True pos (-246, 146) zoom 0.79 
        linear 0.345 subpixel True pos (825, 146) zoom 0.79 
    pause 0.345
    "So why exactly are we here?"
    "In the High-School computer lab..."
    mt "I just wanna vent"
    mt "and no one's here"
    mt "*sigh*"
    "What happened?"
    mt "Trip is cancelling his match..."
    "Damn"
    mt "My life is over"
    "yeah probably"
    mt "I think we just missed something like idk man"
    "Perhaps in another life or run we can do that :/"
    $ renpy.quit()