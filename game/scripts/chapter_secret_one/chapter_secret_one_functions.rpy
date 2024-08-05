init python:
    def get_label_name_up(origin):
        return f"chs01_area{origin - 4}"
    def get_label_name_down(origin):
        return f"chs01_area{origin + 4}"
    def get_label_name_left(origin):
        return f"chs01_area{origin - 1}"
    def get_label_name_right(origin):
        return f"chs01_area{origin + 1}"

label chapter_secret_one_movement:
    screen chapter_secret_one_up_button(origin):
        imagebutton:
            xalign 0.5
            yalign -0.05
            idle "images/ArrowUpPress.png"
            hover "images/ArrowUpPress.png"
            action Jump(get_label_name_up(origin))

    screen chapter_secret_one_down_button(origin):
        imagebutton:
            xalign 0.5
            yalign 0.995
            idle "images/ArrowDownPress.png"
            hover "images/ArrowDownPress.png"
            action Jump(get_label_name_down(origin))
    screen chapter_secret_one_left_button(origin):
        imagebutton:
            xalign 0.005
            yalign 0.5
            idle "images/ArrowLeftPress.png"
            hover "images/ArrowLeftPress.png"
            action Jump(get_label_name_left(origin))
    screen chapter_secret_one_right_button(origin):
        imagebutton:
            xalign 0.995
            yalign 0.5
            idle "images/ArrowRightPress.png"
            hover "images/ArrowRightPress.png"
            action Jump(get_label_name_right(origin))
label chs01_hide_screens:
    hide screen chapter_secret_one_left_button
    hide screen chapter_secret_one_right_button
    hide screen chapter_secret_one_down_button
    hide screen chapter_secret_one_up_button
    hide screen clickable_chs01_matt
    hide screen clickable_chs01_note1
    hide screen clickable_chs01_note2
    hide screen clickable_chs01_note3
    hide screen clickable_chs01_note4
    hide screen clickable_chs01_note5
    hide screen clickable_chs01_note6
    hide screen clickable_chs01_note7
    hide screen clickable_chs01_note8
    return
label chs01_restore_movement(location):
    if location > 4:
        show screen chapter_secret_one_up_button(location)
    if location < 13:
        show screen chapter_secret_one_down_button(location)
    if not (location % 4 == 1):
        show screen chapter_secret_one_left_button(location)
    if not (location % 4 == 0):
        show screen chapter_secret_one_right_button(location)
    call screen clickable_chs01_matt
    return
label chs01_restore_screens(location):
    $ renpy.sound.play("audio/sound/chapter_one/street1.ogg")
    if location == 2 and not chapter_secret_one_notes[0]:
        show screen clickable_chs01_note1
    elif location == 4 and not chapter_secret_one_notes[1]: 
        show screen clickable_chs01_note2
    elif location == 6 and not chapter_secret_one_notes[2]:
        show screen clickable_chs01_note3
    elif location == 7 and not chapter_secret_one_notes[3]:
        show screen clickable_chs01_note4
    elif location == 9 and not chapter_secret_one_notes[4]:
        show screen clickable_chs01_note5
    elif location == 11 and not chapter_secret_one_notes[5]:
        show screen clickable_chs01_note6
    elif location == 14 and not chapter_secret_one_notes[6]:
        show screen clickable_chs01_note7
    elif location == 16 and not chapter_secret_one_notes[7]:
        show screen clickable_chs01_note8
    call chs01_slender_movement
    if (slender_location == location):
        show slendy
        play sound "audio/sound/general/shock_horror.ogg"
        if (count > 0):
            $ count -= 1
        else:
            call chs01_hide_screens
            play movie "video/general/slendy.webm"
            pause 2.0
            call stab_blood_screen
            pause 0.9
            show black with vpunch and hpunch
            jump game_over
    elif (slender_location - location == 1 or location - slender_location == 1 or slender_location - location == 4 or location - slender_location == 4 ):
        play sound "audio/sound/general/slendy_laugh.ogg"
    call chs01_restore_movement(location)
    return

label chs01_slender_movement:
    $ rngint = renpy.random.randint(0,3)
    if rngint % 2 == 0:
        pass
    else:
        if (location - 1) // 4 == (slender_location-1) // 4: #On the same row
            if (location - slender_location) > 0:
                $ slender_location += 1
            elif (location - slender_location) < 0:
                $ slender_location -= 1
        else:                                                # Not on the same row
            if(location - slender_location) < 0:
                $ slender_location -= 4
            elif (location - slender_location) > 0:
                $ slender_location += 4
    return
label chs01_matt:
    screen clickable_chs01_matt:
        imagebutton:
            pos((310, 230)) at Transform(zoom=0.18)
            idle "images/matt2.jpg"
            hover At("images/matt2.jpg", animated_outline)
            action Call("chs01_matt_filler")
    label chs01_matt_filler:
        mt "LET ME GET OUTTA THIS SHITTY FOREST OH MY FUCKING GOD!"
        return

