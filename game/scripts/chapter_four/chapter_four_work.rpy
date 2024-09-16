# Code for the Work Section of Chapter Four

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
    call chapter_four_hide_office
    jump expression "ch04_event_" + str(rngint)

label chapter_four_work_events():
    label ch04_event_1:

        scene ch04_ice_cream_exterior with dissolve:
            subpixel True xzoom 1.26 yzoom 1.09 
        "test2"