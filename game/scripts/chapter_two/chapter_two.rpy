# This is the codebase written for Chapter Two
# Main Writer: TacticalVortex
# Extra Help: SonuTheNecro
# All images: Google Images
# All sounds: Freesounds.com


# Chapter Two Variables
default persistent.chapter_two_gym = False

label chapter_two:
    scene black with fade
    stop music
    $ discord.update(details = "In Chapter Two", large_image = "chapter_two")
    "Chapter 2: The Trial of Eights"
    t "NO PLEASE NOT AGAIN"
    if persistent.ch02:
        $ config.rollback_enabled = True
    scene street1 with fade:
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
            subpixel True pos (1008, 585) xzoom 0.5 yzoom 0.5 
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
            subpixel True pos (1065, 580) xzoom 0.5 yzoom 0.5
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
            subpixel True pos (1065, 580) xzoom 0.5 yzoom 0.5
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
        window auto hide
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
            m "7"
            k "7 P.M?? LETS FUCKING GO"
            m "7 A.M"
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
            b "I just realized I am going to miss work"
            b "I gotta call my manager rq"
            ev "YOU HAVE YOUR PHONE!"
            t "BRIAN CALL THE POLICE OR SOMETHING" #Ring sound here

            $ renpy.pause(delay = 1.0, hard = True)
            b "Uh hey, I won't be able to make it to work"
            ev "..."
            b "yeah its a \"family\" emergency "
            b "dang my pay just got cut by $27 per hour"
            mt "wait how much were you making per hour?"
            b "14.50"
            mt "WHATTTTTTTTTTTTTTTTTTTTTTT"
            t "BRIAN!"
            b "what?"
            t "CALL SOMEONE FOR HELP!"
            b "uhhhh my phone just died..."
            ev "..."
            t "soooo let me get this straight"
            t "We are stuck in a vault bunker with a murderous bear"
            t "and you WASTE our ONE phone-call"
            t "for FUCKING WORK?"
            b "yeah?"
            t "BRIAN YOU CAN'T HAVE WORK IF YOU FUCKING DIE RIGHT HERE"
            b "oh"
            b "maybe the bear is like chill?"
            t "NO IM THE ONLY ONE HERE WHO KNOWS WHAT THAT BEAR IS CAPABLE OF"
            t "WE ARE DEAD"
            march "Thang, I think you need to calm down"
            ocho "(Barks in sadness)"
            heavy "Yelling is ztrezzin heavy weapons guy"
            mt "let's just go to bed and think over our options tomorrow"
            b "yeah matt's right"
            $ count = 0
            jump ch02_area_1
            $ persistent.chapter_two_gym = True #Better testing to get back here
            "test"
    

    label ch02_area_1:
        $ location = 1
        call chapter_two_hide_screens
        scene danganronpa_dorm with fade:
            subpixel True
        call chapter_two_restore_screens(location)
    label ch02_area_2:
        $ location = 2
        call chapter_two_hide_screens
        scene danganronpa_changing with fade:
            subpixel True xzoom 0.76 yzoom 0.76
        call chapter_two_restore_screens(location)
    label ch02_area_3:
        $ location = 3
        call chapter_two_hide_screens
        scene danganronpa_lobby with fade:
            subpixel True xzoom 0.76 yzoom 0.76
        call chapter_two_restore_screens(location)
    label ch02_area_4:
        $ location = 4
        call chapter_two_hide_screens
        scene danganronpa_hall with fade:
            subpixel True zoom 0.76
        call chapter_two_restore_screens(location)
    label ch02_area_5:
        $ location = 5
        call chapter_two_hide_screens
        scene danganronpa_nurse with fade:
            subpixel True zoom 0.76
        call chapter_two_restore_screens(location)
    label ch02_area_6:
        $ location = 6
        call chapter_two_hide_screens
        scene danganronpa_hallway with fade:
            subpixel True xzoom 0.76 yzoom 0.76
        call chapter_two_restore_screens(location)
    label ch02_area_7:
        $ location = 7
        call chapter_two_hide_screens
        scene danganronpa_gym with fade:
            subpixel True xzoom 0.76 yzoom 0.76
        call chapter_two_restore_screens(location)

    label chapter_two_trial:
        hide screen clickable_chapter_two_hidden_door
        show black with fade
        pause 1.5
        hide danganronpa_dorm
        t "wow... its dark in here"
        t "and why was the hidden door my bathroom?"
        t "how did i never notice?"
        questionmark "cause you suck thang"
        t "WHO SAID THAT"
        show danganronpa_elevator with fade:
            subpixel True zoom 0.75
        pause 0.5
        b "i did"
        b "bitch"
        hide black
        t "how are all of you in here"
        t "this was in my bathroom"
        b "cause we all found it before you"
        b "your slow ass took 4 hours to find it"
        k "yea i found it when i was gooning in here before"
        t "..."
        pw "Well, now that we are all here..."
        pw "What's going to happen?"
        march "I'm wondering that too!"
        t "well im guessing that the elevator is going to..."
        window auto hide
        play sound "audio/sound/chapter_two/elevator_sound.ogg"
        pause 0.3
        show danganronpa_elevator with vpunch:
            subpixel True zoom 0.75
        $ renpy.pause(19.4, hard=True)
        show danganronpa_elevator with vpunch:
            subpixel True zoom 0.75
        pause 1.0
        t "..."
        t "really"
        t "we had to wait 20 seconds for that?"
        pw "It seems we have reached the bottom"
        pw "Is everyone ready?"
        march "I think I am..."
        heavy "heavy going in"
        t "WAIT"
        window auto hide
        show black with fade
        pause 3.0
        show danganronpa_trial_monokuma with dissolve:
            subpixel True zoom 0.77
        pause 0.6
        play sound "audio/sound/chapter_two/monokuma_laugh.ogg"
        m "guess you guys are finally here"
        m "it is finally time to..."
        m "START THE TRIAL"
        window auto hide
        hide danganronpa_trial_monokuma with fade
        pause 2.0
        show danganronpa_full_trial with dissolve:
            subpixel True zoom 1.88
        show danganronpa_full_trial with dissolve:
            subpixel True zoom 1.88
            linear 20.0 xpos -7665
        $ renpy.pause(20.5, hard=True)
        t "what the...."
        show danganronpa_full_trial with hpunch:
            subpixel True zoom 1.88
            linear 1.0 xpos -3201
        pause 1.5
        t "this is the trial room?"
        call chapter_two_trial_phoenix
        pw "What is all of this?"
        call chapter_two_trial_brian
        b "yea why the fuck am i next to thang"
        call chapter_two_trial_thang
        t "idk bitch ask monokuma"
        call chapter_two_trial_kody
        k "YEA STUPID BEAR WHY AM I NOT NEXT TO MARCH"
        call chapter_two_trial_heavy
        heavy "heavy is confused"
        play sound "audio/sound/chapter_two/monokuma_mad.ogg"
        m "CAN ALL OF YOU SHUT THE FUCK UP"
        m "YOU ARE MAKING THE CAMERA MOVE TOO MUCH"
        call chapter_two_trial_thang
        t "how is that our problem?"
        t "and where the fuck is there a camera?"
        m "bro you are looking straight at it"
        m "..."
        m "fine"
        m "ill make it so the camera is focused on the most important person talking"
        call chapter_two_trial_kody
        play sound "audio/sound/general/rizz.ogg"
        k "thats gotta be me right?"
        call chapter_two_trial_brian
        b "no fucker its me"
        t "can you guys stop talking?"
        t "..."
        t "WHY THE FUCK IS IT NOT FOCUSING ON ME"
        m "cuz you a bitch"
        m "anyway..."
        m "its time for the trial to commence!"
        call chapter_two_trial_thang
        m "all of you will discuss the evidence you have collected..."
        call chapter_two_trial_phoenix
        m "in this special game of whodunnit"
        call chapter_two_trial_march
        m "if you can figure out who the whitened is..."
        call chapter_two_trial_cody
        m "then only they will die"
        call chapter_two_trial_heavy
        m "however, if anyone guesses incorrectly..."
        call chapter_two_trial_matt
        m "then everyone except for the whitened will die"
        call chapter_two_trial_brian
        m "who will be voted out?"
        call chapter_two_trial_kody
        m "who is the true whitened?"
        call chapter_two_trial_thang
        m "play the game to find out"
        t "..."
        t "thats what they are doing dumbass"
        t "also i thought it was the blackened not the whitened"
        m "bro thats racist"
        t "..."
        m "anyway..."
        m "start talking"
        t "..."
        t "i mean"
        t "its definitely cody right?"
        call chapter_two_trial_cody
        march "Yeah, i was suspecting him too"
        c "WHAT THE FUCK ARE YOU TALKING ABOUT"
        c "I WOULD NEVER DO THAT TO OCHO"
        c "IF ANYTHING"
        c "I THINK ITS KODY"
        c "HE DIDNT SEEM TO CARE WHEN OCHO DIED"
        call chapter_two_trial_kody
        k "..."
        c "WELL KODY"
        c "WHAT DO YOU HAVE TO SAY"
        k "..."
        k "i was gooning bro"
        t "..."
        t "yea that sounds about right"
        b "yup"
        mt "yup"
        k "and what reason would i have to kill ocho anyway?"
        c "cause he got in the way of your gooning"
        k "..."
        t "kody"
        k "..."
        c "SEE"
        c "NOW LETS VOTE HIM OUT"
        $ count = 0
        "Are you ready to vote?"
        menu:
            "Yes":
                jump chapter_two_vote
            "No":
                jump chapter_two_deny_first_vote

    label chapter_two_deny_first_vote:
        t "NO NOT YET"
        t "we havent even gone over any of the clues"
        pw "Correct, we need to look at every piece of evidence"
        call chapter_two_trial_heavy
        heavy "heavy find picture"
        march "You did? Does it show who did it?"
        heavy "heavy forgot"
        heavy "heavy gave picture to thang"
        t "yea he found it after running around a bit in the lobby"
        t "its just a picture of ocho"
        t "but it was taken when he was still alive"
        t "it could have been used to plan the murder..."
        t "or planted to blame someone else"
        c "OR KODY COULD HAVE USED IT FOR GOONING"
        t "..."
        t "no"
        t "but i dont think this helps us that much"
        t "anyone could have taken a picture of him"
        pw "But who would most likely have it?"
        call chapter_two_trial_matt
        pw "It would of course be Matt!"
        t "and?"
        t "it wouldnt be weird that he had a picture of his dog"
        t "that doesnt help us"
        mt "but i didnt"
        t "what"
        mt "why would i just have a picture of him on me?"
        mt "he was literally with me"
        t "idk cause you love him?"
        mt "well thats fair"
        pw "So, if Matt didn't have the picture..."
        pw "Then who did?"
        t "yeah bro thats what we are trying to figure out"
        t "did anyone have this picture"
        heavy "no"
        march "no"
        b "no"
        k "no"
        c "no"
        m "no"
        t "we didnt ask you"
        t "so, someone is lying"
        c "IT HAS TO BE KODY"
        t "SHUT UP"
        pw "Well should we look at the other clues?"
        call chapter_two_trial_phoenix
        pw "I found some liquid under one of the benches"
        b "was it kodys piss"
        t "no i already asked that"
        t "it was apparently just water"
        pw "Yes, and based off of the temperature..."
        pw "It was only there for around an hour"
        pw "Which lines up with the murder"
        t "how did you even calculate that?"
        mt "so the murderer messed up some how?"
        pw "That is a possibility"
        c "THAT MEANS IT HAS TO BE KODY"
        c "BRO HAS BEEN WATERMAXXING"
        t "but i dont think he would spill it"
        k "..."
        t "kody"
        k "..."
        c "AGAIN ITS GOTTA BE HIM"
        t "chill out"
        t "we still have some clues to look at"
        t "and wouldnt you be watermaxxing too since you are also cody?"
        march "I was thinking about that too..."
        march "This makes me even more suspicious of Cody"
        c "..."
        c "FORGET ABOUT THAT"
        c "WE NEED TO FIGURE OUT HOW HE DIED"
        pw "I found a puncture wound in the side of his neck"
        c "THEN THERE SHOULD HAVE BEEN BLOOD"
        c "WAS THE WATER USED TO CLEAN IT UP?"
        pw "No, the water was not disturbed at all"
        pw "And if they used it to clean up..."
        pw "Then they would not have left any at the scene"
        t "wait..."
        t "this doesnt add up"
        t "something contradicts this"
        $ count2 = 0
        "What clue contradicts Phoenix's claim?"
        menu:
            "Spotless Crime Scene":
                t "THEN HOW WAS THE CRIME SCENE SPOTLESS?"
                $ count2 = 1    
            "Water Puddle":
                t "THEN WHY WAS THE WATER PUDDLE THERE?"
            "Picture of Ocho":
                t "THEN WHY WAS THERE A PICTURE OF OCHO?"
            "Missing Paper Towels and Toilet Paper":
                t "THEN WHY WERE THE PAPER TOWELS AND TOILET PAPER MISSING?"
            "Monokumas Tape":
                t "THEN WHY DOES MONOKUMA HAVE A SEXTAPE?"
                m "HOW THE FUCK DO YOU KNOW ABOUT THAT"
        if count2 == 0:
            b "thang you dumb as hell boy"
            k "yea thang that has nothing to do with this"
            march "I think that there being no blood is weird though..."
            march "How would the scene be spotless if the water wasn't used?"
        else:
            b "wow thang you actually thought of something good for once"
        pw "I do find that peculiar..."
        pw "One theory I have is that Ocho was killed somewhere else..."
        pw "And brought to the changing room"
        march "Oh yeah, me and Thang talked about that too"
        pw "That seems the most plausible..."
        pw "But then what about the smell of the blood?"
        pw "Did anyone smell anything when searching the building?"
        ev "No"
        pw "Then this just adds more questions to the equation"
        mt "couldnt they have just cleaned it up in another room?"
        pw "To do that, they would need a lot of supplies to clean it up"
        mt "well i went to the nurses office and a lot of stuff was gone"
        mt "like the paper towels and toilet paper"
        pw "..."
        pw "THAT'S A MASSIVE CLUE"
        pw "Does anyone know who took them?"
        t "..."
        t "i think i have an idea"
        call chapter_two_hangman
    
    label chapter_two_hangman_win:
        scene black with fade
        pause 1.5
        window auto hide  
        show danganronpa_full_trial with dissolve:
            subpixel True xpos -3201 zoom 1.88 
        pause 0.6
        t "its gotta be kody"
        t "bro has been gooning the whole time"
        k "..."
        pw "Kody..."
        b "of course it would be him"
        k "yea it was"
        t "..."
        t "guess thats one less clue we have"
        k "i didnt take all of them tho"
        k "i left behind half of a toilet paper roll"
        t "..."
        t "thats it?"
        t "but thats still important"
        t "we dont know who took that"
        t "..."
        t "but thats everything"
        t "we dont have any more clues"
        pw "We don't?"
        t "no, thats everything that was found"
        b "damn yall suck"
        t "YOU DIDNT DO ANYTHING"
        call chapter_two_trial_kody
        k "but what about the tape i found?"
        ev "..."
        pw "WHAT TAPE"
        k "the one i found in the gym"
        t "..."
        t "I FUCKING TOLD YOU TO NOT TALK ABOUT THAT"
        window auto hide
        play sound "audio/sound/chapter_two/monokuma_appear.ogg"
        show monokuma:
            subpixel True pos (0.54, 0.6) xzoom 0.7 yzoom 0.7
            ypos 1.0
            yzoom 0.0
            linear 0.35 ypos 0.66 yzoom 0.7
        pause 1.5  
        show gun2:
            subpixel True pos (0.49, 0.75) zoom 0.3 rotate 9.0  
        play sound "audio/sound/chapter_one/glock_magchange.ogg"
        pause 2.0
        m "give me the fucking tape"
        m "NOW"
        k "OK OK"  
        window auto hide 
        show ipad:
            subpixel True pos (966, 456) zoom 0.3
        pause 0.3    
        show ipad:
            subpixel True pos (966, 456) zoom 0.3
            linear 0.2 xpos 1183 ypos 888
        pause 0.4
        play sound "audio/sound/chapter_two/monokuma_appear.ogg"
        pause 0.2
        show monokuma:
            subpixel True pos (0.54, 0.6) xzoom 0.7 yzoom 0.7
            linear 0.2 ypos 1.1 
        show ipad:
            subpixel True pos (1183, 888) zoom 0.3
            linear 0.2 ypos 1200 
        show gun2:
            subpixel True pos (0.49, 0.75) zoom 0.3 rotate 9.0
            linear 0.2 ypos 1.1
        pause 1.6
        k "..."
        t "NOW YOU FUCKED EVERYTHING UP"
        t "THAT WAS OUR LAST CLUE"
        t "EVERYTHING WOULD BE SOLVED WITH THAT"
        pw "What was it?"
        march "Yeah, why was that so important?"
        b "i thought that was just his goon shit"
        t "NO IT HAD FOOTAGE OF THE MURDER"
        t "WE WOULD HAVE KNOWN WHO DID IT"
        ev "..."
        ev "WHAT THE FUCK KODY"
        k "..."
        k "my b"
        t "BROTHA"
        t "..."
        t "well..."
        t "now what?"
        t "we dont have any more clues"
        t "so the only thing we have left is to vote"
        c "YES"
        c "NOW ITS TIME TO VOTE FOR KODY"
        c "HE JUST GAVE UP THE MOST IMPORTANT EVIDENCE"
        c "ITS OBVIOUS THAT ITS HIM"
        t "shut up cody"
        t "i think we have everything we need"
        call chapter_two_trial_thang
        t "given all of the clues..."
        t "its obvious who it is"
        t "they put the blame on someone else..."
        t "could have had the picture..."
        t "has a relation to the water..."
        t "and monokuma never went to their room"
        t "..."
        t "do we all agree on this?"
        ev "Yes"
        window auto hide
        pause 1.5
        $ count = 1
        call chapter_two_vote     

    label chapter_two_vote:
        m "looks like everyone is ready to vote"
        "Who are you voting for?"
        menu:
            "Thang":
                jump chapter_two_trial_fail
            "Brian":
                jump chapter_two_trial_fail
            "Kody":
                jump chapter_two_trial_fail
            "Phoenix":
                jump chapter_two_trial_fail
            "March":
                if count == 0:
                    jump chapter_two_trial_fail
                else:
                    $ choice = 0
                    jump chapter_two_trial_win
            "Matt":
                jump chapter_two_trial_fail
            "Heavy":
                jump chapter_two_trial_fail
            "Cody":
                if count == 0:
                    jump chapter_two_trial_fail
                else:
                    $ choice = 1
                    jump chapter_two_trial_win
    
    label chapter_two_trial_fail:
        scene black with fade
        pause 1.5
        show danganronpa_trial_monokuma with dissolve:
            subpixel True zoom 0.77
        pause 0.6
        if count == 0:
            m "everyone voted for the wrong person"      
            show gun2:
                subpixel True pos (0.37, 0.27) xzoom 0.28 yzoom 0.28  
            play sound "audio/sound/chapter_one/glock_magchange.ogg"
            pause 2.0       
            show gunflare:
                subpixel True pos (621, 256) xzoom 0.25 yzoom 0.25  
            $ baldi_shoot(15)
            jump game_over
        else:
            m "thangs dumbass voted for the wrong person"
            show gun2:
                subpixel True pos (0.37, 0.27) xzoom 0.28 yzoom 0.28  
            play sound "audio/sound/chapter_one/glock_magchange.ogg"
            pause 2.0 
            show gunflare:
                subpixel True pos (621, 256) xzoom 0.25 yzoom 0.25 
            $ baldi_shoot(15)
            jump game_over

    label chapter_two_trial_win:
        scene black with fade
        pause 1.5
        show danganronpa_trial_monokuma with dissolve:
            subpixel True zoom 0.77
        pause 0.6
        m "lets see who everyone voted for!"
        window auto hide
        if choice == 1:
            hide danganronpa_trial_monokuma with dissolve
            pause 1.0
            show danganronpa_final_vote_cody with dissolve:
                subpixel True xzoom 0.95 yzoom 0.81 
            pause 1.0
            m "..."
            m "wow"
            m "looks like everyone except for two people voted for march"
            t "WHAT THE FUCK ARE YOU GUYS DOING"
            t "YOU ARE LITERALLY THROWING"
            m "most of you got it!"
            m "except for thang"
            m "his dumbass chose kody"
            m "but ill let it slide"
            m "cause it was expected"
            t "..."
            t "what"
            t "what do you mean they got it"
            t "its cody"
            play sound "audio/sound/chapter_two/monokuma_wrong.ogg"
            m "mmm no"
            m "its march"
            t "..."
            t "WWWWWHHHHHAAAAAATTTTTTTT"
            t "HOW"
            t "ALL OF THE CLUES POINTED TO CODY"
            t "THE WATERMAXXING"
            t "THE BLAMING IT ON KODY"
            t "HAVING THE PICTURE"
            t "AND YOU NOT BEING ABLE TO GET INTO HIS ROOM"
            t "HOW IS IT NOT HIM"
            ev "..."
            pw "Well..."
            pw "I don't recall Monokuma ever going into March's room either"
            pw "And her taking pictures would make sense"
            pw "Also, she was pinning the blame on cody the whole time"
            pw "And the water being there would be from her ice powers"
            pw "I realized that the puncture wound was from her arrow..."
            pw "That's why there was no blood..."
            pw "And why March said the body was cold..."
            pw "Even though he died less than 1 hour before we found him"
            pw "All of the clues that you said pointed to cody..."
            pw "Were the ones that pointed to March"
            t "..."
            b "yea thang we all got that"
            b "how did you not?"
            b "you literally layed everything out"
            b "and your dumbass still couldnt get it"
            t "..."
            t "thats not important anymore"
            t "whats important now is why march did this"
            march "..."
            window auto hide
            hide danganronpa_final_vote_cody with dissolve
        else:
            hide danganronpa_trial_monokuma with dissolve
            pause 1.0     
            show danganronpa_final_vote_march with dissolve:
                subpixel True xzoom 0.95 yzoom 0.81 
            pause 1.0
            m "..."
            m "wow"
            m "looks like everyone except for one person voted for march"
            m "you guys got it!"
            b "dang thang i didnt think you would get that"
            k "me neither"
            c "or me"
            mt "or me"
            pw "..."
            heavy "heavy think thang dumb"
            t "CMON GUYS"
            t "I TOTALLY KNEW THE WHOLE TIME"
            t "I WAS DEFINITELY THE ONE WHO CHOSE MARCH"
            t "..."
            t "wait"
            t "wtf do you mean its march"
            pw "Well..."
            pw "All of the clues you just said all pointed to March"
            pw "As well as the puncture wound and body being cold"
            k "THATS NOT IMPORTANT"
            k "WHY WOULD MY QUEEN DO THIS"
            k "AND WHY DID I GET A VOTE"
            march "..."
            window auto hide
            hide danganronpa_final_vote_march with dissolve
        pause 1.0
        show danganronpa_full_trial with dissolve:
            subpixel True xpos -838 zoom 1.88 
        pause 0.6
        m "..."
        t "uh..."
        k "PLEASE TELL ME I WAS WRONG"
        k "I DIDNT WANT TO VOTE YOU"
        window auto hide
        pause 0.6
        play sound "audio/sound/general/dramatic_violin.ogg"  
        show danganronpa_trial_scary_march with Dissolve(2.0):
            subpixel True xpos 362 zoom 1.88
        pause 1.0
        emarch "shut the fuck up kody"
        emarch "it was me"
        emarch "i killed that stupid fucking dog"
        k "NNNNOOOOOOO"
        mt "..."
        mt "it cant be"
        mt "you are my waifu"
        mt "you cant do this to me"
        emarch "shut your stupid mouth"
        emarch "that dog was annoying the fuck out of me"
        emarch "so i killed him"
        emarch "easy as that"
        mt "..."
        mt "no..."
        mt "WHERE AM I GOING TO FIND A NEW DOG NOW"
        mt "NNNNNNNNNOOOOOOOOOOOOOO"
        t "..."
        t "is that why you were sad the whole time"
        mt "..."
        mt "yes"
        t "SO YOU DIDNT CARE EITHER?"
        t "YOU JUST DIDNT WANT TO LOOK FOR A NEW DOG?"
        mt "..."
        t "OH MY FUCKING GOD"
        t "WHY ARE WE EVEN DOING THIS"
        play sound "audio/sound/chapter_two/monokuma_mad.ogg"
        m "DONT YOU SPEAK BADLY OF OCHO"
        c "HE WAS THE BEST DOG"
        t "..."
        t "why do you guys love him so much more than everyone else"
        emarch "i sure didnt"
        emarch "im glad i killed his ass"
        pw "How could you do this march?"
        heavy "heavy thought he loved you"
        heavy "guess heavy was wrong"
        k "WAIT WAIT WAIT"
        k "ARE YOU TRYING TO STEAL MY GIRL"
        k "GET THE FUCK OVER HERE"
        play sound "audio/sound/chapter_two/monokuma_angry.ogg"
        m "EVERYONE SHUT THE FUCK UP"
        m "THE VOTING IS OVER"
        m "THE TRIAL IS OVER"
        m "MARCH IS GOING TO GET WHAT SHE FUCKING DESERVES"
        emarch "im fine with that"
        emarch "as long as that fucking dog is dead"
        emarch "i dont care what happens next"
        k "march..."
        play sound "audio/sound/chapter_two/monokuma_punishment.ogg"
        m "LETS GIVE IT EVERYTHING WEVE GOT! ITS PUNISHMENT TIME!"
        scene black with Dissolve(2.5)
        play sound "audio/sound/chapter_one/glock_magchange.ogg"
        pause 2.0
        $ baldi_shoot(50)
        pause 1.0
        show danganronpa_trial_monokuma with dissolve:
            subpixel True zoom 0.77
        pause 0.6
        m "..."
        m "well shes dead"
        t "..."
        t "thats it?"
        t "theres no elaborate punishment?"
        t "like getting hit by a train?"
        t "or being frozen in a block of ice?"
        m "hell no"
        m "i aint got time to set up something like that"
        b "BORING"
        play sound "audio/sound/chapter_two/monokuma_angry.ogg"
        m "SHUT THE FUCK UP OR YOU ARE NEXT"
        b "..."
        m "..."
        m "well thats it"
        m "get the fuck out of here"
        m "i dont want to do this anymore"
        m "without ocho being here..." 
        m "there is no point in continuing the killing game"
        play sound "audio/sound/chapter_two/monokuma_laugh.ogg"
        m "See you all next time!"
        scene black with Dissolve(2.0)
        play sound "audio/sound/chapter_two/vault_open.ogg"
        pause 5.0
        jump chapter_two_after_trial

    label chapter_two_after_trial:
        scene street1 with fade:
            subpixel True yzoom 1.06   
        show thanga2:
            subpixel True pos (0.02, 486) 
        show kody:
            subpixel True pos (0.14, 548) 
        show brian1:
            subpixel True pos (0.27, 576) zoom 0.87 
        show matt2:
            subpixel True pos (1043, 495) xzoom 0.55 yzoom 0.55 
        show phoenix_wright:
            subpixel True pos (1235, 445) xzoom 0.72 yzoom 0.72 
        show heavy_tf2:
            subpixel True pos (1493, 420) xzoom 0.45 yzoom 0.45
        pause 1.0
        t "wow..."
        t "that sucked"
        k "MY GIRL IS GONE"
        mt "MY WAIFUUUU"
        mt "AND DOGGG"
        pw "Well..."
        pw "Now that we're out..."
        pw "I gotta head back to Wright Anything Agency"
        pw "Seeya!"
        window auto hide
        hide phoenix_wright with dissolve
        pause 1.0
        heavy "..."
        heavy "heavy going to go too"
        window auto hide
        hide heavy_tf2 with dissolve
        pause 1.0
        k "WAIT YOU BITCH"
        k "YOU TRIED TO TAKE MY GIRL"
        window auto hide
        show kody:
            subpixel True pos (0.14, 548)
            linear 0.2 xpos 1.1
        pause 1.0
        b "ill get his bitch ass"
        window auto hide
        show brian1:
            subpixel True pos (0.27, 576) zoom 0.87 
            linear 1.0 xpos 1.1
        pause 2.0 
        show thanga2:
            subpixel True pos (0.02, 486)
            linear 2.5 xpos 0.4
        t "please matt"
        t "this is like the 3rd time"
        mt "..."
        mt "i gotta buy a new dog" 
        window auto hide
        show matt2:
            subpixel True pos (1043, 495) xzoom 0.55 yzoom 0.55 
            linear 0.4 xpos 1.1
        pause 1.0
        t "..."
        t "im done"
        t "FUCK ALL OF YOU"
        t "THIS FUCKING CHAPTER IS OVER"
        $ persistent.ch02 = True
        $ renpy.quit()
        return