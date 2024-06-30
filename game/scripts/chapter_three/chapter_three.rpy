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
define afton = Character("William Afton")
define freddy = Character("Freddy Fazgyatt")
define bonnie = Character("Bonnie Looksmaxxer")
define chica = Character("Chica FanumTaxxer")
define foxy = Character("Foxy FurryFukker")
define fnafpg = Character("Pizza Delivery Guy")
define puppet = Character("The Puppet")
define balloon = Character("Balloon Boy")
default chapter_three_jewels_check = [False, False, False, False, False]
default chapter_three_secret = [False, False, False, False]
default chapter_three_fnaf_money = [False, False, False, False, False, False, False, False] # 2 $5, 5 $1, 2 0.25
default chapter_three_key_items = {
    "chapter_three_phonecall": ItemState.NOT_OBTAINED,
    "chapter_three_flour"    : ItemState.NOT_OBTAINED,
    "chapter_three_yeast"    : ItemState.NOT_OBTAINED,
    "chapter_three_water"    : ItemState.NOT_OBTAINED,
    "chapter_three_salt"     : ItemState.NOT_OBTAINED,
    "chapter_three_sugar"    : ItemState.NOT_OBTAINED,
    "chapter_three_cornmeal" : ItemState.NOT_OBTAINED,
    "chapter_three_garlic"   : ItemState.NOT_OBTAINED,
    "chapter_three_wheat"    : ItemState.NOT_OBTAINED,
    "chapter_three_cheese"   : ItemState.NOT_OBTAINED,
    "chapter_three_pepperoni": ItemState.NOT_OBTAINED,
    "chapter_three_olive_oil": ItemState.NOT_OBTAINED,
    "chapter_three_pizza2"   : ItemState.NOT_OBTAINED,
    "chapter_three_drip"     : ItemState.NOT_OBTAINED,
    "chapter_three_toilet"   : ItemState.NOT_OBTAINED,
    "chapter_three_key"      : ItemState.NOT_OBTAINED,
    "chapter_three_gun"      : ItemState.NOT_OBTAINED,
    "chapter_three_pills"    : ItemState.NOT_OBTAINED,
    }

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
       
        if choice == -1:
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
            play sound "audio/sound/chapter_one/street1.ogg" loop
            k "Why am I hearing street1.ogg playing?"
            k "OH SHIT THERE IS SOMEONE HERE!"
            hb "ugh"
            hb "let me go deal with this bozo real quick"
            window auto hide
            show ch03_herobrine2:
                yrotate 180.0 
                linear 1.5 subpixel True pos (-93, 286) 
                linear 1.5 subpixel True pos (-93, -56)
            pause 3.0
            hide ch03_herobrine2
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
            play sound "audio/sound/chapter_one/street1.ogg" loop
            k "What the hell is that noise?"
            k "YO THANG cAME TO SAVE ME LETS FUCKING GO"
            questionmark "How did someone find this spot"
            questionmark "meh, another hostage for that bread"
            window auto hide
            show ch03_shadow_guy:
                subpixel True pos (-51, 352) zoom 0.44 
                linear 0.987 subpixel True pos (-51, -107) zoom 0.44 
            hide ch03_shadow_guy
        stop sound
        questionmark "HOLY UP PARTNER"
        questionmark "What do you want... I am busy here"
        questionmark "I heard you got kody here"
        questionmark "h-how did you know that"
        questionmark "doesn't matter, I want him or you can die"
        questionmark "oh really?"
        play sound "audio/sound/chapter_three/mag_load.ogg"
        $ _preferences.afm_enable = True
        $ _preferences.afm_time = 5
        questionmark "wtf we don't have to do that"
        questionmark "MMMMMMMMMM I THINK WE WILL"
        questionmark "wait dont do that"
        $ _preferences.afm_enable = False
        $ _preferences.afm_time = 15
        $ chapter_three_gunshots(5)
        questionmark "WHAT A FUCKING IDIOT"
        questionmark "ugh got my fancy suit all messy"
        play sound "audio/sound/chapter_one/street1.ogg" loop
        show ch03_afton1:
            subpixel True xpos -333 
            linear 1.5 subpixel True pos (-91, 296)
            linear 1.5 subpixel True pos (346, 358)
        pause 3.0
        stop sound
        questionmark "There you are"
        questionmark "The Final Piece"
        k "huh?"
        k "can you help me"
        questionmark "As long as you cooperate with the next few steps"
        k "uh sure boss?"
        questionmark "Alright let's go"
        k "can you fix my legs?"
        questionmark "I will try my best"
        show ch03_afton1:
            linear 0.5 subpixel True pos (610, 355) 
        pause 0.5
        show kody as kody1:
            linear 1.0 subpixel True pos (860, 572) rotate 0.0 
        k "oh this is great"
        k "I really like having legs again, this is so awesome"
        questionmark "Alright let's get to my office to discuss what's next"
        k "got it boss"
    label chapter_three_office:
        scene ch03_office with dissolve:
            subpixel True xzoom 1.43 zoom 2.46 
        show ch03_afton1:
            subpixel True pos (281, 223) zoom 1.37 
        show kody:
            subpixel True pos (1091, 390) yrotate 180.0 
        k "What is this place?"
        questionmark "My office"
        k "So who even are you?"
        afton "My name is William Afton"
        k "Oh like Five Nights at Freddy's?"
        afton "nah just a big coincidence"
        k "alright I guess"
        k "So what do you want from me?"
        afton "I saw you at the Post Office looking for work to do"
        afton "And I saw the Poppy Playtime video"
        afton "I think I have an opportunity for you"
        k "Does it have to do with looksmaxxing with fanum taxxing"
        afton "I will have to ask my superior about that but my guess is yes to whatever that is"
        k "LET'S FUCKING GO!"
        afton "Let me show you what you have to do"
        k "alrighty"
        afton "follow me"
        scene ch03_fnaf_prep1 with dissolve:
            subpixel True zoom 0.75 
        show ch03_afton1:
            subpixel True pos (616, 315) 
        afton "So here is the entrance"
        k "So this isn't fnaf..."
        k "I can see the posters right there"
        afton "just a coincidence"
        k "ok"
        afton "lets just move onto the next area"
        k "k"
        scene ch03_fnaf_prep2 with dissolve:
            subpixel True zoom 0.75
        k "THIS IS SO FNAF" #TODO: put a lock sfx here
        afton "alright so I have locked us in here so might as well show you your job"
        afton "This is the main area of the building"
        scene ch03_fnaf_prep3 with dissolve:
            subpixel True zoom 0.75
        afton "These are the animatronics"
        afton "This is just straight up fnaf"
        k "YEAH I FUCKING CAN TELL"
        afton "So the middle guy is Freddy Fazgyatt"
        afton "The left one is Bonnie Looksmaxxer"
        afton "and the right one is Chica Fanum Taxxer"
        k "I don't remember this in Fnaf"
        afton "This is the new FNAF"
        scene ch03_fnaf_prep5 with dissolve:
            subpixel True zoom 0.75
        afton "This is the backrooms of the building"
        k "THE BACKROOMS?"
        afton "yes"
        scene ch03_fnaf_prep4 with dissolve:
            subpixel True zoom 0.75
        afton "and this is the fnaf office"
        k "So am i just the nightguard for fnaf"
        afton "yes"
        k "fuck this shit"
        k "I ain't doing this"
        afton "Well you are locked in"
        afton "and Cody gives me a big payday for bringing you here"
        k "WHAT?"
        k "HES INVOLVED?"
        afton "yeah later asshole, have fun with fnaf" #TODO: Fnaf power out sfx here
        #show screen ch03_fnaf_map
        
        label chapter_three_fnaf_start:
        python:
            choice = 0
            count = 0
            count2 = 0
            location = 1
            Freddy = Animatronic("Freddy Fazgyatt")
            Bonnie = Animatronic("Bonnie Looksmaxxer")
            Chica = Animatronic("Chica Fanum Taxxer")
            Foxy = Animatronic("Foxy")
        #jump chapter_three_office
        jump ch03_fnaf_office
        "test"
