default chapter_four_matt_house_fte = [False, False,False, False,False, False,False, False,False]

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
    show matt2:
        linear 0.1 subpixel True pos (543, 0) rotate 0.0 
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
    scene ch04_china_bedroom with fade: 
        subpixel True xzoom 1.32 zoom 1.52 
    show matt2:
        subpixel True pos (1435, 180)  zoom 0.79
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
    "when do you have work?"
    mt "uh 12 why?"
    mt "what time is it currently?"
    "12:03"
    mt "am?"
    mt "pm"
    hide matt2
    show ch04_matt_reaction:
        subpixel True pos (-40, 101) xzoom 1.22 zoom 1.63 
    mt "WHAT"
    mt "NO WAY I AM LATE FOR WORK"
    "So lets go"
    mt "I NEED TO GET READY FOR WORK THOUGH"
    "ugh"
    call auto_advance(1)
    "huh?"
    call auto_advance(0)
    $ count2 = 0
    label ch04_matt_area_1:
        $ location = 1
        call chapter_four_matt_hide_screens
        scene ch04_china_bedroom with dissolve:
            subpixel True xzoom 1.35 zoom 1.53 
        call chapter_four_matt_restore_screens(location)
    label ch04_matt_area_2:
        $ location = 2
        call chapter_four_matt_hide_screens
        scene ch04_china_kitchen with dissolve:
            subpixel True xzoom 1.77 zoom 1.36 
        call chapter_four_matt_restore_screens(location)
    label ch04_matt_area_3:
        $ location = 3
        call chapter_four_matt_hide_screens
        scene ch04_gaming_room with dissolve:
            subpixel True
        call chapter_four_matt_restore_screens(location)
    label ch04_matt_area_4:
        $ location = 4
        call chapter_four_matt_hide_screens
        scene ch04_china_living_room with dissolve:
            subpixel True xzoom 1.16 zoom 2.77 
        call chapter_four_matt_restore_screens(location)
    label ch04_matt_area_5:
        $ location = 5
        call chapter_four_matt_hide_screens
        scene ch04_china_garage with dissolve:
            subpixel True xzoom 1.2 
        call chapter_four_matt_restore_screens(location)
    label ch04_matt_area_6:
        $ location = 6
        call chapter_four_matt_hide_screens
        scene ch04_china_hallway with dissolve:
            subpixel True xzoom 1.2 zoom 1.64 
        call chapter_four_matt_restore_screens(location)
    label ch04_matt_area_7:
        $ location = 7
        call chapter_four_matt_hide_screens
        scene ch04_china_exit with dissolve:
            subpixel True zoom 1.61 
        call chapter_four_matt_restore_screens(location)
    label ch04_matt_area_8:
        $ location = 8
        call chapter_four_matt_hide_screens
        scene ch04_china_master_bedroom with dissolve:
            subpixel True xzoom 1.38 zoom 2.32 
        call chapter_four_matt_restore_screens(location)
    label ch04_matt_area_9:
        $ location = 9
        call chapter_four_matt_hide_screens
        scene ch04_china_master_bathroom with dissolve:
            subpixel True xzoom 1.17 zoom 1.62 
        call chapter_four_matt_restore_screens(location)
    label ch04_matt_area_10:
        $ location = 10
        if not chapter_four_item_check("matt_bathroom_access"):
            call chapter_four_matt_bathroom_locked
        call chapter_four_matt_hide_screens
        scene ch04_china_bathroom with dissolve:
            subpixel True xzoom 2.22 yzoom 1.08 
        call chapter_four_matt_restore_screens(location)

