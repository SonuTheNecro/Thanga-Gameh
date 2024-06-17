# This is the codebase written for Chapter One
# Main Writer: SonuTheNecro
# Extra Help: TactialVortex
# All imagees: Google Images
# All sounds: Freesounds.com


# Chapter One Characters/Variables
define ce = Character("Chick-Fil-A Employee")
define pe = Character("Panda Express Employee")
define se = Character("Subway Employee")
define bt = Character("Brian and Thang")
define baldi = Character("Baldi")
define gos = Character("God of Sweep")
define pott = Character("Principal Of The Thing!")
define itsabully = Character("Its a Bully!")
define pt = Character("Playtime")
default key_items = {
    "chapter_one_clock": ItemState.NOT_OBTAINED,
    "chapter_one_hands": ItemState.NOT_OBTAINED,
    "chapter_one_battery": ItemState.NOT_OBTAINED,
    "chapter_one_wrench": ItemState.NOT_OBTAINED,
    "chapter_one_food" : ItemState.NOT_OBTAINED,
    "chapter_one_book" : ItemState.NOT_OBTAINED,
    "chapter_one_faculty": ItemState.NOT_OBTAINED,
    "chapter_one_cleanup": ItemState.NOT_OBTAINED,
    "chapter_one_mop": ItemState.NOT_OBTAINED, 
    "chapter_one_key": ItemState.NOT_OBTAINED,
    "chapter_one_giftcard": ItemState.NOT_OBTAINED,
    }
default chapter_one_dirt_piles = [False, False, False, False]
default lopunny_count = 0
label chapter_one:
    scene inside car with fade:
        subpixel True xzoom 1.5 yzoom 1.13 zoom 0.67 
    "Chapter 1: The Hunt for the Elusive..."
    questionmark "Lopunny..."
    questionmark "Why would you write it like this?"

    "It all began one day..."
    "The Exact day is Friday, Marth 15, 2027"
    show brian1:
        subpixel True pos (0.75, 406) zpos 0.0 xrotate 0.0 yrotate 0.0    
    show thanga2:
        subpixel True pos (343, 485)  xzoom 2.43 yzoom 0.92 zoom 1.0 
    show kody:
        subpixel True pos (0.6, 0.29) 

    b "so what should we get to eat?"
    t "I am good with whatever."
    b "anything?"
    b "so we can get the shittiest mcdonalds ever"
    t "no mcdonalds"
    t "not everyone eats 30 meals of McDoonalds a week like you!"
    menu:
        "Chick Fil-A":
            jump chapter_one_chick
        "Panda Express":
            jump chapter_one_panda
        "Subway":
            jump chapter_one_subway
    label chapter_one_chick:
        k "Lets go get some Chick Fil-A!, lets get out of the car"
        t "Kody"
        t "You stupid motherfucker"
        # t "Its a sunday DURR DURR DURR DURR"
        k "????? it isn't?"
        k "The chapter intro said Friday??????"
        # k "DURR DURR DURR DURR"
        k "You stupid idiot"
        t "Fuck off you asshat"
        scene chick1:
            subpixel True zoom 2.46 
        b "Well"
        b "Here we are!"
        b "Chick Fil-A"
        t "Why are you announcing where we are going?"
        b "You can walk you know bitch ass"
        t "Maybe I will with your ass driving"
        k "..."
        t "..."
        b "..."
        # t "Kill yourself you stupid ni-"
        # questionmark "DO NOT SAY THE REST OF THAT WORD!"
        # t "-ce and wondering person..."
        # b "You weren't going to call me a slur?"
        # t "..."
        # t "Did you not hear that?"
        # b "hear what?"
        # t "(so they didn't just hear or see that...)"
        # t "nevermind what I said"
        t "Who is going to get the food?"
        t "Since you know... we are out of the car"

        b "oh we were just going to use the drive-through"
        t "..."
        k "WHY WOULD WE GET OUT OF THE CAR SO WE CAN GET BACK IN THE CAR"
        "An intense shouting match happened between two man children"

        b "alright alright let's just go get the food"
        scene chick2 with fade:
            subpixel True zoom 2.25 
        b "That sucks for those employees, there is grafitti on the menu screen..."
        k "deserved for cucking me outta fries"
        b "you have problems"
        b "because you guys are being dickheads, i'm choosing the food"
        b "and I'm getting chicken sandwiches"
        t "what?"
        t "no"
        t "I want something else"
        b "nah I'm paying bitch"

        scene chick3 with dissolve:
            subpixel True xzoom 1.2 zoom 2.29 
        k "(Dang this line is long)"
        show screen clickable_chapter_one_secret_lopunny(985,3,0.34)
        ce "Hello, Welcome to Chick-Fil-A how many I help you?"
        b "I want 3 #2 Spicy Chickens meal plans"
        ce "Alright that will be $23.49 please pull up at the window"
<<<<<<< HEAD
        b "(Damn $23 that's like 5 hours of work salary money)"

        b "Alright here you go, here is the cash for the meal"
=======
        b82 "(Damn $23 that's like 5 hours of work salary money)"
        hide screen clickable_chapter_one_secret_lopunny
        scene chick_window with dissolve:
            subpixel True pos (-3, 0) xzoom 1.31 zoom 2.48 
        show brian_mcdonalds with dissolve:
            subpixel True pos (603, 235) 
        b82 "Alright here you go, here is the cash for the meal"