label ch03_fnaf_office:
    $ location = 1
    call chapter_three_fnaf_hide_screens
    scene ch03_fnaf1 with dissolve:
        subpixel True yzoom 1.25 zoom 1.2
    if not chapter_three_item_check("chapter_three_phonecall"):
        call chapter_three_phone_time
    else:
        call chapter_three_fnaf_restore_screens(location)
    label ch03_fnaf_office_1:
    "You are located in the Security Office in Freddy Fazgyatt's Rizzaria"
    jump ch03_fnaf_office_1

label ch03_fnaf_2b:
    $ location = 2
    call chapter_three_fnaf_hide_screens
    scene ch03_fnaf2 with dissolve:
        subpixel True yzoom 1.25 zoom 1.2 
    call chapter_three_fnaf_restore_screens(location)
    label ch03_fnaf_2b_1:
    "You are located in the West Hall Corner in Freddy Fazgyatt's Rizzaria"
    jump ch03_fnaf_2b_1

label ch03_fnaf_4b:
    $ location = 3
    call chapter_three_fnaf_hide_screens
    scene ch03_fnaf3 with dissolve:
        subpixel True yzoom 1.25 zoom 1.2
    call chapter_three_fnaf_restore_screens(location)
    label ch03_fnaf_4b_1:
    "You are located in the East Hall Corner in Freddy Fazgyatt's Rizzaria"
    jump ch03_fnaf_4b_1

label ch03_fnaf_6:
    $ location = 4
    call chapter_three_fnaf_hide_screens
    scene ch03_fnaf4 with dissolve:
        subpixel True xzoom 1.34 yzoom 1.02 zoom 1.12 
    call chapter_three_fnaf_restore_screens(location)
    label ch03_fnaf_6_1:
    "You are located in the Kitchen in Freddy Fazgyatt's Rizzaria"
    jump ch03_fnaf_6_1