label chs01_notes:
    screen clickable_chs01_note1:
        imagebutton:
            pos (1090, 223) at Transform(zoom=0.3)
            idle "images/chapter_secret_one/secret_paper1.jpg"
            hover At("images/chapter_secret_one/secret_paper1.jpg", animated_outline)
            action Jump("chs01_note1_found")
    label chs01_note1_found:
        hide secret_paper1
        "You found a note!"
        play sound2 "audio/sound/chapter_one/item_pickup.ogg"
        $ chapter_secret_one_notes[0] = True
        call chs01_note_check
        jump chs01_area2
    screen clickable_chs01_note2:
        imagebutton:
            pos (471, 300) at Transform(zoom=0.3)
            idle "images/chapter_secret_one/secret_paper2.jpg"
            hover At("images/chapter_secret_one/secret_paper2.jpg", animated_outline)
            action Jump("chs01_note2_found")
    label chs01_note2_found:
        hide secret_paper2
        "You found a note!"
        play sound2 "audio/sound/chapter_one/item_pickup.ogg"
        $ chapter_secret_one_notes[1] = True
        call chs01_note_check
        jump chs01_area4
    screen clickable_chs01_note3:
        imagebutton:
            pos (471, 300) at Transform(zoom=0.3)
            idle "images/chapter_secret_one/secret_paper3.jpg"
            hover At("images/chapter_secret_one/secret_paper3.jpg", animated_outline)
            action Jump("chs01_note3_found")
    label chs01_note3_found:
        hide secret_paper3
        "You found a note!"
        play sound2 "audio/sound/chapter_one/item_pickup.ogg"
        $ chapter_secret_one_notes[2] = True
        call chs01_note_check
        jump chs01_area6
    screen clickable_chs01_note4:
        imagebutton:
            pos (1090, 223) at Transform(zoom=0.3)
            idle "images/chapter_secret_one/secret_paper4.jpg"
            hover At("images/chapter_secret_one/secret_paper4.jpg", animated_outline)
            action Jump("chs01_note4_found")
    label chs01_note4_found:
        hide secret_paper4
        "You found a note!"
        play sound2 "audio/sound/chapter_one/item_pickup.ogg"
        $ chapter_secret_one_notes[3] = True
        call chs01_note_check
        jump chs01_area7
    screen clickable_chs01_note5:
        imagebutton:
            pos (1090, 223) at Transform(zoom=0.3)
            idle "images/chapter_secret_one/secret_paper5.jpg"
            hover At("images/chapter_secret_one/secret_paper5.jpg", animated_outline)
            action Jump("chs01_note5_found")
    label chs01_note5_found:
        hide secret_paper5
        "You found a note!"
        play sound2 "audio/sound/chapter_one/item_pickup.ogg"
        $ chapter_secret_one_notes[4] = True
        call chs01_note_check
        jump chs01_area9
    screen clickable_chs01_note6:
        imagebutton:
            pos (471, 300) at Transform(zoom=0.3)
            idle "images/chapter_secret_one/secret_paper6.jpg"
            hover At("images/chapter_secret_one/secret_paper6.jpg", animated_outline)
            action Jump("chs01_note6_found")
    label chs01_note6_found:
        hide secret_paper6
        "You found a note!"
        play sound2 "audio/sound/chapter_one/item_pickup.ogg"
        $ chapter_secret_one_notes[5] = True
        call chs01_note_check
        jump chs01_area11
    screen clickable_chs01_note7:
        imagebutton:
            pos (471, 300) at Transform(zoom=0.3)
            idle "images/chapter_secret_one/secret_paper7.png"
            hover At("images/chapter_secret_one/secret_paper7.png", animated_outline)
            action Jump("chs01_note7_found")
    label chs01_note7_found:
        hide secret_paper7
        "You found a note!"
        play sound2 "audio/sound/chapter_one/item_pickup.ogg"
        $ chapter_secret_one_notes[6] = True
        call chs01_note_check
        jump chs01_area14
    screen clickable_chs01_note8:
        imagebutton:
            pos (1090, 223) at Transform(zoom=0.3)
            idle "images/chapter_secret_one/secret_paper8.png"
            hover At("images/chapter_secret_one/secret_paper8.png", animated_outline)
            action Jump("chs01_note8_found")
    label chs01_note8_found:
        hide secret_paper8
        "You found a note!"
        play sound2 "audio/sound/chapter_one/item_pickup.ogg"
        $ chapter_secret_one_notes[7] = True
        call chs01_note_check
        jump chs01_area16
    label chs01_note_check:
        if all(chapter_secret_one_notes):
            jump chs01_all_notes_found
        return
    label chs01_all_notes_found:
        call chs01_hide_screens
        stop music
        play music "audio/music/chapter_three/youthful_lunch.ogg"
        scene mcdonalds_outside with dissolve:
            xzoom 3.2 yzoom 2.6
        show matt2:
            subpixel True pos (1135, 223) zoom 0.28 
        mt "WHAT THE FUCK WAS THAT?"
        mt "WAIT HOW AM I HERE WHAT!!!!!!!!"
        mt "WHAT IS HAPPENING!!!!!!!"
        mt "WHAT!"
        show thanga2 with moveinleft:
            xzoom 1.3 yzoom 1.3 xalign 0.3 yalign 0.9
        t "yo what are you doing here matt?"
        mt "WHAT!"
        mt "WHAT ARE YOU DOING HERE?"
        t "Well kody is crying about no ice cream in there so I am just waiting for the tantrum"
        "wait a minute"
        stop music
        jump start