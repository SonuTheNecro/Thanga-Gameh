# Extra Code to make chapter_one's code nicer, these functions are for one time events in Chapter One

#Python Code
init python:
    from random import randint
    from enum import Enum
    #Code for the Street Situation's rng, better in Python
    def street1_random():
        random_number = randint(2,6)
        count = 0
        while count < random_number:
            renpy.sound.play("audio/sound/chapter_one/street1.ogg")
            random_sentence = randint(0,10)
            if random_sentence == 0:
                renpy.say("Thanga", "Holy shit we are lost, let's just walk endlessly into the forest")
                renpy.say("B-Bop", "What?  Lets not do that, a Street leads to something, we just gotta keep Following it")
            if random_sentence == 1:
                renpy.say("Kody", "Thang I am so hungry please")
                renpy.say("Thang", "You just had a whole-ass meal wtf")
            if random_sentence == 2:
                renpy.say(None,"The moon is rising slowly, our three dumbasses are miserable")
                renpy.say(None,"They are Hungry, Sleepy, Tired, and mostly NOT remorseful for murdering siete")
            if random_sentence == 3:
                renpy.say(None,"They say Wolves are into weak frail humans who have some juicy meat")
                renpy.say("TactialVortex", "Ayo that is kinda sus")
            if random_sentence == 4:
                renpy.say(None, "The Blood Moon is Rising!")
                renpy.say(None, "Skeletron Prime has Awoken!")
                renpy.say(None, "Supreme Deity Tescoblade_ has challenged you!")
                renpy.say(None, "A new Challenger Appears!")
                renpy.say(None, "Melee Fox!")
            if random_sentence == 5:
                renpy.say("Thanga", "Thanks Brian, now I get to miss Slippi Ranked Today wtf man")
                renpy.say("B-Bop", "THAT?")
                renpy.say("B-Bop", "That is what you are worried about?")
                renpy.say("B-Bop", "You are driving me crazy... Ugh")
            else:                 
                renpy.say(None,"...")
                renpy.say(None,"...")
                renpy.say(None,"...")
            count += 1
            renpy.say(None,f"You have been in the woods for {count} Hours!")
            renpy.sound.stop()
    def baldi_shoot(count):
        random_number = randint(count,count*3)
        count = 0
        while count < random_number:
            renpy.sound.play("audio/sound/chapter_one/gun_shot1.ogg")
            renpy.pause(0.075)
            count += 1
    def baldi_last_answer_check(choice):
        count1 = False
        while not count1:
            try:
                choice = int(choice)
                count1 = True
            except ValueError:
                choice = renpy.input("THAT ISN'T A VALID NUMBER! TRY AGAIN!:", length=17)
        return choice

    def chapter_one_item_check(item):
        return key_items.get(item, ItemState.NOT_OBTAINED) == ItemState.OBTAINED

    def chapter_one_obtain_item(item):
        key_items[item] = ItemState.OBTAINED
    def chapter_one_unobtain_item(item):
        key_items[item] = ItemState.NOT_OBTAINED

    def chapter_one_clean_dirt(id):
        chapter_one_dirt_piles[id] = True
        renpy.call("chapter_one_dirt", id)

    
# Renpy Code
screen clickable_chapter_one_secret_lopunny(xpos, ypos, zoom):
    imagebutton:
        pos (xpos,ypos)
        at Transform(zoom = zoom)
        idle "images/lopunny1.png"
        hover "images/lopunny1.png"
        action Call("chapter_one_lopunny_check")

#The clickable panda giftcard in the car
screen clickable_chapter_one_giftcard():
    imagebutton:
        pos (1091, 793)
        at Transform(zoom = 0.04)
        idle "images/chapter_one/panda1.jpg"
        hover "images/chapter_one/panda1.jpg"
        action Call("chapter_one_panda_giftcard")

#The clickable SonuTheNecro in Subway
screen clickable_chapter_one_stn():
    imagebutton:
        pos (0.07, 0.69) 
        at Transform(zoom = 0.2, yrotate = 180)
        idle "images/sonuthenecro.png"
        hover "images/sonuthenecro.png"
        action Call("chapter_one_subway_conversation")

#These are buttons used to walk around Baldi's school house
screen clickable_button_baldi_chapter_one_up(origin):
    imagebutton:
        xalign 0.5
        yalign -0.05
        idle "images/ArrowUpPress.png"
        hover "images/ArrowUpPress.png"
        if origin == 1:
            action Jump("baldi_main_area")
        else:
            action Jump("baldi_math_puzzle")

screen clickable_button_baldi_chapter_one_down(origin):
    imagebutton:
        xalign 0.5
        yalign 0.995
        idle "images/ArrowDownPress.png"
        hover "images/ArrowDownPress.png"
        if origin == 5:
            action Jump("baldi_main_area")
        else:
            action Jump("baldi_exit")

screen clickable_button_baldi_chapter_one_left(origin):
    imagebutton:
        xalign 0.005
        yalign 0.5
        idle "images/ArrowLeftPress.png"
        hover "images/ArrowLeftPress.png"
        if origin == 3:
            action Jump("baldi_main_area")
        else:
            action Jump("baldi_faculty")

screen clickable_button_baldi_chapter_one_right(origin):
    imagebutton:
        xalign 0.995
        yalign 0.5
        idle "images/ArrowRightPress.png"
        hover "images/ArrowRightPress.png"
        if(origin == 4):
            action Jump("baldi_main_area")
        else: 
            action Jump("baldi_classroom")

#The Code for the key present in the main area
screen clickable_key_chapter_one():
    imagebutton:
        pos(0.63, 0.7)
        at Transform(zoom = 0.08)
        idle "images/key1.png"
        hover "images/key1.png"
        action Call("chapter_one_key")

