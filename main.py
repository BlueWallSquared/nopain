from pystyle import *
from dhooks import Webhook
import colorama
colorama.init(autoreset=True)
print(Colorate.Vertical(Colors.yellow_to_red, """
                                          __          
                                         |  \\         
 _______   ______        ______   ______  \▓▓_______  
|       \\ /      \\      /      \\ |      \\|  \\       \\ 
| ▓▓▓▓▓▓▓\\  ▓▓▓▓▓▓\\    |  ▓▓▓▓▓▓\\ \\▓▓▓▓▓▓\\ ▓▓ ▓▓▓▓▓▓▓\\
| ▓▓  | ▓▓ ▓▓  | ▓▓    | ▓▓  | ▓▓/      ▓▓ ▓▓ ▓▓  | ▓▓
| ▓▓  | ▓▓ ▓▓__/ ▓▓    | ▓▓__/ ▓▓  ▓▓▓▓▓▓▓ ▓▓ ▓▓  | ▓▓
| ▓▓  | ▓▓\\▓▓    ▓▓    | ▓▓    ▓▓\\▓▓    ▓▓ ▓▓ ▓▓  | ▓▓
 \\▓▓   \\▓▓ \\▓▓▓▓▓▓     | ▓▓▓▓▓▓▓  \\▓▓▓▓▓▓▓\\▓▓\\▓▓   \\▓▓ youtube : BlueWall 
                       | ▓▓                            discord : BlueWall'H!PΣD#9376
                       | ▓▓                           
                        \\▓▓                           

""", 1))
def command(command_name: str, command_description: str):
    print(colorama.Fore.LIGHTCYAN_EX + command_name + colorama.Fore.BLUE + " > " + colorama.Fore.WHITE + command_description)


def main():
    res = input(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + "NPN" + colorama.Fore.BLUE + "]" + colorama.Fore.WHITE + " > ")
    if res.lower() == "help":
        print(colorama.Fore.BLUE + "All the commands" + colorama.Fore.RED + " > " + colorama.Fore.LIGHTCYAN_EX + "[] = obligatory {} = optional")
        command("quit", "Exit NoPain.")
        command("webhook","Different webhook utils. Usage : webhook [delete|spam|info] [url] {message}")
        main()
    elif res.split(" ")[0] == "webhook":
        hook = Webhook(res.split(" ")[2])
        hook.get_info()
        if res.split(" ")[1] == "info":
            print(f"- {colorama.Fore.CYAN}GUILD ID    : {colorama.Fore.WHITE}{hook.guild_id}")
            print(f"- {colorama.Fore.CYAN}CHANNEL ID  : {colorama.Fore.WHITE}{hook.channel_id}")
            print(f"- {colorama.Fore.CYAN}USERNAME    : {colorama.Fore.WHITE}{hook.default_name}")
            print(f"- {colorama.Fore.CYAN}IMAGE       : {colorama.Fore.WHITE}{hook.default_avatar_url}")
            main()
        elif res.split(" ")[1] == "delete":
            hook.delete()
            print(f"{colorama.Fore.RED} Successfully deleted webhook !")
            main()
        elif res.split(" ")[1] == "spam":
            i = 0
            while i <= 20:
                hook.send("Webhook got ruined by NoPain @everyone ! - BlueWall ("+ str(i) +"/20)")
                i+=1
            main()
        else:
            print("not info")
            main()
    elif res.lower().startswith("credits"):
        print(colorama.Fore.CYAN + "PyStyle "  + colorama.Fore.WHITE + "> " + colorama.Fore.RED + "billythegoat356, loTus01, and BlueRed (https://github.com/billythegoat356/pystyle)")
        print(colorama.Fore.CYAN + "DHooks " + colorama.Fore.WHITE + "> " + colorama.Fore.RED + "kyb3r (https://github.com/kyb3r/dhooks)")
        print(colorama.Fore.CYAN + "Colorama " + colorama.Fore.WHITE + "> " + colorama.Fore.RED + "Jonathan Hartley (https://github.com/tartley/colorama)")
        print(colorama.Fore.CYAN + "No Pain " + colorama.Fore.WHITE + "> " + colorama.Fore.RED + "BlueWall (BlueWall'H!PΣD#9376) ()")
        main()
    elif res.lower() == "quit":
        print("Quitting...")
    else:
        print("not working")
        main()

main()
