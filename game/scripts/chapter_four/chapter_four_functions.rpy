# Code for the functions in Chapter Four


init python:
    from random import randint
    from enum import Enum
    class Event:
        nid : int
        diff : int
        desc : str
        def __init__(self, nid : int, diff : int, desc : str):
            self.nid = nid
            self.diff = diff
            self.desc = desc
        def get_id(self):
            return self.nid
        def get_diff(self):
            return self.diff
        def get_desc(self):
            return self.desc

        def complete(self):
            #setattr(renpy.store, 'chapter_four_work_event_check[self.get_id() - 1]', True)
            chapter_four_work_event_check[self.get_id() - 1] = True
            work_events.plus(1)
            renpy.jump("chapter_four_office")
        def print_info(self):
            return f"Event {self.get_id()}: Difficulty {self.get_diff()}\n Desc: {self.get_desc()}"
    class EventHandler:
        def __init__(self):
            self.events = {}
        def add_event(self, added_event : Event):
            self.events[added_event.get_id()] = added_event
        def pick_three_events(self, lower_limit : int, upper_limit : int):
            while True:
                rngint = random.randint(lower_limit, upper_limit)
                if not chapter_four_work_event_check[rngint - 1]:
                    break
            while True:
                rngint1 = random.randint(lower_limit, upper_limit)
                if not chapter_four_work_event_check[rngint1 - 1]:
                    break
            while True:
                rngint2 = random.randint(lower_limit, upper_limit)
                if not chapter_four_work_event_check[rngint2 - 1]:
                    break
            check = renpy.display_menu([(self.events[rngint].print_info(),  self.events[rngint].get_id()), 
                                        (self.events[rngint1].print_info(), self.events[rngint1].get_id()),
                                        (self.events[rngint2].print_info(), self.events[rngint2].get_id())])
            renpy.jump(f"ch04_event_{check}")

    # A Resource is essentially an int with a string
    class Resource:
        level = 0
        def __init__(self, name, level = None):
            self.name = name
            self.level = level
        # getters and setters
        def get_name(self):
            return self.name
        def get_level(self):
            return self.level
        def set_level(self, new_level : int):
            self.level = new_level
        def decrement(self):
            self.level -= 1
        def increment(self):
            self.level += 1
        def plus(self, add):
            self.level += add
        def minus(self, sub):
            self.level -= sub
    # Handles All resources with a dictionary
    class ResourceHandler:
        def __init__(self):
            self.resources = {}
        # Adds a resource to the list
        def add_resource(self, added_resource : Resource):
            self.resources[added_resource.get_name()] = added_resource
        # Control the levels for all resources
        def set_all_levels(self, new_level: int):
            for resource in self.resources.values():
                cases = {
                    -1 :  resource.decrement,
                    101 : resource.increment
                }
                try:
                    cases[new_level]()
                except:
                    resource.set_level(new_level)
        # Mostly for testing purposes
        def get_total_levels(self):
            total = 0
            for resource in self.resources.values():
                total += resource.get_level()
            return total
        def print_all(self):
            for resource in self.resources.values():
                print(str(resource.get_name()) + ":" + str(resource.get_level()))
        # This is kinda the default option since you lose food resources but gain customer happiness
        def food_down_level_up(self,nfood,nlevel):
            self.resources['food'].minus(nfood)
            self.resources['customer_enjoyment'].plus(nlevel)
        
        def food_up_level_up(self, nfood,nlevel):
            self.resources['food'].plus(nfood)
            self.resources['customer_enjoyment'].plus(nlevel)
        
        def food_down_level_down(self, nfood, nlevel):
            self.resources['food'].minus(nfood)
            self.resources['customer_enjoyment'].minus(nlevel)


label chapter_four_early_ending_1:
    #TODO: Clock speed effect
    #TODO: More Visual Flair + Longer
    scene ch04_lab with dissolve:
        subpixel True zoom 1.2 
    show matt2:
        subpixel True pos (-246, 146) zoom 0.79 
        linear 0.345 subpixel True pos (825, 146) zoom 0.79 
    pause 0.345
    "So why exactly are we here?"
    "In the High-School computer lab..."
    mt "I just wanna vent"
    mt "and no one's here"
    mt "*sigh*"
    "What happened?"
    mt "Trip is cancelling his match..."
    "Damn"
    mt "My life is over"
    "yeah probably"
    mt "I think we just missed something like idk man"
    "Perhaps in another life or run we can do that :/"
    $ renpy.quit()