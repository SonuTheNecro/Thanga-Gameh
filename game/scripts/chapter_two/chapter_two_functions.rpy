# Extra Code to make chapter_two's code nicer, these functions are for one time events in Chapter Two

#the clickable note in the first room
screen clickable_chapter_two_note():
    imagebutton:
        pos (1126, 765)
        at Transform(zoom = 0.76)
        idle "images/danganronpa_classroom_note.jpg"
        hover "images/danganronpa_classroom_note.jpg"
        action Jump("chapter_two_classroom_note")

screen clickable_chapter_two_ocho():
    imagebutton:
        pos (873, 900)
        at Transform(zoom = 0.35)
        idle "images/ocho.png"
        hover "images/ocho.png"
        action Call("chapter_two_ocho")

screen clickable_chapter_two_matt():
    imagebutton:
        pos (1008, 585)
        at Transform(zoom = 0.17)
        idle "images/matt2.jpg"
        hover "images/matt2.jpg"
        action Call("chapter_two_matt")

screen clickable_chapter_two_phoenix():
    imagebutton:
        pos (1152, 558)
        at Transform(zoom = 0.6)
        idle "images/phoenix_wright.png"
        hover "images/phoenix_wright.png"
        action Call("chapter_two_phoenix")

screen clickable_chapter_two_march():
    imagebutton:
        pos (1359, 603)
        at Transform(zoom = 0.15)
        idle "images/march_7th.png"
        hover "images/march_7th.png"
        action Call("chapter_two_march")

screen clickable_chapter_two_heavy():
    imagebutton:
        pos (1557, 495)
        at Transform(zoom = 0.4)
        idle "images/heavy_tf2.png"
        hover "images/heavy_tf2.png"
        action Call("chapter_two_heavy")

label chapter_two_ocho:
        hide screen clickable_chapter_two_ocho
        hide screen clickable_chapter_two_march
        hide screen clickable_chapter_two_heavy
        hide screen clickable_chapter_two_matt
        hide screen clickable_chapter_two_phoenix
        ocho "hello ThangaMangaLang"
        t "WHAT"
        k "whats wrong?"
        ocho "woof"
        t "nahh bro he talked i swear to god"
        ocho "wooof"
        k "bro you gooning too much"
        if location == 0:
            $ count += 1
        $ location += 1
        return

label chapter_two_march:
    hide screen clickable_chapter_two_ocho
    hide screen clickable_chapter_two_march
    hide screen clickable_chapter_two_heavy
    hide screen clickable_chapter_two_matt
    hide screen clickable_chapter_two_phoenix
    march "Hello! Whats your name?"
    t "ummm i- i- i'm t-t-tha-thang"
    march "Nice to meet you Thang!"
    march "My name is March 7th!"
    play movie "video/chapter_two/march_7th_intro.webm"
    play sound "audio/sound/chapter_two/character_intro.ogg"
    pause 3.0
    stop movie
    k "Holy fuck a woman"
    k "I gotta whip out my mewmaxxing, looksmaxxing, musclemaxxing, cockmaxxing, and armmaxxing"
    march "..."
    march "That's cool"
    march ":3"
    t "AYO WHAT ARE YOU DOING!"
    k "I got me another girlfriend"
    t "???????????????????"
    if rngint == 0:
        $ count += 1
    $ rngint += 1
    return

label chapter_two_heavy:
    hide screen clickable_chapter_two_ocho
    hide screen clickable_chapter_two_march
    hide screen clickable_chapter_two_heavy
    hide screen clickable_chapter_two_matt
    hide screen clickable_chapter_two_phoenix
    #heavy "heavy" 
    questionmark "Look at all these little babies"
    t "I AM NOT A FUCKING BABY!"
    t "also who the fuck are you?"
    questionmark "This is why chinese soldier is weak compared to russian soldier"
    heavy "I am the heavy generation 3 working for Renovation, Excavation, and Destruction"
    play movie "video/chapter_two/heavy_intro.webm"
    play sound "audio/sound/chapter_two/character_intro.ogg"
    pause 3.0
    stop movie
    t "So like the game tf2?"
    heavy "ya, is the video game my employer made merchandice of me"
    t "that game sucks"
    heavy "..."
    heavy "puny man"
    t "ima go now!"
    if rngint1 == 0:
        $ count += 1
    $ rngint1 += 1
    return