#The Code for an early exit using the main area key1
screen clickable_baldi_exit():
    imagebutton:
        pos (0.6, 0.23) 
        at Transform(zoom = 0.9)
        idle "images/chapter_one/baldi_exit_hover.png"
        hover "images/chapter_one/baldi_exit_hover.png"
        action Call("chapter_one_early_exit")

#The Code for the mop found in the exit area
screen clickable_chapter_one_mop():
    imagebutton:
        pos (0.21, 0.29)
        idle "images/chapter_one/mop.png"
        hover "images/chapter_one/mop.png"
        action Call("chapter_one_mop")

#The code for the random dirt that appears throughout the map
screen clickable_chapter_one_dirt(xpos, ypos, zoom_level, id):
    imagebutton:
        pos(xpos, ypos)
        at Transform(zoom = zoom_level)
        idle "images/chapter_one/dirt.png"
        hover "images/chapter_one/dirt.png"
        action Function(chapter_one_clean_dirt, id)

#Code for God Of sweep NPC, after you clean him up
screen clickable_chapter_one_god_of_sweep():
    imagebutton:
        pos(396,358)
        at Transform(zoom = 1.21)
        idle "images/chapter_one/godofsweep.png"
        hover "images/chapter_one/godofsweep.png"
        action Call("chapter_one_post_cleanup")
#Code for the button for Principal of the Thing after you get the book
screen clickable_chapter_one_principal():
    imagebutton:
        pos(0.11,0.34)
        idle "images/chapter_one/principal_of_the_thing_outline.png"
        hover "images/chapter_one/principal_of_the_thing_outline.png"
        action Call("chapter_one_pott_class")

screen clickable_chapter_one_alarmclock():
    imagebutton:
        pos(40,301)
        at Transform(zoom = 1.68)
        idle "images/chapter_one/alarm_clock.png"
        hover "images/chapter_one/alarm_clock.png"
        action Call("chapter_one_alarm_clock")
screen clickable_chapter_one_itsabully():
    imagebutton:
        pos(776, 330)
        at Transform(zoom = 1.46)
        idle "images/chapter_one/itsabully_outline.png"
        hover "images/chapter_one/itsabully_outline.png"
        action Call("chapter_one_bully")
screen clickable_chapter_one_playtime():
    imagebutton:
        pos(358,601)
        xanchor 270
        at Transform(zoom = 0.66)
        idle "images/chapter_one/playtime_outline.png"
        hover "images/chapter_one/playtime_outilne.png"
        action Call("chapter_one_playtime")
screen clickable_chapter_one_thanga():
    imagebutton:
        pos (1496, 306)
        at Transform(yrotate = 180.0)
        idle "images/thanga2.png"
        hover "images/thanga2.png"
        action Call("chapter_one_thanga")

screen clickable_chapter_one_brian():
    imagebutton:
        pos (1433, 385)
        xanchor 270
        at Transform(zoom = 0.83)
        idle "images/brian1.png"
        hover "images/brian1.png"
        action Call("chapter_one_brian")

label chapter_one_lopunny_check():
    hide screen clickable_chapter_one_secret_lopunny
    play sound "audio/sound/chapter_one/item_pickup.ogg"
    $ lopunny_count += 1
    "You have found a lopunny!"
    "Be sure to find them all!"
    return

#The menu for the Panda Express giftcard in the car
label chapter_one_panda_giftcard():
    hide screen clickable_chapter_one_giftcard
    "You find a Panda Express Gift Card"
    menu:
        "Take":
            play sound "audio/sound/chapter_one/item_pickup.ogg"
            "You have acquired a Panda Express Gift Card!"
            $ chapter_one_obtain_item("chapter_one_giftcard")
            k "Yeah I found it, where did you even get this?"
            b "Uh If I remember correctly..."
            b "I think Matt gave it to me since he did not want it"
            return
        "Steal it and Lie":
            "You have chosen to steal this Panda Express Gift Card"
            k "Uh you said Panda Express Giftcard?"
            b "Yes"
            k "It is just not here"
            b "well that sucks"
            b "i guess i won't be getting my mother a nice gift for mothers' day"
            t "Brian I can buy this one if you'd like"
            b "nah nah nah, i don't wanna have to pay you back"
            k "(BRO IS THIS KID BROKE? LIKE LOLLLLLLLL!)"
            t "What you watching back there?"
            k "!"
            k "What do you mean?"
            t "You are giggling back there"
            k "Oh I was watching a tiktok of someone breaking lego fall guys and it falls. \n It is really funny"
            return 

