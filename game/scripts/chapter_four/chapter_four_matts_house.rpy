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
    "matt_toothpaste"      : ItemState.NOT_OBTAINED,
    "matt_love"            : ItemState.NOT_OBTAINED,
    "matt_suit"            : ItemState.NOT_OBTAINED, 
    "matt_bathroom_access" : ItemState.OBTAINED, 
}
default chapter_four_matt_house_chores = [False,False, False, False, False, False]
# The onscreens buttons to handle movement
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
label chapter_four_matt_hide_screens: #Resets every clickable thing when we swap screens
    hide screen clickable_chapter_four_clothes
    hide screen clickable_chapter_four_matts_house_controller
    hide screen clickable_chapter_four_dogfood
    hide screen clickable_chapter_four_makeup
    hide screen clickable_chapter_four_toothpaste
    hide screen clickable_chapter_four_matts_house_ocho
    hide screen chapter_four_matts_house_up_button
    hide screen chapter_four_matts_house_down_button
    hide screen chapter_four_matts_house_left_button
    hide screen chapter_four_matts_house_right_button
    return
label chapter_four_matt_restore_screens(location): #Handles spawning events based on which room we are. Switches are not a thing in Renpy so enjoy the if-else chain
    if location == 1:
        if not chapter_four_matt_house_chores[1]:
            show screen clickable_chapter_four_makeup
        if not chapter_four_matt_house_chores[4] and chapter_four_item_check("matt_suit"):
            call ch04_suit_up
    elif location == 2:
        if not chapter_four_item_check("matt_dog_food"): 
            show screen clickable_chapter_four_dogfood
    elif location == 3:
        if not chapter_four_matt_house_chores[3]:
            show screen clickable_chapter_four_matts_house_controller
    elif location == 4:
        if not chapter_four_matt_house_fte[0]:
            call ch04_fte_ocho_meet
        elif not chapter_four_item_check("matt_love"):
            show screen clickable_chapter_four_matts_house_ocho
        elif not chapter_four_matt_house_chores[2] and chapter_four_item_check("matt_dog_food"):
            call ch04_feed_ocho
    elif location == 5:
        if not chapter_four_matt_house_fte[2]:
            call ch04_fte_garage
    elif location == 6:
        pass
    elif location == 7:
        if not chapter_four_matt_house_fte[4]:
            call ch04_attempt_leave_home
    elif location == 8:
        if not chapter_four_matt_house_chores[4] and not chapter_four_item_check("matt_suit"):
            show screen clickable_chapter_four_clothes
    elif location == 9:
        if not chapter_four_item_check("matt_toothpaste"):
            show screen clickable_chapter_four_toothpaste
    elif location == 10:
        if not chapter_four_matt_house_fte[1]:
            call ch04_fte_bathroom
        if not chapter_four_matt_house_chores[0] and chapter_four_item_check("matt_toothpaste"):
            call ch04_brush_teeth
    if count2 == 5 and not chapter_four_matt_house_fte[3]:
        call ch04_work_ready
    call chapter_four_matt_restore_movement(location)
    return
