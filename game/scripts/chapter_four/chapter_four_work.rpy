# Code for the Work Section of Chapter Four
default chapter_four_work_event_check = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False] #15 events stored :)
label chapter_four_hide_office:
    hide screen clickable_chapter_four_door
    hide screen clickable_chapter_four_register
    return
label chapter_four_setup_resources:
    python:
        #work_events = 0
        rngint = 0
        lower_value = 1
        resource_manager = ResourceHandler()
        customer_enjoyment = Resource("customer_enjoyment", 50)
        resource_manager.add_resource(customer_enjoyment)
        food = Resource("food", 100)
        resource_manager.add_resource(food)
        money = Resource("money", 35)
        resource_manager.add_resource(money)
        clean = Resource("clean", 100)
        resource_manager.add_resource(clean)
        work_events = Resource("work_events", 0)


        event_manager = EventHandler()
        event_1 = Event(1, 1, "Serve an Old Friend")
        event_2 = Event(2, 1, "Help a mogger")
        event_3 = Event(3, 3, "A New Challenger Appears!")
        event_4 = Event(4, 1, "Stay High!")
        event_5 = Event(5, 9999999, "????????????????????????????????????????") #TODO: Error and glitch text here
        event_6 = Event(6, 2, "Mathematics is the most important Subject!")
        event_7 = Event(7, 2, "Remember! No Gooning!")
        event_8 = Event(8, 1, "For the 8th Day of Christmas...")
        event_9 = Event(9, 3, "Fish outta water!")
        event_10 = Event(10,4, "Remember to restock those shelves!")
        event_11 = Event(11,1, "TBD" )
        event_manager.add_event(event_1)
        event_manager.add_event(event_2)
        event_manager.add_event(event_3)
        event_manager.add_event(event_4)
        event_manager.add_event(event_5)
        event_manager.add_event(event_6)
        event_manager.add_event(event_7)
        event_manager.add_event(event_8)
        event_manager.add_event(event_9)
        event_manager.add_event(event_10)
        event_manager.add_event(event_11)
        
    jump chapter_four_office
# Recover Screens
label chapter_four_office_show_screens:
    show screen clickable_chapter_four_register
    call screen clickable_chapter_four_door
    return
# Shows all images when we dont wanna show screens
label chapter_four_office_show_images:
    show ch04_exit_door:
        subpixel True pos (-320, 176) rotate -9.0 zoom 0.4 
    show ch04_counter:
        subpixel True pos (290, 508) zoom 1.4 
    show ch04_register:
        subpixel True pos (736, 353) zoom 0.41 
    show ch04_mop:
        subpixel True pos (1375, 391) zoom 0.76 xrotate 0.0 yrotate 180.0 
    show ch04_exit_door:
        subpixel True pos (-320, 176) rotate -9.0 zoom 0.4 
    return
label chapter_four_office:
    call auto_advance(0)
    scene ch04_work_bg with dissolve:
        subpixel True xzoom 1.28 zoom 2.4
    show ch04_counter:
        subpixel True pos (290, 508) zoom 1.4
    show ch04_mop:
        subpixel True pos (1375, 391) zoom 0.76 xrotate 0.0 yrotate 180.0 
    call chapter_four_office_show_screens


screen clickable_chapter_four_register:
    imagebutton:
        pos (736, 353) at Transform(zoom =0.41 )
        idle "images/chapter_four/ch04_register.png"
        hover "images/chapter_four/ch04_register.png"
        action Jump("chapter_four_random_work")
screen clickable_chapter_four_door:
    imagebutton:
        pos (-320, 176) at Transform(rotate=-9.0, zoom =0.4 )
        idle "images/chapter_four/ch04_exit_door.png"
        hover "images/chapter_four/ch04_exit_door.png"
        action Call("chapter_four_attempt_leave_work")

label chapter_four_random_work:
    call chapter_four_hide_office
    call chapter_four_office_show_images 
    $ event_manager.pick_three_events(10,10)
    if work_events.get_level() == 5:
        $ lower_value = 5
        $ event_manager.pick_three_events(5,5)
    $ event_manager.pick_three_events(lower_value,4)
    jump expression "ch04_event_" + str(rngint)
