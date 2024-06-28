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
screen ch03_fnaf_stage_no_chica():
    imagemap:
        ground "images/ch03_fnaf7_no_chica.png" at Transform(yzoom=1.25, zoom=1.92)
        hotspot(150,0,230,448)  action Call("chapter_three_bonnie")
        # hotspot(727,0,280,720)  action Call("chapter_three_chica")
        hotspot(630,0,320,448) action Call("chapter_three_freddy")
screen ch03_fnaf_stage_no_bonnie():
    imagemap:
        ground "images/ch03_fnaf7_no_bonnie.png" at Transform(yzoom=1.25, zoom=1.92)
        #hotspot(150,0,230,448)  action Call("chapter_three_bonnie")
        hotspot(440,0,160,448)  action Call("chapter_three_chica")
        hotspot(630,0,320,448) action Call("chapter_three_freddy")
screen ch03_fnaf_stage_only_freddy():
    imagemap:
        ground "images/ch03_fnaf7_only_freddy.png" at Transform(yzoom=1.25, zoom=1.92)
        #hotspot(150,0,230,448)  action Call("chapter_three_bonnie")
        #hotspot(440,0,160,448)  action Call("chapter_three_chica")
        hotspot(630,0,320,448) action Call("chapter_three_freddy")
screen ch03_fnaf_closet_bonnie():
    imagemap:
        ground "images/ch03_fnaf5_bonnie.png" at Transform(yzoom=1.25, zoom=1.92)
        hotspot(25,90,400,280) action Call("chapter_three_closet_bonnie")
label chapter_three_fnaf_hide_screens:
    hide screen clickable_chapter_three_bonnie1_telephone
    hide screen ch03_fnaf_closet_bonnie
    hide screen ch03_fnaf_stage_no_bonnie
    hide screen ch03_fnaf_stage_only_freddy
    hide screen chapter_three_chica_health_bar
    hide screen clickable_chapter_three_chica3_cupcakes
    hide screen clickable_chapter_three_chica3_dining_area
    hide screen clickable_chapter_three_chica2_landline
    hide screen clickable_chapter_three_chica2_quarter
    hide screen clickable_chapter_three_chica2_1bill
    hide screen clickable_chapter_three_chica2_5bill
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
    hide screen ch03_fnaf_stage_no_chica
    return

