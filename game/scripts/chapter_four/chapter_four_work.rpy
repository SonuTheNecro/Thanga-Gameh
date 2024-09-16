# Code for the Work Section of Chapter Four
default chapter_four_work_event_check = [False, False,]
init python:
    class Resource:
        level = 0
        def __init__(self, name, level = None):
            self.name = name
            self.level = level
        def get_name(self):
            return self.name
    
        def get_level(self):
            return self.level
        def set_level(self, new_level : int):
            self.level = new_level
        def level_minus(self):
            self.level -= 1
        def level_plus(self):
            self.level += 1
    class ResourceHandler:
        def __init__(self):
            self.resources = {}
            
        def add_resource(self, added_resource : Resource):
            self.resources[added_resource.get_name()] = added_resource
        
        def set_all_levels(self, new_level: int):
            for resource in self.resources.values():
                cases = {
                    -1 :  resource.level_minus,
                    101 : resource.level_plus
                }
                try:
                    cases[new_level]()
                except:
                    resource.set_level(new_level)
        def get_total_levels(self):
            total = 0
            for resource in self.resources.values():
                total += resource.get_level()
            return total
        def print_all(self):
            for resource in self.resources.values():
                print(str(resource.get_name()) + ":" + str(resource.get_level()))

label chapter_four_hide_office:
    hide screen clickable_chapter_four_register
    return

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
    #$ rngint = renpy.random.randint(0,5)
    $ rngint = 1
    if chapter_four_work_event_check[rngint - 1]:
        jump chapter_four_random_work
    call chapter_four_hide_office
    jump expression "ch04_event_" + str(rngint)

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
                $ customer_enjoyment += 5
            "Caseoh Creampies":
                $ customer_enjoyment += 5
            "Kai Cenat Cookies":
                $ customer_enjoyment += 5
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
