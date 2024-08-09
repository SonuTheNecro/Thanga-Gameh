
define trip = Character("Trip")
define maan = Character("Maan")
define dante = Character("Dante")
define carl = Character("Carl")



label chapter_four:
    "Chapter Four"
    "The Steve Disease"
    if persistent.ch04:
        $ config.rollback_enabled = True
    scene ch04_smash_locals with dissolve:
        subpixel True xzoom 1.33 zoom 1.06
    show kody:
        subpixel True pos (161, 178) xzoom 1.86 
    show matt2:
        subpixel True pos (48, 473) xzoom 3.22 zoom 0.2 
    #TODO: Put smash controller sounds here on straight up loop
    "..."
    "..."
    mt "OOO GET READ"
    "..."
    mt "OH LETS FUCKING GOOOOOOOOOOOOOOOOO"
    mt "I HIT THOSE BACK AIRS"
    k "..."
    "..."
    "..."
    #TODO: GAME! Sfx here
    mt "Alright good games kody"
    k  "..."
    mt "you good?"
    k "fuck you mean good games after all that trash talk"
    mt "its just banter"
    mt "it aint serious"
    k "you shit talked for 8 minutes"
    mt "you sonic stalled me you bitch"
    mt "Ima give a little bit of trash talk"
    k "Honestly this game is too much for me"
    k "I also hate being stretched so im outa here"
    show kody:
        yrotate 180.0
        linear 0.65 xalign -2.0
    mt "hoes mad"
    k "I CAN HEAR YOU"
    mt "YOU HAD IT COMING LMAO!!!!!!!!"
    mt "Guess I'll practice alone for now, although I do need to figure out how to beat Trip next time"
    mt "Maybe I should play friendlies with him?"
    "(Small scene of Matt imagining him losing every game to trip in friendlies)"
    trip "(turns to Matt) good games Matt!"
    mt "..."
    mt "(Punches him in the face)"
    mt "Fuck that. I don't think I can play him right now without potentially getting banned from locals"
    mt "I'll just practice my movement and combos"
    "While practicing, Matt continues to remember all those times he's lost to Trip"
    "(Three different mini scenes)"
    "(Scene 1: At a different smash locals, Matt Chokes a 2-0 lead on trip. Trip pops off)"
    #TODO: Add two additional characters, commentator1 and 2.
    
    $ count = 0

    show screen chapter_four_ocho_timer(15,"chapter_four_post_ocho")
    call screen clickable_chapter_four_ocho(30,40,0.25)

    label chapter_four_post_ocho:
        "wow"
        "You popped [count] times"