label chapter_three_fnaf_restore_screens(location):
    if location == 1:
        if Bonnie.get_happiness() == 0 and Bonnie.get_mission() and choice == 100:
            show screen clickable_chapter_three_bonnie1_telephone
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_flour"):
            show screen clickable_chapter_three_chica1_flour
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[2]:
            show screen clickable_chapter_three_chica2_1bill(635,518,0.4,2)
    elif location == 2:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_yeast"):
            show screen clickable_chapter_three_chica1_yeast
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[3]:
            show screen clickable_chapter_three_chica2_1bill(431,616,0.33,3)
    elif location == 3:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_water"):
            show screen clickable_chapter_three_chica1_water
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[4]:
            show screen clickable_chapter_three_chica2_1bill(1003,593,0.45,4)
    elif location == 4:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_salt"):
            show screen clickable_chapter_three_chica1_salt
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[1]:
            show screen clickable_chapter_three_chica2_5bill(695,496,0.41,1)
    elif location == 5:
        if Bonnie.get_happiness() == 0 and Bonnie.get_mission:
            show screen ch03_fnaf_closet_bonnie
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_sugar"):
            show screen clickable_chapter_three_chica1_sugar
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[7]:
            show screen clickable_chapter_three_chica2_1bill(635,518,0.4,7)
    elif location == 6:
        if Chica.get_happiness() == 2 and not Chica.get_mission():
            show screen clickable_chapter_three_chica3_dining_area
        elif Chica.get_mission() and not chapter_three_item_check("chapter_three_cornmeal"):
            show screen clickable_chapter_three_chica1_cornmeal
        elif Chica.get_happiness() == 1 and Chica.get_mission() and count2 >= 10.00 and not chapter_three_item_check("chapter_three_pizza2"):
            show screen clickable_chapter_three_chica2_landline
    elif location == 7:
        if Bonnie.get_happiness() == 0 and Bonnie.get_mission() and Chica.get_happiness() == 2 and not Chica.get_mission():
            show screen ch03_fnaf_stage_only_freddy
        elif Bonnie.get_happiness() == 0 and Bonnie.get_mission():
            show screen ch03_fnaf_stage_no_bonnie
        elif Chica.get_happiness() == 2 and not Chica.get_mission():
            show screen ch03_fnaf_stage_no_chica
        else:
            show screen ch03_fnaf_stage
    elif location == 8:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_wheat"):
            show screen clickable_chapter_three_chica1_wheat_flour
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[0]:
            show screen clickable_chapter_three_chica2_5bill(936,583,0.26,0)
    elif location == 9:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_cheese"):
            show screen clickable_chapter_three_chica1_cheese
    elif location == 10:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_pepperoni"):
            show screen clickable_chapter_three_chica1_pepperoni
    elif location == 11:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_olive_oil"):
            show screen clickable_chapter_three_chica1_olive_oil
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[6]:
            show screen clickable_chapter_three_chica2_1bill(635,518,0.4,6)
    elif location == 12:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_garlic"):
            show screen clickable_chapter_three_chica1_garlic
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[5]:
            show screen clickable_chapter_three_chica2_1bill(635,518,0.4,5)
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
    if Bonnie.get_happiness() == 0 and not Bonnie.get_mission():
        bonnie "yo yo yo what is good little child"
        k "I am 14"
        bonnie "oh perfect!"
        k "Am i getting groomed"
        bonnie "no thats freddy"
        bonnie "I need your help with something"
        k "okay?"
        k "What do you need help with?"
        bonnie "I am really embarrassed so we should meet somewhere else"
        k "okay where?"
        bonnie "A true looksmaxxer will know where to find me!"
        k "I am a true looksmaxxer but I got no idea where you are going..."
        $ Bonnie.set_mission(True)
    return
