# The labels and functions for the Fnaf Code in Chapter Three, since my brain cannot handle scrolling up and down for so long and the tabs keep resetting
screen ch03_fnaf_map():
    imagemap:
        ground "images/ch03_fnaf_map.png" pos (1423, 13) at Transform(zoom=1.1)
        hotspot(202,309,43,105) action Jump("ch03_fnaf_office")
        hotspot(140,320,60,40)  action Jump("ch03_fnaf_2b")
        hotspot(257,321,60,40)  action Jump("ch03_fnaf_4b")
        hotspot(361,235,60,40)  action Jump("ch03_fnaf_6")
        hotspot(45,254,60,40)   action Jump("ch03_fnaf_3")
        hotspot(115,60,60,40)   action Jump("ch03_fnaf_1b")
        hotspot(137,0,60,40)    action Jump("ch03_fnaf_1a")
        hotspot(1,92,60,40)     action Jump("ch03_fnaf_5")
        hotspot(80,146,60,40)   action Jump("ch03_fnaf_1c")
        hotspot(371,91,60,40)   action Jump("ch03_fnaf_7")
        hotspot(137,274,60,40)  action Jump("ch03_fnaf_2a")
        hotspot(254,275,60,40)  action Jump("ch03_fnaf_4a")
screen ch03_fnaf_stage():
    imagemap:
        ground "images/ch03_fnaf7.png" at Transform(yzoom=1.25,zoom=1.2)
        hotspot(258,0,300,720)  action Call("chapter_three_bonnie")
        hotspot(727,0,280,720)  action Call("chapter_three_chica")
        hotspot(1125,0,300,729) action Call("chapter_three_freddy")

label chapter_three_fnaf_hide_screens:
    hide screen clickable_chapter_three_chica1_flour
    hide screen clickable_chapter_three_chica1_yeast
    hide screen clickable_chapter_three_chica1_water
    hide screen clickable_chapter_three_chica1_salt
    hide screen clickable_chapter_three_chica1_sugar
    hide screen clickable_chapter_three_chica1_cornmeal
    hide screen clickable_chapter_three_chica1_garlic
    hide screen clickable_chapter_three_chica1_wheat_flour
    hide screen clickable_chapter_three_chica1_cheese
    hide screen clickable_chapter_three_chica1_pepperoni
    hide screen clickable_chapter_three_chica1_olive_oil
    hide screen ch03_fnaf_map
    hide screen ch03_fnaf_stage
    return

label chapter_three_fnaf_restore_screens(location):
    if location == 1:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_flour"):
            show screen clickable_chapter_three_chica1_flour
    elif location == 2:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_yeast"):
            show screen clickable_chapter_three_chica1_yeast
    elif location == 3:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_water"):
            show screen clickable_chapter_three_chica1_water
    elif location == 4:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_salt"):
            show screen clickable_chapter_three_chica1_salt
    elif location == 5:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_sugar"):
            show screen clickable_chapter_three_chica1_sugar
    elif location == 6:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_cornmeal"):
            show screen clickable_chapter_three_chica1_cornmeal
    elif location == 7:
        show screen ch03_fnaf_stage
    elif location == 8:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_wheat"):
            show screen clickable_chapter_three_chica1_wheat_flour
    elif location == 9:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_cheese"):
            show screen clickable_chapter_three_chica1_cheese
    elif location == 10:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_pepperoni"):
            show screen clickable_chapter_three_chica1_pepperoni
    elif location == 11:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_olive_oil"):
            show screen clickable_chapter_three_chica1_olive_oil
    elif location == 12:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_garlic"):
            show screen clickable_chapter_three_chica1_garlic
    show screen ch03_fnaf_map
    return

label chapter_three_screen_control(location):
    call chapter_three_fnaf_hide_screens
    call chapter_three_fnaf_restore_screens(location)
    return


screen chapter_three_office_timer(max, endup):
    frame:
        xalign 0.5
        yalign 0.0
        hbox:
            timer 0.1 action If(time > max, false = SetVariable("time", time + 0.1), true = [Hide("chapter_three_office_timer"), SetVariable("time", 0), Jump("%s"%endup) ]) repeat True
            bar: #an animated bar top center screen
                value AnimatedValue(value=time, range=max, delay= 0.5)
                xalign 0.0
                yalign 0.0
                xmaximum 200

