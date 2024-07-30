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
    hide screen clickable_chs01_note
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

    call chs01_slender_movement
    if (slender_location == location):
        show slendy
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
            pos((450, 230)) at Transform(zoom=0.18)
            idle "images/matt2.jpg"
            hover "images/matt2.jpg"
            action Call("chs01_matt_filler")
        label chs01_matt_filler:
        mt "LET ME GET OUTTA THIS SHITTY FOREST OH MY FUCKING GOD!"
        return

label chs01_notes:
    screen clickable_chs01_note1:
        imagebutton:
            pos (0, 0)
            idle "images/chapter_secret_one/secret_paper1.jpg"
            hover "images/chapter_secret_one/secret_paper1.jpg"
            action Call("chs01_note1_found")
    label chs01_note1_found:
        hide secret_paper1
        "You found a note!"
        $ chapter_secret_one_notes[0] = False
        return