
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
    "test"