# Extra Code to make chapter_three's code nicer, these functions are for one time events in Chapter three
# Python Code
init python:
    from random import randint
    from enum import Enum

    class Animatronic:
        happiness = 0
        mission = False
        def __init__(self, name):
            self.name = name
        def get_happiness(self):
            return self.happiness
        def set_happiness(self,happiness: int):
            self.happiness = happiness
        def set_mission(self, status: bool):
            self.mission = status
        def get_mission(self):
            return self.mission
        def get_name(self):
            return self.name

    def chapter_three_jewels_mark(id):
        chapter_three_jewels_check[id] = True
    def chapter_three_anime_talk():
        try:
            with renpy.file("scripts/chapter_three/chapter_three_anime_speech.txt") as file:
                for line in file:
                    renpy.say("Kody", str(line)[2:-5])
        except FileNotFoundError:
            renpy.say(None, "File not found: 'scripts/chapter_three/chapter_three_anime_speech.txt'")
    def chapter_three_gunshots(gunshots):
        count = 0
        while count < gunshots:
            renpy.sound.play("audio/sound/chapter_three/gunshot2.ogg")
            renpy.pause(0.25)
            count += 1
    def chapter_three_item_check(item):
        return chapter_three_key_items.get(item, ItemState.NOT_OBTAINED) == ItemState.OBTAINED
    def chapter_three_obtain_item(item):
        chapter_three_key_items[item] = ItemState.OBTAINED
    def chapter_three_unobtain_item(item):
        chapter_three_key_items[item] = ItemState.NOT_OBTAINED
    def fnaf_shoot(count):
        random_number = randint(count,count*2)
        count = 0
        while count < random_number:
            renpy.sound.play("audio/sound/chapter_one/gun_shot1.ogg")
            renpy.pause(0.075)
            count += 1 

#Renpy Code
screen clickable_chapter_three_jewel_osco():
    imagebutton:
        pos (611, 20) 
        at Transform(yzoom = 1.0, zoom = 0.07)
        idle "images/chapter_three/ch03jewel.jpg"
        hover At("images/chapter_three/ch03jewel.jpg", animated_outline)
        action Jump("chapter_three_jewel_osco")
screen clickable_chapter_three_house():
    imagebutton:
        pos (1513, 0) 
        at Transform(zoom = 0.71)
        idle "images/chapter_three/ch03house_clipart.png"
        hover At("images/chapter_three/ch03house_clipart.png", animated_outline)
        action Jump("chapter_three_streaming")
screen clickable_chapter_three_mail():
    imagebutton:
        pos (585, 581) 
        at Transform(zoom = 0.13)
        idle "images/chapter_three/ch03_mail.png"
        hover At("images/chapter_three/ch03_mail.png", animated_outline)
        action Jump("chapter_three_mailman")
screen clickable_chapter_three_herobrine():
    imagebutton:
        pos (1838, 201) 
        at Transform(zoom=0.06)
        idle "images/chapter_three/ch03_herobrine_alter.png"
        hover At("images/chapter_three/ch03_herobrine_alter.png", animated_outline)
        action Jump("chapter_three_herobrine_found")

