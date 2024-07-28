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
    if choice != str(rngint * rngint2 + rngint // 2):
        $ count2 +=1
    else:
        $ count += 1
    call minigame_baldi_message
    scene baldi_q3 with dissolve:
        subpixel True pos (-333, -0.26)
    $ rngint = renpy.random.randint(4 + count, 7 + count)
    $ rngint2 = renpy.random.randint(2 * count2, 222 * count2)
    baldi "WHAT IS [rngint] * [rngint2] - [location] / [rngint2 // 2]"
    $ choice = renpy.input("What is [rngint] * [rngint2] - [location] / [rngint//2]?", length = 25)
    if choice != str(rngint * rngint2 - location / (rngint2 // 2)):
        $ count2 +=1
    else:
        $ count += 1
    call minigame_baldi_message
    "Correct Answers: [count]\n Incorrect Answers: [count2]"
    jump minigame_math_start

label minigame_baldi_message:
    $ location += 1
    baldi "WOW!"
    baldi "You are Incredible!"
    baldi "Problem #[location]!"
    return