label chapter_four_attempt_leave_work:
    call chapter_four_hide_office
    call chapter_four_office_show_images
    if work_events.get_level() >= 25:
        jump chapter_four_post_work
    else:
        mt "idk if I can leave yet..."
        "why not?"
        mt "I gotta fulful my work quote"
        "well how much closer are we to hitting it?"
        mt "well we are [25 - work_events.get_level()] commissions left"
        if 25 - work_events.get_level() > 20:
            "damn thats alot let"
            mt "yeah"
        elif 25 - work_events.get_levels() > 10:
            "we aren't that far away, we are making our way"
            mt "trudat"
        elif 25 - work_events.get_levels() > 5:
            mt "my favorite part of work.  The last hour"
            mt "kinda like its the last hour of school"
            mt "so exciting!"
        hide ch04_register
        hide ch04_exit_door
        call chapter_four_office_show_screens
        return
# calls a random background from a variety of backgrounds
label chapter_four_random_background():
    $ rngint = renpy.random.randint(0,1)
    # $ rngint = 1
    if rngint == 0:
        scene ch04_ice_cream_interior with dissolve:
            subpixel True xzoom 1.18 zoom 1.64
    elif rngint == 1:
        scene ch04_ice_cream_interior2 with dissolve:
            subpixel True xzoom 1.15 zoom 2.38 
    show matt2:
        subpixel True pos (-314, 160) zoom 0.75
        linear 0.345 subpixel True pos (847, 160) zoom 0.75
    return
