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
default chapter_three_jewels_check = [False, False, False, False, False]


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
        show screen clickable_chapter_three_jewel_osco
        if count2 >= 5:
            show screen clickable_chapter_three_house
            show screen clickable_chapter_three_mail

        "Current Objective: Get a Job!"
        jump chapter_three_map