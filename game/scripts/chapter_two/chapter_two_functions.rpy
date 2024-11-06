# Extra Code to make chapter_two's code nicer, these functions are for one time events in Chapter Two

#the clickable note in the first room
screen clickable_chapter_two_note():
    imagebutton:
        pos (1126, 765)
        at Transform(zoom = 0.76)
        idle "images/danganronpa_classroom_note.jpg"
        hover At("images/danganronpa_classroom_note.jpg", animated_outline)
        action Jump("chapter_two_classroom_note")

screen clickable_chapter_two_ocho():
    imagebutton:
        pos (873, 900)
        at Transform(zoom = 0.35)
        idle "images/ocho.png"
        hover At("images/ocho.png", animated_outline)
        action Call("chapter_two_ocho")

screen clickable_chapter_two_matt():
    imagebutton:
        pos (1008, 585)
        at Transform(zoom = 0.5)
        idle "images/matt2.jpg"
        hover At("images/matt2.jpg", animated_outline)
        action Call("chapter_two_matt")

screen clickable_chapter_two_phoenix():
    imagebutton:
        pos (1152, 558)
        at Transform(zoom = 0.6)
        idle "images/phoenix_wright.png"
        hover At("images/phoenix_wright.png", animated_outline)
        action Call("chapter_two_phoenix")

screen clickable_chapter_two_march():
    imagebutton:
        pos (1359, 603)
        at Transform(zoom = 0.15)
        idle "images/march_7th.png"
        hover At("images/march_7th.png", animated_outline)
        action Call("chapter_two_march")

screen clickable_chapter_two_heavy():
    imagebutton:
        pos (1557, 495)
        at Transform(zoom = 0.4)
        idle "images/heavy_tf2.png"
        hover At("images/heavy_tf2.png", animated_outline)
        action Call("chapter_two_heavy")

screen clickable_chapter_two_march2():
    imagebutton:
        pos (76, 541)
        at Transform(zoom = 0.18, yrotate = 180)
        idle "images/march_7th.png"
        hover At("images/march_7th.png", animated_outline)
        action Call("chapter_two_march2")

screen clickable_chapter_two_phoenix2():
    imagebutton:
        pos (568, 526)
        at Transform(zoom = 0.7)
        idle "images/phoenix_wright.png"
        hover At("images/phoenix_wright.png", animated_outline)
        action Call("chapter_two_phoenix2")

screen clickable_chapter_two_hidden_door():
    imagebutton:
        pos (1020, 423)
        at Transform(zoom = 1.114)
        idle "images/danganronpa_hidden_door.png"
        hover At("images/danganronpa_hidden_door.png", animated_outline)
        action Call("chapter_two_trial")

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

label chapter_two_march2:
    hide screen clickable_chapter_two_march2
    hide screen clickable_chapter_two_phoenix2
    march "Hey Thang. It's so sad what happened to Ocho isn't it?"
    t "yea it sucks"
    march "We will definitely find whoever did this!"
    t "did you find any clues besides his time of death?"
    march "Yea, there was one thing I noticed that was weird"
    t "what was it?"
    march "There are no blood stains anywhere"
    t "couldnt they have just cleaned it up?"
    march "Yes, but there should have been some kind of residue or something left behind"
    march "But everything around Ocho is spotless"
    #TODO:make clue picture
    t "Does that mean he was killed somewhere else?"
    march "That's what I'm thinking"
    march "But I haven't checked any of the other rooms yet"
    march "So I'm not sure where it could have been done"
    t "guess ill have to do it"
    march "Thanks Thang!"
    march "I think I'll go to my room to review the clues so far"
    t "ok"
    if choice == 0:
        $ count += 1
    $ choice += 1
    jump chapter_two_death_repeat
  
