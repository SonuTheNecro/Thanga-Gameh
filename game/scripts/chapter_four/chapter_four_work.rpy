# Code for the Work Section of Chapter Four
default chapter_four_work_event_check = [False, False, False, False, False, False, False, False]

label chapter_four_hide_office:
    hide screen clickable_chapter_four_register
    return
label chapter_four_setup_resources:
    python:
        work_events = 0
        rngint = 0
        resource_manager = ResourceHandler()
        customer_enjoyment = Resource("customer_enjoyment", 50)
        resource_manager.add_resource(customer_enjoyment)
        food = Resource("food", 100)
        resource_manager.add_resource(food)
        money = Resource("money", 35)
        resource_manager.add_resource(money)

        event_manager = EventHandler()
        event_1 = Event(1, 1, "Serve an Old Friend")
        event_2 = Event(2, 1, "Help a sad fool")
        event_3 = Event(3, 4, "A New Challenger Appears!")
        event_4 = Event(4, 1, "Stay High!")
        event_5 = Event(5, 1, "HIM!")
        event_manager.add_event(event_1)
        event_manager.add_event(event_2)
        event_manager.add_event(event_3)
        event_manager.add_event(event_4)
        event_manager.add_event(event_5)
        
    jump chapter_four_office

label chapter_four_office:
    scene ch04_work_bg with dissolve:
        subpixel True xzoom 1.28 zoom 2.4 
    show ch04_counter:
        subpixel True pos (290, 508) zoom 1.4 
    #show ch04_register:
        #subpixel True pos (736, 353) zoom 0.41 
    show screen clickable_chapter_four_register
    show ch04_mop:
        subpixel True pos (1375, 391) zoom 0.76 xrotate 0.0 yrotate 180.0 
    show ch04_exit_door:
        subpixel True pos (-320, 176) rotate -9.0 zoom 0.4 





    $ renpy.pause(hard = True, delay = 10)


    "test1"
    jump chapter_four_office

screen clickable_chapter_four_register:
    imagebutton:
        pos (736, 353) at Transform(zoom =0.41 )
        idle "images/chapter_four/ch04_register.png"
        hover "images/chapter_four/ch04_register.png"
        action Jump("chapter_four_random_work")


label chapter_four_random_work:
    label ch04_rng_1:
    $ rngint = renpy.random.randint(1, 5)
    if chapter_four_work_event_check[rngint - 1]:
        jump ch04_rng_1
    label ch04_rng_2:
    $ rngint1 = renpy.random.randint(1, 5)
    if chapter_four_work_event_check[rngint1 - 1]:
        jump ch04_rng_2
    label ch04_rng_3:
    $ rngint2 = renpy.random.randint(1, 5)
    if chapter_four_work_event_check[rngint2 - 1]:
        jump ch04_rng_3


    $ rngint = 5
    $ event_option_1 = str(f"{eval('event_' + str(rngint)).print_info()}")
    $ event_option_2 = str(f"{eval('event_' + str(rngint1)).print_info()}")
    $ event_option_3 = str(f"{eval('event_' + str(rngint2)).print_info()}")
    call chapter_four_hide_office
    $ event_manager.pick_three_events(4)
    jump expression "ch04_event_" + str(rngint)
