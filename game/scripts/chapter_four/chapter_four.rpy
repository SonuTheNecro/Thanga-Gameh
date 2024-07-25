
define trip = Character("Trip")
define maan = Character("Maan")
define d = Character("Dante")
define c = Character("Carl")



label chapter_four:
    "Chapter Four"
    "The Steve Disease"
    if persistent.ch04:
        $ config.rollback_enabled = True