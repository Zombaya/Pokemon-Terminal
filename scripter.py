# Used for creating, running and analyzing applescript and bash scripts.

import os
import sys
from Terminals.Terminology import Terminology

cwd = os.path.dirname(os.path.realpath(__file__))

class Scripter:
    __terminal = None
    __wallpaper = None

    def __init__(self):
        self.__terminal = self.__get_terminal()
        #__wallpaper = self.__get_wallpaper

    def __get_terminal(self):
        #print("Getting scripter")
        if sys.platform == "darwin":
            raise NotImplementedError('darwinTerminal not yet implemented') 
        if sys.platform == "linux":
            if os.environ.get("TERMINOLOGY") == '1':
                return Terminology()
            else:
                print("Terminal emulator not supported")
                exit(1)

    def __get_wallpaper(self):
            raise NotImplementedError('wallpaper not yet implemented') 

    def __terminal_script(path):
        # Create the content for script that will change the terminal background image.
        content = "tell application \"iTerm\"\n"
        content += "\ttell current session of current window\n"
        content += "\t\tset background image to \"" + path + "\"\n"
        content += "\tend tell\n"
        content += "end tell"
        return content


    def __wallpaper_script(pokemon):
        # Create the content for the script that will change the wallpaper.
        content = "tell application \"System Events\"\n"
        content += "\ttell current desktop\n"
        content += "\t\tset picture to \"" + pokemon.get_path() + "\"\n"
        content += "\tend tell\n"
        content += "end tell"
        return content


    def __iterm2_create_terminal_script(pokemon):
        # Create and save the script for changing the terminal background image.
        content = __terminal_script(pokemon.get_path())
        file = open(cwd + "/./Scripts/background.scpt", "wb")
        file.write(bytes(content, 'UTF-8'))
        file.close()


    def __iterm2_clear_script():
        # Create and save the script for clearing the terminal background image.
        content = __terminal_script("")
        file = open(cwd + "/./Scripts/background.scpt", "wb")
        file.write(bytes(content, 'UTF-8'))
        file.close()


    def __darwin_create_wallpaper_script(pokemon):
        # Create and save the script for changing the wallpaper.
        content = __wallpaper_script(pokemon)
        file = open(cwd + "/./Scripts/wallpaper.scpt", "wb")
        file.write(bytes(content, 'UTF-8'))
        file.close()


    def __darwin_create_terminal_bash():
        # Create and save the run.sh that will execute the AppleScript if the correct run.sh doesn't already exist.
        content = "#!/bin/bash\n" + "osascript " + cwd + "/./Scripts/background.scpt"
        if open(cwd + "/./Scripts/run.sh", 'r').read() == content:
            return
        file = open(cwd + "/./Scripts/run.sh", 'wb')
        file.write(bytes(content, 'UTF-8'))
        file.close()


    # Create and save the run.sh that will execute the AppleScript if the correct run.sh
    # doesn't already exist.
    def __darwin_create_wallpaper_bash():
        content = "#!/bin/bash\n" + "osascript " + cwd + "/./Scripts/wallpaper.scpt"
        if open(cwd + "/./Scripts/run.sh", 'r').read() == content:
            return
        file = open(cwd + "/./Scripts/run.sh", 'wb')
        file.write(bytes(content, 'UTF-8'))
        file.close()


    def change_terminal(self,pokemon):
        self.__terminal.change_terminal(pokemon)

    # Old way
    def change_wallpaper(self,pokemon):
        if sys.platform == "darwin":
            # Create, save and run the bash script to change the wallpaper.
            __darwin_create_wallpaper_script(pokemon)
            __darwin_create_wallpaper_bash()
            os.system(cwd + "/./Scripts/run.sh")
        if sys.platform == "linux":
            os.system(__linux_create_wallpaper_script(pokemon))


    def clear_terminal(self):
        self.__terminal.clear_terminal()

        #if sys.platform == "darwin":
        #    __iterm2_clear_script()
            # __darwin_create_terminal_bash()
            # os.system(cwd + "/./Scripts/run.sh")
        # if sys.platform == "linux":
            # os.system(__linux_clear_terminal())


    def __linux_create_wallpaper_script(pokemon):
        # If its gnome... aka GDMSESSION=gnome-xorg, etc.
        if os.environ.get("GDMSESSION").find("gnome") >= 0:
            return "gsettings set org.gnome.desktop.background picture-uri " + \
                "\"file://"+ pokemon.get_path()+"\""
        #elif condition of KDE...
        else:
            print("Window manager not supported ")
            exit(1)

    # Print the current Pokemon that is being used as the terminal background.
    def determine_terminal_pokemon(self,db):
        __image_name = self.__terminal.determine_terminal_pokemon()
        self.__determine_pokemon(db,__image_name)


    # Print the current Pokemon that is being used the wallpaper.
    def determine_wallpaper_pokemon(self,db):
        __determine_pokemon(db, "wallpaper.scpt")

    # Helper method to get the current Pokemon that is in the specified script.
    def __determine_pokemon(self,db, image_name):
        if image_name != None and type(image_name) == "string":
            pokemon = db.get_pokemon(image_name)
            print(pokemon.get_id(), pokemon.get_name().capitalize())