# This is the conversation for the first visit in baldi's schoolhouse
label baldi_main_area_first_visit():
    show screen clickable_chapter_one_secret_lopunny(1776,913,0.36)
    
    baldi "Welcome to my schoolhouse!"
    baldi "So explain to me what this Lopunny is!"
    b "Okay so its a brownish bunny?"
    baldi "Oh-ho-ho"
    baldi "So it is like the chocolate easter bunny"
    baldi "He was a GREAT drinking buddy!"
    baldi "Tell me more about this fella"
    b "And the bunny has this HUGE Oppai and Gyatt."
    b "Like I am like Gyatt damn that is holy!"
    baldi "..."
    t "..."
    k "..."
    baldi "I don't know what any of those words mean but I think I got what you are looking for!"
    baldi "Now you gotta solve my math problem!"
    hide screen clickable_chapter_one_secret_lopunny
    stop music
    play music "audio/music/chapter_one/baldi_math.ogg"
    scene baldi_q1 with dissolve:
        subpixel True pos (-333, -0.26) 
    baldi "What is 4 - 4?"
    $ choice = renpy.input("What is 4-4?", length = 10)
    if choice != "0":
        play sound "audio/sound/chapter_one/glock_magchange.ogg"
        show baldi_q1:
            subpixel True blur 7.82 
        show baldi2:
            subpixel True xpos 702
        show gun2:
            subpixel True pos (361, 193)
        baldi "You are stupid as fuck!"
        stop sound
        baldi "begone"
        show gunflare:
            subpixel True
        $ baldi_shoot(10)
        # baldi "How you mess up math this bad?"
        jump game_over
    baldi "WOW!"
    baldi "You are Incredible!"
    baldi "Problem #2!"
    scene baldi_q2 with dissolve:
        subpixel True pos (-333, -0.26)
    baldi "What is the value of the mathematical constant e, rounded to three decimal places?"
    $ choice = renpy.input("What is the value of the mathematical constant e, rounded to three decimal places?", length = 5)
    if choice != "2.718":
        play sound "audio/sound/chapter_one/glock_magchange.ogg"
        show baldi_q2:
            subpixel True blur 7.82 
        show baldi2:
            subpixel True xpos 702
        show gun2:
            subpixel True pos (361, 193)
        baldi "Wow you suck at mathematics!"
        baldi "DIE!"
        show gunflare:
            subpixel True
        $ baldi_shoot(15)
        jump game_over
    baldi "Incredible!"
    baldi "You might even be smarter than me!"
    baldi "Time for problem 3!"
    k "LISTEN HERE OLD BALD FACE FUCKER!"
    k "WE DO NOT GIVE A SHIT ABOUT YOUR MATH PROBLEMS!"
    k "Give brian his fucking lopunny then give us the car key then we can fucking leave!"
    k "and for your information, math is a useless skill!"
    k "Why would I learn math when I have chatgpt and a calculator in my pocket"
    k "imagine working for 60k a year when I make youtube videos and get 250k a year you bozo"
    k "no bread and no lie"
    t "..."
    b "..."
    baldi "..."
    t "I am so sorry for him, hes stupid"
    baldi "No-no"
    baldi "Don't be sorry, I got a hard problem for you!"
    scene baldi_q3 with dissolve:
        subpixel True pos (-333, -0.26)
    baldi "一堆小數3攻擊等176於什麼?"
    b "I don't know..."
    t "THOSE AREN'T LETTERS!"
    scene baldi_q3_mad with dissolve:
        subpixel True pos (-333, -0.26)
    stop music
    baldi "GET THE FUCK OUT OF HERE YOU USELESS BITCH, I AM LOCKING THE DOORS SO YOU CANNOT LEAVE!"
    b "so how do we leave if you are locking the doors..."
    baldi "I WILL STARVE ALL OF YOU FUCKERS AND MAKE MATH PROBLEMS OUT OF YOUR CORPSES"
    $ count = -1
    play music "audio/music/chapter_one/baldi_main.ogg"
    jump baldi_main_area
