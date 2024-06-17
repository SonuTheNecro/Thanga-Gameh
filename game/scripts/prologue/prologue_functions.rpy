# The Script file for the extra scripts and functions for prologue


# Animating the hands for the Rock Paper Scissors game
label chapter_zero_hands:
    show hands1:
        subpixel True xanchor 27 pos (355, 118) rotate 30.0 yrotate 180.0 orientation (0.0, 0.0, 0.0) 
    show hands1:
        linear 0.25 subpixel True pos (496, 248) rotate -30.0 point_to None 
    show hands1 as chapter_zero_rhand:
        subpixel True pos (1075, 148) rotate 15.0 xrotate 0.0 
    show hands1 as chapter_zero_rhand:
        linear 0.25 subpixel True pos (1091, 250) rotate -30.0 
    return

label chapter_zero_secret:
    hide hands1
    hide chapter_zero_rhand
    c "Holy fuck"
    c "Just take this victory because you are just cheating"
    k "explain some things"
    k "what are you?"
    k "Who are you?"
    k "and what are your plans?"

    c "I can't say much due to my contractual obligations"
    c "BUTTTTT!"
    k "chicken-butt!"
    c "..."
    k "..."
    k "okay im sorry"
    c "I suppose I can give a hint, me and some other evil people are going to do some evil things"
    c "Apparently the meeting is at a Subway?"
    c "Weird spot but the host loves that place so if you can get there, maybe you'll catch us"
    c "anyways, later bozo"
    # k "Perhaps we both are more similar than we thought"
    #k "You win this one but let it be known that there will be a day where all of your loved ones will..."
    #k "D I E !"
    #k "Until then, I'll be watching you!"

    #c "Wait! Explain what is even happening"
    #k "All you need is I got some new friends at Hierarchy and they have demands I need to fulfil"
    show cody:
        yrotate 180.0
        linear 0.25 xalign 1.3
    k "..."
    "You have gained a basic understanding of Cody.  This will be important at a future date"
    k "I really didn't..."
    "Just bare with us here"
    k "So is this some kinda secret ending?"
    "yeah basically"
    $ secret0 = True
    jump chapter_zero_ending

label chapter_zero_battle:
    call chapter_zero_hands
    menu: 
        "Rock":
            $ choice1 = 1
            jump chapter_zero_check
        "Paper":
            $ choice1 = 2
            jump chapter_zero_check
        "Scissors":
            $ choice1 = 3
            jump chapter_zero_check

label chapter_zero_check:
    $ rngint = renpy.random.randint(1,3)
    if choice1 == rngint:
        if(count == 2):
            jump chapter_zero_secret
        $ count = count + 1
        "You both picked the same choice! AGAIN!"
        "Run that Shit Back!"
        jump chapter_zero_battle
    elif choice1 == 1:
        if rngint == 3:
            jump chapter_zero_win
        else:
            jump chapter_zero_lose
    elif choice1 == 2:
        if rngint == 1:
            jump chapter_zero_win
        else:
            jump chapter_zero_lose
    elif choice1 == 3:
        if rngint == 2:
            jump chapter_zero_win
        else:
            jump chapter_zero_lose

label chapter_zero_win:
    if choice1 == 1:
        $ choice1 = "Rock"
        $ rngint = "Scissors"
    elif choice1 == 2:
        $ choice1 = "Paper"
        $ rngint = "Rock"
    elif choice1 == 3:
        $ choice1 = "Scissors"
        $ rngint = "paper"
    "You picked [choice1] which beats Cody's [rngint]!"
    "Incredible gameplay"
    hide hands1
    hide chapter_zero_rhand
    k "Yeah I agree Narrator guy"
    c "WAIT WHAT YOU CAN HEAR HIM TOO?"
    k "I mean it's right there"
    c "NO CHANGE THIS YOU FUCKING CHEATED!"
    k "cope bro, you lost lol"
    c "Whatever..."
    c "You may have won this battle"
    if rngint1 == 1:
        show wild_west1 with dissolve:
            xzoom 3.9 yzoom 3.2 yalign 0.8 matrixcolor InvertMatrix(1.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    else:
        show wild_west2 with dissolve:
            xzoom 3.9 yzoom 3.2 yalign 0.8 matrixcolor InvertMatrix(1.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    call dio_time_stop
    c "BUT YOU AREN'T WINNING THE WAR!"
    c "I WILL BE BACK!"
    show cody:
        yrotate 180.0
        linear 0.25 xalign 1.3
    if rngint1 == 1:
        show wild_west1 with dissolve:
            xzoom 3.9 yzoom 3.2 yalign 0.8 matrixcolor ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    else:
        show wild_west2 with dissolve:
            xzoom 3.9 yzoom 3.2 yalign 0.8 matrixcolor ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    jump chapter_zero_ending

    #c "WHAT! IMPOSSIBLE!"
    #k"lol"
    #k "I am just straight better!"
    #jump test1
    

label chapter_zero_lose:
    
    if choice1 == 1:
        $ choice1 = "Rock"
        $ rngint = "Scissors"
    elif choice1 == 2:
        $ choice1 = "Paper"
        $ rngint = "Rock"
    elif choice1 == 3:
        $ choice1 = "Scissors"
        $ rngint = "paper"
    hide hands1
    hide chapter_zero_rhand
    "You picked [choice1] which loses to Cody's [rngint]!"
    k "Nahhhh"
    c "fuck you mean 'Nahhhh'"
    c "You lost"
    c "You Trash"
    c "Goodbye bozo"
    play sound "audio/sound/prologue/laser.ogg" loop
    show laser with dissolve:
        subpixel True offset (-1071.0, -432.0) pos (1303, 23) rotate 30.0 zoom 3.29 

    k "WHAT THE FUCK IS THIS?"
    c "Die"
    stop sound
    hide kody with dissolve
    c "You are trash!"
    jump game_over