#TODO: Add a lot more visual flair to each and every event so they are prime neeto
label chapter_four_work_events():
    label ch04_event_1:
        call chapter_four_random_background()
        show thanga2 with dissolve:
            subpixel True pos (1331, 166) zoom 1.17 yrotate 180.0 
        mt "THANG!"
        show matt2:
            linear 0.345 subpixel True xpos 559 
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
        $ event_1.complete()
    label ch04_event_2:
        call chapter_four_random_background()
        show kody with dissolve:
            subpixel True pos (1185, 290) zoom 1.21 yrotate 180.0
        show matt2:
            linear 0.3 subpixel True xpos 550 
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
        $ event_2.complete()
    label ch04_event_3:
        call chapter_four_random_background()
        mt "oh god I wonder who is gonna come in next"
        show ch04_toni with dissolve:
            subpixel True crop_relative True pos (1920, 27) zoom 0.9 crop (0.0, -0.07, 1.0, 1.0) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yrotate 180.0 
            linear 0.45 subpixel True xpos 1110 
        toni "yooooooo matt"
        toni "what is up my f#gg0t!"
        show matt2:
            linear 0.3 subpixel True xpos 550 
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
        $ event_3.complete()
    label ch04_event_4:
        call chapter_four_random_background()
        mt "oh god I wonder who is gonna come in next"
        show ch04_toni with dissolve:
            subpixel True crop_relative True pos (1920, 27) zoom 0.9 crop (0.0, -0.07, 1.0, 1.0) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yrotate 180.0 
            linear 0.45 subpixel True xpos 1110
        call auto_advance(1)
        toni "YO WHAT IS GOOD MY NI-"
        show matt2:
            linear 0.24 subpixel True pos (573, 153) 
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
        $ event_4.complete()
    label ch04_event_5:
        call chapter_four_random_background()
        show matt2:
            linear 0.3 subpixel True xpos 550 
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
        $ event_5.complete()
    label ch04_event_6:
        call chapter_four_random_background()
        mt "I Should start doing my math homework..."
        mt "since brian is going to be forcing me to DO THE WHOLE SHIFT BY MY FUCKING SELF"
        mt "might as well do some math problems :)"
        mt "hmmm what did Mr Maths give me for today..."
        mt "100 CALCULUS PROBLEMS?"
        mt "ugh lets start this"
        mt "Find the Derivative of e^2x..."
        mt "IDK THIS?!?"
        mt "YO NARRATOR YOU KNOW THIS SHIT"
        "I'm Just reading the book man"
        "I can guess though"
        menu:
            "2e^2x":
                $ resource_manager.food_up_level_up(5,5)
            "e^x":
                $ resource_manager.food_down_level_down(1,1)
            "e^2x":
                $ resource_manager.food_down_level_down(1,1)
            "(e^x / 2)":
                $ resource_manager.food_down_level_down(4,4)
            "e^x^2":
                $ resource_manager.food_down_level_down(5,5)
            "4e":
                $ resource_manager.food_down_level_down(10,10)
        mt "Dang that was a hard problem..."
        mt "I wish I could just be like Kody and just have ez math problems"
        "You mean like a super senior?"
        mt "yeah I will have all day to myself"
        mt "me and my goon day"
        mt "...."
        mt "wait."
        mt "I WANNA BE LIKE KODY?!?"
        mt "oh god"
        questionmark "IS SOMEONE DOING MATH?"
        show baldi1:
            subpixel True pos (-612, 126) 
            linear 0.345 subpixel True pos (243, 126) 
        show matt2:
            linear 0.345 subpixel True xpos 1162 
        $ renpy.pause(hard = True, delay = 0.4)
        baldi "ITS ME!"
        mt "who?"
        baldi "TIME TO TEACH EVERYBODY'S FAVORITE SUBJECT!"
        baldi "MATH!"
        mt "are you MR MATH?"
        baldi "My name Is Baldi!"
        baldi "Welcome to My SCHOOL HOUSE!"
        mt "but its my school house..."
        mt "wait this isn't even a schoolhouse"
        mt "thsi is an ice cream store"
        scene baldi_q1 with dissolve:
            subpixel True pos (-333, -0.26) 
        baldi "What is 120 - 91?"
        $ choice = renpy.input("What is 120-91?", length = 10)
        if choice != "29":
            play sound "audio/sound/chapter_one/glock_magchange.ogg"
            show baldi_q1:
                subpixel True pos (-333, -0.26) blur 7.82 
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
                subpixel True pos (-333, -0.26) blur 7.82 
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
                subpixel True 
        baldi "Whats 9 + 10?"
        menu:
            "19":
                baldi "WOW THAT'S CRAZY!"
                baldi "SHIT TALK MATH AND YOU CAN'T EVEN DO IT?"
                baldi "DIE! YOU SHITTER!"
                show baldi_q3_mad:
                    subpixel True pos (-333, -0.26) blur 7.82 
                show baldi2:
                    subpixel True xpos 702
                show gun2:
                    subpixel True pos (361, 193)
                show gunflare:
                    subpixel True
                $ baldi_shoot(25)
                jump game_over
            "21":
                pass
        scene baldi_q3_happy with dissolve:
            subpixel True pos (-333, -0.26)
        baldi "I guess you do know a thing or two about math!"
        scene ch04_ice_cream_interior2 with dissolve:
            subpixel True xzoom 1.15 zoom 2.38 
        show baldi1:
            subpixel True pos (243, 126) 
        show matt2:
            subpixel True pos (1180, 130) zoom 0.74 
        mt "WHAT WAS THE FUCKING POINT TO THAT"
        baldi "idk man"
        mt "GET THE FUCK OUT OF HERE"
        baldi "okay :("
        show baldi1:
            linear 0.5 subpixel True xpos 1701 
        $ renpy.pause(0.5, hard = True)
        mt "WHAT A FUCKING DICKHEAD BRO!"
        $ event_6.complete()
    label ch04_event_7:
        call chapter_four_random_background()
        mt "Can't wait for another annoying prick"
        window auto hide
        show march_7th:
            subpixel True pos (1947, 211) zoom 0.24 
            linear 0.345 subpixel True pos (1128, 211) zoom 0.24 
        pause 0.345
        mt "wtf"
        mt "fuck you doing here"
        show matt2:
            linear 0.4 subpixel True xpos 568 
        march "boba :)"
        mt "this is an ice cream store..."
        march "idgaf"
        mt "I HATE ALL OF YOU FUCKERS"
        window auto hide
        show ch04_boba_tea:
            subpixel True pos (733, 496) zoom 0.15 
            linear 0.123 subpixel True pos (1173, 186) zoom 0.15 
        $ resource_manager.food_down_level_up(3, 4)
        pause 0.2
        hide ch04_boba_tea
        mt "that all?"
        march "no :)"
        mt "I would normally do more for my wife but im pissed and peaved right now"
        march ":("
        march "ill go"
        march "Have a good day matt"
        window auto hide
        show march_7th:
            linear 0.2 subpixel True xpos 1902
        $ renpy.pause(0.2, hard = True)
        mt "WAIT"
        mt "MARCH I CAN HELP MORE"
        window auto hide
        show march_7th:
            linear 0.3 subpixel True xpos 1038 
        pause 0.3
        mt "what did you even need?"
        march "mmmmm"
        march "well I need some new arrows for my bow"
        march "I need some snacks for stelle"
        march "I need some tea for daniel"
        menu:
            "'Idgaf'":
                mt "honestly"
                mt "i dont give a fucking or flying fuck"
                "thats idgafoff"
                mt "idgaf"
                march "WOWWWWWWWWWWWWWWWWWWWWW"
                march "well fuck you too bitch"
                show march_7th:
                    linear 0.3 subpixel True xpos 1911 
                mt "jesus"
                show march_7th:
                    linear 0.4 subpixel True xpos 1623
                march "AND IM LEAVING A BAD REVIEW"
                show ch04_doritos:
                    subpixel True pos (1501, 375) zoom 0.43 
                march "AND IM TAKING THESE DORITOS"
                mt "I DONT CARE"
                march "FUCK YOU"
                mt "FUCK YOU"
                window auto hide
                show march_7th:
                    linear 0.3 subpixel True pos (1971, 228) 
                show ch04_doritos:
                    linear 0.3 subpixel True pos (1921, 393) zoom 0.43 
                $ renpy.pause(0.4, hard = True)
                mt "jesus"
                $ resource_manager.food_down_level_down(3,5)
            "Help Her":
                march "WAIT YOU HAVE ALL I NEEDED?"
                mt "yes yes yes"
                march "FOR REAL?"
                mt "yes..."
                march "well where is it?"
                show ch03_giftbox with dissolve:
                    subpixel True pos (635, 510) zoom 0.54 
                mt "its all in this birthday box"
                march "GIMMIE GIMMIE"
                window auto hide
                show ch03_giftbox:
                    linear 0.4 subpixel True pos (970, 361) zoom 0.54 
                pause 0.4 
                march "YAY THANKS SO MUCH"
                hide ch03_giftbox
                march "I AM GOING TO LEAVE A GOOD YELP REVIEW"
                window auto hide
                show march_7th:
                    linear 0.5 subpixel True xpos 1920 
                pause 0.5
                mt "what a fucking bitch jesus"
                mt "can't believe she fell for that..."
                $ resource_manager.food_down_level_up(10,12)
        mt "thank god shes gone"
        mt "WHO EVER WROTE THIS IM OVER HERE YOU FUCKER"
        "lol"
        $ event_7.complete()
    label ch04_event_8:
        call chapter_four_random_background()
        mt "So who even called for the order"
        mt "order 8..."
        mt "WAIT"
        "what"
        mt "DON'T DO THE OBVIOUS JOKE"
        window auto hide
        show ch04_ocho with dissolve:
            subpixel True xpos 1899 yrotate 180.0 
            linear 0.5 subpixel True xpos 9 yrotate 180.0 
        $ renpy.pause(0.5, hard = True)
        mt "AH"
        mt "WHY ARE YOU SO BIGGGGGGGGGGGGGGGGGG"
        "Thats what she said"
        mt "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
        mt "WHAT DO YOU WANT OCHO"
        ocho "food"
        mt "WHATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
        mt "YOU CAN TALK NOW?"
        ocho "bark"
        mt "NAH YOU AIN'T PULLING THIS SHIT ON ME"
        ocho "I'm here to give food :)"
        mt "YOOOOOOOOOOOOOOOO IM GETTING MATS?"
        window auto hide
        show ch04_ice_cream_supplies with dissolve:
            subpixel True pos (310, 643) zoom 0.33 
            linear 0.4 subpixel True pos (936, 338) zoom 0.33
        $ renpy.pause(0.5, hard= True)
        mt "wtf"
        ocho "My people need me"
        ocho "good bye mathew soya125 beans man"
        window auto hide
        show ch04_ocho:
            yrotate 0.0 
            linear 0.3 subpixel True xpos 2088 
        pause 0.31
        mt "wtf"
        mt "did my dog just get me fortnite mats?"
        "I guess so?"
        mt "im not even gonna question this anymore"
        "You have received max food supplies!"
        $ food.set_level(100)
        mt "pretty sweet"
        $ event_8.complete()
    label ch04_event_9:
        call chapter_four_random_background()
        mt "oh god"
        camera:
            linear 1.0 subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(9.15)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        mt "my head really hurts badly..."
        mt "I feel like I'm about to be annoyed"
        mt "IS TRIP COMING IN?!?"
        questionmark "OH I LOVE ICE CREAM"
        mt "that isn't trip"
        window auto hide
        show ch04_fishy_boopkins:
            subpixel True pos (1928, 261) zoom 0.64 yrotate 180.0 
            linear 0.6 subpixel True pos (1019, 261) zoom 0.64 yrotate 180.0 
        $ renpy.pause(0.6, hard = True)
        mt "who"
        mt "THE FUCK ARE YOU????????????????????"
        questionmark "They call me"
        boopkins "FISHY BOOPKINS : D"
        mt "what"
        $ reset_camera(0.5)
        mt "oh good my headache cleared..."
        camera:
            linear 5.0 subpixel True alpha 1.0 additive 0.09 matrixcolor InvertMatrix(0.0)*ContrastMatrix(9.29)*SaturationMatrix(9.27)*BrightnessMatrix(-0.47)*HueMatrix(0.0) 
        mt "nevermind"
        mt "this is like stage 5 terminal cancer..."
        mt "get away from me you creature"
        show matt2:
            linear 0.345 subpixel True xpos 514 
        boopkins "why..."
        boopkins "I am just here for some food"
        call auto_advance(1)
        mt "make an order"
        mt "make"
        mt "it"
        mt "fast"
        mt "I dont wanna hear your voice"
        call auto_advance(0)
        mt "I never thought I'd find something more annoying than Thang and Brian's yapping"
        show ch04_bob:
            subpixel True xpos 1872 
            linear 0.4 subpixel True xpos 1206 
        pause 0.4
        bob "yo what is up my og top g boopkins"
        boopkins "HI BOB"
        mt "fuck off"
        camera:
            linear 1.0 subpixel True additive 0.0 matrixcolor InvertMatrix(0.29)*ContrastMatrix(13.37)*SaturationMatrix(12.64)*BrightnessMatrix(-0.51)*HueMatrix(-270.0) 
        mt "OH GOD I CAN'T HANDLE THIS"
        mt "I NEED TO FUCKING PUKE"
        show matt2:
            linear 0.189 subpixel True xpos 2116 
        pause 0.189
        scene ch04_ice_cream_exterior with dissolve:
            subpixel True xzoom 1.26 yzoom 1.09 
        show ch04_trash_can:
            subpixel True pos (1563, 515) zoom 0.39 
        show matt2:
            subpixel True
        window auto hide
        show matt2:
            subpixel True zoom 0.61 
            parallel:
                pos (428, 170) 
                linear 0.42 pos (1465, 240) 
                linear 0.31 pos (1145, 296) 
                linear 0.99 pos (1176, 165) 
            parallel:
                rotate 0.0 
                linear 0.73 rotate 45.0 
                linear 0.31 rotate -27.0 
                linear 0.13 rotate 108.0 
                linear 0.18 rotate -99.0 
                linear 0.09 rotate 63.0 
                linear 0.15 rotate -495.0 
                linear 0.13 rotate 0.0 
                linear 0.34 rotate -63.0 
                linear 0.09 rotate 126.0 
        with Pause(2.25)
        show matt2:
            pos (1176, 165) rotate 126.0 
        window auto show
        mt "oh my god" #TODO: Puking sfx here
        $ reset_camera(1.5)
        mt "okay im starting to feel a bit better."
        window auto hide
        show matt2:
            linear 0.23 subpixel True pos (948, 291) rotate 0.0 
        $ renpy.pause(0.23, hard = True)
        mt "well fuck"
        mt "idk what to do now"
        window auto hide
        show ch04_bob with dissolve:
            subpixel True zoom 0.83 yrotate 180.0 
            pos (6, 140) 
            linear 0.24 pos (21, 191) 
            linear 0.01 pos (26, 243) 
        show ch04_fishy_boopkins with dissolve:
            subpixel True zoom 0.53 
            pos (351, 350) 
            linear 0.24 pos (461, 465) 
            linear 0.01 pos (541, 525) 
        with Pause(0.35)
        show ch04_bob:
            pos (26, 243) 
        show ch04_fishy_boopkins:
            pos (541, 525) 
        window auto show
        bob "btw we robbed your store :)"
        bob "thanks for the mr beast bars and candy bars"
        window auto hide
        show ch04_bob:
            subpixel True 
            pos (26, 243) 
            linear 0.25 pos (1950, 251) 
        show ch04_fishy_boopkins:
            subpixel True 
            pos (541, 525) 
            linear 0.25 pos (2045, 443) 
        with Pause(0.35)
        show ch04_bob:
            pos (1950, 251) 
        show ch04_fishy_boopkins:
            pos (2045, 443) 
        window auto show
        mt "you fucking kidding me..."
        mt "ugh Idgaf anymore"
        $ resource_manager.food_down_level_down(10,5)
        bob "OH YEAH WE ALSO CLEANED YOUR STORE"
        bob "IM JUST A NICE CLEANER"
        boopkins "hey!"
        boopkins "That was me!"
        bob "shut up retard it was me im the rapper bob and i am the goat so stfu"
        mt "ugh"
        $ event_9.complete()
    label ch04_event_10:
        scene ch04_storeroom with dissolve:
            subpixel True xzoom 1.12 zoom 2.12 
        show matt2:
            subpixel True pos (-194, 220) zoom 0.66 
            linear 0.345 subpixel True pos (553, 220) zoom 0.66 
        $ renpy.pause(0.4, hard = True)
        mt "okay so I have to check the supplies"
        mt "apparently we are out of..."
        call auto_advance(1)
        window auto hide
        show matt2:
            subpixel True zoom 0.66 
            pos (553, 220) 
            linear 0.10 pos (683, 211) 
            linear 0.10 pos (1063, 230) 
            linear 0.20 pos (1415, 190) 
            linear 0.18 pos (1560, 216) 
            linear 0.15 pos (1400, 306) 
            linear 0.12 pos (1043, 306) 
            linear 0.14 pos (795, 341) 
            linear 0.19 pos (610, 330) 
            linear 0.18 pos (286, 331) 
            linear 0.17 pos (426, 163) 
            linear 0.11 pos (653, 123) 
            linear 0.11 pos (753, 116) 
            linear 0.13 pos (903, 165) 
            linear 0.11 pos (1006, 156) 
            linear 0.13 pos (1101, 131) 
            linear 0.10 pos (1658, 305) 
            linear 0.23 pos (1298, 353) 
            linear 0.12 pos (1078, 333) 
            linear 0.09 pos (813, 376) 
            linear 0.09 pos (645, 373) 
            linear 0.12 pos (433, 333) 
            repeat
        window auto show
        mt "milk"
        mt "eggs"
        mt "cream"
        mt "ice"
        mt "strawberry"
        mt "milk"
        mt "flour"
        mt "baking powder"
        call auto_advance(0)
        mt "HUH?"
        show matt2:
            subpixel True
        mt "HOW ARE WE OUT OF EVERY FUCKING SUPPLY"
        mt "ugh guess I gotta buy mats..."
        window auto hide
        show matt2:
            linear 0.5 subpixel True pos (-215, 236) 
        pause 0.4
        scene ch04_street2 with dissolve:
            subpixel True zoom 1.51 
        show matt2:
            subpixel True pos (928, 185) zoom 0.55 crop_relative True crop (0.0, 0.0, 1.0, 0.7) 
        show car1:
            subpixel True pos (521, 238) zoom 1.3 
        mt "I better get some good gas mileage and grocery bill recovery"
        mt "brian better pay up"
        window auto hide
        show matt2:
            crop_relative True crop (0.0, 0.0, 1.0, 0.7) 
            linear 0.45 subpixel True pos (875, -63) zoom 1.34 
        show car1:
            linear 0.45 subpixel True pos (51, -18) zoom 2.84 
        pause 0.45
        mt "damn I look good"
        "nah"
        mt "fuck you"
        scene ch04_walmart with dissolve:
            subpixel True zoom 1.62 
        show matt2:
            subpixel True pos (-258, 393) zoom 0.61 
            linear 0.345 subpixel True xpos 552 
        pause 0.345
        mt "I fucking hate walmart"
        mt "this is the black people store"
        "YOU CAN'T SAY THAT!!!!!!!!!!!!!!!!!!!!!!!1"
        mt "fuckkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
        mt "its the ghetto white people store"
        "yeah thats fine"
        "we can make fun of white people and not black people"
        mt ":ThumbsUp:"
        show matt2:
            linear .345 subpixel True pos (1013, 711) zoom 0.2 
        pause 0.345
        
        mt "alright so I got..."
        mt "damn"
        "how much you got?"
        mt "I got like $[money.get_level()].99"
        mt "alright what do I need..."
        label ch04_walmart_main: #TODO: Implement an rng op that appears kinda like playing with fire
        scene ch04_walmart_inside_main with dissolve:
            subpixel True xzoom 1.21 
        $ randint = renpy.random.randint(1,20)
        if randint == 7:
            jump ch04_walmart_death
        menu:
            "ICE":
                jump ch04_walmart_ice
            "Sugar":
                jump ch04_walmart_sugar
            "Eggs":
                jump ch04_walmart_eggs
            "Chocolate":
                jump ch04_walmart_chocolate
            "Baking Powder & Soda":
                jump ch04_walmart_baking
            "Leave Walmart":
                jump ch04_post_walmart
        label ch04_walmart_ice:
            scene ch04_walmart_ice with dissolve:
                subpixel True xzoom 1.33 zoom 1.43 
            show matt2 with moveinright:
                subpixel True pos (1150, 268) zoom 1.91 
            mt "alright so according to this manifesto"
            $ randint2 = renpy.random.randint(1,5)
            mt "The Ice costs $[randint2 - 0.50]"
            mt "now if I wanna pay that price for this..."
            menu:
                "Pay":
                    $ money.minus(randint2 - 0.50)
                    $ food.plus(10)
                "Leave":
                    "Maybe if we come back later, the price will be better..."
                    mt "yeah true"
            $ randint2 = renpy.random.randint(1,100)
            jump ch04_walmart_main
        label ch04_walmart_sugar:
            scene ch04_walmart_sugar with dissolve:
                subpixel True xzoom 1.21 
            show matt2 with moveinleft:
                subpixel True
            mt "alright so according to this manifesto"
            $ randint2 = renpy.random.randint(4,6)
            mt "The Sugar costs $[randint2 - 1.50]"
            mt "now if I wanna pay that price for this..."
            menu:
                "Pay":
                    $ money.minus(randint2 - 1.50)
                    $ food.plus(20)
                "Leave":
                    "Maybe if we come back later, the price will be better..."
                    mt "yeah true"
            $ randint2 = renpy.random.randint(1,100)
            jump ch04_walmart_main
        label ch04_walmart_eggs:
            scene ch04_walmart_eggs with dissolve:
                subpixel True xzoom 1.2 
            show matt2 with moveinleft:
                subpixel True
            mt "alright so according to this manifesto"
            $ randint2 = renpy.random.randint(1,3)
            mt "The eggs costs $[randint2 + 1.50]"
            mt "now if I wanna pay that price for this..."
            menu:
                "Pay":
                    $ money.minus(randint2 + 1.50)
                    $ food.plus(7 + randint2)
                "Leave":
                    "Maybe if we come back later, the price will be better..."
                    mt "yeah true"
            $ randint2 = renpy.random.randint(1,100)
            jump ch04_walmart_main
        label ch04_walmart_chocolate:
            scene ch04_walmart_chocolate with dissolve:
                subpixel True zoom 1.53 
            show matt2 with moveinright:
                subpixel True xpos 1485 
            mt "alright so according to this manifesto"
            $ randint2 = renpy.random.randint(10,12)
            mt "The chocolate costs $[randint2 - 4]"
            mt "damn"
            mt "now if I wanna pay that price for this..."
            menu:
                "Pay":
                    $ money.minus(randint2 - 4)
                    $ food.plus(30 - randint2)
                "Leave":
                    "Maybe if we come back later, the price will be better..."
                    mt "yeah true"
            $ randint2 = renpy.random.randint(1,100)
            jump ch04_walmart_main
        label ch04_walmart_baking:
            scene ch04_walmart_baking with dissolve:
                subpixel True xzoom 1.38 zoom 1.82 
            show matt2 with moveinright:
                subpixel True xpos 1485 
            mt "alright so according to this manifesto"
            $ randint2 = renpy.random.randint(2,4)
            mt "The baking ingredient costs $[randint2 * 2 + 1]"
            mt "damn"
            mt "now if I wanna pay that price for this..."
            menu:
                "Pay":
                    $ money.minus(randint2 * 2 + 1)
                    $ food.plus(12 - randint2)
                "Leave":
                    "Maybe if we come back later, the price will be better..."
                    mt "yeah true"
            $ randint2 = renpy.random.randint(1,100)
            jump ch04_walmart_main
        label ch04_walmart_death:
            show ch04_toon_link with dissolve:
                subpixel True xpos 432 
            mt "WHATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
            toonlink "yo you iz that nigga I met online"
            mt "YOU AREN'T EVEN BLACK YOU CANNOT SAY THAT"
            toonlink "I DONT GIVE A FLYING FUCK NIGAAAAAAAAAAAAAAAAAAAAAAAAAA!"
            mt "you are a loser"
            show gun2:
                subpixel True pos (296, 526) 
            mt "fuck"
            toonlink "I want it all!"
            menu:
                "Give ALL Food":
                    $ food.set_level(0)
                    toonlink "thanks fucker"
                    mt "no problem sir"
                    hide ch04_toon_link with dissolve
                    mt "what a shithole..."
                    mt "let's get out of here..."
                    "yeah..."
                    $ event_10.complete()
                "Give ALL Money":
                    $ money.set_level(0)
                    toonlink "thanks for the bread you idiot"
                    mt "got it sir man thing!"
                    hide ch04_toon_link with dissolve
                    mt "what a dick"
                    mt "let's get out of here..."
                    $ event_10.complete()
                "Attempt to Negoiate":
                    $ rngint = renpy.random.randint(1,4)
                    mt "listen man"
                    mt "I need some of this since its for work"
                    $ money_value = int(money.get_level() / 4)
                    mt "best I can give you is $[money_value]"
                    mt "that good man?"
                    if rngint == 2:
                        toonlink "NAH YOU FUCKER LATER BOZO"
                        show gunflare:
                            subpixel True pos (-78, 328) 
                        $ fnaf_shoot(20)
                        jump game_over
                    toonlink "eh I will take it"
                    toonlink "I only need cash for some snacks"
                    "Toon Link Takes Your Deal!"
                    $ food.minus(money_value)
                    toonlink "see ya man"
                    hide ch04_toon_link with dissolve
                    mt "ugh atleast I didn't get fully robbed"
                    mt "let's get out of here"
                    $ event_10.complete()
                "Don't Give anything":
                    mt "NAH I AINT GIVING SHIT"
                    toonlink "okay man"
                    toonlink "makes it easier for me"
                    show gunflare:
                            subpixel True pos (-78, 328) 
                    $ fnaf_shoot(20)
                    jump game_over

        label ch04_post_walmart:
            mt "alright I got all I wanted"
            "I feel like you coulda haggled for a bit more"
            mt "yeah maybe but the walmart crowd is super ghetto so ima just dip from that shit"
            "fair I guess"
            "You are the protagonist rn"
            mt "YESSSSSSSSSSSSSSSSSSSSSSS"
            mt "wait rn?"
            "dont worry about it"
            mt "ok"
        $ event_10.complete()
    label ch04_event_11:
