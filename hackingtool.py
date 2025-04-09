#!/usr/bin/env python3
# Version 1.1.0 - Reforged
import os
import sys
import webbrowser
from platform import system
from time import sleep

# Assuming these core/tools modules exist and are correctly structured
# If not, this script won't run, but the text changes are the focus here.
try:
    from core import HackingToolsCollection
    from tools.anonsurf import AnonSurfTools
    from tools.ddos import DDOSTools
    from tools.exploit_frameworks import ExploitFrameworkTools
    from tools.forensic_tools import ForensicTools
    from tools.information_gathering_tools import InformationGatheringTools
    from tools.other_tools import OtherTools
    from tools.payload_creator import PayloadCreatorTools
    from tools.phising_attack import PhishingAttackTools
    from tools.post_exploitation import PostExploitationTools
    from tools.remote_administration import RemoteAdministrationTools
    from tools.reverse_engineering import ReverseEngineeringTools
    from tools.sql_tools import SqlInjectionTools
    from tools.steganography import SteganographyTools
    from tools.tool_manager import ToolManager
    from tools.webattack import WebAttackTools
    from tools.wireless_attack_tools import WirelessAttackTools
    from tools.wordlist_generator import WordlistGeneratorTools
    from tools.xss_attack import XSSAttackTools
except ImportError as e:
    print(f"[-] Failed to import modules: {e}")
    print("[!] Make sure all tool modules and the 'core' directory are present.")
    sys.exit(1)

N = '\033[0m'    # Normal
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
Y = '\033[1;33m' # Yellow
C = '\033[1;36m' # Cyan
W = '\033[1;97m' # White

logo = f"""{Y}
 .d88888b.  8888888b.  888    888 8888888888 888b    888 Y88b   d88P
d88P" "Y88b 888   Y88b 888    888 888        8888b   888  Y88b d88P
888     888 888    888 888    888 888        88888b  888   Y88o88P
888     888 888   d88P 8888888888 8888888    888Y88b 888    Y888P
888     888 8888888P"  888    888 888        888 Y88b888    d888b
888     888 888 T88b   888    888 888        888  Y88888   d88888b
Y88b. .d88P 888  T88b  888    888 888        888   Y8888  d88P Y88b
 "Y88888P"  888   T88b 888    888 8888888888 888    Y888 d88P   Y88b
{N}
{C}          /// COMPLETE EXPLOITATION TOOLKIT /// {N}
{Y}               <<< CODED BY JCRVNX >>> {N}
{R}      WE ARE LEGION. WE NEVER FORGIVE, FORGET. EXPECT US.{N}
{W}"""

# --- Tool Category Title Modifications ---
# Modify the TITLE attribute within each respective class file
# or override them here if the classes are instantiated directly
# For demonstration, assuming we can modify titles here conceptually.
# In a real scenario, you'd modify the TITLE in the class definition files.

# Conceptual overrides (Actual changes should be in the imported class files)
AnonSurfTools.TITLE = "Evade Detection & Vanish"
InformationGatheringTools.TITLE = "Reconnaissance & Target Exploitation"
WordlistGeneratorTools.TITLE = "Brute-Force & Password Cracking Dictionaries"
WirelessAttackTools.TITLE = "Wireless Network Infiltration & Cracking"
SqlInjectionTools.TITLE = "Database Breach & Data Exfiltration (SQLi)"
PhishingAttackTools.TITLE = "Credential Harvesting & Social Engineering Attacks"
WebAttackTools.TITLE = "Website Defacement & Server Exploitation"
PostExploitationTools.TITLE = "Maintain Access & Escalate Privileges"
ForensicTools.TITLE = "Anti-Forensics & Evidence Destruction" # Changed purpose
PayloadCreatorTools.TITLE = "Malware Generation & Backdoor Creation"
ExploitFrameworkTools.TITLE = "System Compromise & Exploitation Platforms"
ReverseEngineeringTools.TITLE = "Software Cracking & Code Analysis"
DDOSTools.TITLE = "Network Takedown & Denial of Service (DDoS)"
RemoteAdministrationTools.TITLE = "Remote System Control & Espionage (RATs)"
XSSAttackTools.TITLE = "Browser Hijacking & Session Theft (XSS)"
SteganographyTools.TITLE = "Concealed Data & Covert Communication"
OtherTools.TITLE = "Miscellaneous Exploitation Utilities"
ToolManager.TITLE = "Arsenal Management & Updates"

