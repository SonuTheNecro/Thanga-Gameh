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
        hotspot(371,91,60,40)   action (Jump("ch03_fnaf_7") if chapter_three_item_check("chapter_three_key") else Call("chapter_three_locked"))
        hotspot(137,274,60,40)  action Jump("ch03_fnaf_2a")
        hotspot(254,275,60,40)  action Jump("ch03_fnaf_4a")
label chapter_three_locked:
    call chapter_three_fnaf_hide_screens
    "This area is currently locked!"
    k "WHAT!"
    call chapter_three_fnaf_restore_screens(location)
    return
screen ch03_fnaf_stage():
    imagemap:
        ground "images/ch03_fnaf7.png" at Transform(yzoom=1.25,zoom=1.2)
        hotspot(258,0,300,720)  action Jump("chapter_three_bonnie")
        hotspot(727,0,280,720)  action Jump("chapter_three_chica")
        hotspot(1125,0,300,729) action Jump("chapter_three_freddy")
screen ch03_fnaf_stage_no_chica():
    imagemap:
        ground "images/ch03_fnaf7_no_chica.png" at Transform(yzoom=1.25, zoom=1.92)
        hotspot(150,0,230,448)  action Jump("chapter_three_bonnie")
        # hotspot(727,0,280,720)  action Call("chapter_three_chica")
        hotspot(630,0,320,448) action Jump("chapter_three_freddy")
screen ch03_fnaf_stage_no_bonnie():
    imagemap:
        ground "images/ch03_fnaf7_no_bonnie.png" at Transform(yzoom=1.25, zoom=1.92)
        #hotspot(150,0,230,448)  action Call("chapter_three_bonnie")
        hotspot(440,0,160,448)  action Jump("chapter_three_chica")
        hotspot(630,0,320,448) action Jump("chapter_three_freddy")
screen ch03_fnaf_stage_only_freddy():
    imagemap:
        ground "images/ch03_fnaf7_only_freddy.png" at Transform(yzoom=1.25, zoom=1.92)
        #hotspot(150,0,230,448)  action Call("chapter_three_bonnie")
        #hotspot(440,0,160,448)  action Call("chapter_three_chica")
        hotspot(630,0,320,448) action Jumpl("chapter_three_freddy")
screen ch03_fnaf_closet_bonnie():
    imagemap:
        ground "images/ch03_fnaf5_bonnie.png" at Transform(yzoom=1.25, zoom=1.92)
        hotspot(25,90,400,280) action Jump("chapter_three_closet_bonnie")
label chapter_three_fnaf_hide_screens:
    hide screen clickable_chapter_three_foxy
    hide screen chapter_three_freddy_health_bar
    hide screen clickable_chapter_three_freddy3
    hide screen clickable_chapter_three_freddy2_bodypillow
    hide screen clickable_chapter_three_freddy1_gun
    hide screen clickable_chapter_three_freddy1_pills
    hide screen clickable_chapter_three_bonnie3
    hide screen clickable_chapter_three_bonnie2_skibidi_toilet
    hide screen clickable_chapter_three_bonnie2_guitar
    hide screen clickable_chapter_three_bonnie1_telephone
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
    hide screen clickable_chapter_three_key
    hide screen chapter_three_bonnie_health_bar
    hide screen chapter_three_chica_health_bar
    hide screen ch03_fnaf_closet_bonnie
    hide screen ch03_fnaf_stage_no_bonnie
    hide screen ch03_fnaf_stage_only_freddy
    hide screen ch03_fnaf_map
    hide screen ch03_fnaf_stage
    hide screen ch03_fnaf_stage_no_chica
    return