>>>>>>> 34b9103 (did some more todos)
        ce "Alright here is the -0.99 Cents"
        k "What Demonination did Brian pay in again?"
        b "Alright let's chow down"
        play sound "audio/sound/chapter_one/eat1.ogg" loop
        "A lot of sloppy eating is now taking place"
        "No i mean it"
        "It is really bad"
        "Thanga dropped the bbq sauce on his lap"
        "Kody is eating the Sandwich sideways"
        "Brian is putting the fries and the box into the sandwich like WHAT?"
        "Kody is now stuffing French Fries into his nose..."
        "Brian is eating the sandwich sideways..."
        stn "I AM NOT animating this sequence!"
        stn "Henry can do it!"
        tv "WHAT THE FUCK?"
        tv "WHY I DO IT?"
        tv "I'M THE ONE WRITING THIS SHIT!"
        stn "I guess no one is animating this then!"
        stop sound
        jump chapter_one_post_lunch
    label chapter_one_panda:
        k "I want some chinese food. Let's get some Panda Express!"
        t "That isn't real chinese food though"
        k "I don't give a fuck, I'm bulking on chinese food now :)."
        show screen clickable_chapter_one_giftcard()
        b "Hey Thang, can you check if I have a Panda Express Giftcard in my glove compartment"
        t "Nah there is nothing here maybe its in the back?"
        t "Yo Kodster, can you check if its in the back?"
        k "Give me a sec real quick"
        $ renpy.pause(15.5)        
        hide screen clickable_chapter_one_giftcard
        label chapter_one_panda_part_2:
        
        window auto hide
        scene panda2:
            default
            subpixel True 
            Null(2880.0, 1350.0)
            'panda2' with dissolve
        with Pause(0.60)
        window auto show
        b "Well here we are!"
        b "Panda Express"
        b "The Greatest Korean Restaurant!"
        t "You idiot!"
        t "this is chinese food"
        menu:
            "Dunk On Brian":
                k "Yeah Brian, doesn't know races LOL"
                b "Im not driving you bitches home"
                k "YOOOOOOOOOOOOOOOOO"
                k "WAITTTTTTTTTTTTTTT"
                k "I JK"
                jump chapter_one_panda_part_3
            "Dunk On Thang":
                k "NOW ITS CHINESE FOOD?"
                t "uh"
                k "UH HUH?"
                k "I KNEW THIS FOOD WAS CHINESE"
                b "He got you there lol"
                t "Kill yo sel-"
                "..."
                t "We done now?"
                b "yes lol"
                jump chapter_one_panda_part_3
        label chapter_one_panda_part_3:
        show screen clickable_chapter_one_secret_lopunny(1823,681,0.29)
        b "Alright what do we want? I guess Thang can go first"
        t "Alrighty"
        pe "HAI SELAMAT DATANG DI PANDA EXPRESS BAGAIMANA SAYA BISA MEMBANTU ANDA" # HI WELCOME TO PANDA EXPRESS HOW CAN I HELP YOU
        t "UH HALO BISAKAH SAYA PUNYA AYAM ORANGE DAN APAKAH KALIAN PUNYA KARTU HADIAH CLASH ROYALE" # UH HELLO CAN I HAVE ORANGE CHICKEN AND DO YOU GUYS HAVE CLASH ROYALE GIFT CARDS
        pe "TIDAK ADA RETARD, KAMI PANDA EXPRESS BUKAN WALMART IDIOT OKE SATU AYAM ORANGE UNTUK ANAK TAIWAN RETARD" #NO RETARD, WE PANDA EXPRESS NOT WALMART IDIOT OKAY ONE ORANGE CHICKEN FOR THE RETARD TAIWAN BOY
        b "Damn, vietnamese is so beautiful"
        b "I need me a Google translator for this"
        b "Why do the koreans only talk in all caps though, its a weird language"
        b "I guess you can go next Kody since Im still picking my food"
        k "Alrighty"
        hide screen clickable_chapter_one_secret_lopunny
        menu:
            "Orange Chicken":
                k "BOLEH AKU PESAN BANYAK AYAM JERUK CANTIK DAN BEBERAPA CHOW MEIN YUM YUM YUM DAN BEBERAPA NASI" #Can I have LOTS of ORANGE CHICEKN PRETTY PLEASE AND SOME CHOW MEIN YUM YUM YUM AND SOME RICE
                pe "OKE AYAM x2 LAGI UNTUK ANAK VIETNAME GEMUK" #OKAY CHICKEN x2 AGAIN FOR THE FAT VIETNAME BOY
                jump chapter_one_panda_part_4
            "Beijing Beef":
                k "kerja bagus menemukan petunjuk ini! Apa pentingnya Brian mendapat nilai 82 hanya di rute CFA?" #nice job finding this clue! What is the significance behind Brian having 82 only in CFA route?
                pe "waspadalah terhadap ide-ide pawai, itu akan segera terjadi!" #be ware of the ides of march, they are soon!
                jump chapter_one_panda_part_4
            "Frog Legs":
                k "tunggu, mereka menjual kaki katak di Panda Express, itu lucu sekali" #wait they sell frog legs at Panda Express that is funny as fuck
                pe "jangan biarkan batu utuh jika Anda menginginkan akhir yang sebenarnya! Mungkin Anda melewatkan akhir rahasia prolog?" #leave no stone untouched if you want the true ending! Maybe you missed the prologue secret ending?
                jump chapter_one_panda_part_4
            "Dog":
                k "hahaha lelucon Asia rasis di mana orang Cina memakan anjing sungguh lucu" #hahah racist asian joke where chinese eat dogs so god damn funny
                pe "Baiklah OCHO AKAN MATI HAHAHAH BYE BYE MATT DOG" #ALRIGHT OCHO WILL DIE HAHAHAH BYE BYE MATT DOG
                jump chapter_one_panda_part_4
        label chapter_one_panda_part_4:
        b "Uh hello I do not speak whatever fake language this is so ima need Thang to order for me"
        pe "NO NEED CRACKER WHITE BOY I SPEAK ENGLISH WELL!"
        b "okay thanks korean lady, I would like twenty eggrolls, seven orange chickens- speaking of which"
        b "are like the chickens oranges or are they orange flavor?"
        t "I am so sorry for him, he is mentally challenged"
        pe "IT OKAY CRACKERS ALL DUMB, NEVER LET MY SON SEE ONE THEY BAD THEY HAVE DRUGS"
        b "I also want 3 Large Soda cups"
        pe "okay so this order comes out to $98.54"
        if not is_item_obtained("chapter_one_giftcard"):
            b "Okay I will pay with this Giftcard with $100 on it!"
            pe "STUPID BOY THIS CARD IS EMPTY!"
            k "LOL DID MATT JUST GET YOU LOL!"
            t "well that sucks, I guess we cannot eat"
            b "Nah nah, I will break into my savings for this one"
            t "You have savings?"
            b "shut up asshatt"
        else:
            b "Okay I think we are gonna need to split this one up Thang"
            t "How is this fair?"
            t "I got one meal and Kody got one meal and you have like 17"
            b "PLEASEEEEEEE"
            t "fine you dickhead but you owe me!"
            b "alrighty so here is 4 from me and 100 from Thang so that should cover it"
        "Brian pays the Cashier the amount owed"
        pe "YES YES THANK YOU FOR PAYMENTNOW GET OUT OF MY STORE"
        b "TIME TO EAT >:)"
        play sound "audio/sound/chapter_one/eat1.ogg" loop
        "Wha..."
        "WHAT IS HAPPENING!"
        "THESE GUYS ARE NASTY!"
        "WE GOT BRIAN WHO IS DRINKING THE SODA WITH HIS NOSE LIKE WHAT?"
        "THANG IS MIXING HIS ORANGE CHICKEN ONTO HIS PHONE SO HE CAN EAT AND CLASH ROYALE AT THE SAME TIME"
        "AND KODY JUST THREW THE FOOD OUT"
        "huh?"
        "You wanna see this?"
        "No you can imagine it or beg on https://github.com/SonuTheNecro/Thanga-Gameh/tree/master"
        "sweet promo!"
        stop sound
        jump chapter_one_post_lunch
    label chapter_one_subway:
    k "I want to have a long 12 incher"
    b "don't we all..."
    t "ayoooo?"
    b "You aren't austin"
    t "who?"
    t "asked"
    b "..."
    b "..."
    t "Do NOT give me the silent treatment you bozo"
    t "kill yourself!"
    b "maybe i will you dickhead"
    t "anyways...."
    t "what do you ACTUALLY want to eat Kody?"
    k "I just fucking said I want a long 12 incher"
    t "ugh this guy"
    k "IM TALKING SUBWAY YOU FUCKING NINKAPOOP HOW YOU NOT UNDERSTAND ME"
    k "YOU GOT COTTIN IN YOUR EAR?????????"
    b "hell is a ninkapoop..."
    b "I actually have never had subway before, is it even good"
    t "i dont know I dont eat shitty American white people food like you bozos."
<<<<<<< HEAD
    t "I can smell the smash player breathe from here" #T
=======
    t "I can smell the smash player breathe from here"
>>>>>>> 34b9103 (did some more todos)
    b "Why are you always a dickhead"
    b "you do this to me intentionally like i did nothing wrong"
    b "everyday its shittalk and i cannot handle it like i am this close man"
    k "(This fucking BOZO.)"
    k "(ICANT)"
    k "man that sucks"
    scene subway1 with dissolve:
        subpixel True xzoom 1.31 zoom 2.69
    show thanga2 with dissolve:
        subpixel True pos (0.06, 455) 
    show brian1 with dissolve:
        subpixel True pos (0.36, 0.46) 
    show kody with dissolve:
        subpixel True pos (0.8, 0.43)  yrotate 180.0 
    b "Welcome to Subway!"
    t "Brian you do not work here, why are you introducing us here"
    t "Also you just said you never been here before"
    b "I swear you act like Bhaarat..."
    b "Nitpicking all my words and trying to make me seem like a villian" #THIS IS A COOL REFERENCE BRIAN IZ JOKE OKAY?

    scene subway2 with dissolve:
        subpixel True xzoom 1.1 zoom 3.04 
    show thanga2 with dissolve:
        subpixel True pos (0.06, 455) 
    show brian1 with dissolve:
        subpixel True pos (0.36, 0.46) 
    show kody with dissolve:
        subpixel True pos (0.8, 0.43)  yrotate 180.0 

    se "..."
    t "uh hello!"
    t "uhhhhh"
    b "you good?"
    t "Idk what to order at this ghetto looking place"
    k "it is not that Ghetto"
    show thanga2:
        linear 0.6 subpixel True pos (0.22, 461)
        yrotate 180.0
    t "there is literally a homeless guy!"
    $ count = 0
<<<<<<< HEAD
    show screen clickable_chapter_one_stn
=======
    show screen clickable_stn_chapter_one
>>>>>>> 34b9103 (did some more todos)
    stn "Fuck off Kody Kunt King!"
    k "what a dick!"

    se "oh we have more hungry homeless people"
    
    bt "We are not homeless!"
    b "Jynx you owe me a Soda!"
    t "Fine"
    
    t "I will just copy whatever Kody gets since I don't know this place"
    b "Ditto"
    t "WE GET IT BRIAN"
    t "YOU HAVE NO FRIENDS"
    t "YOUR LIFE IS POKEMON!"
    b "cope harder"
    hide screen clickable_chapter_one_stn
    scene subway3 with pixellate:
        subpixel True xzoom 1.17 zoom 1.27 
    $ count = 0
    "Sandwich Mini-game! START!"
    tv "Why did you make a Sandwich Minigame and make it like this?"
    stn "Fuck off Kody"
    k "IT WASN'T EVEN ME"
    c "bozo"
    jump chapter_one_subway_minigame

    label chapter_one_post_subway:
    play sound "audio/sound/chapter_one/eat1.ogg" loop
    "Oh my god"
    "Kody is gulping done that sandwich!"
    k "THIS IS SO GOOD!"
    t "You are going to get sick..."
    t "Brian... why did we let this happen"
    b "idk man"
    stop sound
    label chapter_one_post_lunch:
    scene inside car with fade:
        subpixel True xzoom 1.5 yzoom 1.13 zoom 0.67 
    show brian1:
        subpixel True pos (0.75, 406) zpos 0.0 xrotate 0.0 yrotate 0.0    
    show thanga2:
        subpixel True pos (343, 485)  xzoom 2.43 yzoom 0.92 zoom 1.0 
    show kody:
        subpixel True pos (0.6, 0.29) 
    b "well that was some good lunch"
    b "however, I am stuffed now"
    t "Yo brian put your phone down"
    t "You are driving..."
    b "dude, i am literally a better driver than you, you asshat"
    b "and i'm trying to get shiny shadow sexy lopunny since it is lopunny community day for pokemon go"
    k "links so I can avoid it?"
    t "shut up"
    $ _preferences.afm_enable = True
    $ _preferences.afm_time = 5
    t "BRIAN!, PAY ATTENTION, THERE IS A DOG ON THE ROAD"
    b "no whe-" 
    play sound "audio/sound/chapter_one/car_crash.ogg"
    window hide
    scene ocho_dead with vpunch and hpunch:
        subpixel True ypos -0.01 xzoom 1.17 zoom 1.67
    $ renpy.pause(2.5)
    show thanga2 with dissolve:
        subpixel True pos (1535, 365)  matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    $ _preferences.afm_enable = False
    $ _preferences.afm_time = 15
    t "holy shit"
    t "this is bad!"
    show kody with dissolve:
        subpixel True pos (0.03, 0.36)
    k "(I have to act normal... What do I say?)"
    menu:
        "What the dog doing?":
            k "What the dog doing?"
            t "NOT THE TIME KODY"
        "LMAO":
            k "LMAO"
            t "You have mental issues"
        "Press F to Pay Respects":
            k "F"
            t "this is real life kody"
            t "not a video-game"
            k "My Life is like a video-game!"
    show brian1 with dissolve:
        subpixel True pos (0.37, 0.07) zoom 0.83
    b "How bad does it look guys?"
    t "It is VERY bad"
    t "It is NOT looking good..."
    t "We should call the Owner to tell them this"
    k "Fuck that, thats an L the owner has to hold!"

    t "This is why you got bullied in High-School"
    k "Im not in highschool"
    t "You will be bullied in Highschool because of these words"
    t "Just read the Collar to me"

    k "Uh..."
    k "It just says Siete"
    k "Like there is no phone number or address"

    t "Well that sucks for the owner"
    b "yeah I agree, I guess we cannot do much for the owner"

    show ocho_dead with dissolve:
        subpixel True matrixcolor InvertMatrix(1.05)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    call dio_time_stop
    show screen clickable_chapter_one_secret_lopunny(1556,125,0.25)

    questionmark "MY DOG WHO DID THIS?"
    bt "WTF"

    k "Oh no..."
    show kody:
        linear 1 subpixel True pos (0.66, 0.2)
        subpixel True yrotate 180.0 
    k "It's Him!"
    questionmark "YOU"
    show cody:
        subpixel True pos (-0.4, 324) 
        subpixel True yrotate 180.0
        linear 0.5 subpixel True pos (0.05, 324) 
    c "You Bitch!"
    c "You cocksuckers"
    c "You Goobers and Geebers"
    b "that last one wasn't even an insult dude"
    t "Why do you look like kody?"
    k "That is because this guy is an evil verison of me"
    t "Huh?"
    t "So you weren't capping that that happened?"

    k "YES!"
    t "oh"
    c "FUCK ALL OF YOU BITCHES!"
    c "I WILL KILL ALL OF YOU"
    b "no my lopunny pls dont"
    c "I am now being told that this one has to live."
    c "I'll just..."
    c "I'll do so-something very cool"

    c "Kody you have a car and a slave now?"
    k "No thats Brian 'B-Bop' Freddy and his car"
    c "Well... Ima destroy that car"
    b "please dont, i need it to get to jewel osco for work"
    b "also pokemon go"
    c "not my problem bozo"
    hide screen clickable_chapter_one_secret_lopunny
    scene street1 with hpunch and vpunch:
        subpixel True yzoom 1.06 
    b "MY CAR!"
    b "..."
    b "where are we?"
    show brian1:
        subpixel True pos (0.62, 320) 
    show thanga2:
        subpixel True pos (0.2, 481) 
    t "We are in the middle of god knows where, It was just dark forest around us..."
    t "I guess we just gotta follow the road until we hit something"
    t "where is kody?"
    show kody with dissolve:
        subpixel True pos (0.51, 716) zoom 0.25
    show screen clickable_chapter_one_secret_lopunny(1731,100,0.13)
    k "I AM FUCKING SMALL HELP ME"
    b "lol you are like an ant to the giant of me"
    k 'THIS IS NOT THE TIME YOU COCKSUCKER I WILL BREAK YOUR KNEE-CAPS'
    b "thats all you can reach little man"
    t "gottem"
    t "Uh i guess we gotta find Cody and force him to fix this..."
    "You start to delve into the woods"
    play sound "audio/sound/chapter_one/street1.ogg"
    $ street1_random()
    "Wait who is that?"
    stop sound
    t "Who is this green guy?"
    show brian1:
        linear 1 subpixel True pos (0.17, 440) 
    show thanga2:
        linear 1 subpixel True pos (0.01, 423) 
    show kody:
        linear 1 subpixel True pos (0.13, 878) 

    questionmark "It is TIME"
    hide screen clickable_chapter_one_secret_lopunny
    show baldi1 with dissolve:
        subpixel True pos (0.57, 0.07) yrotate 180.0 
    baldi "For some MATH!"
    k "What?"
    b "I do not believe in Math!"
    baldi "What is 3 * 6?"
    t "Listen here Luigi, we don't care about math okay?"
    play sound "audio/sound/chapter_one/glock_magchange.ogg"
    window hide
    show gun1:
        subpixel True pos (0.62, 0.29) yrotate 180.0 
    $ renpy.pause(2.0)
    t "Uh we will answer your question right away!"
    t "I cannot do math right now."
    t "Brian!"
    t "You are the accounting major, answer this question!"
    b "Nah I'm looking for this lopunny"
    t "(Sigh)"
    t "I guess you are up Kody!"
    t "Don't mess this up"
    menu:
        "18":
            hide gun1
            baldi "Wow!"
            baldi "You are incredible!"
            baldi "You might be smarter than me!"
            t "Do not stroke this egomaniac's already enormous ego..."
        "24":
            baldi ">:("
            play sound "audio/sound/chapter_one/glock_magchange.ogg"
            baldi "You are trash at math!"
            stop sound
            play sound "audio/sound/chapter_one/gun_shot1.ogg"
            "noob"
            jump game_over
        "36":
            baldi ">:("
            play sound "audio/sound/chapter_one/glock_magchange.ogg"
            baldi "You are trash at math!"
            stop sound
            play sound "audio/sound/chapter_one/gun_shot1.ogg"
            "noob"
            jump game_over
        "52":
            baldi ">:("
            play sound "audio/sound/chapter_one/glock_magchange.ogg"
            baldi "You are trash at math!"
            stop sound
            play sound "audio/sound/chapter_one/gun_shot1.ogg"
            "noob"
            jump game_over
    show street1 with dissolve:
        subpixel True matrixcolor InvertMatrix(1.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    call dio_time_stop
    t "NOT AGAIN!"
    c "I WILL KILL EVERY SINGLE ONE OF YOU FUCKERS!"
    c "THE ENTITY ISN'T HERE TO SAVE YOU THIS TIME >:)"
    baldi "Follow me guys, I know a safe spot from this bozo"
    show baldi1:
        yrotate 0
        linear 0.35 xalign 1.7
    t "Wait for us!"
    show thanga2:
        linear 1 xalign 1.3
    show kody:
        linear 1 xalign 1.3
    show brian1:
        linear 1 xalign 1.7

    scene baldi_exit with dissolve:
        subpixel True pos (-9, -234) zoom 0.92 
    stop music
    play music "audio/music/chapter_one/baldi_main.ogg"
    t "Where the hell are we?"
    show thanga2 with dissolve:
        subpixel True pos (0.11, 0.42) 
    show kody with dissolve:
        subpixel True pos (0.76, 0.45) yrotate 180.0
    show brian1 with dissolve:
        subpixel True pos (0.34, 0.42) 
    b "I think this is a school..."
    b "AH HELL NAH, I JUST GRADUATED FROM HIGH SCHOOL, I AINT GOING BACK"
    t "Were you not a super senior who failed senior year three times so you can just play Smash Bros esports club?"
    b "nah I got a life unlike you losers"
    b "that was joey who is doing that, not me!"
    t "Fair Enough I suppose"
    k "WAIT THIS IS WHAT HIGH SCHOOL LOOKS LIKE!"
    k "I wanna be home-schooled thang"
    t "ask daddi not me bozo"
    
    show kody:
        linear 0.6 subpixel True pos (0.23, 0.48) 
    k "no i will say it to you bitch boy"
    t "I can smell the smash player breath get outta of my space"
    $ renpy.pause(0.3)
    show kody:
        yrotate 0.0
    show baldi1:
        subpixel True pos (0.59, 0.14) yrotate 180.0
    baldi "Welcome to my schoolhouse!"
    baldi "Where we learn things like MATH!"
    k "incredible"
    baldi "I found somebody's car in the woods the other day and I brought it here so hopefully the owner will claim it soon!"
    b "is it a toyota civic tesla cybertrunk x300?"
    baldi "Why yes it is!"
    b "YO!"
    b "i love you man!"
    b "that is my car!"
    b "well i guess that solves that problem"
    b "all i need now is my lopunny"
    baldi "I got me a Lopunny in my office but if you need your car right now"
    baldi "You must solve one of my famous riddles!"
    baldi "What is 1 + 1!"
    b "ffs, it's 2"
    baldi "Wow!"
    baldi "You might be smarter than me!"
    baldi "Here is your key to your car! I did use a lot of the fuel to get here, you got maybe two trips to some fastfood nearby I suppose"
    baldi "I will go get your lopunny, follow me to my office!"
    $ location = 1
    $ count = -2
    $ choice = 0
    # $ print("Location:", location)
    show screen clickable_button_baldi_chapter_one_up(location)
    label chapter_one_baldi_repeat_hold:
        baldi "Click the Green button above me to go into the school!"
        jump chapter_one_baldi_repeat_hold

    #Code for the exit area for Baldi's Schoolhouse, if statements check for items and displays certain buttons depending on progression!
    label baldi_exit:
        if not is_item_obtained("chapter_one_mop"):
            $ count2 += 1
        call chapter_one_hide_screen() from _call_chapter_one_hide_screen
        $ location = 1
        scene baldi_exit with dissolve:
            subpixel True pos (-9, -234) zoom 0.92 
        call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons
        label baldi_exit_1:
        if is_item_obtained("chapter_one_key"):
            show screen clickable_baldi_exit()
        if not is_item_obtained("chapter_one_mop") and count2 >= 4:
            show screen clickable_chapter_one_mop()
        elif chapter_one_dirt_piles[0] == False and is_item_obtained("chapter_one_mop"):
            show screen clickable_chapter_one_dirt(0.03, 0.43, 0.46, 0)
        if is_item_obtained("chapter_one_cleanup"):
            show screen clickable_chapter_one_god_of_sweep()
        "You are currently located at the EXIT of Baldi's Schoolhouse!"
        jump baldi_exit_1

    #Code for the main area for Baldi's Schoolhouse, if statements check for items and displays certain buttons depending on progression!
    label baldi_main_area:
        call chapter_one_hide_screen() from _call_chapter_one_hide_screen_1
        hide screen clickable_baldi_exit
        $ location = 2
        scene baldi_main with dissolve:
            subpixel True zoom 0.75 
        if(count == -2):
            hide screen clickable_button_baldi_chapter_one_up
            show baldi2 with dissolve:
                subpixel True yzoom 1.0 zoom 0.59 pos (861, 0.27)
            jump baldi_main_area_first_visit
        elif(count == -1):
            k "We gotta find a way out of here"
            k "Surely there is clues we need to stop that impossible problem!"
            t "Ugh its a professor layton game..."
            b "I think it will be more efficient if we split up so I guess I will go right"
            t "I guess I will go left"
            k "and I guess I will stay here"
            t "Alright, let's get this bread"
            b "How old are you?"
            t "Ninety-Four..."
            $ count += 1
        call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_1
        label baldi_main_area_1:
        if not is_item_obtained("chapter_one_key"):
            show screen clickable_key_chapter_one
        if chapter_one_dirt_piles[1] == False and is_item_obtained("chapter_one_mop"):
            show screen clickable_chapter_one_dirt(0.75, 0.69, 0.77, 1)
        if not is_item_obtained("chapter_one_hands"):
            show screen clickable_chapter_one_itsabully
        if not is_item_obtained("chapter_one_food") and is_item_obtained("chapter_one_faculty") and count2 != 0:
            show screen clickable_chapter_one_playtime
        "You are currently located at the MAIN AREA of Baldi's Schoolhouse!"
        jump baldi_main_area_1

    #Code for the classroom for Baldi's Schoolhouse, if statements check for items and displays certain buttons depending on progression!
    label baldi_classroom:
        call chapter_one_hide_screen() from _call_chapter_one_hide_screen_2
        $ location = 3
        scene baldi_class with dissolve:
            subpixel True zoom 0.75
        call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_2
        label baldi_classroom_1:
        if chapter_one_dirt_piles[2] == False and is_item_obtained("chapter_one_mop"):
            show screen clickable_chapter_one_dirt(0.7, 0.56, 0.52, 2)
        if not is_item_obtained("chapter_one_faculty"):
            show screen clickable_chapter_one_principal
        if count2 != 0 and is_item_obtained("chapter_one_faculty"):
            show screen clickable_chapter_one_brian
        "You are currently located at the MAIN CLASSROOM of Baldi's Schoolhouse!"
        jump baldi_classroom_1

    #Code for the faculty for Baldi's Schoolhouse, if statements check for items and displays certain buttons depending on progression!
    #Area is locked til you help Principal of the Thing
    label baldi_faculty:
        call chapter_one_hide_screen() from _call_chapter_one_hide_screen_3
        $ location = 4
        scene baldi_faculty with dissolve:
            subpixel True zoom 0.75 
        call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_3
        label baldi_faculty_1:
        # first visit
        if count2 == 0: 
            call chapter_one_faculty_first_enter() from _call_chapter_one_faculty_first_enter
        elif not is_item_obtained("chapter_one_clock"):
            show screen clickable_chapter_one_alarmclock
        if chapter_one_dirt_piles[3] == False and is_item_obtained("chapter_one_mop"):
            show screen clickable_chapter_one_dirt(0.01, 0.52, 0.36, 3)
        if count2 != 0 and is_item_obtained("chapter_one_faculty"):
            show screen clickable_chapter_one_thanga
        "You are currently located at the FACULTY ROOM of Baldi's Schoolhouse!"
        jump baldi_faculty_1
    #Code for Baldi's math game, area is unlocked once you beat the bully!
    #You cannot actually win til you solve the clock!
    label baldi_math_puzzle:
        stop music
        play music "audio/music/chapter_one/baldi_math.ogg"
        call chapter_one_hide_screen() from _call_chapter_one_hide_screen_4
        $ location = 5
        scene baldi_q1 with dissolve:
            subpixel True pos (-333, -0.26) 
        call chapter_one_restore_buttons(location) from _call_chapter_one_restore_buttons_4
        call chapter_one_hide_buttons from _call_chapter_one_hide_buttons
        baldi "Now you gotta solve my math problem!"
        scene baldi_q1 with dissolve:
            subpixel True pos (-333, -0.26) 
        baldi "What is 4 - 4?"
        $ choice = renpy.input("What is 4-4?", length = 10)
        if choice != "0":
            play sound "audio/sound/chapter_one/glock_magchange.ogg"
            show baldi_q1:
                subpixel True blur 7.82 
            show baldi2:
                subpixel True xpos 702
            show gun2:
                subpixel True pos (361, 193)
            baldi "You are stupid as fuck!"
            stop sound
            baldi "begone"
            show gunflare:
                subpixel True
            $ baldi_shoot(10)
            # baldi "How you mess up math this bad?"
            jump game_over
        baldi "WOW!"
        baldi "You are Incredible!"


        baldi "Problem #2!"
        scene baldi_q2 with dissolve:
            subpixel True pos (-333, -0.26)
        baldi "What is the value of the mathematical constant e, rounded to three decimal places?"
        $ choice = renpy.input("What is the value of the mathematical constant e, rounded to three decimal places?", length = 5)
        if choice != "2.718":
            play sound "audio/sound/chapter_one/glock_magchange.ogg"
            show baldi_q2:
                subpixel True blur 7.82 
            show baldi2:
                subpixel True xpos 702
            show gun2:
                subpixel True pos (361, 193)
            baldi "Wow you suck at mathematics!"
            baldi "DIE!"
            show gunflare:
                subpixel True
            $ baldi_shoot(15)
            jump game_over
        baldi "Incredible!"
        baldi "You might even be smarter than me!"


        baldi "Time for problem 3!"
        scene baldi_q3 with dissolve:
                subpixel True pos (-333, -0.26)
        baldi "Whats X*Y*Z / Y*X*Z + YZ equals?"
        $ print("rngint:",rngint1)
        $ choice = renpy.input("QWERTYUIP?!?", length = 17)
        $ count2 = (int)(((rngint1/2) * (rngint1+7) * (rngint1*3) / (rngint1 +7) * (rngint1/2) * (rngint1*3)) + ((rngint1+7) * (rngint1 * 3)))
        $ count1 = False
        $ choice = baldi_last_answer_check(choice)
        if int(choice) != count2:
            $ print("choice:", choice)
            $ print("answer", count2)
            scene baldi_q3_mad with dissolve:
                subpixel True pos (-333, -0.26)
            baldi "WOW THAT'S CRAZY!"
            baldi "SHIT TALK MATH AND YOU CAN'T EVEN DO IT?"
            baldi "DIE! YOU SHITTER!"
            show baldi_q3_mad:
                subpixel True blur 7.82 
            show baldi2:
                subpixel True xpos 702
            show gun2:
                subpixel True pos (361, 193)
            show gunflare:
                subpixel True
            $ baldi_shoot(25)
            jump game_over
        scene baldi_q3_happy with dissolve:
            subpixel True pos (-333, -0.26)
        baldi "I guess you do know a thing or two about math!"
        jump baldi_beaten
        "You are currently located at BALDI'S OFFICE of Baldi's Schoolhouse!"
    
    # The Ending THANK GOD I AM FREE!
    label baldi_beaten:
        play music "audio/music/chapter_one/baldi_main.ogg"
        baldi "Well done students!"
        b "Did we win?"
        k "I AM SO SICK OF MATH!"
        t "KODY SHUT UP!"
        baldi "Its alright that you do not like math right now"
        baldi "I just have to teach it better next time!"
        k "HA CA-"
        t "SHUT THE FUCK UP KODY!"
        t "Yeah Mr. Baldi, we would be honored to learn more math!"
        baldi "That is GREAT to hear!"
        baldi "Let me go get your prize!"
        baldi "It is in the main area!"
        scene baldi_main with dissolve:
            subpixel True zoom 0.75
        t "It feels weird to be cool with you baldi!"

        show thanga2 with dissolve:
            subpixel True pos (50, 381) 
        show kody with dissolve:
            subpixel True pos (346, 448) 
        show brian1 with dissolve:
            subpixel True pos (1285, 333) 
        show baldi2 with dissolve:
            subpixel True pos (868, 208) zoom 0.52 
        baldi "You are all incredible!"
        t "not brian"
        b "fuck off i did all the work"
        t "I ain't even gonna cap!"
        t "kody kinda kooked"
        k "that is because I am the best mogger and mewer"
        t "shut up"
        b "So where is my prize"
        baldi "Ah yes, you have to answer one more question to get it!"
        b "WHAT!"
        baldi "jokes lol"

        show lopunny1:
            subpixel True pos (840, 316) 
        baldi "Here is your prize :)"
        b "oh"
        b "my"
        b "god"
        b "I am so HAPPY!"
        
        show lopunny1:
            linear 2.3 subpixel True pos (1153, 505) 
        b "I am gonna have fun tonight"
        k "can you lead us out baldi"
        baldi "Yeah sure fam"
        scene baldi_exit with dissolve:
            subpixel True pos (-9, -234) zoom 0.92 

        show thanga2 with dissolve:
            subpixel True pos (0.11, 0.42) 
        show kody with dissolve:
            subpixel True pos (0.23, 0.48)
        show brian1 with dissolve:
            subpixel True pos (0.34, 0.42) 
        show baldi1:
            subpixel True pos (0.59, 0.14) yrotate 180.0
        t "wait isn't cody still out there?"
        show baldi_exit with dissolve:
            subpixel True matrixcolor InvertMatrix(1.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        show baldi_exit_hover:
            subpixel True pos (0.6, 0.23) zoom 0.9 matrixcolor InvertMatrix(1.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        b "NOT AGAIN!"
        show cody:
            xalign 1.7
            subpixel True crop_relative True  rotate 0.0 crop (0.42, -0.13, 0.33, 0.37)
            linear 0.35 subpixel True pos (0.99, 0.28)
    
        show thanga2:
            linear 0.4 subpixel True pos (-0.0, 0.39) 
        show kody:
            linear 0.4 subpixel True pos (0.11, 0.45) 
        show brian1:
            linear 0.4 subpixel True pos (0.21, 0.4) 
        show baldi1:
            linear 0.4 subpixel True pos (0.29, 0.19) 
            yrotate 0.0


        c "LET ME IN!"
        c "I WILL AVENGE MY DOG"
        c "OOO A RABBIT"
        c "I WILL EAT THAT TOO!"
        baldi "This is your bozo who is being annoying?"
        c "WAIT BALDI THATS YOU?"
        c "WHY ARE YOU HELPING THEM!"
        baldi "Because our deal is OVER!"
        baldi "Also these are my students and I reserve the right to defend them"
        c "fucker"
        show gun1:
            subpixel True pos (988, 471) 
        play sound "audio/sound/chapter_one/glock_magchange.ogg"
        c "WHY DO YOU HAVE A GUN IN A SCHOOL?????????????????????????????"
        baldi "Because I am not a woke teacher, I will defend my country"
        baldi "and that includes from terrorists like YOU"

        show gunflare:
            subpixel True anchor (234, 99) pos (1248, 441) zoom 0.42 
        play sound "audio/sound/chapter_one/gun_shot1.ogg"
        c "OW WTF"
        hide gunflare
        
        stop sound
        baldi "Get The fuck outta here!"
        c "NO WAY IM KILLING THESE FUCKERS"
        play sound "audio/sound/chapter_one/glock_magchange.ogg"
        c "OKAY OKAY I AM DONE"
        show cody:
            linear 0.85 xalign 1.7
        c "LATER LOSERS!"
        hide cody
        k "what a loser..."
        b "Can i have my car keys"
        baldi "I slipped them into your pocket"
        baldi "You should be safe to leave now"
        k "THANK YOU BALDI WE BIG FANS!"
        show baldi_exit:
            matrixcolor SaturationMatrix(0)
        show baldi1:
            matrixcolor SaturationMatrix(0)
        show thanga2:
            matrixcolor SaturationMatrix(0)
        show kody:
            matrixcolor SaturationMatrix(0)
        show gun1:
            matrixcolor SaturationMatrix(0)
        show baldi_exit_hover:
            matrixcolor SaturationMatrix(0)
        show brian1:
            matrixcolor SaturationMatrix(0)
        "Well that was a complete travesty..."
        "There were some good and bad things"
        show screen clickable_chapter_one_secret_lopunny(618,576,1.0)
        "That is one fine lopunny"
        hide screen clickable_chapter_one_secret_lopunny
        "And after Baldi shot evil cody, the world was saved and everyone lived heavily after ever"
        "Til next time"
        k "Wait why are we black..."
        $ persistent.ch01 = True
        $ if(lopunny_count == 5): persistent.secret1 = True
        if persistent.secret1 == True:
            jump chapter_one_secret
        else:
            return
        label chapter_one_secret:
            questionmark "That is what the ChatGPT script came up with"
            scene crystalball with easeintop:
                subpixel True zoom 1.5 
            show cody:
                subpixel True pos (1516, 275)
            show sonuthenecro:
                subpixel True anchor (387, 108) pos (310, 156) zoom 0.88 
            stn "WHAT THE FUCK MAN!"
            c "IDK MAN"
            stn "YOU LOST TO A BULLET!"
            c "I WANNA SEE YOU DO BETTER!"
            stn "I DONT DECIDE THINGS HERE!"
            c "WELL WHO DOES HUH!"
            questionmark "I believe I do around here"
            stn "that's the boss"
            c "What the fuck are you"
            questionmark "I want someone killed off, I require a blood sacrifice"
            stn "mmmmm That could be in the cards, I'm not letting Kody be the one though."
            c "WHAT!"
            c "WHAT ARE YOU DOING!"
            stn "idk man you can have your final boss later"
            c "FIGHT ME RIGHT NOW"
            c "ARMWRESTLE ME"
            stn "Don't make me play sound 'audio/sound/chapter_one/glock_magchange.ogg'"
            c "YOU HAVE THAT TOO?"
            stn "Of Course"
            questionmark "Would be a shame if someone saw this conversation"
            stn "Yeah imagine there was a secret ending where this was present"
            c "WHAT WHAT WHAT"
            c "MY DOG THOUGH HOW IS THIS AN ENDING FOR ME"
            stn "The dog wasn't even real"
            stn "it was a jpeg file called ocho_dead.jpg"
            c "TRUEEEEEEEEEEEEEEEE!"
            return