label chapter_three_chica:
    call chapter_three_fnaf_hide_screens
    if Chica.get_happiness() == 3:
        chica "Thanks for what you have done for me :)"
        "You feel you cannot help Chica anymore"
        "You have done everything you could have!"
    elif Chica.get_happiness() == 2 and Chica.get_mission():
        chica "That was a close fight"
        k "yeah it was and I straight up d-d-destroyed you"
        chica "well I am still hungry"
        k "fuck off"
        chica "I am kidding"
        "A life-long bond with Chica has been formed!"
        $ Chica.set_happiness(3)
        k "Oh shit I rizzed up another girl"
        chica "I am lesbian"
        k "NEVERMIND!"  
    elif Chica.get_happiness() == 1 and Chica.get_mission() and chapter_three_item_check("chapter_three_pizza2"):
        chica "Damn that smells good!"
        k "yeah its a really good pizza" #TODO: pizza eating stuff here
        chica "that was a good pizza tysm :)"
        "Your bond with Chica has grown even stronger!"
        $ Chica.set_happiness(2)
        $ count2 = 0
        $ Chica.set_mission(False)
        "Mission Completed: Order Chica a Pizza!"
    elif Chica.get_happiness() == 1 and Chica.get_mission():
        chica "I AM FUCKING HUNGRY"
        chica "GET ME MY FUCKING PIZZA!"
        k "jesus woman"
        k "leave me alone!"
    elif Chica.get_happiness() == 1 and not Chica.get_mission():
        chica "That pizza was UNDERCOOKED!"
        k "well yeah"
        k "I didn't make a pizza..."
        k "I just gave the raw ingredients"
        chica "You clearly SUCK at making pizzas"
        chica "I want you to go order one"
        k "Oh that's easy, they are like 9.99 for one"
        "..."
        k "wait"
        k "I have no money"
        k "That's the whole point of me getting a job"
        k "Do you have money chica?"
        chica "I am an animatronic in a rundown rizzaria"
        chica "what do you think?"
        k "yes"
        chica "..."
        k "Okay I will go find money"
        "Mission Unlocked: Order Chica a Pizza!"
        $ Chica.set_mission(True)
        $ count2 = 0
    elif Chica.get_happiness() == 0 and chapter_three_item_check("chapter_three_flour") and chapter_three_item_check("chapter_three_yeast") and chapter_three_item_check("chapter_three_water") and chapter_three_item_check("chapter_three_salt") and chapter_three_item_check("chapter_three_sugar") and chapter_three_item_check("chapter_three_cornmeal") and chapter_three_item_check("chapter_three_garlic") and chapter_three_item_check("chapter_three_wheat") and chapter_three_item_check("chapter_three_cheese") and chapter_three_item_check("chapter_three_pepperoni") and chapter_three_item_check("chapter_three_olive_oil"):
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
        "Mission Completed: Make Chica Pizza!"
    elif Chica.get_happiness() == 0 and not Chica.get_mission():
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
    else:
        chica "I AM HUNGRY!"
        k "got it!"
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
label chapter_three_chica_mission2:
    screen clickable_chapter_three_chica2_5bill(xpos,ypos,zoomlevel,id):
        imagebutton:
            pos(xpos,ypos) at Transform(zoom = zoomlevel)
            idle "images/ch03_fnaf_5bill.png"
            hover "images/ch03_fnaf_5bill.png"
            action Call("chapter_three_fnaf_bill5",id)
    screen clickable_chapter_three_chica2_1bill(xpos,ypos,zoomlevel,id):
        imagebutton:
            pos(xpos,ypos) at Transform(zoom = zoomlevel)
            idle "images/ch03_fnaf_1bill.png"
            hover "images/ch03_fnaf_1bill.png"
            action Call("chapter_three_fnaf_bill1",id)
    screen clickable_chapter_three_chica2_quarter(xpos,ypos,zoomlevel,id):
        imagebutton:
            pos(xpos,ypos) at Transform(zoom = zoomlevel)
            idle "images/ch03_fnaf_quarter.png"
            hover "images/ch03_fnaf_quarter.png"
            action Call("chapter_three_fnaf_quarter",id)
    screen clickable_chapter_three_chica2_landline():
        imagebutton:
            pos (775, 145) at Transform(zoom=0.49)
            idle "images/ch03_fnaf_landline.png"
            hover "images/ch03_fnaf_landline.png"
            action Call("chapter_three_landline")

    label chapter_three_fnaf_bill5(id_value):
        "You have found a 5 Dollar Bill!"
        $ count2 += 5.00
        $ chapter_three_fnaf_money[id_value] = True
        return
    label chapter_three_fnaf_bill1(id_value):
        "You have found a 1 Dollar Bill!"
        $ count2 += 1.00
        $ chapter_three_fnaf_money[id_value] = True
        return
    label chapter_three_fnaf_quarter(id_value):
        "You have found a 0.25 Dollar Bill!"
        k "Isn't that just a quarter?"
        $ count2 += 0.25
        $ chapter_three_fnaf_money[id_value] = True
        return
    label chapter_three_landline:
        call chapter_three_fnaf_hide_screens
        #todo put mario elevator music
        k "Alright Let's order this pizza!"
        #Todo ring sound here
        fnafpg "Uh hello!"
        k "Uh hi"
        k "Can I have a large Pepperoni pizza w/ extra cheese tomato mustard mayo pepsi and water"
        k "with some pineapple"
        fnafpg "uh yeah that will be 9.99 for here or to go?"
        k "Uh i need it delivered to Freddy Fazgyatt's Rizzaria"
        fnafpg "..."
        fnafpg "I will not be taking prank-phone calls"
        k "no this isn't a prank phone call, I really need a pizza, i got the cash here!"
        fnafpg "ugh fine"
        fnafpg "be there in 5"
        pause 300

        show ch03_fnaf_delivery with dissolve:
            subpixel True zoom 0.75 
        show ch03_fnaf_delivery_guy:
            subpixel True pos (508, 31) zoom 0.49 


        k "Uh hi can I have my pizza?"
        fnafpg "Uh that will be 9.99"
        k "here you go"
        fnafpg "This is not enough"
        k "I gave you 10 dollars worth?"
        fnafpg "Tax bro"
        fnafpg "This is canada where we got 50%% taxes"
        k "why did you accept usd?"
        fnafpg "meh its money and usd is better than cad"
        fnafpg "later bozo"
        $ chapter_three_obtain_item("chapter_three_pizza2")
        "You have obtained a pizza!"
        scene ch03_fnaf6 with dissolve:
            subpixel True yzoom 1.25 zoom 1.5 
        return