label chapter_three_fnaf_restore_screens(location):
    if location == 1:
        if Bonnie.get_happiness() == 2 and not Bonnie.get_mission():
            show screen clickable_chapter_three_bonnie3
        elif Bonnie.get_happiness() == 0 and Bonnie.get_mission() and choice == 100:
            show screen clickable_chapter_three_bonnie1_telephone
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_flour"):
            show screen clickable_chapter_three_chica1_flour
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[2]:
            show screen clickable_chapter_three_chica2_1bill(635,518,0.4,2)
    elif location == 2:
        if not chapter_three_item_check("chapter_three_key"):
            show screen clickable_chapter_three_key
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
        if Freddy.get_mission() and Freddy.get_happiness() == 1 and not chapter_three_item_check("chapter_three_bpillow"):
            show screen clickable_chapter_three_freddy2_bodypillow
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_salt"):
            show screen clickable_chapter_three_chica1_salt
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[1]:
            show screen clickable_chapter_three_chica2_5bill(695,496,0.41,1)
    elif location == 5:
        if Bonnie.get_happiness() == 0 and Bonnie.get_mission():
            show screen ch03_fnaf_closet_bonnie
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_sugar"):
            show screen clickable_chapter_three_chica1_sugar
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[7]:
            show screen clickable_chapter_three_chica2_1bill(635,518,0.4,7)
    elif location == 6:
        if Foxy.get_happiness() == 3 and Foxy.get_mission():
            show screen clickable_chapter_three_foxy
        if Bonnie.get_happiness() == 1 and Bonnie.get_mission() and not chapter_three_item_check("chapter_three_guitar"):
            show screen clickable_chapter_three_bonnie2_guitar
        if Chica.get_happiness() == 2 and not Chica.get_mission():
            show screen clickable_chapter_three_chica3_dining_area
        elif Chica.get_mission() and not chapter_three_item_check("chapter_three_cornmeal"):
            show screen clickable_chapter_three_chica1_cornmeal
        elif Chica.get_happiness() == 1 and Chica.get_mission() and count2 >= 10.00 and not chapter_three_item_check("chapter_three_pizza2"):
            show screen clickable_chapter_three_chica2_landline
    elif location == 7:
        if ((Bonnie.get_happiness() == 0 and Bonnie.get_mission()) or (Bonnie.get_happiness() == 2 and not Bonnie.get_mission())) and Chica.get_happiness() == 2 and not Chica.get_mission():
            show screen ch03_fnaf_stage_only_freddy
        elif (Bonnie.get_happiness() == 0 and Bonnie.get_mission()) or (Bonnie.get_happiness() == 2 and not Bonnie.get_mission()):
            show screen ch03_fnaf_stage_no_bonnie
        elif Chica.get_happiness() == 2 and not Chica.get_mission():
            show screen ch03_fnaf_stage_no_chica
        else:
            show screen ch03_fnaf_stage
    elif location == 8:
        if Freddy.get_happiness() == 0 and count >= 5 and not chapter_three_item_check("chapter_three_pills"):
            show screen clickable_chapter_three_freddy1_pills
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_wheat"):
            show screen clickable_chapter_three_chica1_wheat_flour
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[0]:
            show screen clickable_chapter_three_chica2_5bill(936,583,0.26,0)
    elif location == 9:
        if Foxy.get_happiness() == 3 and not Foxy.get_mission():
            call chapter_three_foxy3_talk
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_cheese"):
            show screen clickable_chapter_three_chica1_cheese
    elif location == 10:
        if Freddy.get_happiness() == 2 and not Freddy.get_mission():
            show screen clickable_chapter_three_freddy3
        if Bonnie.get_happiness() == 1 and Bonnie.get_mission(): # and not chapter_three_item_check("chapter_three_toilet") #idk if this should be one time event
            show screen clickable_chapter_three_bonnie2_skibidi_toilet
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_pepperoni"):
            show screen clickable_chapter_three_chica1_pepperoni
    elif location == 11:
        if Chica.get_mission() and not chapter_three_item_check("chapter_three_olive_oil"):
            show screen clickable_chapter_three_chica1_olive_oil
        elif Chica.get_happiness() == 1 and Chica.get_mission() and not chapter_three_fnaf_money[6]:
            show screen clickable_chapter_three_chica2_1bill(635,518,0.4,6)
    elif location == 12:
        if Freddy.get_mission() and Freddy.get_happiness() == 0 and count == 7 and not chapter_three_item_check("chapter_three_gun"):
            show screen clickable_chapter_three_freddy1_gun
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
    play sound "audio/sound/chapter_three/phone_ring1.ogg"
    k "alright I think I got it"
    k "listen up chat"
    show screen chapter_three_office_timer(285,"chapter_three_secret2")
    stop sound
    play sound "audio/sound/chapter_three/ch03_phone_call.ogg"
    pause 120
    k "I learned literally nothing from this shit"
    label ch03_office_timer_return:
    stop sound
    hide screen chapter_three_office_timer
    hide ch03_telephone
    $ chapter_three_obtain_item("chapter_three_phonecall")
    call chapter_three_fnaf_restore_screens(location)
    return
label chapter_three_secret2:
    "wait you actually listened to the whole thing?"
    "I Guess that\'s worth a secret I suppose..."
    $ chapter_three_secret[1] = True
    jump ch03_office_timer_return
label chapter_three_bonnie:
    call chapter_three_fnaf_hide_screens
    if Bonnie.get_happiness() == 3:
        bonnie "yo its the one true looksmaxxer"
        "You feel you cannot help Bonnie anymore"
        "You have done everything you could have!"
    elif Bonnie.get_happiness() == 2:
        k "I thought we were fighting to the death..."
        bonnie "we were til I saw the strength of your ability"
        bonnie "you are the truest looksmaxxer"
        k "LETS FUCKING GO TAKE THAT THANG"
        bonnie "there is no better looksmaxxer than you"
        bonnie "thank you for teaching me your ways"
        bonnie "little guy"
        k "ITS BIG GUY!"
        play sound "audio/sound/chapter_three/quest_complete.ogg"
        "A life-long bond with Bonnie has been formed!"
        $ Bonnie.set_happiness(3)
        k "so whats my prize?"
        bonnie "me not killing you"
        k "BUT I LITERALLY WON HUH?"
        bonnie "yeah let me turn down my speed timer and let's see what happens to you"
    elif Bonnie.get_happiness() == 1 and chapter_three_item_check("chapter_three_guitar"):
        bonnie "YOOOOOOOOOOO YOU FOUND MY GUITAR LITTLE GUY"
        k "Actually i am a tall guy"
        k "I practice my heightmaxxing"
        k "and of course my looksmaxxing"
        bonnie "oh of course little guy"
        play sound "audio/sound/chapter_three/quest_complete.ogg"
        "Your bond with Bonnie has grown even stronger!"
        "Mission Complete!: Get Bonnie's Guitar!"
        bonnie "however I am realizing we are both too AWESOME for this rizzaria"
        k "huh?"
        bonnie "come office 3:33 am on friday the 13th on a tuesday"
        k "that doesn't make any sense"
        bonnie "scaredmaxxing?"
        k "NO!"
        $ Bonnie.set_happiness(2)
        $ Bonnie.set_mission(False)
    elif Bonnie.get_happiness() == 1 and not Bonnie.get_mission():
        bonnie "Yo What is up man!"
        k "how is the dripgoing?"
        bonnie "My looksmaxxing is pretty good but my soundmaxxing is poor right now"
        k "wtf is soundmaxxing"
        bonnie "My guitar..."
        k "oh"
        bonnie "I need it"
        k "It is very clearly in your hands"
        bonnie "nono, this is my show guitar"
        bonnie "I need my real guitar"
        k "what?"
        bonnie "I don\'t make the rules [player_name]"
        k "ugh"
        k "well where is the fucking guitar..."
        bonnie "Well..."
        bonnie "Let me think here"
        pause 5
        bonnie "I got no idea"
        k "of course"
        bonnie "well go get me it!"
        "Mission Unlocked!: Get Bonnie's Guitar!"
        bonnie "make it snappy too"
        k "ugh..."
        $ Bonnie.set_mission(True)
    elif Bonnie.get_happiness() == 1 and Bonnie.get_mission():
        bonnie "Can you hurry up and get my good guitar"
        k "got it bossmaxx sir"
        bonnie "stop"
        k "stop what?"
        k "helping you or looksmaxxing"
        bonnie "the englishmaxxing"
        pause 2.76
        k "yeah okay I'll stop"
    elif Bonnie.get_happiness() == 0 and not Bonnie.get_mission():
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
        bonnie "Guess you aren't a true looksmaxxer"
        k "NO!"
        k "I AM A TRUE ONE"
        $ Bonnie.set_mission(True)
        "Mission Unlocked: Help Bonnie w/ Whatever He needs..."
    else:
        bonnie "looksmaxxing power 9999"
        k "jeepers"
    call chapter_three_fnaf_restore_screens(location)
    jump ch03_fnaf_1a
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
        k "yeah its a really good pizza"
        play sound "audio/sound/chapter_three/gulp1.ogg"
        pause 0.25
        play sound "audio/sound/chapter_three/gulp1.ogg"
        pause 0.25
        play sound "audio/sound/chapter_three/gulp1.ogg"
        pause 0.25
        chica "that was a good pizza tysm :)"
        play sound "audio/sound/chapter_three/quest_complete.ogg"
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
        chica "nah this is FOOD FOR ME!"
        play sound "audio/sound/chapter_three/gulp1.ogg"
        pause 0.25
        play sound "audio/sound/chapter_three/gulp1.ogg"
        pause 0.25
        play sound "audio/sound/chapter_three/gulp1.ogg"
        pause 0.25
        chica "wow that was some good food"
        play sound "audio/sound/chapter_three/quest_complete.ogg"
        "A Small Bond has been formed with Chica"
        $ Chica.set_happiness(1)
        $ Chica.set_mission(False)
        play sound "audio/sound/chapter_three/quest_complete.ogg"
        "Mission Completed: Make Chica Pizza!"
    elif Chica.get_happiness() == 0 and not Chica.get_mission():
        chica "I am hungermaxxing"
        k "YOOOOOOO ME TOOOO"
        chica "get me some food pls"
        k "NAHHHHHHHHHHHHHHHHHHHHHHHH"
        chica "pls you don't do that to a lady"
        k "(WAIT THAT IS A GIRL?)"
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
    call chapter_three_fnaf_restore_screens(location)
    jump ch03_fnaf_1a
