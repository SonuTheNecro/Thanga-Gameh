# This is the codebase written for Chapter Two
# Main Writer: TacticalVortex
# Extra Help: SonuTheNecro
# All imagees: Google Images
# All sounds: Freesounds.com


# Chapter Two Characters/Variables
define bk = Character("Brian and Kody")
define bkm = Character("Brian, Kody, and Matt")
define m = Character("Monokuma")
define mt = Character("Matt")
define ocho = Character("Ocho")
define march = Character("March 7th", who_color="#B0E6FA")
define emarch = Character("Evil March 7th", who_color="#5c1d1d")
define heavy = Character("Heavy")
define pw = Character("Phoenix Wright")
define ev = Character("Everyone")

default persistent.chapter_two_gym = False

label chapter_two:
    scene black with fade
    stop music
    "Chapter 2: The Trial of Eights"
    t "NO PLEASE NOT AGAIN"
    hide black
    show street1 with fade:
        subpixel True yzoom 1.06
    show thanga2:
        subpixel True pos (0.19, 480) 
    show kody:
        subpixel True pos (0.33, 540) 
    show brian1:
        subpixel True pos (0.69, 490) 
    t "..."
    k "WHY THE FUCK ARE WE BACK HERE?"
    t "THANK GOD IM NOT BLACK STILL"
    k "that's what you're worried about?"
    play music "audio/music/chapter_two/monokuma_theme.ogg"
    window auto hide
    with Pause(4)
    b "what's that weird music?"
    t "nuh uh nope not doing this again"
    bk "do what again?"
    hide thanga2
    hide kody
    hide brian1
    play sound "audio/sound/chapter_two/monokuma_appear.ogg"
    show monokuma:
        subpixel True pos (0.4, 550)
        ypos 1.0
        yzoom 0.0
        linear 0.35 ypos 0.51 yzoom 1.0
    window auto hide
    with Pause(0.7)
    play sound "audio/sound/chapter_two/monokuma_hey.ogg"
    questionmark "what are you guys doing out here?"
    show thanga2:
        subpixel True pos (0.1, 481) 
    show kody:
        subpixel True pos (0.23, 543)  
    show brian1:
        subpixel True pos (0.69, 490) 
    show monokuma:
        subpixel True pos (0.4, 550)
    k "i don't know, we kinda just showed up here again"
    t "STOP TALKING TO HIM I'M LEAVING"
    questionmark "cmon don't be mad, i just want to help"
    questionmark "here, have some water"
    k "thanks"
    b "thanks"
    t "DON'T SAY I DIDN'T WARN YOU ALL"
    play sound "audio/sound/chapter_two/minecraft_drink.ogg"
    window auto hide
    with Pause(2)
    $ _preferences.afm_enable = True
    $ _preferences.afm_time = 8
    b "wait, this isn't water this is cu-"
    show black with fade
    stop music
    play sound "audio/sound/chapter_two/body_fall.ogg"
    play sound "audio/sound/chapter_two/body_fall.ogg"
    play sound "audio/sound/chapter_two/body_fall.ogg"
    $ _preferences.afm_enable = False
    with Pause(5)
    scene danganronpa_classroom with fade:
        subpixel True xzoom 0.76 yzoom 0.76 
    with Pause(1)
    t "how did brian know what that was..."
    t "nevermind"
    t "more importantly WHAT THE FUCK AM I DOING HERE"
    t "..."
    t "...."
    t "....."
    t "guess i'll have to use my knowledge to beat this game"

    label chapter_two_note_repeat:
        "Click on parts of a room to interact with them"
        call screen clickable_chapter_two_note()
        jump chapter_two_note_repeat

    label chapter_two_classroom_note:
        hide screen clickable_chapter_two_note
        t "lets see what this note says..."
        questionmark "We have gathered the 8 ultimates in this building."
        questionmark "The next part will reveal itself when you all meet."
        t "..."
        t "damn they really ripping of the game huh"
        t "welp time to leave"
        jump chapter_two_meeting

    label chapter_two_meeting:
        scene danganronpa_vault with fade:
            subpixel True xzoom 0.76 yzoom 0.76 
        show thanga2:
            subpixel True pos (18, 558) xzoom 0.9 yzoom 0.9 
        show kody:
            subpixel True pos (234, 630) xzoom 0.85 yzoom 0.85 
        show brian3:
            subpixel True pos (450, 495) xzoom 0.45 yzoom 0.45 
        show matt2:
            subpixel True pos (1008, 585) xzoom 0.17 yzoom 0.17 
        show ocho:
            subpixel True pos (873, 900) xzoom 0.35 yzoom 0.35 
        show march_7th:
            subpixel True pos (1359, 603) xzoom 0.15 yzoom 0.15 
        show phoenix_wright:
            subpixel True pos (1152, 558) xzoom 0.6 yzoom 0.6 
        show heavy_tf2:
            subpixel True pos (1557, 495) xzoom 0.4 yzoom 0.4  
        t "how is everyone here already"
        k "bro its been like 2 hours where were you?"
        b "probably gooning"
        t "nevermind that, who the fuck are the other guys?"
        t "and how the fuck is matt here?"
        k "idk go talk to them it ain't hard"
        t "no it's really hard"
        t "I need my me time"
        k "Your timemaxxing sucks"
        t "kill yourself"
        $ location = 0
        $ rngint = 0
        $ rngint1 = 0
        $ choice = 0
        $ count = 0
        $ count2 = 0

    label chapter_two_new_characters:
        if count == 5:
            jump chapter_two_after_characters
        while count < 5:
            window hide
            show screen clickable_chapter_two_ocho()
            show screen clickable_chapter_two_march()
            show screen clickable_chapter_two_heavy()
            show screen clickable_chapter_two_matt()
            show screen clickable_chapter_two_phoenix()
            $ renpy.pause()

    label chapter_two_after_characters:
        t "wow this is a weird group of people"
        ev "No you're the weird one"
        t "wow guys"
        t "anyway how come some of you had intro's?"
        pw "I'm not sure. Do you guys have anything you're good at?"
        k "nope"
        b "nope"
        t "yeah a lot of things"
        bk "nothing for thang either"
        pw "Maybe that's why"
        pw "Also wasn't the name of this chapter \"The Trial of Eights\"?"
        pw "Where is the eighth person?"
        k "how do you know that?"
        t "i thought ocho was the eight person"
        march "You're silly Thang! Ocho is a dog!"
        t "then who is the eighth person?"
        play movie "video/chapter_two/cody_intro.webm"
        call dio_time_stop
        pause 2.0
        stop movie
        scene danganronpa_vault:
            subpixel True xzoom 0.76 yzoom 0.76 matrixcolor InvertMatrix(1.0)
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
        show cody:
            subpixel True pos (729, 625) xzoom 0.85 yzoom 0.85 
        c "sup fuckers"
        k "NOT THIS GUY"
        k "AND HOW IS HE THE ULTIMATE HITLER?"
        k "THATS NOT EVEN HIS NAME"
        k "ALSO HOW IS THIS KOSHER?"
        window auto hide
        hide cody
        scene danganronpa_vault:
            subpixel True xzoom 0.76 yzoom 0.76
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
        pause 1.5
        t "uh"
        play sound "audio/sound/chapter_two/monokuma_appear.ogg"
        play music "audio/music/chapter_two/monokuma_theme.ogg"
        show monokuma:
            subpixel True pos (0.38, 0.76) xzoom 0.5 yzoom 0.5
            ypos 1.0
            yzoom 0.0
            linear 0.35 ypos 0.76 yzoom 0.5
        window auto hide
        with Pause(0.7)
        questionmark "don't worry about him i sent him to his room"
        questionmark "i don't want to deal with this inversion stuff either"
        ocho "woof WOOOF"
        ocho "CHOMP"
        play sound "audio/sound/chapter_two/monokuma_mad.ogg"
        questionmark "HEY GET OFF OF ME OCHO"
        ev "its that bear!"
        questionmark "oh i guess i never introduced myself"
        play sound "audio/sound/chapter_two/monokuma_intro.ogg"
        m "My name is Monokuma!"
        t "yea i already knew that i've played your game before"
        m "what game? it hasn't started yet"
        t "but..."  
        stop music
        window auto hide
        play sound "audio/sound/chapter_two/vault_open.ogg"
        show danganronpa_vault_lock:
            subpixel True pos (802, 380) xzoom 0.76 yzoom 0.76
            rotate 0
            linear 3.0 rotate -90
        pause 5.0
        t "huh"
        t "that wasn't in the game"
        show black with fade
        pause 4.0

        label chapter_two_gym:
            scene danganronpa_gym with fade:
                subpixel True xzoom 0.76 yzoom 0.76
            call chapter_two_all_except_cody
            hide monokuma
            t "alright so what do we do now?"
            b "what do we do? we beat this bears ass"
            heavy "Yes. Heavy no lose to little bear"
            t "nuh uh nope no one is fighting that bear. you will die"
            heavy "You are weak man. No need to follow weak man"
            t "what about cody? he would have done something if he could have"
            heavy "..."
            heavy "Heavy will eat sandvich"
            b "alright pussies ill do it then"
            "What should you do?"
            menu:
                "Let Brian fight Monokuma":
                    jump brian_fight_monokuma
                "Stop Brian":
                    jump stop_brian
            label brian_fight_monokuma:
                b "im gonna beat his little ass"
                window auto hide
                show gun2:
                    subpixel True pos (0.48, 0.58) xzoom 0.15 yzoom 0.15 
                play sound "audio/sound/chapter_one/glock_magchange.ogg"
                pause 2.0 
                show gunflare:
                    subpixel True pos (830, 583) xzoom 0.2 yzoom 0.2 
                $ baldi_shoot(15)
                jump game_over
            label stop_brian:
                t "no brian stop don't you see that gun"
                show gun2:
                    subpixel True pos (0.48, 0.58) xzoom 0.15 yzoom 0.15 
                play sound "audio/sound/chapter_one/glock_magchange.ogg"
                pause 2.0 
                b "damn man is strapped"
                play sound "audio/sound/chapter_two/monokuma_agree.ogg"
                m "Yep, and i'm not afraid to use it!"
                march "Alright! We will do whatever you want!"
                march "Just don't shoot anybody!"
                k "see, the rizz worked"
                k "shes trying to protect me"
                t "..."
                pw "Alright, what do you want us to do then?"
                m "I brought you guys here for one reason"
                m "And that is to kill each other!"
                pw "..."
                march "..."
                heavy "..."
                mt "..."
                b "..."
                k "..."
                $ _preferences.afm_enable = True
                $ _preferences.afm_time = 6
                t "yea i knew tha-"
                $ _preferences.afm_enable = False
                ev "WHAAAATTT?!?"
                pw "You can't make us do that!"
                march "That's right!"
                march "Even though I just met these people, I could never kill them!"
                heavy "As long as you have no problem with Heavy, Heavy have no problem with you"
                k "i could never kill brian or matt!"
                b "yea me neither"
                mt "or me!"
                t "what about me"
                bkm "well..."
                t "bruh"
                m "Oh trust me"
                m "I'll make sure you will want to kill each other"
                t "and how will you do that?"
                t "by showing us our families?"
                t "or revealing our deepest secrets?"
                t "well too bad for you"
                t "my family already doesn't care for me!"
                t "and everyone already knows about me gooning!"
                ev "..."
                hide gun2
                m "..."
                m "i was only saying that just in case someone wanted to kill another person"
                m "i was just gonna kill someone and pin it on someone else or something"
                t "..."
                m "im kinda bored now so ill show you the rest of the building"
                show black with fade

        label chapter_two_after_gym:
            scene danganronpa_hallway with fade:
                subpixel True xzoom 0.76 yzoom 0.76
            call chapter_two_all_except_cody
            m "this is the hallway connecting the different rooms"
            m "the bathrooms are broken though so you can't use them"
            m "use the ones in your rooms"
            k "but what if i need to go now?"
            m "too bad"
            b "dont piss your pants like last time"
            scene danganronpa_nurse with fade:
                subpixel True zoom 0.76
            call chapter_two_all_except_cody
            m "this is the nurses office"
            m "come here if you get hurt"
            m "or don't cause i want you guys to die"
            k "but there is no nurse, so who will i be able to rizz?"
            t "what about saving you?"
            march "Don't worry guys! I know a few tricks in first-aid!"
            k "the rizzler strikes again"
            t "???"
            scene danganronpa_hallway with fade:
                subpixel True xzoom 0.76 yzoom 0.76
            scene danganronpa_lobby with fade:
                subpixel True xzoom 0.76 yzoom 0.76
            call chapter_two_all_except_cody
            m "this is the lobby"
            m "it connects to the hall, changing room, dorms, and hallway leading to the gym"
            scene danganronpa_hall with fade:
                subpixel True zoom 0.76
            call chapter_two_all_except_cody
            m "this is the hall where you guys will meet after waking up"
            m "you guys will also be eating here"
            k "WE GET FREE FOOD!?"
            k "IS IT MCDONALDS OR CHUCK E CHEESE??"
            m "no fatass its salads and vitamin shakes only"
            k "FUUCCCKKKK"
            k "also what time will we be waking up?"
            k "12? 1?"
            m "8"
            k "8 P.M?? LETS FUCKING GO"
            m "8 A.M"
            k "FFFFFFUUUUUUUUCCCCCCCKKKKKKK"
            scene danganronpa_lobby with fade:
                subpixel True xzoom 0.76 yzoom 0.76
            scene danganronpa_changing with fade:
                subpixel True xzoom 0.76 yzoom 0.76
            call chapter_two_all_except_cody
            m "this is the changing room for the pool"
            mt "lets go i can swim with ocho"
            heavy "Heavy also like to svim"
            m "sorry but the pool is also closed"
            k "dangit"
            march "Aww man. I was also looking foward to swimming."
            k "NNNNNNNOOOOOOOOOOOOOOOOOOOOOOOO"
            scene danganronpa_lobby with fade:
                subpixel True xzoom 0.76 yzoom 0.76
            scene danganronpa_hall with fade:
                subpixel True zoom 0.76
            call chapter_two_all_except_cody
                
            $ persistent.chapter_two_gym = True #Better testing to get back here
            "test"
    

