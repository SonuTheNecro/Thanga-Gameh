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
            yalign -0.05
            idle "images/ArrowUpPress.png"
            hover "images/ArrowUpPress.png"
            if origin == 7:
                action Jump("ch02_area_6")
            elif origin == 6:
                action Jump("ch02_area_3")
            elif origin == 3:
                action Jump("ch02_area_1")
    screen chapter_two_danganronpa_down_button(origin):
        imagebutton:
            xalign 0.5
            yalign 0.995
            idle "images/ArrowDownPress.png"
            hover "images/ArrowDownPress.png"
            if origin == 1:
                action Jump("ch02_area_3")
            elif origin == 3:
                action Jump("ch02_area_6")
            elif origin == 6:
                action Jump("ch02_area_7")
    screen chapter_two_danganronpa_left_button(origin):
        imagebutton:
            xalign 0.005
            yalign 0.5
            idle "images/ArrowLeftPress.png"
            hover "images/ArrowLeftPress.png"
            if origin == 3:
                action Jump("ch02_area_2")
            elif origin == 4:
                action Jump("ch02_area_3")
            elif origin == 6:
                action Jump("ch02_area_5")
    screen chapter_two_danganronpa_right_button(origin):
        imagebutton:
            xalign 0.995
            yalign 0.5
            idle "images/ArrowRightPress.png"
            hover "images/ArrowRightPress.png"
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
        pass
    elif location == 2:
        pass
    elif location == 3:
        pass
    elif location == 4:
        pass
    elif location == 5:
        pass
    elif location == 6:
        pass
    elif location == 7:
        pass
    call chapter_two_restore_movement(location)
    return