label chapter_three_phone_time:
    show ch03_telephone:
        subpixel True pos (626, 228) zoom 0.83 
    k "Woah is that a payphone?"
    k "this shit must be from like the 14th century"
    k "gotta be like older than Thang!"
    k "alright let's turn this shit on"
    k "..."
    k "..."
    k "..."
    k "how do i use this phone..."
    k "i dont got thang here"
    "Okay so put your finger in the digit you want to dial"
    k "okay i put it in 9"
    "Now rotate it to the end"
    k "okay..."
    "now repeat"
    k "thanks narrator from the stanley parable"
    "I don't wanna see here for 45 minutes watching you struggle"
    k "alright I think I got it"
    k "listen up chat"
    show screen chapter_three_office_timer(285,"chapter_three_secret2")
    play sound "audio/sound/chapter_three/ch03_phone_call.ogg"
    pause 120
    k "I learned literally nothing from this shit"
    label ch03_office_timer_return:
    stop sound
    hide screen chapter_three_office_timer
    hide ch03_telephone
    $ chapter_three_obtain_item("chapter_three_phonecall")
    return
label chapter_three_secret2:
    "WOW YOU ARE INCREDIBLE"
    #$ print("Length:", len(chapter_three_secret))
    #"a"
    $ chapter_three_secret[1] = True
    jump ch03_office_timer_return
label chapter_three_bonnie:
    call chapter_three_fnaf_hide_screens
    "test1"
    return
label chapter_three_chica:
    call chapter_three_fnaf_hide_screens
    if Chica.get_happiness() == 0 and chapter_three_item_check("chapter_three_flour") and chapter_three_item_check("chapter_three_yeast") and chapter_three_item_check("chapter_three_water") and chapter_three_item_check("chapter_three_salt") and chapter_three_item_check("chapter_three_sugar") and chapter_three_item_check("chapter_three_cornmeal") and chapter_three_item_check("chapter_three_garlic") and chapter_three_item_check("chapter_three_wheat") and chapter_three_item_check("chapter_three_cheese") and chapter_three_item_check("chapter_three_pepperoni") and chapter_three_item_check("chapter_three_olive_oil"):
        k "wait..."
        k "This isn't a pizza..."
        k "This is just ingredients..."
        chica "FOOD!"
        k "wait!"
        k "This isn't edible, its just ingredients"
        chica "nah this is FOOD FOR ME!" #TODO: put eat thingy here

        chica "wow that was some good food"
        "A Small Bond has been formed with Chica"
        $ Chica.set_happiness(1)
        $ Chica.set_mission(False)
    if Chica.get_happiness() == 0 and not Chica.get_mission():
        chica "I am hungermaxxing"
        k "YOOOOOOO ME TOOOO"
        chica "get me some food pls"
        k "NAHHHHHHHHHHHHHHHHHHHHHHHH"
        chica "pls you don't do that to a lady"
        k "(WAIT SHE IS A GIRL?)"
        k "oh of course ml'lady"
        k "anything for the female gender"
        k "what would you like?"
        chica "PIZZA!!"
        k "where do i get that"
        chica "make your own, its a pizza restaurant"
        k "damn"
        "Mission Unlocked: Make Chica Pizza!"
        $ Chica.set_mission(True)
    elif Chica.get_happiness() == 0 and Chica.get_mission():
        chica "I AM WAITING FOR MY PIZZA!"
        k "SHEESH I WILL GET YOUR PIZZA YOU BITCH!"
        chica "EXCUSE ME?"
        k "uhhh I mean you best lady?"
        chica "that's what I thought!"
        chica "HMP!"
    return
label chapter_three_freddy:
    call chapter_three_fnaf_hide_screens
    "test3"
    return





