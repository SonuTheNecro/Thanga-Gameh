default chapter_secret_one_notes = [False, False, False, False, False, False, False, False]
label chapter_secret_one_start:
    $ discord.update(state = "??????????", details = "In Chapter Secret One", large_image = "chapter_one")
    scene street2 with dissolve:
        subpixel True xzoom 1.16 zoom 0.79
    show matt2:
        subpixel True crop_relative True pos (1015, 405) zoom 0.08  crop (0.0, 0.0, 1.0, 0.61)
    show car1:
        subpixel True pos (833, 405) zoom 0.57 

    mt "Damn work fucking sucked dick"
    mt "like WHY"
    mt "WHY DID KODY COME IN WITH THANG ASKING FOR AN ICE CREAM HOTDOG"
    mt "WE DON'T EVEN SERVE THAT"
    mt "I FUCKING HATE THE THANG HOUSEHOLD"

    mt "AND I FUCKING HATE MY CO-WORKERS"
    mt "FUCKING SPILLED WATER ON THE FLOOR WHILE I WAS TAKING A FUCKING POO"
    mt "HOLY SHIT"
    mt "UGH I ACTUALLY HATE KOREANS GOD"

    mt "ugh I got a discord ping"
    mt "'@Lethal Company'"
    mt "Fuck that"
    mt "I AINT DEALING WITH THE 94 YEAR OLD AND THE 22 YEAR OLD MAN CHILDREN"
    mt "AND I DONT WANNA STUDY"
    mt "I WISH I DIDN'T HAVE TO GO HOME AND JUST DISAPPEAR FOREVER"

    questionmark "hehehe"
    mt "HUH?"
    questionmark "...."
    mt "SHOW YOURSELF"
    call auto_advance(1)
    stop music
    play sound "audio/sound/chapter_one/car_crash.ogg"
    window hide
    scene car_crash2 with vpunch and hpunch:
        subpixel True pos (-18, -81) xzoom 1.23 yzoom 1.1 zoom 2.11
    $ renpy.pause(2.5)
    call auto_advance(0)
    show matt2 with dissolve:
        subpixel True pos (1730, 418) zoom 0.18 
    mt "..."
    mt "FUCKING HELL"
    mt "WHO THE HELL CAUSED THIS SHIT"
    mt "I GOTTA POO AGAIN"
    mt "I GOTTA CALL MY FUCKING MOM TO PICK ME UP"
    mt "holy shit the insurance is gonna go crazy"
    play sound "audio/sound/chapter_three/phone_ring1.ogg"
    mt "pick up pick up pick up pls...."
    mt "..."
    stop sound
    mt "ugh no signal"
    mt "well"
    mt "Let's get outta here"
    mt "How am i so far away from the road"
    $ slender_location = renpy.random.randint(1,16)
    label chs01_area1:
        $ location =1
        call chs01_hide_screens
        scene secret_forest1 with dissolve:
            subpixel True xzoom 1.28 yzoom 1.09 
        call chs01_restore_screens(location)
    label chs01_area2:
        $ location = 2
        call chs01_hide_screens
        scene secret_forest2 with dissolve:
            subpixel True xzoom 1.77 zoom 1.06 
        call chs01_restore_screens(location)
    label chs01_area3:
        $ location = 3
        call chs01_hide_screens
        scene secret_forest3 with dissolve:
            subpixel True xzoom 1.19 zoom 1.08 
        call chs01_restore_screens(location)
    label chs01_area4:
        $ location = 4
        call chs01_hide_screens
        scene secret_forest4 with dissolve:
            subpixel True xzoom 1.21 zoom 3.01 
        call chs01_restore_screens(location)
    label chs01_area5:
        $ location = 5
        call chs01_hide_screens
        scene secret_forest5 with dissolve:
            subpixel True zoom 1.6 
        call chs01_restore_screens(location)
    label chs01_area6:
        $ location = 6
        call chs01_hide_screens
        scene secret_forest6 with dissolve:
            subpixel True xzoom 1.05 yzoom 1.11 zoom 2.75 
        call chs01_restore_screens(location)
    label chs01_area7:
        $ location = 7
        call chs01_hide_screens
        scene secret_forest7 with dissolve:
            subpixel True xzoom 1.2 zoom 1.6 
        call chs01_restore_screens(location)
    label chs01_area8:
        $ location = 8
        call chs01_hide_screens
        scene secret_forest8 with dissolve:
            subpixel True xzoom 1.1 zoom 1.37 
        call chs01_restore_screens(location)
    label chs01_area9:
        $ location = 9
        call chs01_hide_screens
        scene secret_forest9 with dissolve:
            subpixel True xzoom 1.19 zoom 3.2 
        call chs01_restore_screens(location)
    label chs01_area10:
        $ location = 10
        call chs01_hide_screens
        scene secret_forest10 with dissolve:
            subpixel True xzoom 1.18 zoom 3.02 
        call chs01_restore_screens(location)
    label chs01_area11:
        $ location = 11
        call chs01_hide_screens
        scene secret_forest11 with dissolve:
            subpixel True xzoom 1.17 zoom 0.56 
        call chs01_restore_screens(location)
    label chs01_area12:
        $ location = 12
        call chs01_hide_screens
        scene secret_forest12 with dissolve:
            subpixel True yzoom 1.06 zoom 2.75 
        call chs01_restore_screens(location)
    label chs01_area13:
        $ location = 13
        call chs01_hide_screens
        scene secret_forest13 with dissolve:
            subpixel True yzoom 1.03 zoom 1.6 
        call chs01_restore_screens(location)
    label chs01_area14:
        $ location = 14
        call chs01_hide_screens
        scene secret_forest14 with dissolve:
            subpixel True zoom 1.6 
        call chs01_restore_screens(location)
    label chs01_area15:
        $ location = 15
        call chs01_hide_screens
        scene secret_forest15 with dissolve:
            subpixel True xzoom 1.2 zoom 1.82 
        call chs01_restore_screens(location)
    label chs01_area16:
        $ location = 16
        call chs01_hide_screens
        scene secret_forest16 with dissolve:
            subpixel True zoom 2.01 
        call chs01_restore_screens(location)




    "test"