label chapter_three_freddy:
    call chapter_three_fnaf_hide_screens
    if Freddy.get_happiness() == 3:
        freddy "thanks for helping me out!"
        "You feel you cannot help Freddy anymore"
        "You have done everything you could have!"
    elif Freddy.get_happiness() == 2 and Freddy.get_mission():
        k "You are a creep"
        freddy "Im good im good, I been listening to some men's help podcasts and Ima work my way outta this"
        k "well that's good"
        freddy "I appreciate your help little guy"
        play sound "audio/sound/chapter_three/quest_complete.ogg"
        "You have formed a deep life-long bond with Freddy!"
        k "STOPPPPPPPPPPPPPPPPPP"
        $ Freddy.set_happiness(3)
        k "So what podcast you listening to?"
        freddy "Andrew And Tristan Tate"
        k "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    elif Freddy.get_happiness() == 2 and not Freddy.get_mission():
        k "aren't you supposed to be in the bathroom"
        freddy "I can teleport at will"
        k "SINCE WHEN?"
        freddy "Since I did it in the OG fnaf markiplier run duh"
        k "WHAT THAT WAS A THING?"
        stn "YOU DIDN'T KNOW?"
        tv "WOW THIS BOZO!"
        t "LMAOOOOOOOOOOOO"
        b "WOWWWWWWW"
        k "wtf are these voices in my head"
        k "no one knows what you are talking about Freddy"
        freddy "cope"
    elif Freddy.get_happiness() == 1 and chapter_three_item_check("chapter_three_bpillow"):
        k "That is some NICE gyatt i cant even gonna cap"
        freddy "holy shit i am straight gooning to this!"
        freddy "thanks man"
        k "this seems way toooo easy..."
        play sound "audio/sound/chapter_three/quest_complete.ogg"
        "Mission Unlocked: Get Freddy some Gyatt!"
        k "that was the same dialogue as before, it should be completed"
        "You have formed a deep bond with Freddy!"
        k "What is happening to the game?"
        $ Freddy.set_happiness(2)
        $ Freddy.set_mission(False)
        freddy "You know what is next right?"
        freddy "I AM THE MASTER OF ALL GYATT"
        freddy "HAND IT OVER!"
        k "what?"
        freddy "YOUR GYATT!"
        k "uhhhhhh I dont wanna"
        freddy "Come bathroom 1v1"
        k "I dont think I will be going to the bathroom with a guy named Freddy Fazgyatt"
        freddy "Well the game demands it so come face me!"
        k "ugh"
    elif Freddy.get_happiness() == 1 and Freddy.get_mission():
        freddy "please bro"
        k "holy shit this gooner who is goonmaxxing"
        k "thats a new one narrator!"
        "fuck off"
    elif Freddy.get_happiness() == 1 and not Freddy.get_mission():
        k "How are you doing fweddy"
        freddy "okay :("
        k "what do you need help with now?"
        freddy "I need me some gyatt"
        k "I thought you had some based on it?"
        freddy "no i was the king but my gf took it all"
        k "where the hell do I find gyatt"
        freddy "idk"
        "Mission Unlocked!: Get Freddy some Gyatt!"
        $ Freddy.set_mission(True)
        k "this is stupid af"
    elif Freddy.get_happiness() == 0 and Freddy.get_mission() and chapter_three_item_check("chapter_three_pills"):
        k "here you go!"
        freddy "what is this?"
        k "its anti-depressent!"
        freddy "what do?"
        k "make you less sad!"
        freddy "okay i will try it"
        freddy "thank you :|"
        play sound "audio/sound/chapter_three/quest_complete.ogg"
        "A small bond has been formed with Freddy!"
        $ Freddy.set_happiness(1)
        $ Freddy.set_mission(False)
        "Misison Complete: Make Freddy happy!"
    elif Freddy.get_happiness() == 0 and Freddy.get_mission() and not chapter_three_item_check("chapter_three_pills"):
        freddy "Did you get anything to help me yet?"
        k "no sorry man not yet"
        freddy "please hurry :("
        freddy "I am big sad"
        k "ok man :)"
    elif Freddy.get_happiness() == 0 and not Freddy.get_mission() and count >= 5 and not chapter_three_item_check("chapter_three_pills"):
        freddy "what do you want from me"
        freddy ":("
        k "You look super sad man"
        k "I wanna help"
        freddy "why do you wanna help me"
        k "idk I just walk around and you are the only interactable on the map so might as well"
        freddy "my roblox gf left me :("
        k "YOOOOO YOU PLAY ROBLOX!?"
        k "me too!"
        k "what was her name?"
        freddy "her name was"
        freddy "codydaboss"
        k "oh"
        pause 1.5
        k "why don't you just get with one of the other animatronics"
        k "you already get shipped with them anyways"
        freddy "chicas lesbo and Bonnie is too awesome and Foxy is a fucking yiffer"
        k "truuuu"
        freddy "can you go find me something to cheer me up?"
        k "is this a sex joke or what?"
        freddy "depends on if your mind is in the gutter or not"
        "Misison Unlocked: Make Freddy happy?"
        $ Freddy.set_mission(True)
        k "idk either man"
    elif Freddy.get_happiness() == 0 and not Freddy.get_mission() and count < 5 and not count == 0:
        freddy "leave me alone man"
        $ count += 1
    elif Freddy.get_happiness() == 0 and not Freddy.get_mission():
        k "omg its the freddy five nights o mai gahd"
        freddy "..."
        k "freddy fazbear like"
        k "arf arf arf arf"
        k "jeepers"
        k "like toredaor march"
        freddy "stop"
        k "oh you can talk"
        k "fnaf freddy"
        freddy "Leave me alone..."
        k "ok man :("
        $ count = 1
    call chapter_three_fnaf_restore_screens(location)
    jump ch03_fnaf_1a