label chapter_three_jewel_osco:
    call chapter_three_hide_map_buttons
    #show ch03jewel:
        #subpixel True pos (611, 20) yzoom 1.0 zoom 0.07
    if count > 0:
        k "I SHOULD NOT GO BACK THERE"
        k "THEY MIGHT KILL ME"
        jump chapter_three_map
    scene ch03jewel_outside with dissolve:
        subpixel True xzoom 1.32 zoom 1.23 
    k "Ugh... I guess I can try working in Grocery"
    show brian1 with dissolve:
        subpixel True pos (668, 491) 
    b "Yo What is up Kody?"
    
    show brian1:
        linear 0.15 subpixel True pos (103, 486) 
    show kody with dissolve:
        subpixel True pos (1145, 556) yrotate 180.0 
    $ renpy.pause(0.15, hard=True)
    k "oh great what is this bozo doing here?!"
    b "i work here : D"
    k "huh?"
    b "You thought it was all a meme?"
    k "yes"
    b "fuck you"
    b "yeah well I work here, what can I help you with?"
    menu:
        "I will mog on you!":
            k "uh"
            k "gimmie job or i will show off my mogmaxxing"
    b "you already showed me that"
    k "oh"
    b "Uh let me see what I can do for you!"
    scene ch03jewel1 with dissolve:
        subpixel True xzoom 1.2 zoom 2.58 
    show brian1:
        subpixel True pos (260, 306) 
    show kody:
        subpixel True pos (1116, 361) yrotate 180.0 

    call auto_advance(1)
    b "okay so I talked with CEO Osco and"
    call auto_advance(0)
    k "wait you talked with CEO Mr. Jewel Osco?"
    b "yes"
    menu:
        "How?":
            k "How does a cashier talk to the CEO for a simple job at one location of a multinational business?"
        "What?":
            k "How does a cashier talk to the CEO for a simple job at one location of a multinational business?"
    b "yeah its a really bad bottleneck"
    b "The point is"
    b "I got you a trial job"
    k "so an internship at jewel osco"
    b "no its a trial job"
    b "just help people out and if Mr. Osco likes it"
    b "He will give you a job"
    k "bet thats so FREE!"
    b "you'll see"
    "Go help out Jewel Osco Customers"
    "Show what you are made of!"
    "YEAH!"
    stop music
    play music "audio/music/chapter_three/butterfly_kiss.ogg" loop
    $ count2 = 0
    jump ch03_jewel_main
    label ch03_jewel_main:
        call chapter_three_jewel_hide_all_buttons
        $ location = 1
        $ print(count2)
        scene ch03jewel1 with dissolve:
            subpixel True xzoom 1.2 zoom 2.58
        label ch03_jewel_main_1:
        if chapter_three_jewels_check[0] == False:
            show screen clickable_chapter_three_wet_floor_sign
        elif count2 == 5:
            jump chapter_three_jewel_end
        call chapter_three_jewel_restore_buttons(location)
        "You are currently in the middle of Jewel Osco!"
        jump ch03_jewel_main_1

    label ch03_jewel_grocery:
        call chapter_three_jewel_hide_all_buttons
        $ location = 2
        scene ch03jewel2 with dissolve:
            subpixel True xzoom 1.17 zoom 2.61 
        label ch03_jewel_grocery_1:
        if chapter_three_jewels_check[1] == False:
            show screen clickable_chapter_three_grocery_cart
        call chapter_three_jewel_restore_buttons(location)
        "You are currently in the Grocery Section of Jewel Osco!"
        jump ch03_jewel_grocery_1

    label ch03_jewel_meat:
        call chapter_three_jewel_hide_all_buttons
        $ location = 3
        scene ch03jewel3 with dissolve:
            subpixel True yzoom 1.17 zoom 1.41 
        label ch03_jewel_meat_1:
        if chapter_three_jewels_check[2] == False:
            show screen clickable_chapter_three_butcher
        call chapter_three_jewel_restore_buttons(location)
        "You are currently in the Meat Section of Jewel Osco!"
        jump ch03_jewel_meat_1

    label ch03_jewel_shelf:
        call chapter_three_jewel_hide_all_buttons
        $ location = 4
        scene ch03jewel4 with dissolve:
            subpixel True xzoom 1.2 zoom 2.71
        label ch03_jewel_shelf_1:
        if chapter_three_jewels_check[3] == False:
            show screen clickable_chapter_three_candy
        call chapter_three_jewel_restore_buttons(location)
        "You are currently in the Shelfed Goods Section of Jewel Osco!"
        jump ch03_jewel_shelf_1

    label ch03_jewel_checkout:
        call chapter_three_jewel_hide_all_buttons
        $ location = 5
        scene ch03jewel5 with dissolve:
            subpixel True yzoom 1.06 zoom 2.55
        label ch03_jewel_checkout_1:
        if chapter_three_jewels_check[4] == False:
            show screen clickable_chapter_three_customer
        call chapter_three_jewel_restore_buttons(location)
        "You are currently in the Checkout Section of Jewel Osco!"
        jump ch03_jewel_checkout_1

    #These are buttons used to walk around Baldi's school house
    screen clickable_button_jewel_chapter_three_up(origin):
        imagebutton:
            xalign 0.5
            yalign -0.05
            idle "images/ArrowUpPress.png"
            hover At("images/ArrowUpPress.png", animated_outline)
            if origin == 1:
                action Jump("ch03_jewel_meat")
            else:
                action Jump("ch03_jewel_main")

    screen clickable_button_jewel_chapter_three_down(origin):
        imagebutton:
            xalign 0.5
            yalign 0.995
            idle "images/ArrowDownPress.png"
            hover At("images/ArrowDownPress.png", animated_outline)
            if origin == 3:
                action Jump("ch03_jewel_main")
            else:
                action Jump("ch03_jewel_checkout")

    screen clickable_button_jewel_chapter_three_left(origin):
        imagebutton:
            xalign 0.005
            yalign 0.5
            idle "images/ArrowLeftPress.png"
            hover At("images/ArrowLeftPress.png", animated_outline)
            if origin == 4:
                action Jump("ch03_jewel_main")
            else:
                action Jump("ch03_jewel_grocery")

    screen clickable_button_jewel_chapter_three_right(origin):
        imagebutton:
            xalign 0.995
            yalign 0.5
            idle "images/ArrowRightPress.png"
            hover At("images/ArrowRightPress.png", animated_outline)
            if(origin == 2):
                action Jump("ch03_jewel_main")
            else: 
                action Jump("ch03_jewel_shelf")
    screen clickable_chapter_three_wet_floor_sign():
        imagebutton:
            pos (991, 561)
            idle "images/chapter_three/ch03_wetfloorsign.png"
            hover At("images/chapter_three/ch03_wetfloorsign.png", animated_outline)
            action Call("chapter_three_wet_floor_sign")
    screen clickable_chapter_three_grocery_cart():
        imagebutton:
            pos (1071, 451) 
            at Transform(rotate = -36.0 , zoom = 0.7)
            idle "images/chapter_three/ch03_cart.png"
            hover At("images/chapter_three/ch03_cart.png", animated_outline)
            action Call("chapter_three_cart")
    screen clickable_chapter_three_butcher():
        imagebutton:
            pos (55, 326)
            idle "images/chapter_three/ch03_butcher.png"
            hover At("images/chapter_three/ch03_butcher.png", animated_outline)
            action Call("chapter_three_butcher")
    screen clickable_chapter_three_candy():
        imagebutton:
            pos (1390, 475)
            idle "images/chapter_three/ch03_candy.png"
            hover At("images/chapter_three/ch03_candy.png", animated_outline)
            action Call("chapter_three_candy")
    screen clickable_chapter_three_customer():
        imagebutton:
            pos (1106, 226) 
            at Transform(zoom = 1.38)
            idle "images/chapter_three/ch03_woman.png"
            hover At("images/chapter_three/ch03_woman.png", animated_outline)
            action Call("chapter_three_customer")

    # Location One Event
    label chapter_three_wet_floor_sign:
        call chapter_three_jewel_hide_all_buttons
        show ch03_wetfloorsign:
            subpixel True pos (991, 561)
        k "Hmmmm"
        k "Here is a wet-floor sign"
        k "It'd be really funny if I just..."
        play sound "audio/sound/chapter_three/sign_fallover.ogg"
        hide ch03_wetfloorsign
        k "Knock this over"
        k ">:)"
        show ch03_man:
            subpixel True pos (-298, 293) zoom 0.54
            linear 0.45 subpixel True xpos 962
        $ renpy.pause(0.45, True)
        play sound "audio/sound/chapter_three/slip1.ogg"
        show ch03_man:
            linear 0.65 subpixel True pos (953, 63) rotate -90
            linear 0.35 subpixel True pos (936, 541) rotate 270.0
        $ renpy.pause(1.0, True)
        play sound "audio/sound/chapter_three/back_crack.ogg"
        questionmark "YO WHAT THE HELL!"
        questionmark "MY BACK"
        k "uh"
        questionmark "CALL AN AMBULANCE!"
        questionmark "I NEED MY LAWYER"
        k "nah you faking lol"
        questionmark "DID YOU NOT SEE MY BACK CRUNCH?"
        questionmark "IM SUEING ALL OF YOU FUCKERS!"
        k "hahah"
        k "(Im getting outta here, this guy is WACK)"
        $ chapter_three_jewels_mark(0)
        hide ch03_man
        #call chapter_three_jewel_restore_buttons(location)
        $ count2 += 1
        return
    # Location Two Event
    label chapter_three_cart:
        call chapter_three_jewel_hide_all_buttons
        show ch03_cart:
            subpixel True pos (1071, 451) rotate -36.0 zoom 0.7 
        k "hmmm"
        k "here is a cart..."
        k "but no one is here..."
        k "I guess this is..."
        k "LOST MEDIA?!?" 
        k "alright time to piss into the groceries >:)"
        play sound "audio/sound/chapter_three/water_pouring.ogg"
        pause 10.0
        stop sound
        hide ch03_cart
        k "well that was fun"
        k "I should dip!"
        $ chapter_three_jewels_mark(1)
        #call chapter_three_jewel_restore_buttons(location)
        $ count2 += 1
        return
    # Location Three Event
    label chapter_three_butcher:
        call chapter_three_jewel_hide_all_buttons
        show ch03_butcher:
            subpixel True pos(55,326)
        jb "Hello sir, how can I help you!"
        k "Uh hey! I am your boss now and I got here an order for you"
        jb "Uh I was not informed of getting a new boss"
        k "Well that was a strike, there was an email about it"
        jb "Let me verify this real quick"
        k "Shoulda done that before work, now you are on the clock"
        k "You want to be fired?"
        jb "No sir!"
        k "Alright I want an order of 1200 Chicken Thighs"
        k "1600 Chicken Breasts"
        k "2000 Chicken Wings"
        jb "..."
        jb "You are capping"
        k "I am not"
        jb "Sir thats impossible!"
        jb "who is this even for?"
        menu:
            "MrBeast":
                k "MrBeast!"
            "Elon Musk":
                k "Elon Musk"
            "Donald Trump":
                k "Donald Trump"
        jb "wait for real?"
        k "yeah no cap"
        jb "We literally cannot do that"
        k "guess you are fired bozo"
        jb "I need this job to feed my 3 children"
        k "GET OUT BOZO!"
        jb "okay sir"
        $ chapter_three_jewels_mark(2)
        #call chapter_three_jewel_restore_buttons(location)
        $ count2 += 1
        return
    # Location Four Event
    label chapter_three_candy:
        call chapter_three_jewel_hide_all_buttons
        show ch03_candy:
            subpixel True pos (1390, 475)
        k "Dang..."
        k "That is a big bag of candy..."
        k "nobody would mind if I..."
        k "ate it real fast"
        play sound "audio/sound/chapter_three/chomp.ogg"
        hide ch03_candy
        k "That was some good candy >:)"
        $ chapter_three_jewels_mark(3)
        #call chapter_three_jewel_restore_buttons(location)
        $ count2 += 1
        return
    # Location Five Event
    label chapter_three_customer:
        call chapter_three_jewel_hide_all_buttons
        show ch03_woman:
            subpixel True pos (1106, 226) zoom 1.38 
        jc "Hey Can you help me with something?"
        k "yeah sure, what's up"
        jc "Well my card isn't working and It should work..."
        k "yeah that's weird, you can just leave"
        jc "?"
        k "the food is now free, now get out"
        jc "omg really?"
        k "yes"
        jc "This made my day thanks man"
        k "ez rizz"
        menu:
            "Can I get yo number?":
                jc "wtf no"
                k "damn"
                k "why?"
                jc "this is harassment!"
            "You tryna go on a jewel date?":
                jc "no!"
                k "why?"
                jc "I got a boyfriend"
                jc "and you are weird"
                jc "and this is harassment!"
                k "damn"
        hide ch03_woman
        $ chapter_three_jewels_mark(4)
        #call chapter_three_jewel_restore_buttons(location)
        $ count2 += 1
        return
    # Restores buttons once they are closed when an interaction starts/restores button once we swap areas
    label chapter_three_jewel_restore_buttons(current_location):
        if current_location == 1:
            show screen clickable_button_jewel_chapter_three_up(location)
            show screen clickable_button_jewel_chapter_three_down(location)
            show screen clickable_button_jewel_chapter_three_left(location)
            call screen clickable_button_jewel_chapter_three_right(location)
        elif current_location == 2:
            call screen clickable_button_jewel_chapter_three_right(location)
        elif current_location == 3:
            call screen clickable_button_jewel_chapter_three_down(location)
        elif current_location == 4:
            call screen clickable_button_jewel_chapter_three_left(location)
        elif current_location == 5:
            call screen clickable_button_jewel_chapter_three_up(location)
        return
    label chapter_three_jewel_hide_buttons:
        hide screen clickable_button_jewel_chapter_three_up
        hide screen clickable_button_jewel_chapter_three_down
        hide screen clickable_button_jewel_chapter_three_left
        hide screen clickable_button_jewel_chapter_three_right
        return
    label chapter_three_jewel_hide_all_buttons:
        call chapter_three_jewel_hide_buttons
        hide screen clickable_chapter_three_wet_floor_sign
        hide screen clickable_chapter_three_grocery_cart
        hide screen clickable_chapter_three_butcher
        hide screen clickable_chapter_three_candy
        hide screen clickable_chapter_three_customer
        return
    label chapter_three_jewel_end:
        stop music
        play music "audio/music/chapter_three/troubled.ogg" loop
        call chapter_three_jewel_hide_all_buttons
        show ch03_ceo with dissolve:
            subpixel True pos (616, 68) zoom 3.41 
        jceo "Hello Kody"
        k "Who the hell are you?"
        k "looking like a straight up gooner"
        jceo "I would like to say something"
        play sound "audio/sound/general/vine_boom.ogg"
        jceo "and that is YOU ARE FUCKING FIRED"
        jceo "YOU ATE OUR MERCHANDISE, GAVE FREE PRODUCE AWAY, FIRED AN EMPLOYEE, BROKE HEALTH SAFETY PROTOCOL, AND PISSED IN SOMEONE'S FOOD!"
        k "yeah and it was freakin awesome"
        jceo "You are FUCKING BANNED FROM EVERY JEWEL OSCO FOR EVER"
        jceo "YOU HAVE 5 MINUTES TO LEAVE BEFORE I CALL THE FUCKING POLICE!"
        k "Fine jeez"
        menu:
            "'What about my Paycheck?'":
                k "Can i still have my paycheck?"
            "'About Health Benefits'":
                k "Do I still get my health benefits"
                k "I need em for my mog sessions"
            "'About Good work'":
                k "Was i a better employee than brian?"
                k "like was i the absolute GOAT of jewel osco"
        jceo "WHAT DO YOU FUCKING THINK?"
        k "yes"
        #jceo "..."
        pause 2.0
        k "okay i will go"
        stop music
        play music "audio/music/chapter_three/forest1.ogg" loop
        scene ch03map with dissolve:
            subpixel True pos (-63, -63) xzoom 1.31 yzoom 1.14 zoom 3.14 blur 3.48
        "Well that coulda gone better"
        k "yeah I FUCKING KNOW!"
        $ count += 1
        jump chapter_three_map

