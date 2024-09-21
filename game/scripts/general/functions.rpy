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
    config.keymap['hide_windows'].remove('mouseup_2')
    config.keymap['hide_windows'].remove('noshift_K_h')
    # returns the label of the game_over screen based on value
    def game_over_jump(value):
        return f"game_over_{value}"

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
    $ rngint = renpy.random.randint(1,2)
    #$ rngint = 2
    $ renpy.jump(game_over_jump(rngint))

label game_over_1:
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
    ice "amen america!"
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


label main_menu_code:
    label hide_clickable_menus:
        hide screen clickable_main_menu_ch00
        hide screen clickable_main_menu_ch01
        hide screen clickable_main_menu_ch02
        hide screen clickable_main_menu_ch03
        hide screen clickable_main_menu_ch04
        hide screen clickable_main_menu_question_screen1
        hide screen clickable_main_menu_question_screen2
        hide screen clickable_main_menu_question_screen3
        hide screen clickable_main_menu_question_screen4
        hide screen clickable_main_menu_question_screen5
        hide screen clickable_main_menu_trash_can
        hide screen clickable_main_menu_trophy
        hide screen clickable_main_menu_clock
        hide screen clickable_main_menu_minigames
        hide screen clickable_chapter_secret_one
        return
            
    label clickable_menus:
        screen clickable_main_menu_ch00:
            imagebutton:
                pos (140, 13) at Transform(zoom=0.62)
                idle "images/main_menu/chapter_zero_screen.png"
                hover "images/main_menu/chapter_zero_screen.png"
                action Jump("chapter_start0")
        screen clickable_main_menu_ch01:
            imagebutton:
                pos (768, 13) at Transform(zoom=0.62)
                idle "images/main_menu/chapter_one_screen.png"
                hover "images/main_menu/chapter_one_screen.png"
                action Jump("chapter_start1")
        screen clickable_main_menu_ch02:
            imagebutton:
                pos (1444, 13) at Transform(zoom=0.62)
                idle "images/main_menu/chapter_two_screen.png"
                hover "images/main_menu/chapter_two_screen.png"
                action Jump("chapter_start2")
        screen clickable_main_menu_ch03:
            imagebutton:
                pos (140, 541) at Transform(zoom=0.62)
                idle "images/main_menu/chapter_three_screen.png"
                hover "images/main_menu/chapter_three_screen.png"
                action Jump("chapter_start3")
        screen clickable_main_menu_ch04:
            imagebutton:
                pos (768, 541) at Transform(zoom=0.62)
                idle "images/main_menu/question_screen.png"
                hover "images/main_menu/question_screen.png"
                action Jump("chapter_start4")
        screen clickable_main_menu_question_screen1(xpos,ypos):
            imagebutton:
                pos (xpos, ypos) at Transform(zoom=0.62)
                idle "images/main_menu/question_screen.png"
                hover "images/main_menu/question_screen.png"
                action Jump("chapter_start_question")
        screen clickable_main_menu_question_screen2(xpos,ypos):
            imagebutton:
                pos (xpos, ypos) at Transform(zoom=0.62)
                idle "images/main_menu/question_screen.png"
                hover "images/main_menu/question_screen.png"
                action Jump("chapter_start_question")
        screen clickable_main_menu_question_screen3(xpos,ypos):
            imagebutton:
                pos (xpos, ypos) at Transform(zoom=0.62)
                idle "images/main_menu/question_screen.png"
                hover "images/main_menu/question_screen.png"
                action Jump("chapter_start_question")
        screen clickable_main_menu_question_screen4(xpos,ypos):
            imagebutton:
                pos (xpos, ypos) at Transform(zoom=0.62)
                idle "images/main_menu/question_screen.png"
                hover "images/main_menu/question_screen.png"
                action Jump("chapter_start_question")
        screen clickable_main_menu_question_screen5(xpos,ypos):
            imagebutton:
                pos (xpos, ypos) at Transform(zoom=0.62)
                idle "images/main_menu/question_screen.png"
                hover "images/main_menu/question_screen.png"
                action Jump("chapter_start_question")
        label chapter_start0():
            "Do you want to start the Prologue?"
            menu:
                "Yes":
                    call hide_clickable_menus
                    jump prologue
                "No":
                    jump main_menu_chapter_select
        label chapter_start1():
            "Do you want to start Chapter One?"
            menu:
                "Yes":
                    call hide_clickable_menus
                    jump chapter_one
                "No":
                    jump main_menu_chapter_select
        label chapter_start2():
            "Do you want to start Chapter Two?"
            menu:
                "Yes":
                    call hide_clickable_menus
                    jump chapter_two
                "No":
                    jump main_menu_chapter_select
        label chapter_start3():
            "Do you want to start the Chapter Three?"
            menu:
                "Yes":
                    call hide_clickable_menus
                    jump chapter_three
                "No":
                    jump main_menu_chapter_select
        label chapter_start4():
            "Do you want to start the Chapter Four?"
            menu:
                "Yes":
                    call hide_clickable_menus
                    jump chapter_four
                "No":
                    jump main_menu_chapter_select

        label chapter_start_question:
            "That chapter is currently locked/unavailable!"
            "Please select another chapter!"
            jump main_menu_chapter_select
        screen clickable_main_menu_trash_can:
            imagebutton:
                pos((0, 1020))
                idle "images/main_menu/main_menu_delete.png"
                hover "images/main_menu/main_menu_delete.png"
                action Jump("main_menu_delete")
        label main_menu_delete:
            "Do you want to delete all of your Save Data"
            "This includes your Chapter Completions, Secrets Found, and the player name!"
            "This is an IRREVERSIBLE ACTION!"
            "Would you like to continue?"
            menu:
                "Yes, delete my DATA":
                    $ check = "bloxwich"
                    $ reset_data()
                    jump main_menu_chapter_select
                "No, Don't Do That":
                    jump main_menu_chapter_select
                "Max Save File!":
                    $ persistent.ch00 = True
                    $ persistent.ch01 = True
                    $ persistent.ch02 = True
                    $ persistent.ch03 = True
                    $ persistent.ch04 = True
                    $ persistent.secret0 = True
                    $ persistent.secret1 = True
                    $ persistent.secret2 = True
                    $ persistent.secret3 = True
                    jump main_menu_chapter_select
        screen clickable_main_menu_trophy:
            imagebutton:
                pos(60,1020)
                idle "images/main_menu/main_menu_trophy.png"
                hover "images/main_menu/main_menu_trophy.png"
                action Jump("main_menu_stats")
        label main_menu_stats:
            if persistent.ch00:
                "Prologue has been Completed!"
                if persistent.secret0:
                    "Prologue's Secret has been Found!"
            if persistent.ch01:
                "Chapter One has been Completed!"
                if persistent.secret1:
                    "The secret of Kody has been Found!"
            if persistent.ch02:
                "Chapter two has been Completed!"
                if persistent.secret2:
                    "Chapter Two's Secret has been Found!"
            if persistent.ch03:
                "Chapter Three has been Completed!"
                if persistent.secret3:
                    "The SpringTrap has been Formed!"
            jump main_menu_chapter_select
        screen clickable_main_menu_clock:
            imagebutton:
                pos(0,960)
                idle "images/main_menu/main_menu_clock.png"
                hover "images/main_menu/main_menu_clock.png"
                action Jump("main_menu_playtime")
        label main_menu_playtime:
            $ persistent.play_time -= temp_playtime
            $ temp_playtime = renpy.get_game_runtime()
            $ persistent.play_time += temp_playtime
            $ hours = int(persistent.play_time // 3600)
            $ minutes = int((persistent.play_time % 3600) // 60)
            $ seconds = int(persistent.play_time % 60)
            $ formatted_time = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
            "Playtime: [formatted_time]"
            jump main_menu_chapter_select
        screen clickable_main_menu_minigames:
            imagebutton:
                pos(60,960)
                idle "images/main_menu/main_menu_minigames.png"
                hover "images/main_menu/main_menu_minigames.png"
                action Jump("main_menu_minigames")
        label main_menu_minigames:
            menu:
                "The Clash of Cody's Connundrum!":
                    jump minigame_rps
                "Baldi's Mathmatical Madness!":
                    jump minigame_math
                "Puppet's Paradoxical Predicament!":
                    jump minigame_puppet
                "debug":
                    jump debug_menu
                "Return to Main Menu":
                    jump main_menu_chapter_select

        screen clickable_chapter_secret_one:
            imagebutton:
                pos (549, 210)
                idle "images/main_menu/slender_man.png"
                hover At("images/main_menu/slender_man.png", animated_outline)
                action Jump("chapter_start_secret1")
        label chapter_start_secret1:
            "Do you want to start the Secret Chapter?"
            menu:
                "Yes":
                    call hide_clickable_menus
                    jump chapter_secret_one_start
                "No":
                    jump main_menu_chapter_select
        label debug_menu:
            call hide_clickable_menus
            menu:
                "Chapter Three Secret":
                    jump chapter_three_secret
                "Chapter One baldi_math_puzzle":
                    jump baldi_math_puzzle
                "chapter three post map":
                    jump chapter_three_post_map
                "chapter one ending":
                    jump baldi_beaten
                "Chapter Four Matt's House":
                    jump ch04_matt_area_1
                "Chapter_Four Act 2":
                    jump chapter_four_act_2
                "Chapter_Four_Office":
                    jump chapter_four_office
                "Chapter_Four_office_create":
                    jump chapter_four_setup_resources
                "chapter_three_chica_mission3":
                    jump chapter_three_chica_mission3
                "game_over":
                    jump game_over