label chapter_three_chica_mission3:
    screen clickable_chapter_three_chica3_dining_area:
        imagebutton:
            pos (320, 90) at Transform(zoom=0.72)
            idle "images/ch03_fnaf_wchica.png" 
            hover "images/ch03_fnaf_wchica.png"
            action Jump("chapter_three_chica_fight")
    screen chapter_three_chica_health_bar(max,endup):
        frame:
            xalign 0.5
            yalign 0.0
            hbox:
                bar:
                    value AnimatedValue(count2, 25, delay = 0.5)
                    xalign 0.0
                    yalign 0.0
                    xmaximum 200
    screen clickable_chapter_three_chica3_cupcakes(xpos,ypos,zoom,count2):
        timer 0.25 + (count2 / 10) action Call("chapter_three_chica_death",xpos,ypos)
        imagebutton:
            pos (xpos,ypos) at Transform(zoom = zoom)
            idle "images/ch03_fnaf_cupcake.png"
            hover "images/ch03_fnaf_cupcake.png"
            action [
                #SetVariable("count2", count2-1),
                Hide("clickable_chapter_three_chica3_cupcakes"),
                #Return()
            ]
    label chapter_three_chica_fight:
        call chapter_three_fnaf_hide_screens
        show ch03_fnaf_wchica:
            subpixel True pos (320, 90) zoom 0.72
        k "Why are you here?"
        chica "FUCK OFF KODY FUCKBOY"
        k "Huh What did I do?"
        $ count2 = 25
        scene ch03_fnaf_chica_fight:
            subpixel True yzoom 1.05 zoom 2.61
        chica "F"
        chica "I"
        chica "G"
        chica "H"
        chica "T"
        chica " "
        chica "M"
        chica "E"
        k "That was so unneccessary, get ready to get decked!"
        show screen chapter_three_chica_health_bar(26.25,"chapter_three_chica_victory")
        while count2 > 0:
            if count2 == 17:
                chica "Ow!"
                chica "That hurts!"
                window auto hide
            elif count2 == 10:
                chica "Yowch!"
                chica "Speed up the cupcakes!"
                window auto hide
            $ randint = renpy.random.randint(330,1500) # X-Value
            $ randint2 = renpy.random.randint(400,750) # Y-Value
            show screen clickable_chapter_three_chica3_cupcakes(randint,randint2,1.0,count2)
            $ count2 -= 1
            $ renpy.pause(delay = 0.25 + (count2/10), hard=True)
        label chapter_three_chica_victory:
        chica "OW!"
        chica "WTF!"
        chica "Okay I concede!"
        chica "Im going back to stage!"
        $ Chica.set_mission(True)
        jump ch03_fnaf_1b
    
    label chapter_three_chica_death(xpos,ypos):
        #explosion sfx here
        "TOO SLOW!"
        show ch03_fnaf_explosion with dissolve:
            subpixel True pos(xpos, ypos)
        pause 1.0
        call chapter_three_fnaf_hide_screens
        jump game_over