label chapter_three_streaming:
    call chapter_three_hide_map_buttons
    scene ch03_desk with dissolve:
        subpixel True xzoom 1.18 zoom 1.59 
    show kody with dissolve:
        subpixel True pos (990, 33) zoom 1.87 yrotate 180.0
    stop music
    play music "audio/music/chapter_three/investigation.ogg"
    if count2 == 5:
        #k "Well that fucking sucks..."
        k "okay so I saw Thang do this before with Danganronpa"
        k "I watched Markiplier"
        k "I got this, I am the straight goat and the next JackSepticEye :)"

        show thanga2:
            subpixel True pos (-459,28) zoom 1.71
            linear 0.35 subpixel True pos (108, 28) zoom 1.71 
        t "I heard my name"
        k "rememeber danganronpa?"
        t "The game or what happened last week?"
        k "the game"
        t "yeah why?"
        k "remember how you recorded that game?"
        t "like ddlc?"
        k "yeah yeah"
        show ch03_reaction:
            subpixel True yzoom 1.06 zoom 1.52 
        k "I loved your reactions"
        t "solid content I ain't even gonna cap"
        hide ch03_reaction
        t "but why are you bringing this up right now?"
        k "ima be the next pewdiepie"
        k "ima be a millionaire"
        t "straight copium"
        k "no it aint, its straight bopium"
        t "yeah okay buddy, good luck w/ that"
        t "after this fails, you will go get a REAL job okay?"
        k "yeah yeah yeah"
        k "get out of my room now"
        show thanga2:
            yrotate 180.0
            linear 0.35 subpixel True pos (-459,28) zoom 1.71
        t "later kodster"
        k "alright let's get this bread"
        k "now what game should I do?"
        k "hmmm"
        k "oh ho ho ho"
        k "I got the ultimate idea!"

        scene ch03_markiplier1:
            subpixel True zoom 1.54 
        show kody:
            subpixel True crop_relative True yoffset -162.0 pos (-30, 30) xzoom 1.62 zoom 1.38 crop (0.0, -0.14, 1.0, 0.66) 
        play sound "audio/sound/chapter_three/markiplier.ogg"
        $ renpy.pause(3.0)
        
        k "Welcome to Poppy's Playtime!"
        k "I have heard this game is awesome"
        k "and before we start!"
        k "can we get 100k likes for a part two"
        k "and be sure to subscribe if you enjoy the content"
        k "alright, let's go"
        scene ch03_markiplier2:
            subpixel True zoom 1.54
        show kody:
            subpixel True crop_relative True yoffset -162.0 pos (-30, 40) xzoom 1.62 zoom 1.38 crop (0.0, -0.14, 1.0, 0.66) 
        k "Alright this game looking real baby"
        k "like is this game for babies?"
        stop music
        play movie "video/chapter_three/markiplier.webm"
        play music "audio/music/chapter_three/investigation.ogg"
        scene ch03_desk with dissolve:
            subpixel True xzoom 1.18 zoom 1.59 
        show kody with dissolve:
            subpixel True pos (990, 33) zoom 1.87 yrotate 180.0
        k "BRO"
        k "THIS GAME IS SO SCARY WTF"
        show thanga2:
            subpixel True pos (-459,28) zoom 1.71
            linear 0.35 subpixel True pos (108, 28) zoom 1.71
        t "I heard yelling, what happened?"
        k "I died in this game and it was super scary"
        t "get a real job"
        k "k fine fine"
        $ count2 = 6
        $ count += 1
    elif count2 == 6:
        k "okay gaming didn't work out"
        k "but I simply won't do scary vidya games"
        k "hmmmm"
        k "THANGGGGGGGGGGGGGGGGGGG"
        show thanga2:
            subpixel True pos (-459,28) zoom 1.71
            linear 0.35 subpixel True pos (108, 28) zoom 1.71
        t "I thought I told you to get a real job"
        k "iz too hard for me"
        t "well what do you need?"
        k "I need a not scary thing to do for youtube content"
        t "hmmm"
        t "Well can you do a thanga anime news network?"
        k "?"
        t "its MY show and nobody elses"
        t "you just talk about current anime"
        k "got it"
        k "3"
        k "THANG GET OUT"
        show thanga2:
            yrotate 180.0
            linear 0.35 subpixel True pos (-459,28) zoom 1.71
        t "how much are you going to reuse this animation?"
        hide thanga2
        k "alright here we go"
        k "3"
        k "2"
        k "1"
        k "drop it"
        show ch03_crunchy:
            subpixel True xpos -180 xzoom 1.11 zoom 1.51
        stop music
        play music "audio/music/chapter_three/anime1.ogg" loop
        $ chapter_three_anime_talk()
        scene ch03_desk with dissolve:
            subpixel True xzoom 1.18 zoom 1.59 
        show kody with dissolve:
            subpixel True pos (990, 33) zoom 1.87 yrotate 180.0
        stop music
        k "alright the video finished"
        k "COME HERE!"
        show thanga2:
            subpixel True pos (108, 28) zoom 1.71
        k "how did you just appear"
        t "not reusing the animation"
        t "video looks pretty good to me"
        t "alright now hit upload and in like 10 minutes you are good to go"
        k "alright ima get like 10million dollars from this video"
        t "more like ten wasted minutes"
        k "what?"
        t "you need to be basically a big youtuber to get money"
        k "what a scam"
        t "that is how supply and demand works"
        k "fuck this then"
        t "atleast upload the video you have already made!"
        k "okay okay!"
        k "I got a pop-up"
        show ch03_dmca:
            subpixel True xzoom 1.09 zoom 2.71 
        t "You got a DMCA L Bozo"
        hide ch03_dmca
        k "THIS JOB FUCKING SUCKS I HATE THIS SHIT!"
        k "YOUTUBE IS FUCKING RIGGED GRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR!"
        t "get out of here"
        $ count += 1
        $ count2 = 7
    else:
        k "Honestly fuck this shit"
        k "I ain't doing this streamer shit again"
        k "Everyone who got famous is obviously hacking!"
    stop music
    play music "audio/music/chapter_three/forest1.ogg" loop
    jump chapter_three_map