label chapter_four_act_2:
    show matt2:
        subpixel True pos (861, 206) zoom 0.74 
    mt "oh fuck"
    mt "what time is it?"
    "12:32"
    mt "WE HAVE TO GO NOW"
    "well you are the mc"
    "its literally up to you"
    mt "I'm waiting for the jumpcut"
    call auto_advance(1)
    "huh?"
    call auto_advance(0)
    show matt2:
        linear 0.234567 subpixel True pos (-286, 200) zoom 0.79
    #ACT 2 STARTS HERE
    pause 0.3
    scene ch04_street1 with dissolve:
        subpixel True yzoom 1.19 zoom 2.0 
    show matt2:
        subpixel True pos (1086, 380) zpos 0.0 zoom 0.41 
    show car1:
        subpixel True pos (780, 406)
    pause 3.5
    "what"
    mt "see told ya"
    "Where do you even work at?"
    mt "I work at this legally distinct american ice cream shop"
    call auto_advance(1)
    "You can say ba-"
    call auto_advance(0)
    mt "NO WE CANNOT"
    "okay"
    "Generic Ice Cream Store here we go."
    scene ch04_ice_cream_exterior with dissolve:
        subpixel True xzoom 1.26 yzoom 1.09 
    show matt2:
        subpixel True pos (1935, 263) zoom 0.63 
        linear 0.234567 subpixel True pos (1505, 268) zoom 0.63 
    mt "WHAT CITY ARE WE IN?????????????????????????????????????????????????????????????????"
    mt "THIS IS THE MOST GHETTO AND UGLY STORE EVER"
    mt "well I guess I gotta clock in..."
    camera:
        linear 0.56 subpixel True pos (-1584, -1773) zoom 4.13
    pause 0.6
    $ reset_camera(0)
    scene ch04_ice_cream_interior with dissolve:
        subpixel True xzoom 1.18 zoom 1.64 
    show matt2:
        subpixel True pos (1923, 208) zoom 0.67 
        linear 0.45 subpixel True pos (1212, 208) zoom 0.67 
    mt "damn"
    "is this your workplace?"
    mt "I guess?"
    "what do you mean by 'I Guess'"
    mt "well it is an icecream store"
    mt "but like its so girly and gay"
    mt "oh right..."
    pause 1.0
    "what?"
    mt "I got this new boss.."
    "isn't that a good thing?"
    mt "well apparently my co-worker was just laying about how he is the worst"
    mt "like apparently he is the hitler of bosses"
    "damn we are allowed to say that word?"
    mt "uhhhhhh yeah?"
    mt "well I suppose I gotta meet this asshole"
    show brian1:
        subpixel True pos (-627, 203) zoom 1.17 
        linear 0.5 subpixel True pos (300, 203) zoom 1.17 
    bm "ITS YOU"
    bm "WHY ARE YOU THERE"
    bm "STOP COPYING ME!"
    $ renpy.pause(1.5, hard = True)
    b "you first"
    mt "okay"
    mt "WHY ARRE YOUUUUUUUUUUUUUUUUUUUUUUUUUUUU HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
    b "Oh i got offered a management position here thanks to my credentials!"
    mt "ughhhhhhhh"
    b "well what would you like to have?"
    b "we got a chocolate sale"
    mt "i work here..."
    b "wait"
    b "really?"
    mt "yes"
    b "well thats cool"
    mt "where are the other employees?"
    b "oh its just us"
    mt "You think two people can handle the whole store"
    mt "especially when you don't even know how any of the machiens work"
    b "I dont handle the machines bozo"
    mt "GRRRRRRRRRRRRRRRRRRR"
    mt "THATS THE PROBLEM"
    mt "BRIANNNNNNNNNNNNNNNN"
    b "well I gotta pick my sister up from the airport" #TODO Phone call thing segment here
    mt "WHATTTTTTTTTTTTTTTTTTTTTT"
    b "you got it right?"
    call auto_advance(1)
    mt "wait no"
    mt "I can't one-man a whole fucking store"
    b "later matt!"
    show brian1:
        linear 0.45 subpixel True xpos 2091
    pause 0.2
    show matt2:
        linear 0.5 subpixel True pos (908, 211) 
    call auto_advance(0)
    "..."
    mt "..."
    mt "im so fucked"
    mt "Alright..."
    mt "let's get this break"
    jump chapter_four_setup_resources
