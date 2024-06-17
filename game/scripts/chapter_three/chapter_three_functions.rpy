# Extra Code to make chapter_three's code nicer, these functions are for one time events in Chapter three
# Python Code
init python:
    def chapter_three_jewels_mark(id):
        chapter_three_jewels_check[id] = True


#Renpy Code
screen clickable_chapter_three_jewel_osco():
    imagebutton:
        pos (611, 20) 
        at Transform(yzoom = 1.0, zoom = 0.07)
        idle "images/ch03jewel.jpg"
        hover "images/ch03jewel.jpg"
        action Jump("chapter_three_jewel_osco")

label chapter_three_jewel_osco:
    call chapter_three_hide_map_buttons
    #show ch03jewel:
        #subpixel True pos (611, 20) yzoom 1.0 zoom 0.07
    if count >= 0:
        k "I SHOULD NOT GO BACK THERE"
        k "THEY MIGHT KILL ME"
        jump chapter_three_map
    scene ch03jewel_outside:
        subpixel True xzoom 1.32 zoom 1.23 
    k "Ugh... I guess I can try working in Grocery"
    show brian1 with dissolve:
        subpixel True pos (668, 491) 
    b "Yo What is up Kody?"
    
    show brian1:
        linear 0.15 subpixel True pos (103, 486) 
    show kody with dissolve:
        subpixel True pos (1145, 556) yrotate 180.0 
    k "oh great what is the lopunny lover doing here?"
    b "i work here : D"
    k "huh?"
    b "You thought making fun of me for two chapters and it was all a meme?"
    k "yes"
    b "fuck you"
    b "yeah well I work here, what can I help you with?"
    k "uh"
    k "gimmie job or i will show off my mogmaxxing"
    b "Uh let me see what I can do for you!"
    "Some Time Passes"
    scene ch03jewel1 with dissolve:
        subpixel True xzoom 1.2 zoom 2.58 
    show brian1:
        subpixel True pos (260, 306) 
    show kody:
        subpixel True pos (1116, 361) yrotate 180.0 


    b "okay so I talked with CEO Osco and" #TODO have this auto-advance
    k "wait you talked with CEO Mr. Jewel Osco?"
    b "yes"
    k "How does a cashier talk to the ceo for a simple job at one location of a multinational location?"
    b "yeah its a really bad bottleneck"
    b "but!"
    k "hey butts"
    b "SHUT IT"
    b "The point is"
    b "I got you a trial job"
    k "so an internship at jewel osco"
    b "no its a trial job"
    b "just help people out and if Mr. Osco likes it"
    b "He will give you a job"
    k "bet thats so FREE!"
    "Go help out Jewel Osco Customers"
    "Show what you are made of!"
    "YEAH!"
    $ count2 = 0
    jump ch03_jewel_main
    label ch03_jewel_main:
        call chapter_three_jewel_hide_all_buttons
        $ location = 1
        scene ch03jewel1 with dissolve:
            subpixel True xzoom 1.2 zoom 2.58
        call chapter_three_jewel_restore_buttons(location)
        label ch03_jewel_main_1:
        if chapter_three_jewels_check[0] == False:
            show screen clickable_chapter_three_wet_floor_sign
        elif count2 == 5:
            jump chapter_three_jewel_end
        "You are currently located in the middle of Jewel Osco!"
        jump ch03_jewel_main_1

    label ch03_jewel_grocery:
        call chapter_three_jewel_hide_all_buttons
        $ location = 2
        scene ch03jewel2 with dissolve:
            subpixel True xzoom 1.17 zoom 2.61 
        call chapter_three_jewel_restore_buttons(location)
        label ch03_jewel_grocery_1:
        if chapter_three_jewels_check[1] == False:
            show screen clickable_chapter_three_grocery_cart
        "You are currently located in the Grocery Section of Jewel Osco!"
        jump ch03_jewel_grocery_1

    label ch03_jewel_meat:
        call chapter_three_jewel_hide_all_buttons
        $ location = 3
        scene ch03jewel3 with dissolve:
            subpixel True yzoom 1.17 zoom 1.41 
        call chapter_three_jewel_restore_buttons(location)
        label ch03_jewel_meat_1:
        if chapter_three_jewels_check[2] == False:
            show screen clickable_chapter_three_butcher
        "You are currently located in the Meat Section of Jewel Osco!"
        jump ch03_jewel_meat_1

    label ch03_jewel_shelf:
        call chapter_three_jewel_hide_all_buttons
        $ location = 4
        scene ch03jewel4 with dissolve:
            subpixel True xzoom 1.2 zoom 2.71
        call chapter_three_jewel_restore_buttons(location)
        label ch03_jewel_shelf_1:
        if chapter_three_jewels_check[3] == False:
            show screen clickable_chapter_three_candy
        "You are currently located in the Shelfed Goods Section of Jewel Osco!"
        jump ch03_jewel_shelf_1

    label ch03_jewel_checkout:
        call chapter_three_jewel_hide_all_buttons
        $ location = 5
        scene ch03jewel5 with dissolve:
            subpixel True yzoom 1.06 zoom 2.55
        call chapter_three_jewel_restore_buttons(location)
        label ch03_jewel_checkout_1:
        if chapter_three_jewels_check[4] == False:
            show screen clickable_chapter_three_customer
        "You are currently located in the Checkout Section of Jewel Osco!"
        jump ch03_jewel_checkout_1

    #These are buttons used to walk around Baldi's school house
    screen clickable_button_jewel_chapter_three_up(origin):
        imagebutton:
            xalign 0.5
            yalign -0.05
            idle "images/ArrowUpPress.png"
            hover "images/ArrowUpPress.png"
            if origin == 1:
                action Jump("ch03_jewel_meat")
            else:
                action Jump("ch03_jewel_main")

    screen clickable_button_jewel_chapter_three_down(origin):
        imagebutton:
            xalign 0.5
            yalign 0.995
            idle "images/ArrowDownPress.png"
            hover "images/ArrowDownPress.png"
            if origin == 3:
                action Jump("ch03_jewel_main")
            else:
                action Jump("ch03_jewel_checkout")

    screen clickable_button_jewel_chapter_three_left(origin):
        imagebutton:
            xalign 0.005
            yalign 0.5
            idle "images/ArrowLeftPress.png"
            hover "images/ArrowLeftPress.png"
            if origin == 4:
                action Jump("ch03_jewel_main")
            else:
                action Jump("ch03_jewel_grocery")

    screen clickable_button_jewel_chapter_three_right(origin):
        imagebutton:
            xalign 0.995
            yalign 0.5
            idle "images/ArrowRightPress.png"
            hover "images/ArrowRightPress.png"
            if(origin == 2):
                action Jump("ch03_jewel_main")
            else: 
                action Jump("ch03_jewel_shelf")
    screen clickable_chapter_three_wet_floor_sign():
        imagebutton:
            pos (991, 561)
            idle "images/ch03_wetfloorsign.png"
            hover "images/ch03_wetfloorsign.png"
            action Call("chapter_three_wet_floor_sign")
    screen clickable_chapter_three_grocery_cart():
        imagebutton:
            pos (1071, 451) 
            at Transform(rotate = -36.0 , zoom = 0.7)
            idle "images/ch03_cart.png"
            hover "images/ch03_cart.png"
            action Call("chapter_three_cart")
    screen clickable_chapter_three_butcher():
        imagebutton:
            pos (55, 326)
            idle "images/ch03_butcher.png"
            hover "images/ch03_butcher.png"
            action Call("chapter_three_butcher")
    screen clickable_chapter_three_candy():
        imagebutton:
            pos (1390, 475)
            idle "images/ch03_candy.png"
            hover "images/ch03_candy.png"
            action Call("chapter_three_candy")
    screen clickable_chapter_three_customer():
        imagebutton:
            pos (1106, 226) 
            at Transform(zoom = 1.38)
            idle "images/ch03_woman.png"
            hover "images/ch03_woman.png"
            action Call("chapter_three_customer")

    # Location One Event
    label chapter_three_wet_floor_sign:
        call chapter_three_jewel_hide_all_buttons
        show ch03_wetfloorsign:
            subpixel True pos (991, 561)
        k "Hmmmm"
        k "Here is a wet-floor sign"
        k "It'd be really funny if I just..." #TODO, knock-over sfx
        hide ch03_wetfloorsign
        k "Knock this over"
        k ">:)"
        show ch03_man:
            subpixel True pos (-298, 293) zoom 0.54
            linear 0.45 subpixel True xpos 962 
            linear 0.65 subpixel True pos (953, 63) rotate -90
            linear 0.35 subpixel True pos (936, 541) rotate 270.0 #sfx here as well
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
        call chapter_three_jewel_restore_buttons(location)
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
        k "alright time to piss into the groceries >:)" #TODO SFX
        hide ch03_cart
        k "well that was fun"
        k "I should dip!"
        $ chapter_three_jewels_mark(1)
        call chapter_three_jewel_restore_buttons
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
        k "Elon Musk"
        jb "We literally cannot do that"
        k "guess you are fired bozo"
        jb "I need this job to feed my 3 children"
        k "GET OUT BOZO!"
        jb "okay sir"
        $ chapter_three_jewels_mark(2)
        call chapter_three_jewel_restore_buttons(location)
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
        k "ate it real fast" #TODO chomp sound effect
        hide ch03_candy
        k "That was some good candy :)"
        $ chapter_three_jewels_mark(3)
        call chapter_three_jewel_restore_buttons(location)
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
        hide ch03_woman
        k "ez rizz"
        $ chapter_three_jewels_mark(4)
        call chapter_three_jewel_restore_buttons(location)
        $ count2 += 1
        return
    # Restores buttons once they are closed when an interaction starts/restores button once we swap areas
    label chapter_three_jewel_restore_buttons(current_location):
        if current_location == 1:
            show screen clickable_button_jewel_chapter_three_up(location)
            show screen clickable_button_jewel_chapter_three_down(location)
            show screen clickable_button_jewel_chapter_three_left(location)
            show screen clickable_button_jewel_chapter_three_right(location)
        elif current_location == 2:
            show screen clickable_button_jewel_chapter_three_right(location)
        elif current_location == 3:
            show screen clickable_button_jewel_chapter_three_down(location)
        elif current_location == 4:
            show screen clickable_button_jewel_chapter_three_left(location)
        elif current_location == 5:
            show screen clickable_button_jewel_chapter_three_up(location)
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
        call chapter_three_jewel_hide_all_buttons
        show ch03_ceo with dissolve:
            subpixel True
        jceo "Hello Kody"
        k "Who dafaq are you?"
        k "looking like a straight up bozo"
        jceo "I would like to say something"
        jceo "and that is YOU ARE FUCKING FIRED"
        jceo "YOU ATE OUR MERCHANDISE, GAVE FREE PRODUCE AWAY, FIRED AN EMPLOYEE, BROKE HEALTH SAFETY PROTOCOL, AND PISSED IN SOMEONE's FOOD!"
        k "yeah and it was awesome"
        jceo "You are FUCKING BANNED FROM EVERY JEWEL OSCO FOR EVER"
        jceo "YOU HAVE 5 MINUTES TO LEAVE UNTIL I CALL THE FUCKING POLICE!"
        k "Fine jeez"
        k "Can i still have my paycheck?"
        jceo "WHAT DO YOU FUCKING THINK?"
        k "yes"
        jceo "..."
        k "okay i will go"
        scene ch03map:
            subpixel True pos (-63, -63) xzoom 1.31 yzoom 1.14 zoom 3.14 blur 3.48
        "Well that coulda gone better"
        k "yeah I FUCKING KNOW!"
        $ count = 1
        jump chapter_three_map

label chapter_three_hide_map_buttons:
    hide screen clickable_chapter_three_jewel_osco
    return
