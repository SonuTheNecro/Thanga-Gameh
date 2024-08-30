
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
    pause 1.0
    scene ch04_smash_locals:
        subpixel True xzoom 1.33 zoom 1.06
    camera:
        subpixel True pos (-351, -1773) xzoom 1.0 yzoom 1.0 zoom 3.87
    show matt2:
        subpixel True pos (60, 515) xzoom 3.22 zoom 0.54
    pause 0.1
    $ reset_camera(0.45)
    mt "Fuck that. I don't think I can play him right now without getting banned from locals"
    mt "I'm just gonna go home"
    scene ch04_street1 with dissolve:
        subpixel True yzoom 1.19 zoom 2.0 
    show matt2:
        subpixel True pos (1086, 380) zpos 0.0 zoom 0.41 
    show car1:
        subpixel True pos (780, 406) 
    mt "Why am I always driving on these barren roads"
    "It's because you face the camera so we are very limited for shots here"
    mt "truuuuuuuu"
    mt "wait who was that?"
    "..."
    mt "..."
    mt "fucking trip"
    mt "got me all schizo now"
    mt "so angry"
    mt "ima just get to home asap"
    scene ch04_china_bedroom with dissolve:
        subpixel True xzoom 1.32 zoom 1.52 
    show matt2:
        subpixel True pos (-236, 200) zoom 0.79 
    pause 0.56789
    show matt2:
        linear 0.445 subpixel True pos (286, 200) zoom 0.79 
    mt "YOOOOOOOOOOOOOOOOO"
    mt "MY ROOM"
    mt "WHY IS IT SO CHINESE?!?"
    mt "..."
    mt "FUCKING TRIP"
    mt "MADE MY WHOLE HOUSE FUCKING ASIAN"
    "Yo matt"
    mt "huh?"
    "I think you are going a bit crazy"
    mt "no"
    mt "no"
    mt "IM NOT CRAZY"
    mt "IM NOT CRAZY"
    "Why are you repeating yourself then"
    mt "fuck"
    mt "listen invisible man"
    mt "trip got me all worked up"
    mt "ima just go to bed and sleep off"
    camera:
        linear 0.23 subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.98)*SaturationMatrix(0.74)*BrightnessMatrix(-0.54)*HueMatrix(0.0) 
    show matt2:
        linear 0.23 subpixel True pos (561, 150) rotate -18.0 
    "..."
    "..."
    mt "I GOT IT!"
    mt "WHY DID I FUCKING PK-FIRE?!?"
    mt "I SHOULDA HELD YO-YO"
    mt "FUCKING TRIP!"
    mt "RUINING ANOTHER ONE OF MY GOD DAMN LOCALS"
    mt "OH IMA DESTROY HIM NEXT TIME"
    call auto_advance(1)
    mt "I'll ra-"
    # The Next Day...
    call auto_advance(0)
    $ reset_camera(0)
    scene ch04_china_bedroom with dissolve:
        subpixel True xzoom 1.32 zoom 1.52 
    show matt2:
        subpixel True pos (286, 200) zoom 0.79 
    mt "holy shit I slept like an eight dog who is morbidly obese and homosexual"
    "That is oddly specific"
    mt "mhmm"
    "So whats the plan today?"
    mt "Well The Smash Locals, SGS is having a special 2x event thingy"
    mt "basically its just two events so I can rematch trip"
    mt "then I can fry his ass"
    mt "im about to train all day"
    "Should you just not?"
    mt "wdym?"
    "Well you should do some other activities in life and do some warmups and just fight trip"
    mt "nahhhh I dont think so"    
    mt "I'll just practice my movement and combos"
    "Well I'm the one reading the book so I could just skip this"
    mt "yo fourth wall break"
    "Im skipping you"
    menu:
        "Skip":
            jump chapter_four
        "Don't Skip":
            jump chapter_four_no_skip
    
    label chapter_four_no_skip:
        mt "BOOM!"
    mt "yeah you like those forward-airs!"
    mt "oh god"
    mt "The memories"
    mt "AHHHHHHHH"
    
    "While practicing, Matt continues to remember all those times he's lost to Trip"
    "(Three different mini scenes)"
    "(Scene 1: At a different smash locals, Matt Chokes a 2-0 lead on trip. Trip pops off)"
    "(Scene 2: At a school tournament, Matt gets wobbled by Trip in melee)"
    "(Scene 3: Matt gets beat up in some random alleyway)"
    scene ch03_alleyway with dissolve:
        subpixel True xpos -81 xzoom 1.17 yzoom 1.12 zoom 0.9
    show matt2:
        subpixel True pos (1178, 638) rotate 450.0  zoom 0.58
    show trip:
        subpixel True yrotate 180.0
        subpixel True 
        pos (843, 280) 
        linear 0.21 pos (1133, 316) 
        linear 0.34 pos (1251, 18) 
        linear 0.26 pos (1255, 463) 
        linear 0.25 pos (1486, 213) 
        linear 0.08 pos (1413, 48) 
        linear 0.31 pos (1316, 435) 
        linear 0.13 pos (1510, 130) 
        linear 0.35 pos (1501, 435)
        linear 0.312 pos (1501, 435)
        repeat
    with Pause(2.03)
    mt "WAIT THIS ISN'T EVEN SMASH WAIT"
    mt "STOP TRIP"
    mt "AHHHHHHH"
    scene ch04_china_bedroom with dissolve:
        subpixel True xzoom 1.32 zoom 1.52 
    show matt2:
        subpixel True pos (286, 200) zoom 0.79
    mt "huh?"
    mt "Oh"
    mt "it was just a dream"
    mt "Im blaming trip"
    mt "I swear next set"
    mt "next fucking set"
    mt "Next time we play, I'm beating his ass, I don't care what it takes."
    show matt2:
        linear 0.234567 subpixel True pos (-286, 200) zoom 0.79
    #ACT 2 STARTS HERE
    pause 0.3
    scene ch04_china_living_room with dissolve:
        subpixel True xzoom 1.24 zoom 2.71 
    show matt2:
        subpixel True pos (-236, 200) zoom 0.79 
    pause 0.56789
    show matt2:
        linear 0.445 subpixel True pos (286, 200) zoom 0.79 
    mt "YO WHY IS MY WHOLE HOUSE TAIWAN???????"
    mt "WHO DID THIS?"
    mt "IM BLAMING TRIP"
    mt "GRRRRRRRRRRRRRRRRRRRRRRRRRRR"
    show ch04_ocho:
        subpixel True pos (1050, 356) zoom 0.41 yrotate 180.0 
    mt "WHY ARE YOU SO BIG?????????????????????????????"
    mt "WHAT"
    ocho "woof"
    mt "THAT DOESN'T ANSWER MY QUESTION"
    "test"
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