label chapter_two_phoenix2:
    hide screen clickable_chapter_two_march2
    hide screen clickable_chapter_two_phoenix2
    t "hey phoenix, did you find anything out?"
    pw "Yeah, I discovered that there was a puncture wound in the side of his neck"
    t "yea i knew that, it was in the monokuma file"
    t "what else?"
    pw "I found some liquid under this bench"
    t "damn who pissed under there?"
    t "it was probably kody"
    pw "No, I think it's just water"
    t "thats boring"
    t "couldnt it just be from someone using the pool?"
    pw "Don't you remember?"
    pw "The pool is closed, so no one could have gone in"
    t "then what about the sinks in the back?"
    pw "There's a chance, but it's unlikely"
    pw "I would just keep this in mind"
    t "whatever you say bro"
    #TODO:make clue picture
    pw "Well I'm probably gonna go to my room to think some stuff through"
    t "alright, ill look for more stuff then"
    if count2 == 0:
        $ count += 1
    $ count2 += 1
    jump chapter_two_death_repeat

label chapter_two_show_character_lists:
    label chapter_two_all_except_cody:
        show thanga2:
            subpixel True pos (3, 556) xzoom 0.9 yzoom 0.9
        show kody:
            subpixel True pos (186, 625) xzoom 0.85 yzoom 0.85
        show brian3:
            subpixel True pos (381, 498) xzoom 0.45 yzoom 0.45
        show matt2:
            subpixel True pos (1065, 580) xzoom 0.5 yzoom 0.5
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
    if count == 10:
        hide screen clickable_chapter_two_hidden_door
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
        elif count == 7:
            call chapter_two_kody_clue
        elif count == 10:
            show screen clickable_chapter_two_hidden_door()
    elif location == 2:
        if count == 3:
            call chapter_two_ocho_dead
    elif location == 3:
        if count == 4:
            call chapter_two_heavy_clue
    elif location == 4:
        if count == 1:
            call chapter_two_intro_meeting
        elif count == 8:
            call chapter_two_after_clues
        elif count == 9:
            call chapter_two_before_trial
    elif location == 5:
        if count == 6:
            call chapter_two_matt_clue
        pass
    elif location == 6:
        if count == 2:
            call chapter_two_matt_meeting1
        elif count == 5:
            call chapter_two_brian_clue
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
        window auto hide
        show black with fade
        pause 3.0
        hide black with fade
        play sound "audio/sound/chapter_two/monokuma_morning.ogg"
        window auto hide
        $ renpy.pause(16.0, hard=True)
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
            subpixel True pos (1206, 243) zoom 0.6 
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
            subpixel True pos (1950, 405) zoom 0.57 
        t "uhhh wtf"
        t "is that ocho?"
        t "holy shit"
        mt "yo thang are you in there?"
        show matt2:
            linear 0.6 subpixel True pos (1653, 405) zoom 0.57
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
            subpixel True pos (1653, 405) zoom 0.57 
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
            subpixel True pos (600, 405) zoom 0.57 
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
        march "Yeah, he's already kidnapped us, who knows what else he'll do!"
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
            subpixel True pos (600, 405) zoom 0.57
            linear 1.8 xpos 1661 ypos 405
        pause 1.8
        show matt2:
            subpixel True pos (1661, 405) zoom 0.57
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
        $ choice = 0
        $ count2 = 0
        $ count = 0

        label chapter_two_death_repeat:
            if count == 2:
                jump chapter_two_after_two_clues
            while count < 2:
                window hide
                show screen clickable_chapter_two_march2()
                show screen clickable_chapter_two_phoenix2()
                $ renpy.pause()

        label chapter_two_after_two_clues:
            pause 1.0
            t "i dont think im gonna find anything that they cant"
            t "guess its time to look for clues somewhere else"
            $ count = 4
            call chapter_two_restore_movement(2)

        label chapter_two_heavy_clue:
            show thanga2 with dissolve:
                subpixel True pos (538, 240) 
            show heavy_tf2 with dissolve:
                subpixel True pos (1120, 223) zoom 0.45 
            pause 1.0
            t "what are you doing here heavy"
            t "i thought you went to look for clues"
            heavy "heavy no can run far"
            heavy "get out of breath easy"
            t "well have you found anything so far?"
            heavy "still out of breath, no time to look"
            t "alright well should i come back later?"
            heavy "no no, heavy find clue now"
            show heavy_tf2:
                zoom 0.45 subpixel True pos (1120, 223)
                linear 0.3 xpos 1848 ypos 1020
            pause 3.0
            show heavy_tf2:
                zoom 0.45 subpixel True pos (1848, 1020)
                linear 0.3 xpos 1120 ypos 223
            heavy "alright heavy found clue"
            t "how"
            t "and i thought you were out of breath"
            heavy "heavy find lopunny plush with hole in back"
            t "..."
            t "thats just brians"
            t "i dont think thats a clue"
            t "also why was that here?"
            heavy "ok then heavy search for more clues"
            show heavy_tf2:
                zoom 0.45 subpixel True pos (1120, 223)
                linear 0.2 xpos 1848 ypos 1020
            pause 5.0
            show heavy_tf2:
                zoom 0.45 subpixel True pos (1848, 1020)
                linear 0.2 xpos 1120 ypos 223
            heavy "ok heavy find another clue"
            t "it better be one this time"
            t "and how were you running faster?"
            heavy "heavy find picture of dog"
            t "where did you find a picture of ocho?"
            heavy "it was on floor over there"
            heavy "why would someone take photo of dog?"
            t "idk it could be matts or monokumas or something"
            heavy "ok that makes sense"
            heavy "you take photo"
            t "alright"
            #TODO: add clue picture
            t "guess I should look for matt or brian"
            $ count = 5
            call chapter_two_restore_movement(3)
            
        label chapter_two_brian_clue:
            show thanga2 with dissolve:
                subpixel True pos (538, 240) 
            show brian1 with dissolve:
                subpixel True pos (955, 246)
            pause 1.0
            t "what are you doing here brian?"
            t "i thought you were going after matt"
            b "yea dumbass i was going after him"
            b "i just didnt know japanese people were that fast"
            t "damn you slow and fat as hell"
            t "also matt is not japanese hes filipino"
            b "i literally dont care"
            t "..."
            t "anyway, did you find anything else?"
            b "no i was too busy chasing after matt"
            t "damn you suck, everyone else had something"
            b "shut the fuck up bitch"
            b "what was so good that they found?"
            t "march found no blood at the scene"
            t "phoenix found liquid near ocho"
            t "and heavy found a picture of ocho in the lobby"
            b "..."
            b "damn"
            b "how did they find that shit so fast"
            t "also i think heavy found your lopunny plush"
            b "WHAT"
            show brian1:
                subpixel True pos (955, 246)
                linear 0.2 xpos 953 ypos 485 zoom 0.16
            pause 0.2
            hide brian1 with dissolve
            pause 1.0
            t "wow"
            t "never seen him run that fast"
            pause 1.0
            t "guess matt is over here then"
            $ count = 6
            call chapter_two_restore_movement(6)

        label chapter_two_matt_clue:
            show thanga2 with dissolve:
                subpixel True pos (445, 343) 
            show matt2 with dissolve:
                subpixel True pos (995, 313) zoom 0.58
            pause 1.0
            t "hey matt"
            mt "oh..."
            mt "hi thang"
            t "i though you were going with heavy?"
            mt "i was, but he stopped going after like 6 feet"
            mt "so i decided to keep going to look for stuff"
            t "so did you find anything?"
            mt "not really"
            mt "but i did notice that all of the toilet paper and paper towels are gone"
            t "that is kind of interesting"
            t "might as well take note of it"
            #TODO: add clue picture
            t "well is there anything else you found?"
            mt "no thats it"
            mt "this is the only place that i have checked"
            t "alright, well i talked to the others and they found some stuff too"
            mt "ok thats cool"
            t "dont worry matt we will find who did this"
            mt "thanks thang"
            t "im gonna go to my room now"
            t "bye bitch"
            $ count = 7
            call chapter_two_restore_movement(5)

        label chapter_two_kody_clue:
            show thanga2 with dissolve:
                subpixel True pos (445, 343)
            t "alright, so we collected a couple of clues"
            t "but we still dont know the most important parts"
            t "like where the murder happened"
            t "or who did it"
            t "..."
            t "idk when the trial is but it should be soon"
            show kody with dissolve:
                subpixel True pos (1060, 383) zoom 0.75 
            pause 1.0
            k "hi thang"
            t "WHAT THE FUCK"
            t "WHY ARE YOU AND BRIAN ALWAYS IN MY BATHROOM"
            k "i was busy gooning"
            t "DO THAT IN YOUR OWN ROOM"
            k "sucks to suck"
            t "???"
            k "so what happened"
            t "march, phoenix, and matt found some useful clues"
            t "heavy found a picture of ocho"
            t "and brian found nothing"
            k "well thats expected"
            k "but thats all you guys found?"
            k "yall suck ass"
            t "ok bitch all you did was goon"
            k "i found this tape of the security footage"
            t "..."
            t "...."
            t "where the fuck did you find that"
            k "it was in the gym"
            k "that bear must have dropped it"
            t "when did you go to the gym?"
            k "i checked the whole building before i started gooning"
            t "bro how fast are you"
            k "well im going to my room to goon more"
            show kody:
                subpixel True pos (1060, 383) zoom 0.75
                linear 0.2 xpos 1541 ypos 328
            pause 0.2
            hide kody with dissolve
            pause 1.0
            t "how the fuck is he gooning more"
            t "anyway, that tape is super important"
            t "i should keep track of it"
            #TODO: make clue picture
            t "guess i should wait until something happens"
            pause 7.0
            t "..."
            t "is something gonna happen"
            play sound "audio/sound/chapter_two/monokuma_appear.ogg"
            play music "audio/music/chapter_two/monokuma_theme.ogg"
            show monokuma:
                subpixel True pos (0.54, 0.48) zoom 0.7
                ypos 0.82
                yzoom 0.0
                linear 0.35 ypos 0.48 yzoom 1.0
            window auto hide
            with Pause(1.5)
            play sound "audio/sound/chapter_two/monokuma_hey.ogg"
            m "hello thang"
            t "get the fuck out"
            m "dont be like that thang"
            m "i just wanted to tell you to meet in the hall"
            m "everyone else is there"
            t "ok now get out"
            play sound "audio/sound/chapter_two/monokuma_confused.ogg"
            m "why do you want me to leave so bad?"
            m "dont tell me your gooning like kody"
            t "hell no i dont goon like him"
            play sound "audio/sound/chapter_two/monokuma_wrong.ogg"
            m "yeah sure buddy"
            m "anyway i lost something i had"
            m "did you find anything in the gym or the hall?"
            t "no i didnt"
            m "alright well tell me if you find it"
            play sound "audio/sound/chapter_two/monokuma_laugh.ogg"
            m "see you in the hall"
            stop music
            show monokuma:
                subpixel True pos (0.54, 0.48) zoom 0.7
                linear 0.2 xpos 0.75 ypos 0.31
            pause 0.2
            hide monokuma with dissolve
            pause 1.0
            t "guess i should go to the hall then"
            $ count = 8
            call chapter_two_restore_movement(1)
        
        label chapter_two_after_clues:
            call chapter_two_all_except_cody
            hide ocho
            hide monokuma
            hide kody
            hide brian3
            hide thanga2
            pause 0.6           
            show thanga2 with dissolve:
                subpixel True pos (3, 556)
            t "hey guys"
            t "did monokuma tell you to meet here too?"
            mt "..."
            pw "Yes, he did"
            pw "Do you know where the others are?"
            t "kody is too busy gooning"
            t "idk about brian and i dont care about cody"
            march "What do you think he is going to make us do now?"
            t "im guessing the trial is going to start"
            t "thats how it works in this game"
            march "I just don't want any other murders to happen!"
            pw "I agree"
            heavy "heavy agree too"
            mt "..."
            pause 2.0
            show brian3 with dissolve:
                subpixel True pos (381, 498) xzoom 0.45 yzoom 0.45
            b "sup fuckers"
            t "where the fuck were you?"
            b "i had to buy some remote raid passes"
            b "today was the last Hoenn Tour day"
            t "WHAT"
            t "I THOUGHT YOUR PHONE WAS DEAD"
            b "oh i tried turning it on again and it had 2 percent left"
            t "AND YOU PLAYED POKEMON GO"
            t "INSTEAD OF CALLING ANYONE?"
            b "but it was the last day of the tour"
            t "AND I BET YOU WERE USING THAT LOPUNNY PLUSH TOO"
            b "..."
            t "brotha"
            t "now we got 2 gooners in here"
            show kody with dissolve:
                subpixel True pos (186, 625) xzoom 0.85 yzoom 0.85
            k "sup fuckers"
            t "..."
            t "just kill me now"
            play sound "audio/sound/chapter_two/monokuma_appear.ogg"
            play music "audio/music/chapter_two/monokuma_theme.ogg"
            show monokuma:
                subpixel True pos (0.37, 0.76) xzoom 0.5 yzoom 0.5
                ypos 1.0
                yzoom 0.0
                linear 0.35 ypos 0.76 yzoom 0.5
            window auto hide
            with Pause(0.7)
            m "everyone important is here so lets start the meeting"
            t "what about cody?"
            m "he doesnt matter"
            m "also i havent been able to get into his room since yesterday"
            t "thats weird"
            m "oh well"
            pw "So, what's this meeting about?"
            march "Yeah! Are you going to make us do more bad stuff?"
            mt "..."
            t "no i think the trial is going to start"
            m "the trial is being delayed until tomorrow"
            t "what?"
            t "the trial usually starts by now"
            m "well it would but the room isnt ready yet"
            m "i didnt think the first murder would happen this fast"
            t "so what are we going to do then?"
            m "idk just wait until tomorrow"
            b "bro we gotta wait even longer?"
            b "i cant even play pokemon go"
            m "i can charge your phone for it"
            b "LETS FUCKING GO"
            show brian3:
                subpixel True pos (381, 498) xzoom 0.45 yzoom 0.45
                linear 0.2 xpos 1961 ypos 498
            pause 1.0
            t "hes not even gonna call anyone is he"
            pw "Is there anything else you're going to tell us?"
            m "no thats it"
            t "really?"
            t "we all met up just for that?"
            t "couldnt you have just told us this individually?"
            m "shut up thang"
            m "also if any of you find something weird in the gym or anywhere else tell me"
            k "oh like this ta-"
            t "SHUT THE FUCK UP KODY"
            play sound "audio/sound/chapter_two/monokuma_confused.ogg"
            m "did you find something?"
            t "no he didnt find anything"
            m "i know you lyin boy"
            m "anyway just do whatever until tomorrow"
            stop music
            play sound "audio/sound/chapter_two/monokuma_appear.ogg"
            show monokuma:
                subpixel True pos (0.37, 0.76) xzoom 0.5 yzoom 0.5
                ypos 0.76
                yzoom 0.5
                linear 0.2 ypos 1.0 yzoom 0.5
            window auto hide
            with Pause(1.5)
            t "well"
            t "what are you guys gonna do"
            show kody:
                subpixel True pos (186, 625) xzoom 0.85 yzoom 0.85
                linear 0.2 xpos 1200 ypos 625
            pause 0.2
            show phoenix_wright:
                subpixel True pos (1171, 558) xzoom 0.6 yzoom 0.6
                linear 0.2 xpos 975 ypos 558
            show matt2:
                subpixel True pos (1065, 580) xzoom 0.5 yzoom 0.5
                linear 0.2 xpos 850 ypos 580
            pause 0.2
            play sound "audio/sound/general/rizz.ogg"
            k "hello march"
            march "Uhh... hey kody"
            k "what do you say we..."
            k "go back to my room?"
            march "Umm..."
            march "I'm gonna head back to my room"
            show march_7th:
                subpixel True pos (1373, 605) xzoom 0.15 yzoom 0.15
                linear 0.3 xpos 2100 ypos 605
            pause 0.7
            k "WAIT"
            play sound "audio/sound/chapter_two/body_fall.ogg"
            pause 0.2
            show kody:
                subpixel True pos (1200, 625) xzoom 0.85 yzoom 0.85
                linear 0.1 xpos 1500 ypos 625 
            pause 0.6
            k "oof"
            heavy "heavy stop weird kid"
            k "WHY YOU COCKBLOCKING ME HEAVY"
            k "GET THE FUCK OUT OF MY WAY"
            show kody:
                subpixel True pos (1500, 625) xzoom 0.85 yzoom 0.85
                linear 0.1 xpos 2100 ypos 625
            show heavy_tf2:
                subpixel True pos (1563, 498) xzoom 0.4 yzoom 0.4
                linear 0.1 xpos 1200 ypos 498
            pause 1.0
            t "damn"
            show thanga2:
                subpixel True pos (3, 556)
                linear 0.5 xpos 600 ypos 556
            pause 1.0
            t "well what are you guys going to do?"
            heavy "heavy going to polish gun"
            show heavy_tf2:
                subpixel True pos (1200, 498) xzoom 0.4 yzoom 0.4
                linear 0.6 xpos 2100 ypos 498
            pause 1.0
            pw "I think I'm going to look over some of the clues again"
            pw "Do you want to come with me Matt?"
            mt "..."
            mt "sure"
            show phoenix_wright:
                subpixel True pos (975, 558) xzoom 0.6 yzoom 0.6
                linear 0.8 xpos 2225 ypos 558
            show matt2:
                subpixel True pos (850, 580) xzoom 0.5 yzoom 0.5
                linear 0.8 xpos 2100 ypos 580
            pause 1.5
            t "WHY DOES NO ONE WANT TO TALK TO ME"
            t "FUCK ALL OF YOU"
            t "IM GOING TO MY ROOM"
            window auto hide
            show black with fade
            pause 3.5
            play sound "audio/sound/chapter_two/monokuma_morning.ogg"
            window auto hide
            $ renpy.pause(17.0, hard=True)
            t "i dont wanna..."
            t "10 more minutes..."
            window auto hide
            play sound "audio/sound/chapter_one/glock_magchange.ogg"
            pause 2.0
            $ baldi_shoot(20)
            scene danganronpa_dorm with fade:
                subpixel True
            show thanga2 with dissolve:
                subpixel True pos (445, 343)
            t "AAAAHHHHHH"
            t "IM FUCKING DEAD"
            t "..."
            t "huh?"
            t "i thought i got shot"
            play sound "audio/sound/chapter_two/monokuma_appear.ogg"
            play music "audio/music/chapter_two/monokuma_theme.ogg"
            show monokuma:
                subpixel True pos (0.54, 0.48) zoom 0.7
                ypos 0.82
                yzoom 0.0
                linear 0.35 ypos 0.48 yzoom 1.0
            window auto hide
            with Pause(1.5)
            play sound "audio/sound/chapter_two/monokuma_mad.ogg"
            m "I FUCKING HATE THAT ANNOUNCER"
            t "oh i thought you shot me for not waking up"
            m "oh i was about to but you already woke up"      
            show gun2:
                subpixel True pos (0.5, 0.62) xzoom 0.3 yzoom 0.25 
            play sound "audio/sound/chapter_one/glock_magchange.ogg"
            pause 2.5
            m "now get your ass down to the hall"
            t "is the trial ready yet?"
            t "and why are you so mad?"
            m "cause everyone else is already there"
            m "and no, the trial is not ready yet"
            m "but it will be soon"
            t "how is everyone at the hall already?"
            t "the alarm literally went off like 10 seconds ago"
            m "brotha"
            m "you went back to sleep for 30 minutes"
            m "even brian and his slow ass is in the hall"
            m "SO GET MOVING"
            hide gun2
            stop music
            show monokuma:
                subpixel True pos (0.54, 0.48) zoom 0.7
                linear 0.2 xpos 0.75 ypos 0.31
            pause 0.2
            hide monokuma with dissolve
            pause 1.0
            t "alright jeez"
            t "can i not sleep in just for one day?"
            $ count = 9
            call chapter_two_restore_movement(1)

        label chapter_two_before_trial:
            call chapter_two_all_except_cody
            hide ocho
            hide thanga2
            pause 0.6           
            show thanga2 with dissolve:
                subpixel True pos (3, 556)
            pause 0.5
            b "look whos slow ass finally got out of bed"
            k "shut up brian you only got here 3 minutes ago"
            b "..."
            m "now that everyone is here"
            m "the trial will be ready soon"
            m "you just need to find the hidden door"
            t "what?"
            t "i thought we would take an elevator down"
            m "WELL SOME STUFF CHANGES OKAY THANG"
            m "SHUT YOUR WEEB ASS UP AND FIND THE HIDDEN DOOR"
            t "..."
            pw "What is going to happen during the trial?"
            march "Will we have to blame someone for the murder?"
            play sound "audio/sound/chapter_two/monokuma_agree.ogg"
            m "yup"
            m "you will decide who killed ocho and they will face a horrible death"
            march "There's no way we can do that!"
            march "And I still believe that no one killed him!"
            pw "Me too!"
            mt "..."
            m "WELL SOMEONE DID"
            m "AND I WANT TO KNOW AS WELL"
            t "then how is this going to be a fair trial?"
            m "SHUT UP"
            m "JUST GO AND FIND THE HIDDEN DOOR"
            m "BY THE TIME YOUR SLOW ASS FINDS IT THE TRIAL WILL PROBABLY BE OVER"
            play sound "audio/sound/chapter_two/monokuma_appear.ogg"
            show monokuma:
                subpixel True pos (0.37, 0.76) xzoom 0.5 yzoom 0.5
                ypos 0.76
                yzoom 0.5
                linear 0.2 ypos 1.0 yzoom 0.5
            window auto hide
            with Pause(1.5)
            t "damn, why does he hate me so much?"
            k "..."
            b "..."
            mt "..."
            march "..."
            heavy "..."
            pw "..."
            t "come on..."
            pw "Well, we should try to find that hidden door he mentioned"
            heavy "heavy will find it first"
            show heavy_tf2:
                subpixel True pos (1563, 498) xzoom 0.4 yzoom 0.4
                linear 0.3 xpos 2100 ypos 498
            pause 1.5
            march "I will go with him as well"
            show march_7th:
                subpixel True pos (1373, 605) xzoom 0.15 yzoom 0.15
                linear 0.3 xpos 2100 ypos 605
            pause 1.0
            k "COME BACK MY MAIDEN"
            show kody:
                subpixel True pos (186, 625) xzoom 0.85 yzoom 0.85
                linear 0.2 xpos 2100 ypos 625
            pause 3.5
            b "fine..."
            b "ill go after that gooner"
            b "lets go matt"
            show brian3:
                subpixel True pos (381, 498) xzoom 0.45 yzoom 0.45
                linear 0.5 xpos 1961 ypos 498
            pause 1.0
            mt "ok..."
            show matt2:
                subpixel True pos (1065, 580) xzoom 0.5 yzoom 0.5
                linear 0.8 xpos 2100 ypos 580
            pause 1.5
            show thanga2:
                subpixel True pos (3, 556)
                linear 6.0 xpos 900 ypos 556
            t "please phoenix... please stay with me"
            pw "uhh..."
            pw "I'm going to go look for the door as well"
            t "NOOO PLEASE"
            t "I NEED AT LEAST ONE FRIEND"
            show phoenix_wright:
                subpixel True pos (1171, 558) xzoom 0.6 yzoom 0.6
                linear 0.3 xpos 2100 ypos 558
            window auto hide
            pause 3.0
            t "fine..."
            t "ill show you all..."
            t "ILL SHOW ALL OF YOU HOW COOL I AM!!!"
            t "I WILL FIND THE HIDDEN DOOR FIRST!!!"
            t "AND PROVE HOW GOOD I AM!!!"
            $ count = 10
            call chapter_two_restore_movement(4)

        return