label chapter_three_mailman:
    call chapter_three_hide_map_buttons
    stop music
    play music "audio/music/chapter_three/youthful_lunch.ogg"
    scene ch03_post1 with dissolve:
        subpixel True xzoom 1.31 zoom 1.84 
    show kody:
        subpixel True pos (-238, 438)
    if location == 7:
        k "I should not try this..."
        stop music
        play music "audio/music/chapter_three/forest1.ogg" loop
        jump chapter_three_map
    "Somewhere in the U.S."
    show kody:
        linear 0.35 subpixel True pos (482, 438) 
    k "I gotta be the BEST mailman i got the guuuuuuu"
    k "but how do i make this process better than Jewel Osco"
    show phoenix_wright:
        subpixel True pos (2435, 398) zoom 0.63 
        linear 0.35 subpixel True pos (1184, 398) zoom 0.63 
    pw "yo kodster"
    pw "is the usps open?"
    k "uh yeah"
    k "yo felix white"
    k "got any guu gaming ideas on how to become pro mailman"
    pw "I dont know what any of those words mean but I think you just deliver mail in a mail truck"
    k "damn the truck's got pronouns"
    pw "MAIL truck"
    pw "not male truck"
    k "okay ima be the best mail man ever"
    pw "good luck"
    pw "and you will need it!"
    scene ch03_post2 with dissolve:
        subpixel True xzoom 1.37 zoom 2.25 
    k "woah this is the mail system in the united states"
    show ch03_usps_worker:
        subpixel True pos (323, -37) zoom 3.73 
    usps "Hello sir, welcome to the United States Postal Service!"
    usps "What are we delivering today?"
    k "Yo man"
    k "I don't really got anything important to deliver"
    usps "What can I do for you then sir?"
    k "Call me Kody with a K"
    k "speaking of which, did you see a Cody with a C?"
    usps "Uh yes, actually I did deliver a package"
    k "YOOOOO"
    k "WHAT WAS IT?"
    usps "U.S. code states that all mail is anonymous and cannot be tampered with"
    usps "But it was very big"
    usps "kinda like a football"
    k "(Hell Cody is using a football for?)"
    k "so anyways..."
    k "I would like to have a job offer at this governmental position"
    usps "Ah"
    usps "I cannot really do that"
    usps "I cannot give governmental positions"
    k "I really need this job man"
    k "I got 3 kids to pay and my brother is ailing with autism, retardism, and cancerism"
    usps "hmmm"
    usps "I will tell you what"
    usps "I will give you a test run for a couple of blocks and if you can handle that, then I will give you the job"
    usps "It looks like you need it"
    k "alright thanks man"
    scene ch03_usps_suburb with dissolve:
        subpixel True yzoom 1.31 zoom 5.63 
    show ch03_usps_van:
        subpixel True pos (-640, 388) zoom 2.05 yrotate 180.0
    k "Wow are we in pixel town?"
    usps "yes actually, there was a sign for it behind us"
    k "oh"
    usps "anyways deliver this first house"
    show ch03_usps_van:
        linear 1.1 subpixel True pos (820, 671) zoom 2.05
    window auto hide
    $ renpy.pause(1.1, hard = True)
    usps "Drop this package at the front door"
    usps "Super Simple"
    show kody:
        subpixel True pos (1355, 830) zoom 0.34 
        linear 0.556 subpixel True pos (1735, 665) zoom 0.34 
    window auto hide
    $ renpy.pause(0.556, hard = True)
    k "Alright, I just drop the package here and now I am done"
    k "this is pretty easy"
    usps "Yo!"
    usps "No Dilly-Dallying"
    usps "Onto the next house"
    k "k wait for me"
    show kody:
        yrotate 0.0
        linear 0.445 subpixel True pos (1355, 830) zoom 0.34
    window auto hide
    $ renpy.pause(0.445, hard = True)
    hide kody
    usps "alright now go next house"
    show ch03_usps_van:
        linear 0.8 subpixel True pos (1286, 915) 
    window auto hide
    $ renpy.pause(1.0, hard = True)
    scene ch03_usps_suburb2:
        subpixel True
    show ch03_usps_van:
        subpixel True pos (-406, 656) zoom 1.29 yrotate 180.0 
    k "yo is this a.i. land?"
    usps "yes actually, there was a sign for it behind us"
    k "oh"
    usps "We are going to the second house"
    k "got it sir!"
    show ch03_usps_van:
        linear 1.2 subpixel True pos (935, 726) zoom 1.29 yrotate 180.0
    window auto hide
    $ renpy.pause(1.2, hard = True)
    usps "Drop this giftbox at the front door"
    show kody:
        subpixel True pos (1303, 781) zoom 0.32 
        linear 0.35 subpixel True pos (1668, 696) 
    window auto hide
    $ renpy.pause(0.35, hard = True)
    k "Damn, I could get used to this"
    show kody:
        yrotate 180.0
    show ch03_usps_van:
        linear 0.1 subpixel True pos (2560, 1035) 
    window auto hide
    $ renpy.pause(0.1, hard = True)
    k "HEY WAIT FOR ME!"
    k "WHERE ARE YOU GOING"
    k "WTF!"
    show kody:
        yrotate 0
        linear 2.221 subpixel True pos (2590, 1101) 
    window auto hide
    $ renpy.pause(2.1, hard = True)
    scene ch03_usps_dog:
        subpixel True xpos -18 xzoom 1.88 yzoom 1.06 zoom 1.02 
    k "YO YOU ASS WHY DID YOU LEAVE ME BEHIND"
    usps "Mail has no time for waiting in the modern era"
    usps "You either deliver or you fail to deliver"
    k "deep stuff"
    "NO IT ISN'T?????"
    k "stfu"
    k "so uh, the dog warning"
    usps "I am going to need you to deliver some football to this house"
    stop music
    play music "audio/music/chapter_three/zone_time.ogg"
    k "CODY?"
    k "let's do this"
    play sound "audio/sound/chapter_three/gulp1.ogg"
    k "(gulp)"

    show kody:
        subpixel True pos (1918, 145) yrotate 180.0 
        linear 0.556 subpixel True pos (1435, 58) yrotate 180.0 
    show ch03_usps_baby_ocho:
        subpixel True pos (-210, 166) zoom 0.6
    label chapter_three_usps_dog:
    menu:
        "Run!":
            $ confirm_menu_no_jump("chapter_three_usps_dog")
            k "fuck this"
            usps "WHAT?"
            k "im outta there, this baby ocho got me scared!"
            show kody:
                yrotate 0.0
                linear 0.35 subpixel True pos (2346, 266) 
            $ renpy.say("Baby Ocho", "Woof")
        "Punt the fucking dog!":
            $ confirm_menu_no_jump("chapter_three_usps_dog")
            show kody:
                linear 0.556 subpixel True pos (641, 188)
            window auto hide
            $ renpy.pause(1.5, hard = True)
            k "goodbye bastard"
            play sound "audio/sound/chapter_three/falcon_kick.ogg"
            pause 1.4
            show ch03_usps_baby_ocho:
                rotate 0
                linear 0.1 rotate -360 subpixel True pos (-2084, 960) 
            k "goodbye bastard forever"
    $ location = 7
    $ count += 1
    stop music
    play music "audio/music/chapter_three/forest1.ogg" loop
    jump chapter_three_map

label chapter_three_herobrine_found:
    $ choice = 1
    call chapter_three_hide_map_buttons
    show ch03_herobrine_alter with dissolve:
        subpixel True pos (-117, -154) zoom 1.23 
    k "Yo are these minecraft blocks?"
    k "I gotta touch this shit lol"
    "And the retard touched the obvious spawner"
    k "bro what spawner, there are no zombies in the real world"
    hide ch03_herobrine_alter

    show ch03_herobrine1 with dissolve:
        subpixel True pos (643, 38) zoom 1.44 
    hb "What do you fucking want you cocksucker!"
    k "I like minecraft"
    hb "I am going to kidnap you, cut off your legs, and send you to my dungeon"
    k "lol mad cuz bad"
    hb "?"
    k "you don't have legs so you are projecting that onto me"
    hb "..."
    hb "bye"
    hide ch03_herobrine1
    jump chapter_three_map
label chapter_three_hide_map_buttons:
    hide screen clickable_chapter_three_jewel_osco
    hide screen clickable_chapter_three_house
    hide screen clickable_chapter_three_mail
    hide screen clickable_chapter_three_herobrine
    return

