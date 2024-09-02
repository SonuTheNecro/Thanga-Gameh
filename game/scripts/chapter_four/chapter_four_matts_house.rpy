# Code for Matt's House in Act 1 of Chapter Four

init python:
    from enum import Enum
    def chapter_four_item_check(item):
        return chapter_four_key_items.get(item, ItemState.NOT_OBTAINED) == ItemState.OBTAINED
    def chapter_four_obtain_item(item):
        chapter_four_key_items[item] = ItemState.OBTAINED
    def chapter_four_unobtain_item(item):
        chapter_four_key_items[item] = ItemState.NOT_OBTAINED

default chapter_four_key_items = {
    "matt_dog_food"        : ItemState.NOT_OBTAINED,
    "matt_lock_pick"       : ItemState.NOT_OBTAINED,
    "matt_hammer"          : ItemState.NOT_OBTAINED,
    "matt_toothpath"       : ItemState.NOT_OBTAINED,
    "matt_love"            : ItemState.NOT_OBTAINED,
}


label chapter_four_matts_house_movement:
    screen chapter_four_matts_house_up_button(origin):
        imagebutton:
            xalign 0.5
            yalign 0
            idle "images/ArrowUpPress2.png"
            hover "images/ArrowUpPress2.png"
            if origin == 4:
                action Jump("ch04_matt_area_2")
            elif origin == 6:
                action Jump("ch04_matt_area_1")
            elif origin == 5:
                action Jump("ch04_matt_area_4")
            elif origin == 7:
                action Jump("ch04_matt_area_6")
            elif origin == 9:
                action Jump("ch04_matt_area_8")
    screen chapter_four_matts_house_down_button(origin):
        imagebutton:
            xalign 0.5
            yalign 1.0
            idle "images/ArrowDownPress2.png"
            hover "images/ArrowDownPress2.png"
            if origin == 2:
                action Jump("ch04_matt_area_4")
            elif origin == 1:
                action Jump("ch04_matt_area_6")
            elif origin == 4:
                action Jump("ch04_matt_area_5")
            elif origin == 6:
                action Jump("ch04_matt_area_7")
            elif origin == 8:
                action Jump("ch04_matt_area_9")
    screen chapter_four_matts_house_left_button(origin):
        imagebutton:
            xalign 0.0
            yalign 0.5
            idle "images/ArrowLeftPress2.png"
            hover "images/ArrowLeftPress2.png"
            if origin == 4:
                action Jump("ch04_matt_area_3")
            elif origin == 6:
                action Jump("ch04_matt_area_4")
            elif origin == 7:
                action Jump("ch04_matt_area_5")
            elif origin == 8:
                action Jump("ch04_matt_area_6")
            elif origin == 10:
                action Jump("ch04_matt_area_1")
    screen chapter_four_matts_house_right_button(origin):
        imagebutton:
            xalign 1.0
            yalign 0.5
            idle "images/ArrowRightPress2.png"
            hover "images/ArrowRightPress2.png"
            if origin == 3:
                action Jump("ch04_matt_area_4")
            elif origin == 4:
                action Jump("ch04_matt_area_6")
            elif origin == 5:
                action Jump("ch04_matt_area_7")
            elif origin == 6:
                action Jump("ch04_matt_area_8")
            elif origin == 1:
                action Jump("ch04_matt_area_10")
label chapter_four_matt_hide_screens:
    hide screen clickable_chapter_four_matts_house_ocho
    hide screen chapter_four_matts_house_up_button
    hide screen chapter_four_matts_house_down_button
    hide screen chapter_four_matts_house_left_button
    hide screen chapter_four_matts_house_right_button
    return
label chapter_four_matt_restore_screens(location):
    if location == 1:
        pass
    elif location == 2:
        pass
    elif location == 3:
        pass
    elif location == 4:
        if not chapter_four_matt_house_fte[0]:
            call ch04_lr_ocho_meet
        elif not chapter_four_item_check("matt_love"):
            show screen clickable_chapter_four_matts_house_ocho
    elif location == 5:
        pass
    elif location == 6:
        pass
    elif location == 7:
        pass
    elif location == 8:
        pass
    elif location == 9:
        pass
    elif location == 10:
        pass
    call chapter_four_matt_restore_movement(location)
    return