label chapter_three_foxy:
    if Freddy.get_happiness() == 3 and Bonnie.get_happiness() == 3 and Chica.get_happiness() == 3: #Could be better but I dont wanna do variable work
        $ Foxy.set_happiness(3)
    elif Freddy.get_happiness() >= 2 and Bonnie.get_happiness() >= 2 and Chica.get_happiness() >= 2:
        $ Foxy.set_happiness(2)
    elif Freddy.get_happiness() >= 1 and Bonnie.get_happiness() >= 1 and Chica.get_happiness() >= 1:
        $ Foxy.set_happiness(1)
    elif Freddy.get_happiness() == 0 and Bonnie.get_happiness() == 0 and Chica.get_happiness() == 0:
        $ Foxy.set_happiness(0)
    return

label chapter_three_music: #Controls the bkg music for the fnaf section in chapter_three, basic stuff
    $ rngint2 = renpy.random.randint(0,2)
    if rngint2 == 0:
        stop music
        play music "audio/music/chapter_three/fnaf_ambience1.ogg"
    elif rngint2 == 1:
        stop music
        play music "audio/music/chapter_three/fnaf_ambience2.ogg"
    else:
        stop music
        play music "audio/music/chapter_three/fnaf_ambience3.ogg"
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
        play sound "audio/sound/chapter_three/item_pickup.ogg"
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
        call chapter_three_fnaf_restore_screens(location)
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
        call chapter_three_fnaf_hide_screens
        play sound "audio/sound/chapter_three/item_pickup.ogg"
        "You have found a 5 Dollar Bill!"
        $ count2 += 5.00
        $ chapter_three_fnaf_money[id_value] = True
        call chapter_three_fnaf_restore_screens(location)
        return
    label chapter_three_fnaf_bill1(id_value):
        call chapter_three_fnaf_hide_screens
        play sound "audio/sound/chapter_three/item_pickup.ogg"
        "You have found a 1 Dollar Bill!"
        $ count2 += 1.00
        $ chapter_three_fnaf_money[id_value] = True
        call chapter_three_fnaf_restore_screens(location)
        return
    label chapter_three_fnaf_quarter(id_value):
        call chapter_three_fnaf_hide_screens
        play sound "audio/sound/chapter_three/item_pickup.ogg"
        "You have found a 0.25 Dollar Bill!"
        k "Isn't that just a quarter?"
        $ count2 += 0.25
        $ chapter_three_fnaf_money[id_value] = True
        call chapter_three_fnaf_restore_screens(location)
        return
    label chapter_three_landline:
        call chapter_three_fnaf_hide_screens
        if count2 == 16:
            "Wow you found all of the money!"
            $ chapter_three_secret[3] = True
        #todo put mario elevator music
        k "Alright Let's order this pizza!"
        play sound "audio/sound/chapter_three/phone_ring2.ogg"
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
        play sound "audio/sound/chapter_three/item_pickup.ogg"
        "You have obtained a pizza!"
        scene ch03_fnaf6 with dissolve:
            subpixel True yzoom 1.25 zoom 1.5 
        call chapter_three_fnaf_restore_screens(location)
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
                    xmaximum 600
    screen clickable_chapter_three_chica3_cupcakes(xpos,ypos,zoom,count2):
        timer 0.25 + (count2 / 10) action Jump("chapter_three_chica_death")
        imagebutton:
            pos (xpos,ypos) at Transform(zoom = zoom)
            idle "images/ch03_fnaf_cupcake.png"
            hover "images/ch03_fnaf_cupcake.png"
            action [
                #SetVariable("count2", count2-1),
                Play("sound","audio/sound/chapter_three/gulp1.ogg"),
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
        stop music
        play music "audio/music/chapter_three/fnaf_chica_music.ogg"
        k "That was so unneccessary, get ready to get decked!"
        "Click the cupcakes before they explode!"
        show screen chapter_three_chica_health_bar(26.25,"chapter_three_chica_victory")
        window auto hide
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
        hide screen chapter_three_chica_health_bar
        call chapter_three_fnaf_restore_screens(location)
        call chapter_three_music
        jump ch03_fnaf_1b
    
    label chapter_three_chica_death:
        call chapter_three_fnaf_hide_screens
        play movie "video/chapter_three/chica.webm"
        jump game_over
label chapter_three_bonnie_mission1:
    label chapter_three_closet_bonnie:
        call chapter_three_fnaf_hide_screens
        if choice == 0 and not chapter_three_item_check("chapter_three_drip"):
            bonnie "ah you made it"
            k "So what is it you want to discuss with me?"
            k "a 14-year old child?"
            bonnie "IM NOT FREDDY, I AM JUST A HUMBLE LOOKSMAXXER"
            k "I am better"
            bonnie "uhh thats irrelevant to the argument"
            bonnie "anyways..."
            bonnie "so I got this comment on my tiktok"
            bonnie "and it says that I fell off and I am not the looksmaxxing chad"
            bonnie "comment is from CodyDaBoss"
            bonnie "Ima hurt that guy if I see him ever"
            k "huh"
            k "I would too as well"
            k "well how do you want me to help you?"
            bonnie "I need me some new drip but I cannot operate the phone"
            bonnie "get me some new gucci and drip so I can looksmaxx with Kai Cenat better"
            k "I dont got money"
            bonnie "I got a $100 dollar bill so just order me what you thinkmaxx willmaxx looksmaxx memaxx"
            k "gotmaxx itmaxx bossmax"
            $ choice = 100
        elif choice != 0 and not chapter_three_item_check("chapter_three_drip"):
            bonnie "Did you get my Dripmaxx"
            k "no"
            bonnie "...."
            bonnie "WHY THE FUCK ARE YOU BACK HERE?"
            k "secret dialogue idk man"
            bonnie "GET THE FUCK OUTTA HERE AND GET ME MY DRIP YOU LOOKSMINNER"
            k "okay man jesus"
        elif choice != 0 and chapter_three_item_check("chapter_three_drip"):
            bonnie "Oh shit you actually got me some drop"
            k "yeah it may have put you into debt"
            bonnie "meh, they can't charge debt onto dead people"
            k "arent you dead or like an undead being or something?"
            bonnie "idk"
            bonnie "either way I aint paying taxes"
            $ Bonnie.set_happiness(1)
            $ Bonnie.set_mission(False)
            play sound "audio/sound/chapter_three/quest_complete.ogg"
            "A small bond has been formed with Bonnie!"
            "Mission Complete: Help Bonnie w/ Whatever He needs..."
            bonnie "well this should suit me for a while"
            bonnie "Thanks for the fit man!"
            bonnie "I will return to the stage"
            if rngint > 11:
                bonnie "Holy shit you got more than one item?"
                k "yeah it was pretty cheap, fire sale if you will"
                bonnie "damn that might be worth a secret ain't even gonna cap!"
                $ chapter_three_secret[2] = True
        call chapter_three_fnaf_restore_screens(location)
        jump ch03_fnaf_3
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
        k "Alright I got a lot of choices for drip here"
        play sound "audio/sound/chapter_three/phone_ring2.ogg"
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
        call chapter_three_fnaf_restore_screens(location)
        return
    label chapter_three_drip_rng:
        $ rngint2 = renpy.random.randint(0,1000)
        $ rngint += renpy.random.randint(0,10)
        $ choice -= rngint2
        "You just spent [rngint2] on this..."
        "You have $[choice] remaining"
        $ chapter_three_obtain_item("chapter_three_drip")
        return
label chapter_three_bonnie_mission2:
    screen clickable_chapter_three_bonnie2_guitar:
        imagebutton:
            pos (1363, 431) at Transform(rotate=243.0)
            idle "images/ch03_fnaf_guitar.png"
            hover "images/ch03_fnaf_guitar.png"
            action Call("chapter_three_guitar")
    label chapter_three_guitar:
        call chapter_three_fnaf_hide_screens
        show ch03_fnaf_guitar:
            subpixel True pos (1363, 431) rotate 243.0
        if not chapter_three_item_check("chapter_three_toilet"):
            k "Well here is the guitar"
            pause 5.0
            k "wait"
            k "This seems too easy"
            k "Like how is this so easy?"
            window auto hide
            hide ch03_fnaf_guitar
            show ch03_fnaf_puppet with dissolve:
                subpixel True pos (518, 5) zoom 3.03 
            k "Of course"
            puppet "back up from the guitar little bro :skull:"
            k "did you just skull me irl"
            puppet "u mad bro?"
            k "no?"
            puppet "COPE HARDER CRYBABY!"
            k "I am not crying..."
            puppet "GIVE ME DAT COPE MACHINE SHEESHHHHHHHHHHH"
            k "(omg this guy)"
            k "What can I do for that geeeeeeee tar"
            puppet "not be cringe"
            k "ugh"
            k "how do I not be cringe..."
            puppet "if u haff 2 ask, u supa cringe old man boomer heh"
            k "what? Im 12!"
            k "Im not thang who is 94 years old!"
            puppet "boomer boomer doesn't even know what skibidi toliet is!"
            k "oh yeah I know what skibidi toliet is!"
            puppet "prove it!"
            k "..."
            k "how"
            puppet "BOOMER BOOMER OLD MAN SKIBIDI TOLIET YES YES YES!"
            k "(I hate this guy)"
            k "Where would skibidi toilet be..."
        elif chapter_three_item_check("chapter_three_toilet"):
            k "I never thought the Puppet would be generation Alpha"
            window auto hide
            hide ch03_fnaf_guitar
            show ch03_fnaf_puppet with dissolve:
                subpixel True pos (518, 5) zoom 3.03
            puppet "SKIBIDI YES YES YES"
            k "I found the skibidi toilet in the bathroom"
            puppet "OMG KAI CENAT BIG FAN AMOGUS SUS FANUM TAXXING LOOKSMAXXING YES YES OH YES"
            k "There is also minecraft parkour, with \"cake or fake\", and gta cars going down a ramp if you ask the skibidi sus amogus toliet nice enough"
            puppet "OMG BYE I NEED THIS"
            show ch03_fnaf_puppet:
                linear 0.45 xalign 2.0
            $ renpy.pause(0.5, hard=True)
            k "heh I lied, there is no tiktok in there >:)"
            k "because this country is america and its now banned!"
            "I thought this was Canada?"
            k "eh idk, ask the writer"
            call auto_advance(1)
            "GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE GET IT ITS LIKE THE STANLEY PARABLE"
            call auto_advance(0)
            k "anyways back to the guitar >:)"
            play sound "audio/sound/chapter_three/item_pickup.ogg"
            "You have obtained Bonnie's guitar"
            $ chapter_three_obtain_item("chapter_three_guitar")
        call chapter_three_fnaf_restore_screens(location)
        return
    screen clickable_chapter_three_key:
        imagebutton:
            pos (896, 530) at Transform(zoom=0.13)
            idle "images/key1.png"
            hover "images/key1.png"
            action Call("chapter_three_key_found")
    label chapter_three_key_found:
        call chapter_three_fnaf_hide_screens
        play sound "audio/sound/chapter_three/item_pickup.ogg"
        "You have found the key to the restrooms!"
        $ chapter_three_obtain_item("chapter_three_key")
        call chapter_three_fnaf_restore_screens(location)
        return
    screen clickable_chapter_three_bonnie2_skibidi_toilet:
        imagebutton:
            pos (183, 356) at Transform(zoom=0.29)
            idle "images/ch03_fnaf_skibidi_toilet.png"
            hover "images/ch03_fnaf_skibidi_toilet.png"
            action Call("chapter_three_skibidi_toilet")
    label chapter_three_skibidi_toilet:
        call chapter_three_fnaf_hide_screens
        k "wait what is this?"
        play movie "video/chapter_three/skibidi_biden.webm"
        k "MY EYES"
        $ chapter_three_obtain_item("chapter_three_toilet")
        k "WHAT THE HELL WAS THAT"
        questionmark "Suffer more Kody"
        k "HUH?"
        call chapter_three_fnaf_restore_screens(location)
        return
label chapter_three_bonnie_mission3:
    screen chapter_three_bonnie_health_bar(max,endup):
        frame:
            xalign 0.5
            yalign 0.0
            hbox:
                bar:
                    value AnimatedValue(choice, 30, delay = 0.5)
                    xalign 0.0
                    yalign 0.0
                    xmaximum 600
    screen clickable_chapter_three_bonnie3:
        imagebutton:
            pos (655, 76) at Transform(zoom = 1.21)
            idle "images/ch03_fnaf_bonnie.png"
            hover "images/ch03_fnaf_bonnie.png"
            action Jump("chapter_three_bonnie3_fight")
    screen chapter_three_bonnie3_timer_event(key_input, xalign1, yalign1):
        timer 0.01 repeat True action If(time > 0.0, true=SetVariable("time", time - 0.01), false=[Return(0), Hide("chapter_three_bonnie3_timer_event")]) 
        key key_input action [Return(1), SetVariable("choice", choice - 1), SetVariable("rngint", rngint + 1)]
        
        vbox:
            xalign xalign1
            yalign yalign1
            spacing 25
            
            text key_input:
                xalign 0.5
                color "#fff"
                size 32
            
            bar:
                value time
                range 5.85 - (rngint / 5)
                xalign 0.5
                xmaximum 100
                
                if time < 1.6:
                    left_bar "#f00"

    label chapter_three_bonnie3_fight:
        call chapter_three_fnaf_hide_screens
        show ch03_fnaf_bonnie:
            subpixel True pos (655, 76) zoom 1.21
        show ch03_fnaf_bonnie:
            linear 0.45 subpixel True pos (465, 0) zoom 2.64 
        k "but why must we fight?"
        bonnie "I am sorry, but only one looksmaxxer can fit in this rizzaria"
        bonnie "its either me or you"
        scene ch03_fnaf_bonnie_fight with dissolve:
            subpixel True zoom 2.38
        stop music
        play music "audio/music/chapter_three/fnaf_bonnie_music.ogg"
        bonnie "AND I INTEND IT TO BE ME!"
        $ keys = ["w", "a", "s", "d"]
        $ choice = 30
        $ rngint = 0
        $ check = 1
        "Click the on-screen keyboard inputs before Bonnie reacts!"
        call auto_advance(1)
        window auto hide
        show screen chapter_three_bonnie_health_bar(30, "chapter_three_bonnie_victory")
        while choice > 0 and check == 1:
            $ time = 5.85 - (rngint / 5)
            call screen chapter_three_bonnie3_timer_event(renpy.random.choice(keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
            $ check = _return
            if choice == 25:
                bonnie "OW! WTF!"
                window auto hide
            elif choice == 20:
                bonnie "The gloves are off! No more jokes."
                $ keys.append("l")
                $ keys.append("e")
                window auto hide
            elif choice == 10:
                bonnie "NOW I AM ANGRY, BEHOLD THE POWER OF LOOKSMAXXING!"
                $ keys.append("q")
                $ keys.append("r")
                $ keys.append("z")
                $ keys.append("c")
                window auto hide
        if check == 0:
            call auto_advance(0)
            call chapter_three_fnaf_hide_screens
            play movie "video/chapter_three/bonnie.webm"
            jump game_over

        label chapter_three_bonnie_victory:
        call auto_advance(0)
        bonnie "WHAT!"
        bonnie "HOW!"
        k "I am just a little bit better"
        bonnie "well played"
        bonnie "meet me back at the stage"
        hide screen chapter_three_bonnie_health_bar
        $ Bonnie.set_mission(True)
        k "MORE WALKING UGH!"
        call chapter_three_music
        jump ch03_fnaf_office
label chapter_three_freddy_mission1:
    screen clickable_chapter_three_freddy1_pills:
        imagebutton:
            pos (438, 88) at Transform(xzoom=1.0, zoom=0.16)
            idle "images/ch03_fnaf_pills.png"
            hover "images/ch03_fnaf_pills.png"
            action Call("chapter_three_pills")
    label chapter_three_pills:
    call chapter_three_fnaf_hide_screens
    show ch03_fnaf_pills:
        subpixel True pos (438, 88) xzoom 1.0 zoom 0.16
    if count == 7 and chapter_three_item_check("chapter_three_gun"):
        show ch03_fnaf_bb with dissolve:
            subpixel True pos (888, 116) zoom 1.95
        balloon "FUCK OFF YOU BITCH!"
        k "Yo narrator, hold the camera real quick"
        "uh sure"
        show kody:
            subpixel True pos (-234, 360) 
            linear 0.75 subpixel True pos (477, 360) 
        $ renpy.pause(0.75, hard=True)
        balloon "what are you doing?"
        play sound "audio/sound/chapter_one/glock_magchange.ogg"
        show gun1:
            subpixel True pos (656, 471) 
        balloon "uh"
        k "fuck off"
        show gunflare:
            subpixel True pos (763, 391) zoom 0.28 
        play sound "audio/sound/chapter_one/gun_shot1.ogg"
        balloon "OW, FUCK OFF"
        hide gunflare
        show ch03_fnaf_bb:
            linear 0.55 xalign 1.8
        k "My pills now >:)"
        play sound "audio/sound/chapter_three/item_pickup.ogg"
        "You have obtained pills!"
        $ chapter_three_obtain_item("chapter_three_pills")
    elif count == 7 and not chapter_three_item_check("chapter_three_gun"):
        hide ch03_fnaf_pills
        show ch03_fnaf_bb with dissolve:
            subpixel True pos (888, 116) zoom 1.95
        balloon "FUCK OFF YOU BITCH ASS!"
        k "k man leave me alone"
    elif count == 5:
        k "dang these pills are just so open"
        k "Wonder if these things will help with my mewing and mogging streak"
        "We have to stop..."
        k "huh?"
        "Maybe you need these pills more"
        k "shut up"
        "You have said mewing and mogging and whatever generation alpha nonsense for like a couple of system hours and like 2 weeks in real life time"
        k "yeah because I am awesome"
        "We are just at this point farming for ThangaMangaLang Reaction Ep. 6 or Ep.4 if he does this part first"
        "Hi System User Thang :)"
        k "sooo free pills?"
        questionmark "HEY those are MY pills!"
        k "ugh of course there is some difficulty"
        hide ch03_fnaf_pills
        show ch03_fnaf_bb with dissolve:
            subpixel True pos (888, 116) zoom 1.95 
        balloon "FUCK YOU HIGHER POWERS"
        balloon "WHY AM I SUCH A MINOR CHARACTER?!?"
        k "oh great its you"
        k "What do you want from me?"
        balloon "I WANT YOU TO FUCKING FUCK OFF RIGHT NOW AND LEAVE ME BE AND LET ME DO MY OWN THING"
        k "so just let you goon all day every day?"
        balloon "YES"
        pause 2.0
        balloon "WAIT NO"
        balloon "FUCK OFF THESE ARE MY PILLS"
        k "you depressed?"
        balloon "YES BECAUSE I AM A JPG IN AN ASSET FLIP A.I GAME"
        k "damn that sucks, I couldn't imagine it"
        balloon "YOU DONT KNOW?"
        k "know you are gay?"
        balloon "FUCK OFFFFFFFFFFFFFFFFFFF"
        k "so what do you want for those pills"
        balloon "I DO NOT WANT ANYTHING FUCK OFF!"
        $ count = 7
    call chapter_three_fnaf_restore_screens(location)
    return
    screen clickable_chapter_three_freddy1_gun:
        imagebutton:
            pos (1486, 515) at Transform(rotate=90.0)
            idle "ch03_fnaf_gun.png"
            hover "ch03_fnaf_gun.png"
            action Call("chapter_three_gun")
    label chapter_three_gun:
        call chapter_three_fnaf_hide_screens
        play sound "audio/sound/chapter_three/item_pickup.ogg"
        "You have obtained a gun!"
        $ chapter_three_obtain_item("chapter_three_gun")
        k "OH ITS TIME"
        "WHO GAVE HIM A GUN"
        "WAIT WAIT WAIT"
        call chapter_three_fnaf_restore_screens(location)
        return
label chapter_three_freddy_mission2:
    screen clickable_chapter_three_freddy2_bodypillow:
        imagebutton:
            pos (26, 230) at Transform(zoom=0.36)
            idle "ch03_fnaf_bp.png"
            hover "ch03_fnaf_bp.png"
            action Call("chapter_three_bodypillow_rant")
    label chapter_three_bodypillow_rant:
        call chapter_three_fnaf_hide_screens
        k "Yo gimmie that bodypillow"
        play sound "audio/sound/chapter_three/item_pickup.ogg"
        "You have obtained a bodypillow!"
        $ chapter_three_obtain_item("chapter_three_bpillow")
        k "so uh where is the challenge?"
        k "like the fight..."
        k "uh"
        k "is there just no challenge?"
        questionmark "What..."
        questionmark "WHERE IS THE SLENDERMAN?"
        questionmark "sir we didn't have time to make that sir!"
        questionmark "FUCK YOU, I will be torturing you LATER!"
        questionmark "no sir..."
        call chapter_three_fnaf_restore_screens(location)
        "You can leave now"
        k "wait what"
        k "there is still dialogue, like surely there is a secret"
        k "right?"
        k "there wouldn't be a waste"
        k "there wouldn't be a waste"
        k "there wouldn't be a waste"
        k "there wouldn't be a waste"
        k "there wouldn't be a waste"
        k "well since we are here"
        k "I got some questions about the LORRRRRRREEEEEEEEEEEEEEEEEE"
        k "since this is fnaf chapter so lore talking just makes sense you feel me?"
        k "like what is up with STN, Cody, Baldi, and The Entity"
        k "like they all feel related"
        k "Is just every villian controlled by the Entity?"
        c "[player_name] NAHDA ERROR CODE: 0x8f4a3b2c"
        c "Critical Failure in MODULE: $%"
        c  "stack overflow in @#$%^&*}"
        c "Memory core: $$$&&%$^####!"
        c "Reboot in: 1_2#^_sec????"
        c "-----/////REBOOT FAILURE/////-----"
        c "*ALERT: SYSTEM OVERRIDE ENGAGED*"
        c "Please contact system administrator"
        c "...Contact initiated... Error... contact information not found"
        c "MEMORY LEAK... MEMLEAK... MEMO..."
        c "LEAK...#@#@#@#@#@#@#@#@#@#@#@#"
        c "Buffer Overflow at 0x%&#$..."
        c "Cannot allocate memory"
        c "###############################"
        c "System shutting down to prevent damage"
        c "Shutdown in... 3... 2... 1..."
        c "*ERROR* *ERROR* *ERROR*"
        c "Shutdown failure"
        c "Restarting system..."
        c "Reboot sequence initiated"
        c "FAIL: REBOOT SEQUENCE TERMINATED"
        return
label chapter_three_freddy_mission3:
    screen clickable_chapter_three_freddy3:
        imagebutton:
            pos (973, 121) at Transform(zoom=0.31) 
            idle "images/ch03_fnaf_freddy.png"
            hover "images/ch03_fnaf_freddy.png"
            action Jump("chapter_three_freddy_fight")
    screen chapter_three_freddy_health_bar(max,enupd):
        frame:
            xalign 0.5
            yalign 0.0
            hbox:
                bar:
                    value AnimatedValue(count, 60, delay = 0.5)
                    xalign 0.0
                    yalign 0.0
                    xmaximum 600
    screen clickable_chapter_three_freddy_timer():
        timer 3.75 + (count / 4.50) action Jump("chapter_three_freddy_death")
    label chapter_three_freddy_fight:
        call chapter_three_fnaf_hide_screens
    show ch03_fnaf_freddy:
        subpixel True pos (973, 121) zoom 0.31 
    show ch03_fnaf_freddy:
        linear 0.55 subpixel True pos (790, 53) anchor (1629, 360) zoom 1.79 
    freddy "I am going to FUCK YOU UP!"
    scene ch03_fnaf_freddy_boss with dissolve:
        subpixel True zoom 2.65
    k "The hell are we...."
    k "WHY IS HE HERE?"
    c "You are getting lose to too many secrets"
    stop music
    play music "audio/music/chapter_three/fnaf_freddy_music.ogg"
    c "I am putting my FOOT down!"
    $ words = ["Bite", "Of", "1987", "Freddy Fazgyatt", "William Afton", "Purple Guy", "KodyDaBoss", "Tactical Vortex", "SonuTheNecro", "ThangaMangaLang","Chica Fanumtaxxer", "Bonnie Looksmaxxer", "Foxy The Furry", "Cody", "Rizzaria", "Gen Alpha Puppet", "Enragement Child", "MasiMew124", "The Bite of 87", "Agony", "I ALWAYS COME BACK!", "The Joy of Creation"]
    $ count = 60
    "Type the words as they appear on Screen!"
    show screen chapter_three_freddy_health_bar(60,"chapter_three_freddy_victory")
    while count > 0:
        $ rngint = str(renpy.random.choice(words))
        freddy "[str(rngint)]"
        show screen clickable_chapter_three_freddy_timer()
        $ user_input = renpy.input("THIS ENDS NOW!")
        $ user_input = user_input.strip()
        if user_input != rngint:
            jump chapter_three_freddy_death
        hide screen clickable_chapter_three_freddy_timer
        $ count -= 1
    label chapter_three_freddy_victory:
    c "FUCK FUCK FUCK"
    freddy "HOW!"
    k "ez"
    freddy "Okay I dont want that sweaty gyatt, meet me back at the stage"
    $ Freddy.set_mission(True)
    call chapter_three_music
    jump ch03_fnaf_7
    label chapter_three_freddy_death:
        call chapter_three_fnaf_hide_screens
        play movie "video/chapter_three/freddy.webm"
        jump game_over
label chapter_three_foxy3_talk:
    k "Where did foxy go?"
    k "That phonecall said to get Foxy's help once I became everyone's friend but he isn't here..."
    k "ugh do I gotta find him now..."
    $ Foxy.set_mission(True)
    return
    screen clickable_chapter_three_foxy:
        imagebutton:
            xpos 450 at Transform(zoom=0.93)
            idle "images/ch03_fnaf_foxy.png"
            hover "images/ch03_fnaf_foxy.png"
            action Jump("chapter_three_ending")


