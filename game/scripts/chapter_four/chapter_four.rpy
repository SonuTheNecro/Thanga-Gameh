
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
        subpixel True pos (60, 515) xzoom 3.22 zoom 0.54 


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
    camera:
        linear 0.45 subpixel True pos (-351, -1773) xzoom 1.0 yzoom 1.0 zoom 3.87 
    $ renpy.pause(0.45, hard = True)
    scene ch04_smash_locals2 with dissolve:
        subpixel True xzoom 1.22 zoom 2.51 
    $ reset_camera(0.45)
    show matt2:
        subpixel True pos (1041, 11) xzoom 1.12 yzoom 0.64 
    show trip:
        subpixel True pos (1540, 213) xoffset -351.0 
    #"(Small scene of Matt imagining him losing every game to trip in friendlies)"
    $ renpy.pause(1.0)
    show trip:
        linear 0.25 subpixel True pos (1403, 111) xoffset -351.0 rotate 27.0 
    trip "good games Matt!"
    mt "..."
    show hands1:
        subpixel True pos (1243, 150) rotate -45.0 yrotate 180.0 
        linear 0.2 subpixel True pos (1395, 278) rotate -45.0 yrotate 180.0 
        repeat
    mt "Fuck that. I don't think I can play him right now without getting banned from locals"
    mt "I'll just practice my movement and combos"
    "While practicing, Matt continues to remember all those times he's lost to Trip"
    "(Three different mini scenes)"
    "(Scene 1: At a different smash locals, Matt Chokes a 2-0 lead on trip. Trip pops off)"
    "(Scene 2: At a school tournament, Matt gets wobbled by Trip in melee)"
    "(Scene 3: Matt gets beat up in some random alleyway)"
    mt "Next time we play, I'm beating his ass, I don't care what it takes."
    #ACT 2 STARTS HERE
    "Matt wakes up the next day"
    


    #Save Ocho minigame for act 2.
    $ count = 0
    $ xpos = 30
    $ ypos = 40
    $ zoom = 0.25
    show screen chapter_four_ocho_timer(15,"chapter_four_post_ocho")
    call screen clickable_chapter_four_ocho()

    label chapter_four_post_ocho:
        "wow"
        "You popped [count] times"