#TODO: Add a lot more visual flair to each and every event so they are prime neeto
label chapter_four_work_events():
    label ch04_event_1:
        scene ch04_ice_cream_interior with dissolve:
            subpixel True xzoom 1.18 zoom 1.64
        show matt2 with moveinleft:
            pos (513, 151)  zoom 0.75
        show thanga2 with dissolve:
            subpixel True pos (1331, 166) zoom 1.17 yrotate 180.0 
        mt "THANG!"
        t "yo" #TODO: DIscord join sfx here
        mt "..."
        t "so what are you doing here?"
        mt "I WORK HERE DUMBASS"
        t "kill yourself"
        mt "okay you are real"
        t "?"
        mt "DUDE WE ARE IN SOME SORTA BOOK OR NOVEL OR GAME"
        mt "THERE IS THIS GUY WHO IS LIKE GOD"
        mt "AND HE IS TELLING ME WHAT TO DO"
        t "ugh"
        mt "WHY ARE YOU SIGHING?????"
        mt "DO YOU KNOW?!?"
        t "kody has been going off about it for like 2 months now"
        t "I really don't care"
        t "I dont need to hear more yapping about this nonsense"
        mt "DON'T YOU REMEMBER CODY AT THE VAULT?"
        mt "WE HAVE PROOF IT WAS REAL!"
        t "yeah that was kinda strange..."
        t "but just because you have one weird day doesn't mean you are suddenly the protagonist of a book"
        mt "I AM THOUGH!!!!!!!!"
        t "idgaf"
        window auto hide
        $ renpy.pause(2.0, hard = True)
        mt "..."
        mt "fuck you"
        t "well kill yourself too"
        call auto_advance(1)
        mt "THAT DOESN'T MEAN ANYTHING"
        mt "okay whatever"
        call auto_advance(0)
        mt "What do you want to order?"
        t "I would like something that will increase my rizz for my girl"
        mt "you have a girlfriend?"
        t "yeah hutao"
        mt "yeah okay man"
        show ch04_hutao:
            subpixel True pos (1908, 156) 
            linear 0.34 subpixel True pos (1530, 156)
        hutao "my mans need to increase his skibidi rizz"
        show thanga2:
            yrotate 0.0
        t "thanks babe"
        show ch04_hutao:
            linear 0.24 subpixel True pos (1908, 156)
        show thanga2:
            yrotate 180.0
        pause 0.3
        hide matt2
        show ch04_matt_reaction:
            subpixel True pos (99, 198) 
        mt "WHATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
        hide ch04_matt_reaction
        show matt2:
            pos (513, 151)  zoom 0.75
        mt "HOW DID YOU DO THAT?"
        t "idk i went onto tinder and found her"
        mt "alright man"
        t "well"
        t "Im waiting..."
        mt "huh?"
        t "my ORDER"
        menu:
            "Skibidi Crunch Bar":
                $ customer_enjoyment.plus(5)
            "Caseoh Creampies":
                $ customer_enjoyment.plus(5)
            "Kai Cenat Cookies":
                $ customer_enjoyment.plus(5)
        mt "what did BRIAN DO?"
        mt "WHY ARE THESE ON THE MENU!"
        mt "HERES YOUR FUCKING BRAIN-ROT FOOD"
        t "thanks matt, I really enjoy this food lol"
        mt "YOU BETTER!"
        show thanga2:
            yrotate 0.0 
            linear 0.23 subpixel True pos (1963, 203)
        mt "(sigh)"
        $ work_events += 1
        $ chapter_four_work_event_check[rngint - 1] = True
        jump chapter_four_office
    label ch04_event_2:
        scene ch04_ice_cream_interior with dissolve:
            subpixel True xzoom 1.18 zoom 1.64
        show matt2 with moveinleft:
            pos (513, 151)  zoom 0.75
        show kody with dissolve:
            subpixel True pos (1185, 290) zoom 1.21 yrotate 180.0 
        mt "KODY!"
        k "It's me the goat"
        mt "right..."
        k "I haven't been in this chapter yet"
        mt "you literally have..."
        window auto hide
        $ renpy.pause(0.5, hard = True)
        mt "wait"
        mt "SO YOU KNOW?!?"
        k "know what?"
        mt "THAT WE ARE IN A BOOK AND SOME NARRATOR BOZO IS READING OUR LIVES?"
        k "lol"
        mt "FUCK YOU MEAN LOL?"
        k "I thought that, then I just stopped having schizoprenia"
        mt "FUCK YOU"
        mt "IT AINT SCHIZO IF WE BOTH HAVE IT!"
        k "nah im just a mogger and you are just a dogger"
        mt "FUCK DOES THAT EVEN MEAN!"
        k "idk"
        mt "wait..."
        mt "ISN'T THERE SCHOOL?"
        "its sunday"
        mt "right..."
        k "it is indeed sunday man"
        window auto hide
        $ renpy.pause(2.0, hard = True)
        mt "YOU HEARD HIM"
        mt "IM NOT SCHIZO"
        mt "YOU ARE JUST CAPPING ME"
        k "nah you just weird"
        mt "fucking hell"
        mt "i dont even give a fuck rn"
        k "nah you do"
        mt "nah nah idgaf"
        k "'idgaf' as you gaf"
        mt "shut up"
        mt "fuck you even want here?"
        k "oh you guys got some beast bars"
        mt "this is an ice cream shop"
        k "nah the plot demands mr beast bars so ima get some"
        mt "what..."
        show ch04_beast_bar_ac with dissolve:
            subpixel True pos (448, 198) rotate 18.0 
        mt "WHATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
        k "oh shit what flavors you got?"
        menu:
            "Milk Chocolate":
                $ resource_manager.food_down_level_up(10,10)
            "Peanut Butter Crunch":
                $ resource_manager.food_down_level_up(5,5)
            "Dark Chocolate":
                $ resource_manager.food_down_level_up(5,4)
            "Almond":
                $ resource_manager.food_down_level_up(2,2)
            "Peanut Butter":
                $ resource_manager.food_down_level_up(1,4)
            "Dark Chocolate Sea Salt":
                $ resource_manager.food_down_level_up(6,2)
            "Milk Crunch":
                $ resource_manager.food_down_level_up(5,5)
            "Crimson Blood Toasted":
                $ resource_manager.food_down_level_up(3,3)
            "Clipped Toe-Nails Beard Shavings":
                $ resource_manager.food_down_level_up(1,5)
            "Sea Turtle Shell with Toasted used baby-wipes":
                $ resource_manager.food_down_level_up(15,20)
            "Chinese worker factory blood infused with type 0 diabetes":
                $ resource_manager.food_down_level_up(1,15)
            "Mogging Juice":
                $ resource_manager.food_down_level_up(3,7)
            "Goon Liquid fried in a grill-pan":
                $ resource_manager.food_down_level_up(1,1)
            "Mayonaise with a hint of Ice":
                $ resource_manager.food_down_level_up(3,6)
            "Anime-Girl Thigh-High Sweat":
                $ resource_manager.food_down_level_up(20,15)
            "Glass Shards with Chex Mix":
                $ resource_manager.food_down_level_up(5,4)
            "Cheetos with Pizza Crust":
                $ resource_manager.food_down_level_up(4,5)
            "Chocolate Milk with Mustard, Ketchup, Baby Skull Dust, and Lettuce":
                $ resource_manager.food_down_level_up(2,3)
            "Gluten-Free Chocolate":
                $ resource_manager.food_down_level_up(3,4)
            "Chocolate with the choco and is very Late":
                $ resource_manager.food_down_level_up(5,5)
            "Romanian styled Mulch":
                $ resource_manager.food_down_level_up(4,7)
            "Vietnamease Styled Slavery":
                $ resource_manager.food_down_level_up(0,2)
            "Chinese Flavored Dog":
                $ resource_manager.food_down_level_up(1,1)
            "Indian Flavored Curry with a hint of butter chicken but without the er and chicken":
                $ resource_manager.food_down_level_up(17,21)
            "Poison":
                $ resource_manager.food_down_level_up(0,-5)
            "Rat Poison":
                $ resource_manager.food_down_level_up(1,-10)
            "Red-40.1 Chimkin Flavor":
                $ resource_manager.food_down_level_up(3,13)
            "Dominos Pizza but its just the eruption cake":
                $ resource_manager.food_down_level_up(2,6)
            "breadstick without cheese":
                $ resource_manager.food_down_level_up(3,5)
            "pretzel":
                $ resource_manager.food_down_level_up(3,6)
            "German Wine from the 20th Century":
                $ resource_manager.food_down_level_up(10,10)
            "Vietnamese Relics passed down from Thanga's Great-Great-Great-good-Great-Mediocre-bad-horrible-atriocious-good-great godfather":
                $ resource_manager.food_down_level_up(15,10)
            "Burnt Mac & Cheese":
                $ resource_manager.food_down_level_up(3,2)
            "Mac & Dog":
                $ resource_manager.food_down_level_up(2,2)
            "Spicy Mac & Dog":
                $ resource_manager.food_down_level_up(4,6)
            "cuCUMber in water":
                $ resource_manager.food_down_level_up(1,2)
            "Pickle Juice in a glass jar":
                $ resource_manager.food_down_level_up(2,4)
            "Rick's Alcohol":
                $ resource_manager.food_down_level_up(3,4)
            "Quakers":
                $ resource_manager.food_down_level_up(2,5)
            "Vegan Nuts":
                $ resource_manager.food_down_level_up(1,0)
            "The Glazing off of a MrBeast Fan":
                $ resource_manager.food_down_level_up(1,1)
            "Keyboard SKin Cells":
                $ resource_manager.food_down_level_up(0,1)
            "Brian's Computer Dust":
                $ resource_manager.food_down_level_up(3,4)
            "Vu's Basement average liquid (ppm)":
                $ resource_manager.food_down_level_up(4,3)
        show ch04_beast_bar_ac:
            linear 0.5 subpixel True xpos 943 
        pause 0.5
        hide ch04_beast_bar_ac
        mt "WHAT ARE THESE FLAVORS!"
        k "these are great flavors for great moggers"
        mt "BRO THESE AREN'T EVEN FLAVORS"
        k "well thanks for the mog fuel"
        show kody:
            yrotate 0.0
            linear 0.45 subpixel True pos (1953, 288) 
        mt "jesus christ"
        $ work_events += 1
        $ chapter_four_work_event_check[rngint - 1] = True
        jump chapter_four_office
    label ch04_event_3:
        scene ch04_ice_cream_interior with dissolve:
            subpixel True xzoom 1.18 zoom 1.64
        show matt2 with moveinleft:
            pos (513, 151)  zoom 0.75
        mt "oh god I wonder who is gonna come in next"
        show ch04_toni with dissolve:
            subpixel True crop_relative True pos (1920, 27) zoom 0.9 crop (0.0, -0.07, 1.0, 1.0) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yrotate 180.0 
            linear 0.45 subpixel True xpos 1110 
        toni "yooooooo matt"
        toni "what is up my f#gg0t!"
        mt "YOOOOOOOOOOOOOOOOOOOOO"
        mt "YOU CAN'T SAY THAT THAT IS HOMOPHOBIC!"
        call auto_advance(1)
        toni "i dont care ni-"
        mt "NO NO NO NO"
        call auto_advance(0)
        mt "IMA KICK YOU OUT IF YOU KEEP SLURRING"
        toni "awwwwww"
        toni "you gay or something?"
        mt "yeah just keep going with the homophobia"
        mt "it feels like thang"
        toni "yeah man"
        toni "I taught thang the ways of the idubbbz fanboy"
        mt "mmmmmmmmm"
        mt "so uh"
        mt "What do you want exactly?"
        show gun1:
            subpixel True pos (931, 331) yrotate 180.0 
        #TODO: Play audio here
        toni "I want the money in the register"
        show matt2:
            linear 0.345 subpixel True pos (325, 151) 
        mt "DUDE"
        mt "YOU ARE ROBBING AN ICE CREAM STORE FOR MONEY!"
        mt "WHY NOT GO TO THE BANK?!?"
        toni "everyone expects a bank robbery"
        toni "no one expects a ice cream robbery"
        toni "so make it snappy buddy"
        menu:
            "Give Toni All The Money":
                mt "uh here is the money man!"
                "You Gave Toni all of your money!"
                $ money.set_level(0)
            "Give Toni All The Ice Cream":
                mt "Uh here is the ice cream man"
                "You Gave Toni all of the ice cream supplies!"
                $ food.set_level(0)
            "Give Toni Nothing":
                mt "NAH FUCK YOU"
                mt "I AINT GIVING SHIT"
                toni "well man"
                toni "Guess you gotta go"
                show gunflare:
                    subpixel True  pos (466, 95) zoom 0.69 
                $ fnaf_shoot(10)
                jump game_over
        toni "alright thanks man for the loot"
        toni "I think I can buy my citizenship with this"
        hide gun1
        toni "I'll see you later and I will be telling my fellow romanians about this hotspot!"
        show ch04_toni:
            yrotate 0.0
            linear 0.456 subpixel True xpos 2046 
        mt "WHATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
        show matt2:
            linear 0.2 pos (513, 151)  zoom 0.75
        mt "DID I JUST GET FUCKING ROBBED"
        "Yeah I guess you did"
        mt "BRIANS GONNA KILL ME!"
        "maybe we can earn it back and he wont notice?"
        mt "HOW IS BRIAN NOT GONNA NOTICE WE GOT ROBEBD"
        "well if we got cameras then we are good potentially..."
        mt "NO THERE IS NO CAMERAS"
        mt "WE SOLD THEM BECAUSE KIDS WERE SPITTING FOOD AT THEM"
        "oh"
        mt "guess I just gotta earn ALL OF THAT FUCKING MONEY BACK" #TODO: This kinda sort, make this longer
        mt "GREAT!"
        "good luck man!"
        $ work_events += 1
        $ chapter_four_work_event_check[rngint - 1] = True
        jump chapter_four_office
    label ch04_event_4:
        scene ch04_ice_cream_interior with dissolve:
            subpixel True xzoom 1.18 zoom 1.64
        show matt2 with moveinleft:
            pos (513, 151)  zoom 0.75
        mt "oh god I wonder who is gonna come in next"
        show ch04_toni with dissolve:
            subpixel True crop_relative True pos (1920, 27) zoom 0.9 crop (0.0, -0.07, 1.0, 1.0) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yrotate 180.0 
            linear 0.45 subpixel True xpos 1110
        call auto_advance(1)
        toni "YO WHAT IS GOOD MY NI-"
        mt "NO!"
        toni "MY NI-"
        mt "NO!"
        toni "YOU FA!"
        mt "NO!"
        toni "YOU RE-"
        call auto_advance(0)
        mt "NO NO NO NO"
        mt "NONE OF THESE SLURS!"
        toni "what?"
        toni "why?"
        mt "we need to keep a pg-13 rating"
        toni "this isn't a movie man"
        mt "you wouldn't get it"
        window auto hide
        $ renpy.pause(2.0, hard = True)
        mt "sooooo what can I get you"
        toni "some weed"
        mt "bro its an ice cream store"
        toni "I NEED THE WEEEEDDDDDDDD!"
        mt "uh i got marijuana"
        toni "what kind?!?"
        menu:
            "Medical":
                $ customer_enjoyment.plus(5)
            "Medicinal":
                $ customer_enjoyment.plus(4)
            "Meditation":
                $ customer_enjoyment.plus(3)
            "Straight up Illegal":
                $ customer_enjoyment.plus(2)
        show ch04_marijuana with dissolve:
            subpixel True pos (541, 355) 
            linear 0.345 subpixel True pos (892, 355) 
        pause 0.345
        toni "yo thanks for the stick-up man"
        mt "yeah..."
        mt "your welcome..."
        toni "whats wrong man?"
        mt "I don't really like these drugs"
        toni "nah its the shit"
        toni "you should do some"
        mt "i dont think i should"
        toni "i didnt know we had a loser like thang!"
        mt "WHATTTTTTTTTTT"
        mt "I am not a loser!!1111!!!"
        mt "I AM A WINNER"
        mt "GIVE IT TO ME"
        show ch04_marijuana:
            linear 0.345 subpixel True pos (541, 355) 
        pause 0.345
        
        window auto hide
        camera:
            subpixel True 
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(45.0) 
            linear 0.13 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(75.0) 
            linear 0.15 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(105.0) 
            linear 0.14 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(130.0) 
            linear 0.17 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(160.0) 
            linear 0.09 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(190.0) 
            linear 0.14 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(220.0) 
            linear 0.13 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(260.0)
            linear 0.13 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(290.0)
            linear 0.13 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(320.0)
            linear 0.13 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(360.0)
            linear 0.13 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(320.0)
            linear 0.13 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(290.0)
            linear 0.13 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(260.0)
            linear 0.14 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(180.0)
            linear 0.14 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(140.0)
            linear 0.14 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(100.0)
            linear 0.14 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(60.0)
            linear 0.14 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(30.0)
            linear 0.14 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            repeat 
        window auto show
        mt "WHAT"
        mt "I SEE SO MANY COLORS WHATTTTTTTTTTTTTTTT"
        toni "yeah its great man"
        "WHAT HAVE YOU GUYS DONE?!?"
        mt "MAN IM TRIPPING"
        $ reset_camera(0)
        $ work_events += 1
        $ chapter_four_work_event_check[rngint - 1] = True
        jump chapter_four_office
    label ch04_event_5:
        scene ch04_ice_cream_interior with dissolve:
            subpixel True xzoom 1.18 zoom 1.64
        show matt2:
            subpixel True pos (-202, 200) zoom 0.68 
            linear 0.456 subpixel True  pos (536, 200) zoom 0.68 
        pause 0.5
        mt "I am so done with all of these weirdos coming to work"
        mt "wonder who is coming to work"
        questionmark "I would like to place an order..."
        mt "uh sure"
        mt "where are you sir and or madam?"
        show cody with dissolve: #TODO: This sequence could be better
            subpixel True pos (1186, 213) zoom 1.31 
        c "OF VIOLENCE!"
        mt "..."
        c "that was cooler in my head"
        show matt2:
            linear 0.123 subpixel True pos (-15, 211) 
        pause 0.2
        mt "get away from me you weirdo"
        c "why so..."
        
        show cody:
            linear 0.2 subpixel True pos (271, 15) zoom 4.52  #TODO: make a cody jumpscare
        window auto hide
        $ renpy.pause(hard = True, delay = 0.2)
        c "SCARED?!?"
        mt "WTF"
        mt "WHAT DO YOU WANT FROM ME?"
        show cody:
            linear 0.2 subpixel True pos (890, 680) zoom 0.49 
        c "does this make you more comfortable?"
        c "I need some questions answered and you are my best bet?"
        mt "NAH"
        
        window auto hide
        show matt2:
            subpixel True 
            pos (-15, 211) 
            linear 0.20 pos (771, 215) 
            linear 0.15 pos (776, 0) 
            linear 0.10 pos (803, 256) 
            linear 0.10 pos (843, 3)
        with Pause(0.5)
        hide cody
        show matt2:
            subpixel True
            linear 0.15 pos (845, 223) 
            linear 0.18 pos (890, 0) 
            linear 0.19 pos (870, 183) 
            linear 0.23 pos (1193, 225) 
        with Pause(0.9)
        show matt2:
            pos (1193, 225) 
        window auto show
        mt "gottem"
        mt "WAIT?!?"
        mt "THAT WAS THE FINAL BOSS?!?!"
        mt "HOW DID THANG AND CODY STRUGGLE WITH THIS BOZO?!?"
        "I guess?"
        "I think its.... over?"
        # TODO: Roll credits Fake Ending
        if not persistent.secret0:
            jump chapter_four_early_ending_1
        "Congrats matt..."
        mt "YIPPIE!"
        #TODO: Laugh audio
        c "YOU!"
        c "YOU REALLY THOUGHT YOU COULD DEFEAT ME?!?"
        show cody with dissolve:
            subpixel True pos (488, 256) zoom 1.31 yrotate 180.0 
        mt "fuck..."
        mt "who and what even are you?"
        mt "I wasn't there..."
        c "well i am a supreme being of intellectual power of infinite ability meant to devesate the universe using the great Shrody Mogging Technique used to levitate and embalance the photosynthesis and divide the diamater of the logarthmitic of the mangos mirroed glasses pepsi you will need all secrets in each chapter to beat this."
        mt "Whole lotta yapping"
        c "shut the FUCK UP"
        mt "You said earlier you had some questions?"
        c "..."
        mt "well?"
        c "Oh I thought you didn't want me yapping"
        mt "Dang you are still just an annoying 14 year old..."
        c "HEY!"
        mt "well...."
        c "huh?"
        c "oh yeah"
        c "Im meeting up with a boy with a Little Lord Fauntleroy Blue Cap?"
        mt "huh?"
        c "Its like a sailor cap..."
        mt "Seems awfully familar"
        c "I am also meeting up with someone with a blue shirt"
        mt "are your friends just the blue boys?"
        mt "like blue da be dah"
        window auto hide
        $ renpy.pause(hard = True, delay = 1.0)
        c "..."
        c "That wasn't funny"
        mt "Are they evil?"
        mt "like hitler evil?!?"
        c "They are probably worse than me lol"
        mt "So why ask me?"
        c "You know more than everyone"
        c "lets just say something awesome is going to happen at tonight's smash tournament"
        mt "!"
        mt "wtf are you gonna do"
        c "lets' just say tonight is the final day you will see your friends"
        mt "!"
        mt "oh yeah?"
        mt "I will tell everyone to not come to the LGS"
        c "You really think Thang and Brian and Kody and everyone will believe you?"
        c "They won't care about what you say til its too late :)"
        mt "fuck..."
        mt "Well I will stand on guard at the LGS til you show up"
        c "mmmm I dont think so"
        mt "wdym"
        c "You are on the clock buddy"
        c "and I will make sure you go through living hell"
        c "and you will get hella overtime too..."
        c "So thats cool i guess"
        mt "fuck you"
        c "toodles bitch boy"
        c "Say Hi to Igor for me!"
        show matt2:
            linear 0.34 subpixel True pos (875, 235) 
        show cody:
            linear 0.19 subpixel True xpos 2423 
        $ work_events += 1
        $ chapter_four_work_event_check[rngint - 1] = True
        jump chapter_four_office