label chapter_three_bonnie_mission1:
    label chapter_three_closet_bonnie:
        call chapter_three_fnaf_hide_screens
        if choice == 0 and not chapter_three_item_check("chapter_three_drip"):
            bonnie "ah you made it"
            k "So what is it you want to discuss with me?"
            k "a 14-year old child?"
            bonnie "Okay so I got this comment on my tiktok"
            bonnie "and it says that I fell off and I am not the looksmaxxing goat"
            bonnie "comment is from CodyDaBoss"
            bonnie "Ima hurt that guy if I see him ever"
            k "huh"
            k "well how do I help you?"
            bonnie "I need me some new drop but I cannot operate the phone"
            bonnie "get me some new gucci and drop so I can looksmaxx with Kai Cenat better"
            k "I dont got money"
            bonnie "I got a $100 dollar bill so just order me what you thinkmaxx willmaxx looksmaxx memaxx"
            k "gotmaxx itmaxx bossmax"
            $ choice = 100
        elif choice != 0 and not chapter_three_item_check("chapter_three_drip"):
            bonnie "GET ME MY DRIPMAXX!"
            k "okay man jesus"
        elif choice != 0 and chapter_three_item_check("chapter_three_drip"):
            bonnie "thanks man"
            $ Bonnie.set_happiness(1)
            "A small bond has been formed with Bonnie!"
            bonnie "Thanks for the fit man!"
            if rngint > 11:
                "Wow you got more than 1 item!"
                "Incredible!"
                $ chapter_three_secret[2] = True
        return
    screen clickable_chapter_three_bonnie1_telephone:
        imagebutton:
            pos (640, 328) at Transform(zoom=0.64)
            idle "images/ch03_fnaf_landline.png"
            hover "images/ch03_fnaf_landline.png" 
            action Call("Chapter_three_office_driporder")
    label Chapter_three_office_driporder:
        call chapter_three_fnaf_hide_screens
        show ch03_fnaf_landline:
            pos (640, 328) zoom 0.64
        k "Alright I got a lot of choices for drip here" #TODO:Audio for a phonecall
        questionmark "Uh hello Hello"
        questionmark "I am Henry from Looksmaxxers United"
        questionmark "How Can I help you today?"
        k "I want the best drip to ever drip around this part of the canada/us mix we are going for"
        questionmark "got it sir!"
        $ rngint = 0
        while choice >= 0:
            menu:
                "Gucci Jacket": 
                    call chapter_three_drip_rng
                "Gucci Pants":
                    call chapter_three_drip_rng
                "Gucci Shoes":
                    call chapter_three_drip_rng
                "Gucci Hoodie":
                    call chapter_three_drip_rng
                "Supreme Jacket":
                    call chapter_three_drip_rng
                "Supreme Brick":
                    call chapter_three_drip_rng
                "Supreme Pants":
                    call chapter_three_drip_rng
                "Kenzo Shirt":
                    call chapter_three_drip_rng
                "Kenzo Pants":
                    call chapter_three_drip_rng
                "A.P.C Bag":
                    call chapter_three_drip_rng
                "A.P.C Underwear":
                    call chapter_three_drip_rng
                "Billionaire Boyz Hat":
                    call chapter_three_drip_rng
                "Billionaire Boyz Pants":
                    call chapter_three_drip_rng
                "Palace Shirt":
                    call chapter_three_drip_rng
                "Palace Sweatpants":
                    call chapter_three_drip_rng
                "Palace Skateboard":
                    call chapter_three_drip_rng
                "Heron Preston Polo Shirt":
                    call chapter_three_drip_rng
                "Heron Preston Knitwear":
                    call chapter_three_drip_rng
                "Heron Preston Trousers":
                    call chapter_three_drip_rng
                "Heron Preston Beachwear":
                    call chapter_three_drip_rng
                "Faded Tracksuit":
                    call chapter_three_drip_rng
                "Faded Joggers":
                    call chapter_three_drip_rng
                "Faded Overshirts":
                    call chapter_three_drip_rng
                "Prada Bag":
                    call chapter_three_drip_rng
                "Haven Shoes":
                    call chapter_three_drip_rng
                "Haven Hoodie":
                    call chapter_three_drip_rng
                "Haven Brick":
                    call chapter_three_drip_rng
                "Brooklyn Circus T-Shirt":
                    call chapter_three_drip_rng
                "Brooklyn Circus Jacket":
                    call chapter_three_drip_rng
                "Brooklyn Circus Cap":
                    call chapter_three_drip_rng
                "Brooklyn Circus Shoes":
                    call chapter_three_drip_rng
                "Brooklyn Circus Socks":
                    call chapter_three_drip_rng
                "Brooklyn Circus Accessories":
                    call chapter_three_drip_rng
                "Union Los Angeles Top":
                    call chapter_three_drip_rng
                "Union Los Angeles Footwear":
                    call chapter_three_drip_rng
                "Union Los Angeles Bottoms":
                    call chapter_three_drip_rng
                "Union Los Angeles Accessories":
                    call chapter_three_drip_rng
                "Balenciaga Shirt":
                    call chapter_three_drip_rng
                "Balenciaga Pants":
                    call chapter_three_drip_rng
                "Balenciaga Shoes":
                    call chapter_three_drip_rng
                "Balenciaga Jacket":
                    call chapter_three_drip_rng
                "Balenciaga Hat":
                    call chapter_three_drip_rng
                "Balenciaga Bag":
                    call chapter_three_drip_rng
                "Off-White Shirt":
                    call chapter_three_drip_rng
                "Off-White Pants":
                    call chapter_three_drip_rng
                "Off-White Shoes":
                    call chapter_three_drip_rng
                "Off-White Jacket":
                    call chapter_three_drip_rng
                "Off-White Hat":
                    call chapter_three_drip_rng
                "Off-White Bag":
                    call chapter_three_drip_rng
                "Bape Shirt":
                    call chapter_three_drip_rng
                "Bape Pants":
                    call chapter_three_drip_rng
                "Bape Shoes":
                    call chapter_three_drip_rng
                "Bape Hoodie":
                    call chapter_three_drip_rng
                "Bape Cap":
                    call chapter_three_drip_rng
                "Bape Accessories":
                    call chapter_three_drip_rng
                "Yeezy Shoes":
                    call chapter_three_drip_rng
                "Yeezy Hoodie":
                    call chapter_three_drip_rng
                "Yeezy Jacket":
                    call chapter_three_drip_rng
                "Yeezy Pants":
                    call chapter_three_drip_rng
                "Yeezy Accessories":
                    call chapter_three_drip_rng
                "Fear of God Shirt":
                    call chapter_three_drip_rng
                "Fear of God Pants":
                    call chapter_three_drip_rng
                "Fear of God Shoes":
                    call chapter_three_drip_rng
                "Fear of God Jacket":
                    call chapter_three_drip_rng
                "Fear of God Hat":
                    call chapter_three_drip_rng
                "Fear of God Bag":
                    call chapter_three_drip_rng
                "Vetements Shirt":
                    call chapter_three_drip_rng
                "Vetements Pants":
                    call chapter_three_drip_rng
                "Vetements Shoes":
                    call chapter_three_drip_rng
                "Vetements Jacket":
                    call chapter_three_drip_rng
                "Vetements Hat":
                    call chapter_three_drip_rng
                "Vetements Bag":
                    call chapter_three_drip_rng
                "Alexander McQueen Shirt":
                    call chapter_three_drip_rng
                "Alexander McQueen Pants":
                    call chapter_three_drip_rng
                "Alexander McQueen Shoes":
                    call chapter_three_drip_rng
                "Alexander McQueen Jacket":
                    call chapter_three_drip_rng
                "Alexander McQueen Bag":
                    call chapter_three_drip_rng
                "Alexander McQueen Accessories":
                    call chapter_three_drip_rng
                "Saint Laurent Shirt":
                    call chapter_three_drip_rng
                "Saint Laurent Pants":
                    call chapter_three_drip_rng
                "Saint Laurent Shoes":
                    call chapter_three_drip_rng
                "Saint Laurent Jacket":
                    call chapter_three_drip_rng
                "Saint Laurent Bag":
                    call chapter_three_drip_rng
                "Saint Laurent Accessories":
                    call chapter_three_drip_rng
                "Givenchy Shirt":
                    call chapter_three_drip_rng
                "Givenchy Pants":
                    call chapter_three_drip_rng
                "Givenchy Shoes":
                    call chapter_three_drip_rng
                "Givenchy Jacket":
                    call chapter_three_drip_rng
                "Givenchy Bag":
                    call chapter_three_drip_rng
                "Givenchy Accessories":
                    call chapter_three_drip_rng
                "Versace Shirt":
                    call chapter_three_drip_rng
                "Versace Pants":
                    call chapter_three_drip_rng
                "Versace Shoes":
                    call chapter_three_drip_rng
                "Versace Jacket":
                    call chapter_three_drip_rng
                "Versace Bag":
                    call chapter_three_drip_rng
                "Versace Accessories":
                    call chapter_three_drip_rng
                "Louis Vuitton Shirt":
                    call chapter_three_drip_rng
                "Louis Vuitton Pants":
                    call chapter_three_drip_rng
                "Louis Vuitton Shoes":
                    call chapter_three_drip_rng
                "Louis Vuitton Jacket":
                    call chapter_three_drip_rng
                "Louis Vuitton Bag":
                    call chapter_three_drip_rng
                "Louis Vuitton Accessories":
                    call chapter_three_drip_rng
                "Burberry Shirt":
                    call chapter_three_drip_rng
                "Burberry Pants":
                    call chapter_three_drip_rng
                "Burberry Shoes":
                    call chapter_three_drip_rng
                "Burberry Jacket":
                    call chapter_three_drip_rng
                "Burberry Bag":
                    call chapter_three_drip_rng
                "Burberry Accessories":
                    call chapter_three_drip_rng
                "Tom Ford Shirt":
                    call chapter_three_drip_rng
                "Tom Ford Pants":
                    call chapter_three_drip_rng
                "Tom Ford Shoes":
                    call chapter_three_drip_rng
                "Tom Ford Jacket":
                    call chapter_three_drip_rng
                "Tom Ford Bag":
                    call chapter_three_drip_rng
                "Tom Ford Accessories":
                    call chapter_three_drip_rng
                "Raf Simons Shirt":
                    call chapter_three_drip_rng
                "Raf Simons Pants":
                    call chapter_three_drip_rng
                "Raf Simons Shoes":
                    call chapter_three_drip_rng
                "Raf Simons Jacket":
                    call chapter_three_drip_rng
                "Raf Simons Bag":
                    call chapter_three_drip_rng
                "Raf Simons Accessories":
                    call chapter_three_drip_rng
                "Maison Margiela Shirt":
                    call chapter_three_drip_rng
                "Maison Margiela Pants":
                    call chapter_three_drip_rng
                "Maison Margiela Shoes":
                    call chapter_three_drip_rng
                "Maison Margiela Jacket":
                    call chapter_three_drip_rng
                "Maison Margiela Bag":
                    call chapter_three_drip_rng
                "Maison Margiela Accessories":
                    call chapter_three_drip_rng
                "Rick Owens Shirt":
                    call chapter_three_drip_rng
                "Rick Owens Pants":
                    call chapter_three_drip_rng
                "Rick Owens Shoes":
                    call chapter_three_drip_rng
                "Rick Owens Jacket":
                    call chapter_three_drip_rng
                "Rick Owens Bag":
                    call chapter_three_drip_rng
                "Rick Owens Accessories":
                    call chapter_three_drip_rng
                "Dior Shirt":
                    call chapter_three_drip_rng
                "Dior Pants":
                    call chapter_three_drip_rng
                "Dior Shoes":
                    call chapter_three_drip_rng
                "Dior Jacket":
                    call chapter_three_drip_rng
                "Dior Bag":
                    call chapter_three_drip_rng
                "Dior Accessories":
                    call chapter_three_drip_rng
                "Valentino Shirt":
                    call chapter_three_drip_rng
                "Valentino Pants":
                    call chapter_three_drip_rng
                "Valentino Shoes":
                    call chapter_three_drip_rng
                "Valentino Jacket":
                    call chapter_three_drip_rng
                "Valentino Bag":
                    call chapter_three_drip_rng
                "Valentino Accessories":
                    call chapter_three_drip_rng
        return
    label chapter_three_drip_rng:
        $ rngint2 = renpy.random.randint(0,1000)
        $ rngint += renpy.random.randint(0,10)
        $ choice -= rngint2
        "You just spent [rngint2] on this..."
        "You have $[choice] remaining"
        $ chapter_three_obtain_item("chapter_three_drip")
        return