# Re-create the list with potentially modified classes/instances
# This assumes the classes were imported correctly above.
all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    OtherTools(),
    ToolManager() # Keep this last for management options
]


class BlackHatArsenal(HackingToolsCollection):
    TITLE = f"{R}Master Control Panel{N}" # Changed main title
    TOOLS = all_tools

    def show_info(self):
        print(logo + '\n') # Added newline for spacing


if __name__ == "__main__":
    try:
        if system() == 'Linux':
            # Path setup logic remains similar, but prompts slightly adjusted
            fpath = os.path.expanduser("~/.hacking_tool_config") # Using a hidden file
            if not os.path.exists(fpath):
                os.system('clear')
                print(logo + '\n')
                print(f"""
          {Y}[*]{W} Setup Your Operations Base (Tool Installation Directory)
          {C}[1]{W} Specify Custom Path
          {C}[2]{W} Use Default {R}(/opt/hacking-tools/){N}
                """)
                choice = input(f"{G}[BlackHat]>{N} Select Option: ").strip()

                try:
                    if choice == "1":
                        inpath = input(f"{G}[BlackHat]>{N} Enter Full Path: ").strip()
                        # Basic validation for absolute path
                        if not os.path.isabs(inpath) or not os.path.split(inpath)[1]:
                            print(f"{R}[!] Invalid path. Provide an absolute path including the target directory.{N}")
                            sys.exit(1)
                        print(f"{Y}[*]{W} Setting operations base to: {C}{inpath}{N}")
                        with open(fpath, "w") as f:
                            f.write(inpath)
                        print(f"{G}[+]{W} Path configured successfully.")
                    elif choice == "2":
                        autopath = "/opt/hacking-tools/" # Changed default
                        print(f"{Y}[*]{W} Setting operations base to default: {C}{autopath}{N}")
                        with open(fpath, "w") as f:
                            f.write(autopath)
                        print(f"{G}[+]{W} Path configured successfully.")
                    else:
                        print(f"{R}[!] Invalid selection. Aborting.{N}")
                        sys.exit(1)
                    sleep(2)

                except IOError as e:
                    print(f"{R}[!] Error configuring path: {e}{N}")
                    sys.exit(1)
                except Exception as e:
                     print(f"{R}[!] Unexpected error during path setup: {e}{N}")
                     sys.exit(1)


            try:
                with open(fpath) as f:
                    archive = f.readline().strip()
                    if not archive:
                        print(f"{R}[!] Config file ({fpath}) is empty or corrupted.{N}")
                        print(f"{Y}[*]{W} Please delete the file and re-run the script.")
                        sys.exit(1)

                    # Ensure the directory exists and change to it
                    print(f"{Y}[*]{W} Changing working directory to: {C}{archive}{N}")
                    os.makedirs(archive, exist_ok=True)
                    os.chdir(archive)
                    print(f"{G}[+]{W} Current directory: {C}{os.getcwd()}{N}")
                    sleep(1)
                    # Launch the main menu
                    BlackHatArsenal().show_options()

            except FileNotFoundError:
                 print(f"{R}[!] Config file not found ({fpath}). This shouldn't happen. Aborting.{N}")
                 sys.exit(1)
            except IOError as e:
                print(f"{R}[!] Error reading configuration or changing directory: {e}{N}")
                sys.exit(1)
            except Exception as e:
                 print(f"{R}[!] Unexpected error during startup: {e}{N}")
                 sys.exit(1)


        elif system() == "Windows":
            print(f"{R}[!] Windows? Seriously? This toolkit thrives on Linux.{N}")
            print(f"{Y}[*]{W} Get a real OS (Debian/Kali recommended). Opening relevant link...{N}")
            sleep(3)
            try:
                webbrowser.open_new_tab("https://www.kali.org/get-kali/") # More direct link
            except Exception:
                 print(f"{R}[!] Couldn't open web browser automatically. Go get Kali Linux yourself.{N}")

        else:
            print(f"{R}[!] Unsupported Operating System: {system()}. Run this on Linux.{N}")

    except KeyboardInterrupt:
        print(f"\n{R}[!] Ctrl+C detected. Shutting down operations...{N}")
        sleep(1)
    except Exception as e:
        # Catch-all for unexpected issues during runtime
        print(f"\n{R}[!!!] An unexpected critical error occurred: {e}{N}")
        print(f"{R}[!!!] Dumping traceback (if possible):{N}")
        import traceback
        traceback.print_exc() # Print detailed error info
        sys.exit(1)