label chapter_two_matt:
    hide screen clickable_chapter_two_ocho
    hide screen clickable_chapter_two_march
    hide screen clickable_chapter_two_heavy
    hide screen clickable_chapter_two_matt
    hide screen clickable_chapter_two_phoenix
    mt "sup thang"
    t "matt what are you doing here"
    mt "idk i got ocho this new pet toy then we ended up here"
    t "was it a white and black bear?"
    mt "yeah"
    t "brotha"
    play movie "video/chapter_two/matt_intro.webm"
    play sound "audio/sound/chapter_two/character_intro.ogg"
    pause 3.0
    stop movie
    k "doesn't that mean ocho ate the bear?"
    k "shouldn't he be pissed at us?"
    if choice == 0:
        $ count += 1
    $ choice += 1
    return

label chapter_two_phoenix:
    hide screen clickable_chapter_two_ocho
    hide screen clickable_chapter_two_march
    hide screen clickable_chapter_two_heavy
    hide screen clickable_chapter_two_matt
    hide screen clickable_chapter_two_phoenix
    pw "Hello there, I'm Phoenix Wright"
    k "like from the game?"
    pw "What game? I'm an attorney"
    play movie "video/chapter_two/phoenix_wright_intro.webm"
    play sound "audio/sound/chapter_two/character_intro.ogg"
    pause 3.0
    stop movie
    k "Wouldn't this be intellectual infringment?"
    k "Since this isn't a property owned by capcom"
    t "yeah I was thinking that too"
    pw "WAIT THIS ISN'T CAPCOM?"
    pw "GET READY TO GET DECKED LAWYERS!"
    pw "once i get my lawyer team!"
    k "aren't you the lawyer?"
    pw "..."
    if count2 == 0:
        $ count += 1
    $ count2 += 1
    return
label chapter_two_show_character_lists:
    label chapter_two_all_except_cody:
        show thanga2:
            subpixel True pos (3, 556) xzoom 0.9 yzoom 0.9
        show kody:
            subpixel True pos (186, 625) xzoom 0.85 yzoom 0.85
        show brian3:
            subpixel True pos (381, 498) xzoom 0.45 yzoom 0.45
        show matt2:
            subpixel True pos (1065, 580) xzoom 0.17 yzoom 0.17
        show ocho:
            subpixel True pos (930, 906) xzoom 0.35 yzoom 0.35
        show march_7th:
            subpixel True pos (1373, 605) xzoom 0.15 yzoom 0.15
        show phoenix_wright:
            subpixel True pos (1171, 558) xzoom 0.6 yzoom 0.6
        show heavy_tf2:
            subpixel True pos (1563, 498) xzoom 0.4 yzoom 0.4
        show monokuma:
            subpixel True pos (0.38, 0.76) xzoom 0.5 yzoom 0.5
        return

# Handles the movement for the investigation part for chapter two
label chapter_two_movement:
    screen chapter_two_danganronpa_up_button(origin):
        imagebutton:
            xalign 0.5
            yalign 0
            idle "images/ArrowUpPress2.png"
            hover "images/ArrowUpPress2.png"
            if origin == 7:
                action Jump("ch02_area_6")
            elif origin == 6:
                action Jump("ch02_area_3")
            elif origin == 3:
                action Jump("ch02_area_1")
    screen chapter_two_danganronpa_down_button(origin):
        imagebutton:
            xalign 0.5
            yalign 1.0
            idle "images/ArrowDownPress2.png"
            hover "images/ArrowDownPress2.png"
            if origin == 1:
                action Jump("ch02_area_3")
            elif origin == 3:
                action Jump("ch02_area_6")
            elif origin == 6:
                action Jump("ch02_area_7")
    screen chapter_two_danganronpa_left_button(origin):
        imagebutton:
            xalign 0.0
            yalign 0.5
            idle "images/ArrowLeftPress2.png"
            hover "images/ArrowLeftPress2.png"
            if origin == 3:
                action Jump("ch02_area_2")
            elif origin == 4:
                action Jump("ch02_area_3")
            elif origin == 6:
                action Jump("ch02_area_5")
    screen chapter_two_danganronpa_right_button(origin):
        imagebutton:
            xalign 1.0
            yalign 0.5
            idle "images/ArrowRightPress2.png"
            hover "images/ArrowRightPress2.png"
            if origin == 2:
                action Jump("ch02_area_3")
            elif origin == 3:
                action Jump("ch02_area_4")
            elif origin == 5:
                action Jump("ch02_area_6")

# Put all screens into here, so all can be hidden when we transition screens
label chapter_two_hide_screens():
    hide screen chapter_two_danganronpa_up_button
    hide screen chapter_two_danganronpa_down_button
    hide screen chapter_two_danganronpa_left_button
    hide screen chapter_two_danganronpa_right_button
    return
