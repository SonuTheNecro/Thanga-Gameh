# This is the codebase written for Chapter three
# Main Writer: SonuTheNecro
# Extra Help: TactialVortex
# All imagees: Google Images
# All sounds: Freesounds.com

#Variables
define jb = Character("Jewel Osco Butcher")
define jc = Character("Jewel Osco Customer")
define jceo = Character("Jewel Osco CEO")
define usps = Character("USPS Worker Guy")
define hb = Character("Herobrine")
default chapter_three_jewels_check = [False, False, False, False, False]
default chapter_three_secret = [False]

label chapter_three:
    "Chapter Three..."
    "WAIT WAS THAT THE BITE OF 87?"
    show ch03couch:
        subpixel True xpos -126 xzoom 1.35 zoom 1.77 

    show thanga2 with dissolve:
        subpixel True pos (1548, 153) yrotate 180.0 
    show kody with dissolve:
        subpixel True pos (143, 218) 
    play sound "audio/sound/chapter_three/wall_clock.ogg" loop
    t "..."
    k "..."
    t "..."
    k "..."
    k "So I hit a new record with my MewMaxxing"
    k "Its now 2 feet now"
    t "..."
    k "..."
    t "You need a fucking job"
    k "..."
    stop sound
    k "WHY DO I NEED A JOB?"
    t "After what happened last week and what you said in Monokuma's Dungeon"
    t "You need a freakin life"
    k "Yeah I got one, I mewmaxx and mogmaxx all day every day"
    k "what do you do all day?"
    k "goon and look at your art gallery"
    t "..."
    t "I can explain that"
    k "WELL DO IT FOR ALL US THEN BUCKO!"
    t "That isn't important"
    k "I THINK IT IS SO TELL US"
    show march_7th
    "We don't actually know the reason so enjoy this image of march 7th"
    "Anyways..."
    "Back after the nonsense"
    hide march_7th
    t "The point is"
    t "I got a job and you don't"
    t "so go look around and get something"
    t "maybe mow some lawns so you can \"musclemaxx\" better"
    k "OOOOOOOOOOOOOO IMA DO THAT"
    show kody:
        linear 0.56 xalign 1.7
    t "What an idiot..."
    scene ch03house:
        subpixel True xzoom 1.2 zoom 0.62 
    show kody:
        subpixel True pos (1331, 500) zoom 0.5 yrotate 180.0 
    k "Let's get this bread!"
    play sound "audio/sound/chapter_three/footstep.ogg" loop

    show kody:
        linear 0.68 subpixel True pos (1365, 586) zoom 0.5 yrotate 180.0
        linear 0.85 subpixel True pos (496, 553) zoom 0.5 yrotate 180.0 
        linear 0.94 subpixel True pos (-185, 798) zoom 0.5 yrotate 180.0 
    stop sound

    # Set Variables
    label chapter_three_job:
    $ location = -1
    $ rngint = -1
    $ rngint1 = -1
    $ choice = -1
    $ count = 0
    $ count2 = -1

    "Current Objective..."
    "Get a job..."
    k "Yeah I know"
    k "I am goated though!"
    k "they will be paying me for the hard work"
    "That..."
    "That is indeed how jobs work"
    "They pay you for the labor you do"
    k "I ain't getting whatever Brian called it in the school"
    k "What did he call it"
    k "Blue-Collar Jobs!"
    "That is not what I meant..."
    "Like for your time"
    k "yea-yeah-ye"
    k "Let's just fucking start"
    "Current Objective..."
    "Get a job..."
    jump chapter_three_map

    label chapter_three_map:
        scene ch03map with dissolve:
            subpixel True pos (-63, -63) xzoom 1.31 yzoom 1.14 zoom 3.14 blur 3.48
        if choice == -1:
            show screen clickable_chapter_three_herobrine
        show screen clickable_chapter_three_jewel_osco
        if count2 >= 5:
            show screen clickable_chapter_three_house
            show screen clickable_chapter_three_mail
        if count == 4:
            jump chapter_three_post_map
        "Current Objective: Get a Job!"
        jump chapter_three_map
    
    label chapter_three_post_map:
        call chapter_three_hide_map_buttons
        scene ch03_alleyway with dissolve:
            subpixel True xpos -81 xzoom 1.17 zoom 0.43 
        k "Okay I guess this is the last job I can get..."
        k "Dang its already night damn"
        k "According to this note" #TODO:Draw a note

        k "It says Free Robux for Free work..."
        k "I think I can trust that"
        questionmark "Hello child"
        k "!!!"
        show ch03_shadow_guy with dissolve:
            subpixel True pos (306, 88) zoom 1.3
        k "Where are your legs?"
        questionmark "You are coming with me"
        call stab_blood_screen
        pause 0.9
        show black with vpunch and hpunch
        pause 10.0
        k "..."
        k "Am I still alive?"
        k "I am in so much pain"
        k "thang"
        k "thang help me"
        k "pls help me i am hungry"
        k "i need mcdonalds and chuck e cheese's"
        scene ch03_chair with dissolve:
            subpixel True xzoom 1.12 zoom 0.44 
        show kody:
            subpixel True crop_relative True pos (953, 371) zoom 0.78 crop (0.0, 0.0, 1.0, 0.59) yrotate 180.0 
        show kody as kody1: 
            subpixel True zoom 0.78 yrotate 180.0 crop_relative True pos (790, 708) rotate 315.0 crop (0.0, 0.62, 1.0, 1.0)
        pause 1.0
        k "MY LEGS!"
        k "WTF!"
        play sound "audio/sound/chapter_one/street1.ogg" loop
        pause 0.789
       
        if choice != -1:
            show ch03_herobrine2:
                subpixel True pos (-215, 78)
                linear 1.5 subpixel True pos (-46, 365) 
                linear 1.5 subpixel True pos (405, 381) zoom 1.45
            pause 4.0
            stop sound
            $ chapter_three_secret[0] = True
            hb "remember me you cunt?"
            k "oh lol"
            k "WAIT YOU TOLD ME THIS WAS GONNA HAPPEN"
            hb "yeah thats the point dumbfuck"
            k "WHY?"
            hb "Well I used the energy from your legs to give me some swagalicious legs"
            k "never say that again"
            k "well fuck you"
            hb "I will be selling you off"
            hb "I hear some inverted demon wants you"
            hb "Something like 25 looney Tooneys for you"
            k "dafaq is a looney tooney"
            hb "canadian currency"
            k "why use that when the us dollar exists"
            hb "we are in canada..."
            k "oh"
        else:
            show ch03_shadow_guy:
                subpixel True pos (-250, 126) zoom 0.32 
                linear 1.5 subpixel True pos (-23, 441) zoom 0.32 
                linear 1.5 subpixel True pos (205, 251) zoom 0.74 
            pause 4.0
            stop sound
            questionmark "Hello kody"
            k "fuck off you bitch what do you want from me"
            questionmark "I will be selling you off"
            questionmark "I hear some inverted demon wants you"
            questionmark "Something like 25 looney Tooneys for you"
            k "dafaq is a looney tooney"
            questionmark "canadian currency"
            k "why use that when the us dollar exists"
            questionmark "we are in canada..."
            k "oh"
        
        "test"