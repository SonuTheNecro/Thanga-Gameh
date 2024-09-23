label return_to_main_from_minigames:
    play music "audio/music/prologue/phantom.ogg" loop
    scene main_menu_bg3
    $ discord.set(details = "In The Main Menu.", large_image = "main_menu", buttons = [dict(label = "SonuTheNecro's Free Promo", url = "https://github.com/SonuTheNecro/Thanga-Gameh")])
    jump main_menu_chapter_select
label minigame_rps:
    call hide_clickable_menus
    $ location = 0 # Win
    $ count2 = 0 #Lose
    $ count = 0 #Draws
    $ rngint1 = renpy.random.randint(1,2)
    play music "audio/music/prologue/you're_my_brother.ogg"
    if rngint1 == 1:
        scene wild_west1 with fade:
            xzoom 3.9 yzoom 3.2 yalign 0.8
    else:
        scene wild_west2 with fade:
            xzoom 3.9 yzoom 3.2 yalign 0.8
    show cody with moveinright:         
        xalign 0.8 yalign 0.3 xzoom 1.3 yzoom 1.3
    show kody with moveinleft:
        xalign 0.2 yalign 0.3 xzoom 1.3 yzoom 1.3
    label minigame_rps_start:
    "Wins: [location]\n Loses: [count2]\n Draws: [count]"
    call chapter_zero_hands
    menu: 
        "Rock":
            $ choice1 = 1
            jump minigame_rps_check
        "Paper":
            $ choice1 = 2
            jump minigame_rps_check
        "Scissors":
            $ choice1 = 3
            jump minigame_rps_check
    label minigame_rps_check:
        $ rngint = renpy.random.randint(1,3)
        if choice1 == rngint:
            $ count = count + 1
        elif choice1 == 1:
            if rngint == 3:
                $ location += 1
            else:
                $ count2 += 1
        elif choice1 == 2:
            if rngint == 1:
                $ location += 1
            else:
                $ count2 += 1
        elif choice1 == 3:
            if rngint == 2:
                $ location += 1
            else:
                $ count2 += 1
        if ((location + count2 + count) % 10 == 0):
            menu:
                "Retry?":
                    jump minigame_rps_start
                "Main Menu":
                    jump return_to_main_from_minigames
        else:
            jump minigame_rps_start