# Restores the movement, do this last so its on top of everything else
label chapter_two_restore_movement(location):
    if location == 1:
        call screen chapter_two_danganronpa_down_button(location)
    elif location == 2:
        call screen chapter_two_danganronpa_right_button(location)
    elif location == 3:
        show screen chapter_two_danganronpa_up_button(location)
        show screen chapter_two_danganronpa_down_button(location)
        show screen chapter_two_danganronpa_right_button(location)
        call screen chapter_two_danganronpa_left_button(location)
    elif location == 4:
        call screen chapter_two_danganronpa_left_button(location)
    elif location == 5:
        call screen chapter_two_danganronpa_right_button(location)
    elif location == 6:
        show screen chapter_two_danganronpa_up_button(location)
        show screen chapter_two_danganronpa_down_button(location)
        call screen chapter_two_danganronpa_left_button(location)
    elif location == 7:
        call screen chapter_two_danganronpa_up_button(location)
# Put all clickable objects here
label chapter_two_restore_screens(location):
    if location == 1:
        if count == 0:
            call chapter_two_wake_up
    elif location == 2:
        if count == 3:
            call chapter_two_ocho_dead
    elif location == 3:
        pass
    elif location == 4:
        if count == 1:
            call chapter_two_intro_meeting
    elif location == 5:
        pass
    elif location == 6:
        if count == 2:
            call chapter_two_matt_meeting1
    elif location == 7:
        pass
    call chapter_two_restore_movement(location)
    return

