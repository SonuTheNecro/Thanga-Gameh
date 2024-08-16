#Generic Functions intended to be used for the whole project

#Python Code
init python:
    import random
    from renpy.display import im
    from enum import Enum
    renpy.music.register_channel("sound2", "sound", loop = False) # second sound track for dual sound effects
    config.keymap['rollback'].remove('any_K_PAGEUP')
    config.keymap['rollback'].remove('any_KP_PAGEUP')
    config.keymap['rollback'].remove('K_AC_BACK')
    config.keymap['rollback'].remove('mousedown_4')
    config.keymap['screenshot'].remove('alt_K_s')
    config.keymap['screenshot'].remove('alt_shift_K_s')
    config.keymap['screenshot'].remove('noshift_K_s')
    config.keymap['inspector'].remove('alt_K_i')
    config.keymap['inspector'].remove('shift_K_i')
    config.keymap['full_inspector'].remove('alt_shift_K_i')

    #A confirm menu for important decisions, Paramater is the str for the menu label, jump decision is where you would go if you choose yes
    def confirm_menu_jump(original_menu, jump_decision):
        renpy.say(None, "This is an Important Decision that will affect your future gameplay, are you sure about this?")
        check = renpy.display_menu([("Yes", "yes"), ("No", "no")])
        if check == "yes":
            renpy.say(None, "Good luck on your decision")
            renpy.jump(str(jump_decision))
        else:
            renpy.say(None, "Good luck on your decision")
            renpy.jump(str(original_menu))
    
    #A confirm menu for important decisions, Paramater is the str for the menu label
    def confirm_menu_no_jump(original_menu):
        renpy.say(None, "This is an Important Decision that will affect your future gameplay, are you sure about this?")
        check = renpy.display_menu([("Yes", "yes"), ("No", "no")])
        if check == "no":
            renpy.say(None, "Good luck on your decision")
            renpy.jump(str(original_menu))
        else:
            renpy.say(None, "Good luck on your decision")
    
    # Deletes all data in the save file
    def reset_data():
        ## deletes all persistent data use with caution
        for attr in dir(persistent):
            if not callable(attr) and not attr.startswith("_"):
                setattr(persistent, attr, None)

        ## deletes all save games use with caution!
        for slot in renpy.list_saved_games(fast=True):
            renpy.unlink_save(slot)
        ## a Ren'Py relaunch is nessesary
        renpy.quit(relaunch=True)
    
    class ItemState(Enum):
        NOT_OBTAINED = 0
        OBTAINED = 1
    # Resets the camera and calls it on renpy code
    def reset_camera(speed: int):
        setattr(renpy.store, 'camera_speed', speed)
        renpy.call("camera_reset")
#Renpy Code
image blood_red = Solid("#790000")
image evil cody:
    glitch("cody")
    pause 0.15
    glitch("cody_evil", offset = 60, randomkey=None)
    pause 0.15
    glitch("cody_evil")
    pause 0.15
    glitch("cody_evil", offset = 60, randomkey=None)
    pause 0.15
    glitch("cody")
#A game over screen for general use, why is Master Igor shit talking so hard
label game_over:
    stop sound
    stop music
    play music "audio/music/prologue/aria_of_the_soul.ogg"
    scene velvet room with fade:
        subpixel True pos (-0.08, 0.0) yzoom 1.12 zoom 1.22 
    "You have fallen and lost thy life!"
    show igor with dissolve:
        subpixel True pos (0.21, 0.57) yoffset -585.0 xzoom 1.0 zoom 4.2
    igor "But honestly you suck at the game!"
    igor "Like how do you mess up these basic mechanics"
    igor "I got no legs and I coulda walked further and made it further than you you absolute shitter"
    igor "This is a baby-easy visual novel made for stupid people!"
    igor "play a real visual novel made for adults!"
    igor "You fucking suck, use some common sense"
    igor "Straight up bozo!"
    igor "Goodbye forever (Or not)"
    $ renpy.quit()
label game_over_2:
    stop sound
    stop music
    show black with fade
    play sound "audio/sound/general/police_siren.ogg" loop
    questionmark "You are under-arrest!"
    questionmark "President Cody's policy will NOT be disobeyed!"
    $ renpy.pause(1.0, hard = True)
    scene ice_game_over with fade:
        subpixel True
    show thanga2:
        subpixel True pos (870, 225) yrotate 180.0 
    show kody:
        subpixel True pos (931, 393) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    stop sound
    ice "You two will be spent far far away"
    ice "to your country of origin"
    ice "North Korea Pyongyang"
    camera:
        subpixel True pos (-1215, -387) zoom 2.19 
    t "WAIT WE ARENT KOREAN"
    t "WE ARE VIETNAMESE"
    $ reset_camera(0.1)
    ice "look like a korean to me"
    t "Bạn hút tinh ranh lớn"
    t "like that vietnamese?"
    ice "Tôi có thể nói tiếng Việt mà.  Tôi sẽ đảm bảo bạn sẽ đến Bắc Triều Tiên"
    t "shit"
    scene game_over_plane
    play sound "audio/sound/general/airplane_take_off.ogg"
    ice "another illegal immigrant out of our country!"
    $ renpy.quit()

label dio_time_stop():
    $ rngint = renpy.random.randint(0,1)
    if rngint == 0:
        play sound "audio/sound/general/dio1.ogg"
    else:
        play sound "audio/sound/general/dio2.ogg"
    return
label stab_blood_screen():
    window auto hide
    play sound "audio/sound/general/stab_die1.ogg"
    pause .4
    show blood_red at Transform(alpha = 0.5) with Dissolve(1.5)
    return
label gun_blood_screen():
    window auto hide
    play sound "audio/sound/general/gun_die1.ogg"
    pause .4
    show blood_red at Transform(alpha = 0.5) with Dissolve(1.5)
    return
# Code for auto advance as a Pseudo-Function, 1 = Starting it, 0 for Ending it
label auto_advance(value):
    if value == 1:
        $ _preferences.afm_enable = True
        $ _preferences.afm_time = 5
    elif value == 0:
        $ _preferences.afm_enable = False
        $ _preferences.afm_time = 15
    return
# Resets the camera to it's original position w/ original effects
label camera_reset():
    camera:
        linear camera_speed subpixel True pos (0,0) xzoom 1.0 yzoom 1.0 zoom 1.0 alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 


    return