label minigame_math:
    call hide_clickable_menus
    $ count = 0 #Correct Answers
    $ count2 = 0 #Incorrect Answers
    $ rngint = 0 #Number 1
    $ rngint2 = 0 #Number 2
    $ location = 1 # Problem Count
    $ choice = 0 # number 3
    stop music
    play music "audio/music/chapter_one/baldi_math.ogg"
    label minigame_math_start:
    baldi "Problem #[location]!"
    scene baldi_q1 with dissolve:
            subpixel True pos (-333, -0.26) 
    $ rngint = renpy.random.randint(0 - count * 15,10 + count * 15)
    $ rngint2 = renpy.random.randint(0 - count * 5, 15 + count * 5 + count2 * 3)
    baldi "What is [rngint] + [rngint2]?"
    $ choice = renpy.input("What is [rngint] + [rngint2]?", length = 25)
    if choice != str(rngint + rngint2):
        $ count2 +=1
    else:
        $ count += 1
    call minigame_baldi_message
    scene baldi_q2 with dissolve:
        subpixel True pos (-333, -0.26)
    $ rngint = renpy.random.randint(7 + count * 7, 17 + count * 17)
    $ rngint2 = renpy.random.randint(9 - count2 * count - count, 11 + location * count2)
    baldi "What is [rngint] * [rngint2] + [rngint//2]?"
    $ choice = renpy.input("What is [rngint] * [rngint2] + [rngint//2]?", length = 25)
    if choice != str(rngint * rngint2 + (rngint // 2)):
        $ count2 +=1
    else:
        $ count += 1
    call minigame_baldi_message
    scene baldi_q3 with dissolve:
        subpixel True pos (-333, -0.26)
    $ rngint = renpy.random.randint(4 + count, 7 + count)
    $ rngint2 = renpy.random.randint(1 + 2 * count2, 1 + 222 * count2)
    baldi "WHAT IS [rngint] * [rngint2] - [location] * [rngint2 // 2]"
    $ choice = renpy.input("What is [rngint] * [rngint2] - [location] * [rngint2//2]?", length = 25)
    if choice != str((rngint * rngint2) - location * (rngint2 // 2)):
        $ count2 +=1
    else:
        $ count += 1
    call minigame_baldi_message
    "Correct Answers: [count]\n Incorrect Answers: [count2]"
    menu:
        "Retry?":
            jump minigame_math
        "Main Menu":
            jump return_to_main_from_minigames
    label minigame_baldi_message:
        $ location += 1
        baldi "WOW!"
        baldi "You are Incredible!"
        baldi "Problem #[location]!"
        return
label minigame_puppet:
    init python:
        import math
    call hide_clickable_menus
    scene ch03_fnaf7_empty with dissolve:
        subpixel True yzoom 1.25 zoom 1.92
    $ count = 60
    #$ count = 0
    window auto hide
    stop music
    play music "audio/music/chapter_three/wiping_all_out.ogg"
    "Death Approaches!"
    show ch03_fnaf_puppet2:
        subpixel True xanchor 873 pos (1413, 16) zoom 5.43 
    $ jumpscare_check = False
    $ check = 1
    $ location = 1
    $ puppet_keys = ["w","a","s","d","i","j","k","l","f","h", "g", "r", "u"]
    $ puppet_words = ["GIVE GIFTS", "GIVE LIFE", "LIES", "AFTON", "HENRY", "LIFE", "DEATH", "FAILED", "A CYCLE", "GENESIS", "REVELATIONS", "HE ALWAYS COMES BACK", "CODY", "VORTEX", "NECRO", "HIM", "???", "MATHEW", "VANCE", "CROOKS"]
    while check == 1 and location == 1:
        $ choice = renpy.random.randint(0,2)
        if choice == 0:
            $ randint = renpy.random.randint(330,1500) # X-Value
            $ randint2 = renpy.random.randint(400,750) # Y-Value
            show screen minigame_puppet_cupcakes(randint,randint2,1.0,count)
            $ count -= 1
            $ renpy.pause(delay = (9.5 / math.log(61,10)) * math.log(-count+61,10) + 5, hard=True)
        elif choice == 1:
            $ time = 6 - (4.95 *  math.log(1+count,10)) / (math.log(1+60,10))
            call screen minigame_puppet_timer_event(renpy.random.choice(puppet_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
            $ location = _return
        elif choice == 2:
            $ rngint = str(renpy.random.choice(puppet_words))
            puppet "[str(rngint)]"
            show screen minigame_puppet_timer()
            $ user_input = renpy.input("THE GIFT OF DESTRUCTION APPROACHS!")
            $ user_input = user_input.strip()
            if user_input != rngint:
                jump minigame_puppet_death
            hide screen minigame_puppet_timer
            play sound "audio/sound/chapter_three/the_voices.ogg"
            $ count -= 1
    label minigame_puppet_death:
        call auto_advance(0)
        hide minigame_puppet_cupcakes
        hide minigame_puppet_three_puppet_timer
        hide minigame_puppet_timer_event
        if not jumpscare_check:
            $ jumpscare_check = True
            play movie "video/chapter_three/puppet.webm"
        "Score: [60 - count]"
        menu:
            "Retry?":
                jump minigame_puppet
            "Main Menu":
                jump return_to_main_from_minigames
    label minigame_puppet_timers:
        screen minigame_puppet_cupcakes(xpos,ypos,zoom,count):
            modal True
            timer (4.75 / math.log(61,10)) * math.log(-count+61,10) + 5 action Jump("minigame_puppet_death")
            imagebutton:
                pos (xpos,ypos) at Transform(zoom = zoom)
                idle "images/chapter_three/ch03_giftbox.png"
                hover "images/chapter_three/ch03_giftbox.png"
                action [
                    #SetVariable("count2", count2-1),
                    Play("sound","audio/sound/chapter_three/the_voices.ogg"),
                    Hide("minigame_puppet_cupcakes"),
                    Pause(0.0)
                    #Return()
                ]
        screen minigame_puppet_timer_event(key_input, xalign1, yalign1):
            timer 0.01 repeat True action If(time > 0.0, true=SetVariable("time", time - 0.01), false=[Return(0), Hide("minigame_puppet_timer_event")]) 
            key key_input action [Return(1), SetVariable("count", count-1), Play("sound","audio/sound/chapter_three/the_voices.ogg")]
            
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
                    range 6 - (4.95 * math.log(1+count,10)) / (math.log(1+60,10))
                    xalign 0.5
                    xmaximum 100
                    
                    if time < 1.455:
                        left_bar "#410f0f"
        screen minigame_puppet_timer():
            timer 6.25 * math.exp((math.log(25) / 60) *(count-60)) + 3.75 action Jump("minigame_puppet_death")
    