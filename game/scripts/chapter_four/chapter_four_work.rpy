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










label chapter_four_work_events():
    label ch04_event_1:
        "test"