# Code for the functions in Chapter Four


init python:
    from random import randint
    from enum import Enum








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
            pos(xpos,ypos) at Transform(zoom = zoom)
            idle "images/chapter_three/ch03_usps_baby_ocho.png"
            hover "images/chapter_three/ch03_usps_baby_ocho.png"
            action If(count % 2 == 0, true = [SetVariable("zoom", zoom+0.02), SetVariable("xpos", xpos-2), SetVariable("ypos", ypos-2),Play("sound2","audio/sound/general/pop.ogg"), SetVariable("count", count+1)], false = [Play("sound2","audio/sound/general/pop.ogg"), SetVariable("count", count+1)])