label ch03_fnaf_3:
    $ location = 5
    call chapter_three_fnaf_hide_screens
    if Bonnie.get_happiness() == 0 and Bonnie.get_mission():
        scene ch03_fnaf5_bonnie with dissolve:
            subpixel True yzoom 1.25 zoom 1.92
    else:
        scene ch03_fnaf5 with dissolve:
            subpixel True yzoom 1.25 zoom 1.2 
    call chapter_three_fnaf_restore_screens(location)
    label ch03_fnaf_3_1:
    "You are located in the Broom Closet in Freddy Fazgyatt's Rizzaria"
    jump ch03_fnaf_3_1

label ch03_fnaf_1b:
    $ location = 6
    call chapter_three_fnaf_hide_screens
    scene ch03_fnaf6 with dissolve:
        subpixel True yzoom 1.25 zoom 1.5 
    call chapter_three_fnaf_restore_screens(location)
    label ch03_fnaf_1b_1:
    "You are located in the Dining Area in Freddy Fazgyatt's Rizzaria"
    jump ch03_fnaf_1b_1

label ch03_fnaf_1a:
    $ location = 7
    call chapter_three_fnaf_hide_screens
    if ((Bonnie.get_happiness() == 0 and Bonnie.get_mission()) or (Bonnie.get_happiness() == 2 and not Bonnie.get_mission())) and Chica.get_happiness() == 2 and not Chica.get_mission():
        scene ch03_fnaf7_only_freddy with dissolve:
            subpixel True yzoom 1.25 zoom 1.92
    elif (Bonnie.get_happiness() == 0 and Bonnie.get_mission()) or (Bonnie.get_happiness() == 2 and not Bonnie.get_mission()):
        scene ch03_fnaf7_no_bonnie with dissolve:
            subpixel True yzoom 1.25 zoom 1.92
    elif Chica.get_happiness() == 2 and not Chica.get_mission():
        scene ch03_fnaf7_no_chica with dissolve:
            subpixel True yzoom 1.25 zoom 1.92
    else:
        scene ch03_fnaf7 with dissolve:
            subpixel True yzoom 1.25 zoom 1.2 


    call chapter_three_fnaf_restore_screens(location)
    label ch03_fnaf_1a_1:
    "You are located in the Stage Area in Freddy Fazgyatt's Rizzaria"
    jump ch03_fnaf_1a_1

label ch03_fnaf_5:
    $ location = 8
    call chapter_three_fnaf_hide_screens
    scene ch03_fnaf8 with dissolve:
        subpixel True yzoom 1.25 zoom 1.6 
    call chapter_three_fnaf_restore_screens(location)
    label ch03_fnaf_5_1:
    "You are located in the Backstage Area in Freddy Fazgyatt's Rizzaria"
    jump ch03_fnaf_5_1

label ch03_fnaf_1c:
    $ location = 9
    call chapter_three_fnaf_hide_screens
    $ count = Foxy.happiness
    if count == 1:
        show ch03_fnaf_cove2:
            subpixel True xpos -396 xzoom 1.08 yzoom 1.12 zoom 2.15 
    elif count == 2:
        scene ch03_fnaf_cove3 with dissolve:
            subpixel True xpos -396 xzoom 1.08 yzoom 1.12 zoom 2.15 
    elif count == 3:
        scene ch03_fnaf_cove4 with dissolve:
            subpixel True xpos -396 xzoom 1.08 yzoom 1.12 zoom 2.15
    else:
        scene ch03_fnaf9 with dissolve:
            subpixel True yzoom 1.25 zoom 1.2 
    call chapter_three_fnaf_restore_screens(location)
    label ch03_fnaf_1c_1:
    "You are located in the Pirate Cove in Freddy Fazgyatt's Rizzaria"
    jump ch03_fnaf_1c_1

label ch03_fnaf_7:
    $ location = 10
    call chapter_three_fnaf_hide_screens
    scene ch03_fnaf10 with dissolve:
        subpixel True yzoom 1.25 zoom 1.2 
    call chapter_three_fnaf_restore_screens(location)
    label ch03_fnaf_7_1:
    "You are located in the Restrooms in Freddy Fazgyatt's Rizzaria"
    jump ch03_fnaf_7_1

label ch03_fnaf_2a:
    $ location = 11
    call chapter_three_fnaf_hide_screens
    scene ch03_fnaf11 with dissolve:
        subpixel True xpos -306 yzoom 1.06 zoom 1.77 
    call chapter_three_fnaf_restore_screens(location)
    label ch03_fnaf_2a_1:
    "You are located in the West Hall in Freddy Fazgyatt's Rizzaria"
    jump ch03_fnaf_2a_1

label ch03_fnaf_4a:
    $ location = 12
    call chapter_three_fnaf_hide_screens
    scene ch03_fnaf12 with dissolve:
        subpixel True xpos -234 yzoom 1.1 zoom 1.72 
    call chapter_three_fnaf_restore_screens(location)
    label ch03_fnaf_4a_1:
    "You are located in the East Hall in Freddy Fazgyatt's Rizzaria"
    jump ch03_fnaf_4a_1