label chapter_two_events:
    label chapter_two_wake_up:
        show thanga2:
            subpixel True pos (560, 295) 
        t "Why did I get the girl's room"
        t "oh well it has anime guess its my room now"
        show black with fade
        pause 3.0
        hide black with fade
        play sound "audio/sound/chapter_two/monokuma_morning.ogg"
        window auto hide
        pause 16.0
        play sound "audio/sound/chapter_two/monokuma_angry.ogg"
        m "GOD FUCKING DAMMMN STUPID FUCKING PIECE OF SHIT ANNOUNCER"
        m "It's time to wake up fuckers. Meet at the hall"
        t "..."
        t "I guess I should go meet up with everyone else and discuss"
        t "but holy shit Brian is a dumbass"
        show brian1:
            subpixel True pos (1900, 323) 
            linear 0.65 subpixel True pos (1153, 323) 
        pause 0.7
        b "shut the fuck up"
        t "where the fuck were you?"
        b "I was in the bathroom"
        t "oh"
        b "it was very important for me to call off work"
        b "The CEO is like this mega powerful guy who would literally murder me if I didn't call in"
        b "For me, dealing with the bear has better odds than dealing with Jewel Osco's Ceo"
        t "you need to get a new job"
        b "cant"
        t "why?"
        b "Jewel Osco is more like a cult"
        b "you don't just leave the job"
        b "the job leaves you"
        t "okay brian"
        $ count = 1
        return
    label chapter_two_intro_meeting:
        call chapter_two_all_except_cody
        hide matt2
        hide monokuma
        hide ocho
        k "Thang you look so sleepy"
        t "can't sleep when there is a murderous bear nearby waiting to strike at any opportunity"
        b "well technically"
        b "everyday you are at risk of being shot"
        b "so you should just accept death being an inevitable being"
        t "that doesn't help me feel better"
        march "Well smiling always keeps me feeling good"
        march ":)"
        t ":("
        march ";)"
        k ":)"
        march ":)"
        k "W Rizz"
        t "Shut the fuck up"
        t "uhh where is matt"
        heavy "Heavy weapons guy could not locate singapore boy"
        b "I thought he was Korean?"
        t "hes from the flipino land"
        heavy "iz the same to me"
        heavy "russia will beat all china countries the same"
        t "right..."
        t "(I should go find matt)"
        t "Yo guys I am going to go find matt since he should be here"
        t "(I swear if that kid is fucking gooning to march 7th I am fucking done)"
        $ count = 2
        return
    label chapter_two_matt_meeting1:
        show thanga2 with dissolve:
            subpixel True pos (510, 278) 
        show matt2 with dissolve:
            subpixel True pos (1206, 243) zoom 0.21 
        t "Yo matt are you good?"
        mt "yeah why?"
        t "you weren't at the meeting in the hall?"
        t "did you goon too hard?"
        mt "nahhhhh I am goonminning right now"
        t "I hate everyone in this building"
        mt "but uh Ocho is missing"
        t "So you aren't good"
        mt "I am"
        mt "Ocho isn't"
        t "ugh, i guess I will help look for him"
        mt "thanks man!"
        $ count = 3
        return
    label chapter_two_ocho_dead:

        show ch02_ocho_dead:
            subpixel True pos (30, 671) zoom 0.71 
        show thanga2:
            subpixel True pos (1951, 211) yrotate 180.0
            linear 0.6 subpixel True pos (1411, 211) yrotate 180.0 
        show matt2:
            subpixel True pos (1950, 405) zoom 0.2 
        t "uhhh wtf"
        t "is that ocho?"
        t "holy shit"
        mt "yo thang are you in there?"
        show matt2:
            linear 0.6 subpixel True pos (1653, 405) zoom 0.2 
        mt "The pool's closed thang"
        pause 1.2
        mt "OCHOOOOOOOOOOOOOOOOOOOOOOOOOOO"
        mt "WTF HAPPENED"
        play sound "audio/sound/chapter_two/monokuma_discovery.ogg"
        window auto hide
        pause 16.0
        play sound "audio/sound/chapter_two/monokuma_appear.ogg"
        play music "audio/music/chapter_two/monokuma_theme.ogg"
        show monokuma:
            subpixel True pos (0.45, 0.5) xzoom 0.5 yzoom 0.5
            ypos 0.8
            yzoom 0.0
            linear 0.35 ypos 0.5 yzoom 0.5
        window auto hide
        with Pause(0.7)
        m "welp guess the first murder happened without me needing to-"
        m "NNNOOOOOOO OOCHOOOOO"
        play sound "audio/sound/chapter_two/monokuma_angry.ogg"
        m "WHO FUCKING DID THIS I WILL KILL THEM"
        t "why are you more angry than matt"
        t "also i thought you always knew the murderer"
        m "I WAS BUSY TRYING TO SET UP A MURDER"
        t "ok no need to yell"
        m "IM BRINGING EVERYONE HERE"
        window auto hide
        stop music
        show monokuma:
            subpixel True pos (0.45, 0.5) xzoom 0.5 yzoom 0.5
            linear 0.2 ypos 1.5
        pause 1.5
        t "guess we will have to wait here then"
        show matt2:
            subpixel True pos (1653, 405) zoom 0.2 
            linear 4.0 xpos 600
        mt "ocho..."
        show thanga2:
            subpixel True pos (1411, 211) yrotate 180.0
            linear 0.2 xpos 771 ypos 200
        show kody with hpunch:
            zoom 0.8 subpixel True pos (1500, 600) yrotate 180.0
            linear 0.2 xpos 850 ypos 300
        show march_7th:
            zoom 0.18 subpixel True pos (1500, 600) yrotate 180.0
            linear 0.2 xpos 1361 ypos 515
        show heavy_tf2:
            zoom 0.4 subpixel True pos (1500, 600) yrotate 180.0
            linear 0.2 xpos 998 ypos 238
        show phoenix_wright:
            zoom 0.7 subpixel True pos (1500, 600)
            linear 0.2 xpos 1156 ypos 488
        show brian3:
            zoom 0.45 subpixel True pos (1500, 600) yrotate 180.0
            linear 0.2 xpos 790 ypos 525
        k "oof"
        t "ow get off of me"
        k "i cant were all shoved in here"
        play sound "audio/sound/chapter_two/monokuma_appear.ogg"
        play music "audio/music/chapter_two/monokuma_theme.ogg"
        show monokuma:
            subpixel True pos (0.88, 0.5)
            ypos 1.0
            yzoom 0.0
            linear 0.35 ypos 0.76 yzoom 0.5
        window auto hide
        with Pause(0.7)
        m "alright fuckers who did it"
        m "WHO FUCKING KILLED OCHO"
        march "There's no way one of us did!"
        march "It must have been you!"
        pw "Yeah! You already said you were planning something!"
        m "YEAH I WAS PLANNING ON KILLING ONE OF YOU NOT OCHO"
        heavy "heavy no like this bear"
        b "yea bitch how dare you kill matt's dog"
        k "i actually didn't like ocho that much"
        stop music
        march "..."
        pw "..."
        heavy "..."
        b "..."
        t "..."
        mt "..."
        m "..."
        window auto hide
        show gun2:
            subpixel True pos (0.86, 0.87) xzoom 0.15 yzoom 0.15 
        play sound "audio/sound/chapter_one/glock_magchange.ogg"
        pause 2.5
        mt "wow you just had to bring that up when he just died"
        k "its not my fault i didnt like him"
        mt "it literally is"
        call dio_time_stop
        show danganronpa_changing:
            subpixel True matrixcolor InvertMatrix(1.0)
        show cody:
            subpixel True pos (1628, 330) xzoom 0.85 yzoom 0.85
        show matt2:
            subpixel True pos (600, 405) zoom 0.2 
        show thanga2:
            subpixel True pos (771, 200) yrotate 180.0
        show kody:
            zoom 0.8 subpixel True pos (850, 300) yrotate 180.0
        show march_7th:
            zoom 0.18 subpixel True pos (1361, 515) yrotate 180.0
        show heavy_tf2:
            zoom 0.4 subpixel True pos (998, 238) yrotate 180.0
        show phoenix_wright:
            zoom 0.7 subpixel True pos (1156, 488)
        show brian3:
            zoom 0.45 subpixel True pos (790, 525) yrotate 180.0
        show monokuma:
            subpixel True pos (0.88, 0.76)
        show ch02_ocho_dead:
            subpixel True pos (30, 671) zoom 0.71
        c "..."
        c "NNOOOOOOOO OOOCCCHHHHOOOOOOO"
        t "why are you also more upset then matt"
        c "SHUT UP BITCH"
        c "I WILL FIND WHO DID THIS"
        c "JUST YOU WAIT"
        show danganronpa_changing:
            subpixel True matrixcolor InvertMatrix(0.0)
        hide cody
        pause 1.0
        m "wow he really made us do all that work just to say like 4 lines"
        k "it was 5"
        m "LITERALLY SHUT THE FUCK UP"
        show ipad_screen:
            subpixel True
        m "alright guys here is the monokuma file"
        hide ipad_screen
        m "it has the details of the murder"
        t "how did you make this?"
        t "i thought you didnt know the murderer or what happened"
        m "idk i just had it on me"
        m "well bye"
        hide gun2
        show monokuma:
            subpixel True pos (0.88, 0.76) xzoom 0.5 yzoom 0.5
            linear 0.2 ypos 1.5
        pause 1.5
        t "alright guys lets look at this and solve the crime"
        pw "No, why should we trust what he's giving us?"
        march "Yeah, he's already kidnapped us who knows what else he'll do!"
        k "i agree with whatever this lady says"
        t "guys thats not how the game works"
        show march_7th:
            zoom 0.18 subpixel True pos (1361, 515) yrotate 180.0
            linear 0.6 xpos 76 ypos 541
        show heavy_tf2:
            zoom 0.4 subpixel True pos (998, 238) yrotate 180.0
            linear 0.6 xpos 178 ypos 95
        show phoenix_wright:
            zoom 0.7 subpixel True pos (1156, 488)
            linear 0.6 xpos 568 ypos 526
        pause 1.5
        pw "Looks like the cause of death was a puncture to the side of the neck"
        march "And he's cold so he must have died a while ago"
        heavy "heavy will look for clues around building"
        show heavy_tf2:
            zoom 0.4 subpixel True pos (178, 95) yrotate 180.0
            linear 0.4 xpos 1270 ypos 220
        pause 0.4
        show heavy_tf2:
            zoom 0.4 subpixel True pos (1270, 220) yrotate 180.0
            linear 0.4 xpos 1848 ypos 1020
        pause 1.3
        mt "i guess ill go with him..."
        show matt2:
            subpixel True pos (600, 405) zoom 0.2
            linear 1.8 xpos 1661 ypos 405
        pause 1.8
        show matt2:
            subpixel True pos (1661, 405) zoom 0.2
            linear 1.5 xpos 1958 ypos 901
        pause 3.0
        b "..."
        b "fine ill go cheer matt up"
        show brian3:
            zoom 0.45 subpixel True pos (790, 525) yrotate 180.0
            linear 0.6 xpos 1518 ypos 525
        pause 0.6
        show brian3:
            zoom 0.45 subpixel True pos (1518, 525) yrotate 180.0
            linear 0.6 xpos 1938 ypos 1051
        pause 1.5
        k "I NEED TO GOON"
        show kody:
            zoom 0.8 subpixel True pos (850, 300) yrotate 180.0
            linear 0.08 xpos 1505 ypos 398
        pause 0.08
        show kody:
            zoom 0.8 subpixel True pos (1505, 398) yrotate 180.0
            linear 0.08 xpos 1966 ypos 720
        pause 1.2
        t "guess ill look at the monokuma file"
        window auto hide
        show black with fade
        show monokuma_file_ocho with fade:
            subpixel True zoom 0.8
        t "ocho is dead, 2 ft 9, 55 lbs, yea yea"
        t "damn he is fat"
        t "and wtf is blood type c"
        t "died at 6:35 from a puncture to the neck"
        t "looks like Phoenix and March were right"
        window auto hide
        hide monokuma_file_ocho with fade
        hide black with fade
        t "guess i should talk to people and look for clues"
        "test"

        #TODO:more dialogue here
        
        $ count = 4
        return