label chapter_four_matt_restore_movement(location):
    if location == 1:
        show screen chapter_four_matts_house_down_button(location)
        call screen chapter_four_matts_house_right_button(location)
    elif location == 2:
        call screen chapter_four_matts_house_down_button(location)
    elif location == 3:
        call screen chapter_four_matts_house_right_button(location)
    elif location == 4:
        show screen chapter_four_matts_house_up_button(location)
        show screen chapter_four_matts_house_down_button(location)
        show screen chapter_four_matts_house_left_button(location)
        call screen chapter_four_matts_house_right_button(location)
    elif location == 5:
        show screen chapter_four_matts_house_right_button(location)
        call screen chapter_four_matts_house_up_button(location)
    elif location == 6:
        show screen chapter_four_matts_house_up_button(location)
        show screen chapter_four_matts_house_down_button(location)
        show screen chapter_four_matts_house_left_button(location)
        call screen chapter_four_matts_house_right_button(location)
    elif location == 7:
        show screen chapter_four_matts_house_left_button(location)
        call screen chapter_four_matts_house_up_button(location)
    elif location == 8:
        show screen chapter_four_matts_house_down_button(location)
        call screen chapter_four_matts_house_left_button(location)
    elif location == 9:
        call screen chapter_four_matts_house_up_button(location)
    elif location == 10:
        call screen chapter_four_matts_house_left_button(location)
label chapter_four_matt_events:
    label ch04_lr_ocho_meet:
        show matt2:
            subpixel True pos (-236, 200) zoom 0.79 
        pause 0.56789
        show matt2:
            linear 0.445 subpixel True pos (286, 200) zoom 0.79 
        mt "YO WHY IS MY WHOLE HOUSE TAIWAN???????"
        mt "WHO DID THIS?"
        mt "IM BLAMING TRIP"
        mt "GRRRRRRRRRRRRRRRRRRRRRRRRRRR"
        show ch04_ocho with fade:
            subpixel True 
        mt "WHY ARE YOU SO BIG?????????????????????????????"
        mt "WHAT"
        show ch04_ocho:
            linear 0.34567 subpixel True pos (1050, 356) zoom 0.41
            yrotate 180.0 
        ocho "woof"
        mt "THAT DOESN'T ANSWER MY QUESTION"
        ocho "barks in sadness"
        mt "god damn this dog is the literal weirdest dog from ohio"
        mt "why did they make these fuckers so damn cute wtf"
        mt "come here ocho"
        mt "bark"
        $ chapter_four_matt_house_fte[0] = True
        return
    label ch04_ocho_event:
        screen clickable_chapter_four_matts_house_ocho:
            imagebutton:
                pos (1050,356) at Transform(zoom = 0.41)
                idle "images/chapter_four/ch04_ocho.png"
                hover "images/chapter_four/ch04_ocho.png"
                action Call("ch04_ocho_mash")
        screen chapter_four_ocho_timer(max, endup):
            frame:
                xalign 0.5
                yalign 0.0
                hbox:
                    timer 0.1 action If(time > max, false = SetVariable("time", time + 0.1), true = [Hide("chapter_four_ocho_timer"), SetVariable("time", 0), Jump("%s"%endup) ]) repeat True
                    bar: #an animated bar top center screen
                        value AnimatedValue(value=time, range=max, delay= 0.1)
                        xalign 0.0
                        yalign 0.0
                        xmaximum 600

        screen clickable_chapter_four_ocho():
            imagebutton:
                pos(xpos,ypos) at Transform(zoom = zoom,yrotate = 180.0)
                idle "images/chapter_four/ch04_ocho.png"
                hover "images/chapter_four/ch04_ocho.png"
                action If(count % 2 == 0, true = [SetVariable("zoom", zoom+0.02), SetVariable("xpos", xpos-2), SetVariable("ypos", ypos-2),Play("sound2","audio/sound/general/pop.ogg"), SetVariable("count", count+1)], false = [Play("sound2","audio/sound/general/pop.ogg"), SetVariable("count", count+1)])
        label ch04_ocho_mash:
            call chapter_four_matt_hide_screens
            show ch04_ocho:
                subpixel True pos (1050,356) zoom 0.41
            "Pet Ocho as many times as you can!"
            questionmark "You chose this as your first mini-game?"
            carl "yes"
            #Save Ocho minigame for act 2.
            $ count = 0
            $ xpos = 1050
            $ ypos = 356
            $ zoom = 0.41
            show screen chapter_four_ocho_timer(15,"chapter_four_post_ocho")
            hide ch04_ocho
            call screen clickable_chapter_four_ocho()
            label chapter_four_post_ocho:
            show ch04_ocho:
                subpixel True pos (1050, 356) zoom 0.41
                yrotate 180.0 
            "You petted Ocho [count] time(s)!"
            mt "yeah I bet you liked that"
            jump ch04_matt_area_4
            return