label chapter_three_chica_mission1:
    screen clickable_chapter_three_chica1_flour:
        imagebutton:
            pos (333, 275) 
            at Transform(zoom=0.61)
            idle  "images/ch03_fnaf_flour.png"
            hover "images/ch03_fnaf_flour.png"
            action Call("chapter_three_ingredients",1)
    screen clickable_chapter_three_chica1_yeast:
        imagebutton:
            pos (1661, 715) at Transform(zoom=0.36)
            idle "images/ch03_fnaf_yeast.png"
            hover "images/ch03_fnaf_yeast.png"
            action Call("chapter_three_ingredients",2)
    screen clickable_chapter_three_chica1_water:
        imagebutton:
            pos (775, 565) at Transform(zoom=0.43)
            idle "images/ch03_fnaf_water.png"
            hover "images/ch03_fnaf_water.png"
            action Call("chapter_three_ingredients",3)
    screen clickable_chapter_three_chica1_olive_oil:
        imagebutton:
            pos (1046, 218) at Transform(zoom=0.12)
            idle "images/ch03_fnaf_olive_oil.png"
            hover "images/ch03_fnaf_olive_oil.png"
            action Call("chapter_three_ingredients",4)
    screen clickable_chapter_three_chica1_salt:
        imagebutton:
            pos (506, 515) at Transform(zoom=0.1) 
            idle "images/ch03_fnaf_salt.png"
            hover "images/ch03_fnaf_salt.png"
            action Call("chapter_three_ingredients",5)
    screen clickable_chapter_three_chica1_sugar:
        imagebutton:
            pos (826, 505) at Transform(zoom=0.49) 
            idle "images/ch03_fnaf_sugar.png"
            hover "images/ch03_fnaf_sugar.png"
            action Call("chapter_three_ingredients",6)
    screen clickable_chapter_three_chica1_cornmeal:
        imagebutton:
            pos (541, 145) at Transform(zoom=0.43) 
            idle "images/ch03_fnaf_cornmeal.png"
            hover "images/ch03_fnaf_cornmeal.png"
            action Call("chapter_three_ingredients",7)
    screen clickable_chapter_three_chica1_garlic:
        imagebutton:
            pos (0, 0)
            idle "images/ch03_fnaf_garlic.png"
            hover "images/ch03_fnaf_garlic.png"
            action Call("chapter_three_ingredients",8)
    screen clickable_chapter_three_chica1_wheat_flour:
        imagebutton:
            pos (-55, 786) at Transform(zoom=0.25) 
            idle "images/ch03_fnaf_wheat_flour.png"
            hover "images/ch03_fnaf_wheat_flour.png"
            action Call("chapter_three_ingredients",9)
    screen clickable_chapter_three_chica1_cheese:
        imagebutton:
            pos (0, 0) at Transform(zoom=0.09)
            idle "images/ch03_fnaf_cheese.png"
            hover "images/ch03_fnaf_cheese.png"
            action Call("chapter_three_ingredients",10)
    screen clickable_chapter_three_chica1_pepperoni:
        imagebutton:
            pos (686, 283) at Transform(zoom=0.34, rotate=-36.0)
            idle "images/ch03_fnaf_pepperoni.png"
            hover "images/ch03_fnaf_pepperoni.png"
            action Call("chapter_three_ingredients",11)

        
    label chapter_three_ingredients(area):
        call chapter_three_fnaf_hide_screens
        if area == 1:
            "You have obtained Flour!"
            $ chapter_three_obtain_item("chapter_three_flour")
        if area == 2:
            "You have obtained Yeast!"
            $ chapter_three_obtain_item("chapter_three_yeast")
        if area == 3:
            "You have obtained Water!"
            $ chapter_three_obtain_item("chapter_three_water")
        if area == 4:
            "You have obtained Olive Oil!"
            $ chapter_three_obtain_item("chapter_three_olive_oil")
        if area == 5:
            "You have obtained Salt"
            $ chapter_three_obtain_item("chapter_three_salt")
        if area == 6:
            "You have obtained Sugar!"
            $ chapter_three_obtain_item("chapter_three_sugar")
        if area == 7:
            "You have obtained Cornmeal!"
            $ chapter_three_obtain_item("chapter_three_cornmeal")
        if area == 8:
            "You have obtained Garlic!"
            $ chapter_three_obtain_item("chapter_three_garlic")
        if area == 9:
            "You have obtained Wheat Flour!!"
            $ chapter_three_obtain_item("chapter_three_wheat")
        if area == 10:
            "You have obtained Cheese!"
            $ chapter_three_obtain_item("chapter_three_cheese")
        if area == 11:
            "You have obtained Pepperoni"
            $ chapter_three_obtain_item("chapter_three_pepperoni")
        return