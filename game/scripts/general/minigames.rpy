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