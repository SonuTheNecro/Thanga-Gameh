# Code for the functions in Chapter Four


init python:
    from random import randint
    from enum import Enum





label chapter_four_matts_house:
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


label chapter_four_ocho_minigame:
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
            pos(xpos,ypos) at Transform(zoom = zoom, yrotate = 180.0)
            idle "images/chapter_four/ch04_ocho.png"
            hover "images/chapter_four/ch04_ocho.png"
            action If(count % 2 == 0, true = [SetVariable("zoom", zoom+0.02), SetVariable("xpos", xpos-2), SetVariable("ypos", ypos-2),Play("sound2","audio/sound/general/pop.ogg"), SetVariable("count", count+1)], false = [Play("sound2","audio/sound/general/pop.ogg"), SetVariable("count", count+1)])