#The renpy code when you attempt to leave
label chapter_one_early_exit:
    call chapter_one_hide_buttons from _call_chapter_one_hide_buttons_1
    hide screen clickable_baldi_exit
    show baldi_exit_hover:
        subpixel True pos (0.6, 0.23) zoom 0.9
    k "Alright let's leave"
    t "alright bet"
    hide baldi_exit_hover
    show baldi_exit with dissolve:
        subpixel True matrixcolor InvertMatrix(1.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    show baldi_exit_hover:
        subpixel True pos (0.6, 0.23) zoom 0.9 matrixcolor InvertMatrix(1.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    call dio_time_stop
    b "NOT AGAIN!"
    show cody:
        xalign 1.7
        subpixel True crop_relative True  rotate 0.0 crop (0.42, -0.13, 0.33, 0.37)
        linear 0.35 subpixel True pos (0.99, 0.28)
    c "LET ME IN, LET ME FUCKING IN!!!!!"
    b "I dont think we should let him in"
    t "And I'm like 99.9\% sure we should NOT go out there"
    c "I WILL GET REVENGE FOR SIETE! LET ME IN YOU COCKSUCKERS"
    t "Okay I am 100\% sure we are NOT going out there with that crazy psycho!"
    b "Yeah i'm staying here bye"
    hide baldi_exit_hover
    scene baldi_exit with dissolve:
        subpixel True pos (-9, -234) zoom 0.92
    call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_5
    call screen clickable_baldi_exit
    return
#Renpy code when you get the key to attempt to leave early!
label chapter_one_key():
    call chapter_one_hide_buttons from _call_chapter_one_hide_buttons_2
    hide clickable_key_chapter_one
    show key1:
        subpixel True pos(0.63, 0.7) zoom 0.08
    k "Yo sweet the key to leave"
    k "YO BRIAN THANG GET OVER HERE, THIS BALD MOTHERFUCKER LEFT THE KEY HERE LETS JUST LEAVE!"
    play sound "audio/sound/chapter_one/item_pickup.ogg"
    $ chapter_one_obtain_item("chapter_one_key")
    play sound "audio/sound/chapter_one/item_pickup.ogg"
    "You have obtained Baldi's Key to the Schoolhouse!"
    stn "WHAT!"
    stn "YOU LEFT THE KEY JUST OUT IN THE OPEN WHAT THE ACTUAL FUCK!"
    tv "Nah nah just wait for this"
    hide screen clickable_key_chapter_one
    hide key1
    call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_6
    return
#Getting the mop
label chapter_one_mop():
    call chapter_one_hide_buttons from _call_chapter_one_hide_buttons_3
    hide clickable_chapter_one_mop
    hide baldi_exit_hover
    hide screen clickable_baldi_exit
    show mop:
        subpixel True pos (0.21, 0.29)
    "You have obtained..."
    "A rather smelly mop"
    $ chapter_one_obtain_item("chapter_one_mop")
    $ count = 0
    hide screen clickable_chapter_one_mop
    show godofsweep with dissolve:
        subpixel True pos (526, 0.0) zoom 3.16 
    gos "GOTTA SWEEP SWEEP SWEEP!"
    gos "WHERE IS MY FUCKING MOP!"
    gos "OI YOU FUCKING WANKER"
    gos "SINCE YOU TOOK MY FUCKING MOP, YOU CLEAN THIS SHIT UP AND FIND ME WHEN YOU CLEAN THIS MAP UP"
    k "But me and my friends didn't make the mess, we just got here"
    gos "WELL I HEARD TONS OF YELLING SO I DON'T CARE WHO MADE IT BUT I AM GOING TO DO KILL EVERYONE IF IT ISN'T CLEANED!"
    menu:
        "Yes Sir":
            k "I got it sir"
            k "Yes Sir got it Sir!"
            gos "GOOD! HAVE FUN GARBAGE BOY!"
        "God No":
            k "God No, I never cleaned anything at home"
            k "I ain't starting at a random elementary school"
            show gun2:
                subpixel True pos (755, 393) yrotate 180.0
            gos "EXCUSE ME YOU BITCH?"
            gos "YOU WLL PAY!"
            show gunflare:
                subpixel True pos (600, 205) 
            $ baldi_shoot(16)
            hide screen clickable_baldi_exit
            hide screen clickable_button_baldi_chapter_one_up
            jump game_over
    hide godofsweep with dissolve
    "Were... Were you just given chores to do?"
    hide mop
    call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_7
    if chapter_one_item_check("chapter_one_key"):
        show screen clickable_baldi_exit
    return
# cleaning up all the dirt
label chapter_one_dirt(id):
    call chapter_one_hide_buttons from _call_chapter_one_hide_buttons_4
    hide clickable_chapter_one_dirt
    if id == 0:
        show dirt:
            subpixel True pos (0.03, 0.43) zoom 0.46
    elif id == 1:
        show dirt:
            subpixel True pos (0.75, 0.69) zoom 0.77
    elif id == 2:
        show dirt:
            subpixel True pos (0.7, 0.56) zoom 0.52
    elif id == 3:
        show dirt:
            subpixel True pos (0.01, 0.52) zoom 0.36
    k "How the hell does someone get a whole ass dirt pile in a school..."
    k "ugh, guess I have to clean this shit..."
    "You begin to tug at the dirt"
    if count == 0:
        "This is surprisingly Kody's first time cleaning up dirt ever in his life"
        "Kody is an incompotent fool"
        "He is also a lazy mogger.  Crazy combo!"
        k "I can also read the messages dumbass"
        "Yeah I know, you are lazy!"
    elif count == 1:
        k "This ain't my first rodeo"
        k "This is my SECOND rodeo!"
        k "I am so fucking sick at cleaning this dirt!"
    elif count == 2:
        k "Will cleaning dirt teach me better mog methods"
        questionmark "yes"
        k "Thank you entity eldrich being that's probably the final boss but it isn't written yet!"
        "Thats a Fourth Wall Break!"
        "Isn't this writing witty and comedic?"
        "I am like the next stanley parable"
        k "cap is calling!"
        $ chapter_one_obtain_item("chapter_one_cleanup")
    elif count == 3:
        k "I am so nasty dude"
        k "I am dropping outta school"
        k "Ima make a tiktok where I just clean shit!"
        t "I CAN HEAR YOU, NO ONE WOULD WATCH THAT!"
        k "mad?"
        k "cope?"
        k "Seethe?"
        t "SHUT THE FUCK UP KODY!"
        t "YOU WALK AROUND THE HOUSE IN NO UNDERWEAR!"
        k "yooooo that's a secret!"
        $ chapter_one_obtain_item("chapter_one_cleanup")
    elif count == 4:
        k "YOOOOOOOOOOOOO WE GOT A SPEEDRUNNER IN THE HOUSE!"
        k "Imagine this was the way to the secret ending, heh!"
        $ chapter_one_obtain_item("chapter_one_cleanup")
    $ count += 1
    "..."
    hide dirt
    "You have cleaned [count] dirt(s)!"
    k "Woohoo!"
    if chapter_one_item_check("chapter_one_cleanup") and not chapter_one_item_check("chapter_one_book"):
        "You have cleaned up all the dirt!"
        k "Yeah no shit narrator, i was there!"
        "I am giving hints imagine this was a 12 room Ace Attorney Map, you'd be crying rn"
        k "Yeah sorry sorry"
        "You should probably give the mop back to big broom guy"
        k "Didn't he have a name?"
        "No one remembers it lol"
        k "Touche"
    call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_8
    return
# The God of Sweep after you cleanup all the dirt
label chapter_one_post_cleanup():
    call chapter_one_hide_buttons() from _call_chapter_one_hide_buttons_5
    hide screen clickable_chapter_one_god_of_sweep
    hide screen clickable_baldi_exit
    show baldi_exit_hover:
        subpixel True pos (0.6, 0.23) zoom 0.9
    show godofsweep with dissolve:
        subpixel True pos (526, 0.0) zoom 3.16
    if count2 == 2:
        gos "HOW IS MY FAVORITE WANKER!"
        k "I need help :)"
        gos "OH WITH WHAT?"
        k "This hot girl has her jumprope dirty, can you clean it"
        gos "GOT IT SAY NO MORE FAM"
        $ count2 = 3
    elif not chapter_one_item_check("chapter_one_book"):
        gos "AYO YOU FUCKING WANKER GET OVER HERE!"
        k "(Oh god, what did I do this time?)"
        gos "YOU MAKE ME A 'REA SO CLEAN I CAN COOK MY BARBEECOO ON MI THONGS"
        k "???"
        gos "OH FUCK OFF YOU KNOW WHAT I SAID"
        k "Speak a real language..."
        gos "Oh my mistake sir/madam,I waz junder da impresion dat everyon' understood the languag' of Australian"
        gos "sory for 'ot bing posh enuff"
        k "Go back please"
        gos "ALRIGHT THAT'S WHAT I THOUGHT YOU WANKER!"
        gos "WELL THAT AIN'T THE POINT RIGHT NOUGH!"
        gos "I GUESS I OWE YE SMTH REAL GOOD"
        k "Finally some money so i can whale on roblox"
        k "Or genshin impact"
        k "Big chocies for the life of Kody!"
        gos "WHAT NO, HAVE THIS BOOK I FOUND EARLIER!"
        k "I do not want a book"
        gos "I THINK THE OLD MAN AROUND HERE WAS LOOKING FOR A BOOK!"
        k "Thang?"
        gos "NO THE GUY WHO IS POINTING UP"
        gos "MAYBE YOU CAN GET SOMETHING OUT OF HIM"
        gos "WELL I'M DONE NOW"
        gos "IF YOU NEED ANY HELP, YOU KNOW WHERE TO FIND ME!"
        play sound "audio/sound/chapter_one/item_pickup.ogg"
        $ chapter_one_obtain_item("chapter_one_book")
        "You have obtained a book!"
        k "what book is it though?"
        "You have eyes..."
        k "Okay it says... "
        k "Mein Kampf?"
        k "What is that?"
        "Google it after so you can teach yourself history!"
    elif chapter_one_item_check("chapter_one_book"):
        gos "THANKS AGAIN FOR THE HELP LA KODY"
        gos "IF YOU NEED MY HELP AGAIN, JUST RING THE OL BELL"
        k "What is a bell?"
    hide godofsweep
    hide baldi_exit_hover
    call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_9
    return
#Principal of the thing
label chapter_one_pott_class():
    call chapter_one_hide_buttons from _call_chapter_one_hide_buttons_6
    hide screen clickable_chapter_one_principal
    show principal_of_the_thing:
        subpixel True pos (0.11, 0.34) 
    if not chapter_one_item_check("chapter_one_book"):
        k "Yo bitch let me in the side room, im tryna talk to my friends who are locked in"
        pott "I don't have the key man :("
        k "HOW?!?"
        k "ARENT YOU THE PRINCIPAL OF THE PLACE?"
        pott "yes"
        pott "Go find my storage case with my key"
        k "??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"
        k "What the fuck does it even look like"
        pott "It is a big big book about German History!"
        pott "I teach it to my son everyday!"
        k "got it sir"
    elif chapter_one_item_check("chapter_one_book") and not chapter_one_item_check("chapter_one_faculty"):
        pott "Yo is that my book?"
        k "Soooo"
        k "Why are you reading a book about this kinda thing?"
        pott "Who said I was reading the book?"
        pott "If you open the book, there is a key to the faculty room!"
        k "But why..."
        pott "No entering faculty rooms in the halls!"
        k "but we aren't in the halls..."
        pott "Well since you helped find the book, you can go into the faculty room if you'd like"
        pott "here ya go!"
        play sound "audio/sound/chapter_one/item_pickup.ogg"
        $ chapter_one_obtain_item("chapter_one_faculty")
        "You have obtained the key to the Faculty Room!"
        $ count2 = 0

    hide principal_of_the_thing
    call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_10
    return
#Entering the faculty for the first time
label chapter_one_faculty_first_enter():
    call chapter_one_hide_buttons from _call_chapter_one_hide_buttons_7
    show thanga2 with dissolve:
        subpixel True pos (531, 363) 
    show brian1 with dissolve:
        subpixel True pos (986, 356) 
    k "So uh what happened with you guys..."
    t "I think we are in detention..."
    k "wtf did you guys do"
    b "I threw dirt around the school from a potted plant because I was pissed"
    k "THAT WAS YOU?????????????????"
    b "yes why?"
    k "I JUST HAD TO CLEAN UP A BUNCH OF DIRT"
    t "I ran in the halls and I told the principal to kill himself..."
    t "He was not happy"
    t "also i've been listening to brian yapp and mald and cope and cry and seethe and sadge and goon and jelk an-"
    k "I get it I get it"
    k "He has problems"
    k "So did you guys find anything in here..."
    show thanga2:
        linear 0.5 subpixel True pos (1610, 361)
        yrotate 180.0 
    show alarm_clock with dissolve:
        subpixel True pos (40, 301) zoom 1.68 
    t "Well there is a big clock here"
    b "A comically large clock if you will"
    k "This clock looks important to this investigation!"
    k "Why are its hands missing?"
    k "noob clock lol"
    t "That is what we thought too"
    t "Maybe we have to find some new clock-hands for something"
    k "I will look around, brian can you look around the classroom, and Thang"
    t "ye"
    k "look around the faculty room"
    t "bet"
    k "TEAM POND ASSEMBLE!"
    t "..."
    b "..."
    k "what?"
    t "That was so cringe..."
    $ count2 += 1
    hide thanga2
    hide brian1
    hide alarm_clock
    call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_11
    return
#Code for the alarm clock in chapter one
label chapter_one_alarm_clock():
    call chapter_one_hide_buttons from _call_chapter_one_hide_buttons_8
    hide screen clickable_chapter_one_alarmclock
    show alarm_clock:
        subpixel True pos (40,301) zoom 1.68
    if chapter_one_item_check("chapter_one_hands") and not chapter_one_item_check("chapter_one_battery"):
        k "Let's start this bad boy"
        t "I am so excited"
        b "Big clock gaming"
        t "uh..."
        t "shouldn't this be ticking"
        k "uhh is it broken"
        b "Check its pulse"
        t "You retard, there is no pulse in clocks..."
        b "No i mean the battery"
        t "uh i don't think it has one..."
        k "FUCK OFF WITH THE PUZZLES HOLY SHIT CAN WE FUCKING FINISH???"
    elif chapter_one_item_check("chapter_one_hands") and chapter_one_item_check("chapter_one_battery"):
        k "Oh now its ticking"
        b "imagine this is a bomb about to kill of us"
        t "Why would you say that..."
        b "it isn't a bomb"
        t "how do you know?"
        b "Why would there be a disarmed bomb in a school?"
        t "I guess..."
        #DING!
        k "It has kids?"
        t "No you idiot, it opened something"
        $ rngint1 = renpy.random.randint(10,20) * 2
        t "It says the answer is x = [rngint1 /2], y = [rngint1+7], z = [rngint1*3]"
        $ chapter_one_obtain_item("chapter_one_clock")
        k "NO WAYYYY WE GOTTA DO MATHHHHHHHHHHHHHH"
        b "i got this"
        t "no you dont"
    else:
        k "So this is it..."
        k "The weapon that is supposed to extinct all of humanity..."
        k "The warhead..."
        t "you are stupid, it's just a clock puzzle we gotta solve"
    hide alarm_clock
    call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_12
    return
#Code for the bully in the main area
label chapter_one_bully():
    call chapter_one_hide_buttons from _call_chapter_one_hide_buttons_9
    hide screen clickable_chapter_one_itsabully
    show itsabully:
        subpixel True pos(776, 330) zoom 1.46
    if chapter_one_item_check("chapter_one_giftcard") or chapter_one_item_check("chapter_one_food"):
        itsabully "OOOO THAT LOOKS GOOD!"
        k "(What?  This is just shitty gum on the floor)"
        k "Uh yeah i want those hands!"
        itsabully "ugh fine, you can have it"
        play sound "audio/sound/chapter_one/item_pickup.ogg"
        $ chapter_one_obtain_item("chapter_one_hands")
        "You have received the clock's hands.  Time to fix that clock!"
        itsabully "Owugh"
        itsabully "Bully doesn't feel good"
        k "not my problem"
        itsabully "I need to go to the bathroom..."
        show itsabully:
            linear 0.76 subpixel True pos (460, 225) zoom 4.25 
        itsabully "Where is the bathroom!"
        k "To the right!"
        show itsabully:
            linear 0.45 subpixel True pos (2143, 225) zoom 4.25 
        itsabully "Thanks man!"
        k "loser..."
        k "its to the left >:)"
    else:
        itsabully "GIVE ME SOMETHING GREAT TO EAT!"
        k "This guy is my hero"
        k "Anyway, I wanna answer Baldi's Solution"
        itsabully "hmmm, I want food..."
        k "ill trade you for my mewing and mogging lessons"
        itsabully "Tempting but not interested"
        itsabully "I got some hands for a toy train and I'll trade you for some food"
    hide itsabully
    call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_13
    return
#Code for playtime in the main area post faculty
label chapter_one_playtime():
    call chapter_one_hide_buttons from _call_chapter_one_hide_buttons_10
    hide screen clickable_chapter_one_playtime
    show playtime:
        subpixel True pos (413, 76) zoom 1.57
    if count2 == 1:
        pt "Let's play!"
        k "Fuck off, I can't play jumprope"
        pt "Why?"
        k "I cannot because I am busy mogging"
        pt "Can you please help :)"
        k "(Holy shit a girl smiled at me)"
        k "What do you need help with young lady!"
        pt "My jump-rope is covered in gum :("
        pt "can you clean it"
        k "hell nah i do not clean shit, i just cleaned dirt around the map, why would I help you"
        pt "pls"
        pt "ill be best friend :)"
        k "(omg i gotta do this W RIZZ)"
        k "you got it queen!"
        $ count2 = 2
    elif count2 == 2:
        pt "plz i am big sad"
        k "ok ok ok, who would help clean stuff though?"
        k "I got no idea tbh"
    elif count2 == 3:
        show playtime:
            linear 0.3 subpixel True xpos 935 
        show godofsweep with dissolve:
            subpixel True pos(58, 0.06) zoom 3.16
        gos "Oh right where is this umbrella..."
        pt "its a jump-rope"
        gos "alright, here is this vaccumm and its clean"
        pt "that is some silent vaccum"
        k "wow"
        gos "anyways bye"
        gos "oh yeah before i go"
        gos "have this!"
        play sound "audio/sound/chapter_one/item_pickup.ogg"
        "You have been given... some gum?"
        $ chapter_one_obtain_item("chapter_one_food")
        "gross."
        k "Why would I want this?"
        gos "Eat it or smth idk?"
        gos "give it to some fatty?"
        hide godofsweep
        show playtime:
            linear 0.6 subpixel True pos (413, 76) zoom 1.57
        k "anyways queen"
        k "can i get yo number!"
        pt "i dont have a phone but you can have my moms number"
        k "how old are you..."
        pt "9!"
        k "I am exiting this conversation"
    hide playtime
    call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_14
    return
#Code for Thanga post faculty
label chapter_one_thanga():
    call chapter_one_hide_buttons from _call_chapter_one_hide_buttons_11
    hide screen clickable_chapter_one_thanga
    show thanga2:
        subpixel True pos (821, 130) yrotate 180.0 zoom 1.45 
    if not chapter_one_item_check("chapter_one_wrench"):
        t "Yo kodster"
        k "yeah?"
        t "There is this cabinet in this desk?"
        k "Oh i have those in my school"
        t "they weren't in my school!"
        k "You are ninety-four years old, thats why"
        t "okay dude, what is this Thanga Slander"
        k "cope"
        t "Well that is besides the point..."
        t "I cannot open it, ima need some type of tool to open it..."
        k "Okay I can open it!"
        t "no you cannot"
        k "Well i am a master mogger and mewer, i got this"
        show baldi_faculty with vpunch and hpunch:
            subpixel True zoom 0.75 
        "..."
        "..."
        t "..."
        t "you got it?"
        k "no"
        t "so go get me that tool huh"
    elif chapter_one_item_check("chapter_one_wrench") and not chapter_one_item_check("chapter_one_clock"):
        k "yo thang"
        k "i got me some tool?"
        k "i am like the engineer from tf2 i can a scientest"
        t "..."
        t 'gimmie that'
        t "I am the one who knocks "
        show baldi_faculty with vpunch and hpunch:
            subpixel True zoom 0.75
        'The Cabinet opened'
        t "So let's see what is in here"
        t "The Truth about Thanga..."
        t "The Brian doxbin"
        t "uhhh and some random tax documents and some batteries"
        k "Gimmie them, i need em for my switch!"
        play sound "audio/sound/chapter_one/item_pickup.ogg"
        $ chapter_one_obtain_item("chapter_one_battery")
        "Kody has obtained batteries"
        "Now will kody give up those batteries"
        "that is the real question"
    elif chapter_one_item_check("chapter_one_clock"):
        k "Let's beat baldi!"
        t "You mean I have to with my math skills..."
    hide thanga2
    call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_15
    return
#Code for brian post faculty
label chapter_one_brian():
    call chapter_one_hide_buttons from _call_chapter_one_hide_buttons_12
    hide screen clickable_chapter_one_brian
    show brian1 with dissolve:
        subpixel True xanchor 270 pos (826, 136) zoom 1.39  orientation (0.0, 0.0, 0.0) 

    if not chapter_one_item_check("chapter_one_wrench"):
        k "What did you find in this classroom"
        b "Well I didn't find lopunny"
        k "BRIAN"
        k "WHAT THE FUCK!"
        b "I mean I found this wrench but that's about it..."
        k "gimmie that, ima beat the shit outta cody"
        b "That man can invert colors i dont wanna deal with him"
        b "and neither do you"
        k "fair nuff"
        k "anyways what does this wrench thing do, i am not a doctor"
        b "you are stupid"
        b "Doctors use knives and shit like that"
        b "Blue-Collar jobs use this"
        k "Does this imply the existance of red-collar jobs?"
        b "Shut the fuck up"
        play sound "audio/sound/chapter_one/item_pickup.ogg"
        "You have obtained a red-collar wrench!"
        b "ITS BLUE-COLLAR WTF"
        $ chapter_one_obtain_item("chapter_one_wrench")
    elif chapter_one_item_check("chapter_one_clock"):
        b "My accounting skills are ready to cook baldi!"
        k "better be!"
    else:
        b "I want my lopunny"
        b "I want my Pichu"
        b "I want my Lucario"
        b "I want my gardevoir"
        b "Like damn they smol"
        k "(WHAT IS THIS GUY TALKING ABOUT?)"
    hide brian1
    call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_16
    return
# Restores buttons once they are closed when an interaction starts/restores button once we swap areas
label chapter_one_restore_buttons(current_location):
    if current_location == 1:
        show screen clickable_button_baldi_chapter_one_up(location)
    elif current_location == 2:
        if chapter_one_item_check("chapter_one_hands"):
            show screen clickable_button_baldi_chapter_one_up(location)
        show screen clickable_button_baldi_chapter_one_down(location)
        if chapter_one_item_check("chapter_one_faculty"):
            show screen clickable_button_baldi_chapter_one_left(location)
        show screen clickable_button_baldi_chapter_one_right(location)
    elif current_location == 3:
        show screen clickable_button_baldi_chapter_one_left(location)
    elif current_location == 4:
        show screen clickable_button_baldi_chapter_one_right(location)
    elif current_location == 5:
        show screen clickable_button_baldi_chapter_one_down(location)
    return

#Do This when talking to npcs, so you cannot basically save scum :)
label chapter_one_hide_buttons:
    hide screen clickable_button_baldi_chapter_one_down
    hide screen clickable_button_baldi_chapter_one_left
    hide screen clickable_button_baldi_chapter_one_right
    hide screen clickable_button_baldi_chapter_one_up
#Do this to remove screens when you transition so the screens aren't stuck on the screen :)
label chapter_one_hide_screen:
    hide screen clickable_button_baldi_chapter_one_down
    hide screen clickable_button_baldi_chapter_one_left
    hide screen clickable_button_baldi_chapter_one_right
    hide screen clickable_button_baldi_chapter_one_up
    hide screen clickable_key_chapter_one
    hide screen clickable_chapter_one_dirt
    hide screen clickable_chapter_one_mop
    hide screen clickable_chapter_one_god_of_sweep
    hide screen clickable_chapter_one_principal
    hide screen clickable_chapter_one_alarmclock
    hide screen clickable_chapter_one_itsabully
    hide screen clickable_chapter_one_playtime
    hide screen clickable_chapter_one_brian
    hide screen clickable_chapter_one_thanga
    hide screen clickable_baldi_exit
    return
#Code used for the secret Conversion in Chapter One Subway Path
label chapter_one_subway_conversation:
    hide screen clickable_chapter_one_stn
    scene subway_chair:
        subpixel True xzoom 1.36 zoom 2.25
    show baldi1:
        subpixel True pos (0.46, 0.01) yrotate 180.0 
    show cody:
        subpixel True pos (0.79, 0.27) 
    show henry:
        subpixel True pos (0.14, 0.11) zoom 0.59
    show sonuthenecro:
        subpixel True pos (0.15, 0.48)  zoom 0.28
    if count >= 1:
        stn "There is no secret here, this is a formal warning unless you want to just die"
        stn "I suggest you eat all of the lunches though"
        stn "They taste pretty good"
        stn "What is your favorite lunch Henry?"
        tv "I am a big fan of the BLT"
        stn "what's in that?"
        tv "Uh bacon lettuce tomato"
        tv "straight bussin bussin"
        stn "sounds good ain't even gonna cap lol"
    else: 
        show screen clickable_chapter_one_secret_lopunny(910,210,0.29)
        stn "Well I am glad you three have made it to lunch"
        stn "I want to talk about this Kody fella and how we should deal with him"
        tv "Why don't we make him watch Rent-A-Girlfriend"
        stn "Good Idea, but he likes that show.  Also we are past beta now"
        c "I WANT TO MURDER HIM"
        stn "You see, I like that but the ??? entity doesn't like that"
        c "FUCK HIM"
        stn "He doesn't mean that big boss guy :)"
        baldi "I think we should teach them..."
        stn "oooo good idea, what should we teach them?"
        stn "Something edgy and awful like torture or beat the shit outta them"
        baldi "How about..."
        baldi "MATH"
        stn "uh"
        tv "You are hired!"
        stn "Wait why?"
        tv "Brian sucks at math, it is PERFECT!"
        stn "true true, I guess we will be needing you in the future"
        stn "Shake. My. Hand."
        baldi "no fuck you :)"
        stn "What a dick, I'm not paying for your lunch anymore see cya"
    $ count += 1
    scene subway2 with dissolve:
        subpixel True xzoom 1.1 zoom 3.04 
    show thanga2 with dissolve:
        subpixel True pos (0.22, 461)
    show brian1 with dissolve:
        subpixel True pos (0.36, 0.46) 
    show kody with dissolve:
        subpixel True pos (0.8, 0.43)  yrotate 180.0 
    show screen clickable_chapter_one_stn
    hide screen clickable_chapter_one_secret_lopunny
    return

label chapter_one_subway_minigame:
    play music "audio/music/chapter_one/subway_make_sandwich.ogg"
    se "What kind of bread did you want??"
    menu:
        "Honey Oat":
            $ count += 5
        "Wheat Bread":
            $ count += 3
        "White Bread":
            $ count += 2
        "Italian Herb & Cheese":
            $ count += 1
        "Malted Rye":
            $ count += -1
        "Plain Wrap":
            $ count += 0
        "Gluten Free Wrap":
            $ count += -5
        "Multigrain Wrap":
            $ count += 2
    se "What size should that bread be in?"
    menu:
        "6 Inch":
            $ count += -7
        "12 Inch":
            $ count += 4
    se "What kind of Cheese would you like?"
    menu:
        "None":
            se "gross lol"
            $ count += -10
        "Mozzarella":
            $ count += 5
        "Provolone":
            $ count += 6
        "Cheddar":
            $ count += 5
        "Swiss":
            $ count += 6
        "Pepperjack":
            $ count += 4
        "Monterey Cheddar":
            $ count += 2
        "American Cheese":
            $ count += 1
    se "Alright, Which one of our menu items on the Giant Jumbotron would you like?"
    #Choice represents Paper Number
    menu:
        "Spicy Chicken Classic":
            $ count += 4
        "Fiery Harissa Steak":
            $ count += 5
        "Buffalo Chicken":
            $ count += 7
        "Chicken & Bacon Ranch Melt":
            $ count += 2
        "Chicken Classic":
            $ count += 5
        "Chicken Schnitzel":
            $ count += 3
        "Chicken Strips":
            $ count += -3
        "Chicken Teriyaki":
            $ count += 0
        "Italian B.M.T":
            $ count += 7
        "Leg Ham":
            $ count += -4
        "Meatball Melt":
            $ count += -3
        "Pizza Melt":
            $ count += -2
        "Seafood Sensation":
            $ count += 1
        "Smashed Falafel":
            $ count += 0
        "Southern Style Chicken":
            $ count += -1
        "Steak Melt":
            $ count += 3
        "Tuna & Mayo":
            $ count += -2
        "Turkey":
            $ count += 1
        "Veggie Delite With Avo":
            $ count += 1
        "Veggie Patty":
            se "Gross"
            $ count += -5
    se "Would you like any toppings?"
    menu:
        "All of them":
            $ count += 5
        "Just Veggies":
            $ count += 2
        "No Pickles":
            $ count += -1
        "No Tomatos":
            $ count += -3
        "Nothing at all":
            $ count += -5
            se "okay man, its the same price so nice one bozo"
    se "Would you like the sandwich toasted?"
    menu:
        "Yes":
            $ count += 5
        "No":
            $ count += -5
    se "I'll even give one sauce since you are homeless >:)"
    menu:
        "Mayonnaise":
            $ count += 2
        "Ranch":
            $ count += 3
        "Honey Mustard":
            $ count += 5
        "None":
            $ count += -1
    se "Anything else with your order?"
    menu:
        "Chips":
            $ count += 0
        "Coke":
            $ count += 1
        "Chocolate Chip Cookie":
            $ count += 0

    if(count > 0):
        se "Alright, your sandwich will come out to be [count * 1.72]"
    else:
        se "Holy shit your sandwich is so ass you can just have it"

    if(count == 38):
        t "Dang you make the perfect sandwich, maybe you got good taste man!"
        b "yeah thang's right, it looks so beautiful!"
        "You have made the Perfect Sandwich! Your score was [count]!"
    elif(count == -38):
        t "You have trolled us and wasted our time nice one"
        b "yeah wtf is this..."
        "You have made the Failure Sandwich! Your score was [count]!"
    elif (count > 25):
        t "You got a nice sandwich! I gotta order me one"
        b "dang my wallet is getting cooked tonight"
        "You have made the Decent Sandwich! Your score was [count]!"
    elif(count > 10):
        t "I guess Subway makes trash Sandwichs"
        b "trudat"
        "You have made the Mediocre Sandwich! Your score was [count]!"
    elif(count < 0):
        t "That..."
        t "is a sandwich?"
        b "I wouldn't even feed Ocho that..."
        "You have made the Trash Sandwich! Your score was [count]!"
    else:
        "You have made an unremarkable sandwich... Your score was [count]!"
    stop music
    jump chapter_one_post_subway