# coding=utf-8
import subprocess

from core import HackingTool
from core import HackingToolsCollection
from core import validate_input


class StegoCracker(HackingTool):
    TITLE = "StegoCracker"
    DESCRIPTION = "StegoCracker is a tool that let's you hide data into image or audio files and can retrieve from a file " 
                  
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/W1LDN16H7/StegoCracker.git",
        "sudo chmod -R 755 StegoCracker"
    ]
    RUN_COMMANDS = ["cd StegoCracker && python3 -m pip install -r requirements.txt ",
                   "./install.sh"
    ]
    PROJECT_URL = "https://github.com/W1LDN16H7/StegoCracker"
    

class Whitespace(HackingTool):
    TITLE = "Whitespace"
    DESCRIPTION = "Use whitespace and unicode chars for steganography"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/beardog108/snow10.git",
        "sudo chmod -R 755 snow10"
    ]
    RUN_COMMANDS = ["cd snow10 && ./install.sh"]
    PROJECT_URL = "https://github.com/beardog108/snow10"


class SteganographyTools(HackingToolsCollection):
    TITLE = "Steganograhy tools"
    TOOLS = [
        StegoCracker(),
        Whitespace()
    ]