#Controls which movement buttons are shown based on which room we are in
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
# Handles Every event as well as the buttons and any labels or images needed for the event
label chapter_four_matt_events:
    label ch04_fte_ocho_meet:
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
        hide ch04_ocho
        call chapter_four_matt_restore_screens(location)
        return
    label ch04_fte_bathroom:
        show matt2:
            subpixel True pos (-221, 173) zoom 0.77 
        show matt2:
            linear 0.45 subpixel True pos (526, 175) zoom 0.77 
        pause 0.5
        mt "Yo why is my bathroom like clean af now?"
        "This is always your bathroom"
        mt "NAH I HAD THE NASTIEST BATHROOM"
        mt "WHAT THE HELL HAPPENED?"
        "Writing happened"
        mt "mmmmmmmm"
        $ renpy.pause(2.666666, hard = True)
        mt "..."
        mt "I should go brush my teeth for the day"
        "Yeah probably"
        show matt2:
            linear 0.56 subpixel True pos (1258, 275) zoom 0.5 
        #TODO: Sink audio
        $ renpy.pause(2.0, hard = True)
        mt "fuck"
        "what..."
        mt "there is no toothpaste"
        "use water man"
        mt "NAH I ESCAPED THE PHILIPHINES TO NOT BE POOR"
        "isnt that like near philadelphia?"
        "isn't that poor"
        mt "BRO ARE YOU THANG"
        "no"
        mt "BRIAN??????"
        "no"
        mt "SO WHO ARE YOU?"
        " " #TODO:Glitch text plugin here
        mt "right"
        mt "well I need TOOTHPASTE or I AINT BRUSHING MY TEETH"
        "guess you aint brushing your teeth smelly smash player"
        mt 'hahahahha funny joke man'
        mt "fuck off you bitch"
        mt "ima go steal some toothpaste rq"
        $ chapter_four_matt_house_fte[1] = True
        return 
    label ch04_fte_garage:
        show matt2:
            subpixel True pos(2120,175) zoom 0.77 
            linear 0.3456 subpixel True pos(1400,175) zoom 0.77
        $ renpy.pause(0.4, hard = True)
        mt "What happened to the garage?????"
        mt "THIS IS AN AUTOSHOP WHAT!"
        "Its chinese"
        "Like your house"
        mt "nahhhhhhhhhhhhhhhhhhh"
        mt "this isn't chinese"
        "There is chinese text behind you"
        pause 1.0
        mt "..."
        mt "fuck"
        $ chapter_four_matt_house_fte[2] = True
        return 
    label ch04_work_ready:
        mt "alright I got ready for work"
        "nice nice"
        mt "lets go!"
        $ chapter_four_matt_house_fte[3] = True
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
            if count > 90:
                $ chapter_four_obtain_item("matt_love")
            hide ch04_ocho
            call chapter_four_matt_restore_screens(location)
            return
    label ch04_toothpaste:
        screen clickable_chapter_four_toothpaste:
            imagebutton:
                pos (-170, 376) at Transform(zoom = 0.71 )
                idle "images/chapter_four/ch04_toothpaste.png"
                hover "images/chapter_four/ch04_toothpaste.png"
                action Call("chapter_four_toothpaste")
        label chapter_four_toothpaste:
            call chapter_four_matt_hide_screens

            mt "GOTCHA TOOTHPASTE"
            "You have obtained Generic Toothpaste!"
            $ chapter_four_obtain_item("matt_toothpaste")
            call chapter_four_matt_restore_screens(location)
            return
    label ch04_brush_teeth:
        call chapter_four_matt_hide_screens
        show matt2:
            subpixel True pos (-221, 173) zoom 0.77 
        show matt2:
            linear 0.56 subpixel True pos (1258, 275) zoom 0.5
        mt "ALRIGHT LETS BRUSH THESE TEETH"
        "Why are you so excited lol"
        mt "BECAUSE MY BREATH IS SO BAD"
        mt "EVEN I CAN SMELL IT"
        stn "that's disgusting carl"
        stn "why would you write it like this?"
        carl "IT AINT ME ITS HIM!"
        mt "huh who was that?"
        "who was who?"
        mt "nvm"
        mt "lets BRUSH THESE TEETHS LETS FUCKING GO"
        #TODO: brushing sfx
        $ renpy.pause(2.5, hard = True)
        mt "that was fun"
        "im glad"
        $ chapter_four_matt_house_chores[0] = True
        $ count2 += 1
        call chapter_four_matt_restore_screens(location)
        return
    label ch04_makeup:
        screen clickable_chapter_four_makeup:
            imagebutton:
                pos (1648, 715) at Transform(zoom=0.22)
                idle "images/chapter_four/ch04_makeup.png"
                hover "images/chapter_four/ch04_makeup.png"
                action Call("chapter_four_makeup")
        label chapter_four_makeup:
            call chapter_four_matt_hide_screens
            mt "Time to look good af"
            "hA"
            "gay"
            mt "wdym"
            "Gay men use make-up"
            mt "shut yo bish ass up"
            "gay"
            mt "I will not tolerate homophobia"
            mt "also you prob crusty af"
            $ renpy.pause(2.5)
            "..."
            "fuck you"
            "You have put on men's makeup!"
            $ chapter_four_matt_house_chores[1] = True
            $ count2 += 1
            call chapter_four_matt_restore_screens(location)
            return
    label ch04_dog_food:
        screen clickable_chapter_four_dogfood:
            imagebutton:
                pos (896, 141) at Transform(zoom=0.8, yrotate=180.0 )
                idle "images/chapter_four/ch04_dog_food.png"
                hover "images/chapter_four/ch04_dog_food.png"
                action Call("chapter_four_dogfood")
        label chapter_four_dogfood:
            call chapter_four_matt_hide_screens
            "You have obtained Ocho Food"
            mt "ocho food?"
            mt "shouldn't that be dogfood?"
            "I am just reading the book man"
            mt "so..."
            mt "that means the writer of the plot is someone who is obsessed with ocho"
            "STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT STANLEY PARABLE 4TH WALL BREAK YOU GET IT "
            $ chapter_four_obtain_item("matt_dog_food")
            call chapter_four_matt_restore_screens(location)
            return
    label ch04_feed_ocho:
        call chapter_four_matt_hide_screens
        show matt2:
            subpixel True pos (-236, 200) zoom 0.79 
        pause 0.56789
        show matt2:
            linear 0.445 subpixel True pos (286, 200) zoom 0.79 
        show ch04_ocho:
            subpixel True pos (1050, 356) zoom 0.41
            yrotate 180.0
        pause 1.3
        show ch04_dog_food:
            subpixel True pos (283, 228) zoom 0.79 
            linear 1.0 subpixel True pos (513, 366) zoom 0.79 


        mt "This dog is so fat istg"
        ocho "hello matt"
        call auto_advance(1)
        mt "WHATTTTTTTTTTTTTTTTTT"
        call auto_advance(0)
        $ chapter_four_matt_house_chores[2] = True
        $ count2 += 1
        call chapter_four_matt_restore_screens(location)
        return
    label ch04_smash:
        screen clickable_chapter_four_matts_house_controller:
            imagebutton:
                pos (726, 331) at Transform(zoom = 0.71)
                idle "images/chapter_four/ch04_controller.png"
                hover "images/chapter_four/ch04_controller.png"
                action Call("chapter_four_smash_practice")
        label chapter_four_smash_practice:
            call chapter_four_matt_hide_screens
            show matt2:
                subpixel True pos (2600, 256) zoom 0.71 
            show matt2:
                linear 0.45 subpixel True pos (1290, 256) zoom 0.71 
            mt "alright Im going to go practice now"
            mt "..."
            mt "Im not even going to question why my gaming setup is like this"
            mt "Oh I'm ready for this Game Day its going to be great."
            "..."
            mt "BOOM!"
            mt "yeah you like those forward-airs!"
            mt "oh god"
            mt "The memories"
            mt "AHHHHHHHH"
            
            "While practicing, Matt continues to remember all those times he's lost to Trip"
            "(Three different mini scenes)"
            "(Scene 1: At a different smash locals, Matt Chokes a 2-0 lead on trip. Trip pops off)"
            "(Scene 2: At a school tournament, Matt gets wobbled by Trip in melee)" 
            "(Scene 3: Matt gets beat up in some random alleyway)" #Done
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
            scene ch04_gaming_room
            camera:
                subpixel True pos (-4347, -801) zoom 3.81 
            show matt2:
                subpixel True pos (1290, 256) zoom 0.71
            pause 0.1
            $ reset_camera(0.45)
            pause 0.45
            mt "AH"
            mt "oh"
            mt "why am I getting Schizo"
            mt "..."
            "You good man?"
            mt "yeah yeah"
            mt "im just"
            mt "im just"
            mt "im good okay"
            "right..."
            mt "I think thats all the practice I need"
            $ chapter_four_matt_house_chores[3] = True
            $ count2 += 1
            call chapter_four_matt_restore_screens(location)
            return
    label ch04_work_clothes:
        screen clickable_chapter_four_clothes:
            imagebutton:
                pos (810, 370) at Transform(zoom = 0.21 )
                idle "images/chapter_four/ch04_clown_suit.png"
                hover "images/chapter_four/ch04_clown_suit.png"
                action Call("chapter_four_dress_up")
        label chapter_four_dress_up:
            call chapter_four_matt_hide_screens
            mt "okay whoever chose a clown suit as my work clothes"
            mt "yeah you a real funny guy CARL"
            mt "CARLLLLLLLLLLLLLLLLLLLL"
            "You have obtained your working clothes"
            "be sure to wear it though"
            mt "I aint stupid I know how to wear clothes"
            $ chapter_four_obtain_item("matt_suit")
            call chapter_four_matt_restore_screens(location)
            return
    label ch04_suit_up:
        call chapter_four_matt_hide_screens
        mt "alright I got this suit on"
        mt "how come I cannot see it"
        "Just wait, it will be funny for all of us if you just wait for it"
        mt "ugh"
        $ chapter_four_matt_house_chores[4] = True
        $ count2 += 1
        call chapter_four_matt_restore_screens(location)
        return
    label ch04_attempt_leave_home:
        call chapter_four_matt_hide_screens
        mt "alright lets get out of here"
        "yeah honestly"
        mt "wait I gotta POOOOOOOOOOOOOOOOOOOOOO"
        "..."
        "you serious?!?"
        mt "yes"
        "just do it at work"
        "poo on their time"
        mt "nahhh"
        mt "this is an S+ emergency"
        "..."
        mt "I NEED TO GO TO THE BATHROOM!"
        $ chapter_four_matt_house_fte[4] = True
        $ chapter_four_unobtain_item("matt_bathroom_access")
        call chapter_four_matt_restore_screens(location)
        return
    label chapter_four_matt_bathroom_locked:
        call chapter_four_matt_hide_screens
        if chapter_four_item_check("matt_lock_pick") or chapter_four_item_check("matt_hammer"):
            mt "TIME TO OPEN THIS STUPID FUCKING DOOR"
            #TODO: Door unlock sfx
            mt "alright lets go"
            $ chapter_four_obtain_item("matt_bathroom_access")
            $ chapter_four_obtain_item("matt_lock_pick")
            $ chapter_four_obtain_item("matt_hammer")
        else:
            mt "OPEN THE DOOR PLEASE"
        jump ch04_matt_area_1
    label ch04_hammer:
        screen clickable_chapter_four_hammer:
            imagebutton:
                pos (0, 0)
                idle "images/chapter_four/ch04_hammer.png"
                hover "images/chapter_four/ch04_hammer.png"
                action Call("ch04_get_hammer")
        label ch04_get_hammer:
            call chapter_four_matt_hide_screens
            "You have received a hammer!"#TODO: text and anything here
            $ chapter_four_obtain_item("matt_hammer")
            call chapter_four_matt_restore_screens
            return
    label ch04_toni:
        screen clickable_chapter_four_toni:
            imagebutton:
                pos (0,0)
                idle "images/chapter_four/ch04_toni.jpg"
                hover "images/chapter_four/ch04_toni.jpg"
                action Call("ch04_toni_bed")
        label ch04_toni_bed:
            call chapter_four_matt_hide_screens
            show ch04_toni:
                subpixel
            mt "TONIIIIIIIIIIII"
            toni "whats good homes"
            mt "WHY ARE YOU IN MY HOUSE?!?!"
            toni "lets just say"
            toni "I was going to pound town"
            toni "and the only resident of that town is your mother"
            toni "and im the new resident"
            mt "WHATTTTTTTTTTTTTTTTTTTTTT"
            "wow that was so mature"
            "We put a your mom joke in 2026"
            "Im blaming carl"
            carl "ITS NOT MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe"
            $ chapter_four_obtain_item("matt_lockpick")
            call chapter_four_matt_restore_screens
            return