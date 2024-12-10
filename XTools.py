import os

black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"

XTools = """
██╗░░██╗  ░░░░░░  ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
╚██╗██╔╝  ░░░░░░  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
░╚███╔╝░  █████╗  ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
░██╔██╗░  ╚════╝  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
██╔╝╚██╗  ░░░░░░  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
╚═╝░░╚═╝  ░░░░░░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
"""

Abox = """
=============================================================
* Simple Tools Decrypt : .nm / .tnl / .pb / .ziv /.hat /.pcx
* Default Path File NM : /sdcard/Download/Nekogram
* Coded By             : https://t.me/decrypt_files1
* Telegram             : https://t.me/decrypt_file
=============================================================\nChose Menu : 
"""



def menu():
    os.system('clear')
    print(red + XTools + cyan + Abox)
    print(" [1.] NetMod Syna")
    print(" [2.] OpenTunnel")
    print(" [3.] PB Injector")
    print(" [4.] ZIV VPN")
    print(" [5.] hat VPN")
    print(" [6.] pcx VPN")
    print(" [7.] nm VPN")
    print(" [8.] dark tnl") 
    print(" [0.] Exit Script")

    choice = input("\n Select Menu = ")
    return choice

def run_script_python(script_name):
    print("Please Wait !!!")
    os.system("python " + script_name)
    input("\n𝗣𝗿𝗲𝘀𝘀 𝗘𝗻𝘁𝗲𝗿 𝗧𝗼 𝗥𝗲𝘁𝘂𝗿𝗻 𝗧𝗼 𝗧𝗵𝗲 𝗠𝗲𝗻𝘂")
    
def run_script_nodejs(script_name):
    print("Please Wait !!!")
    os.system("node " + script_name)
    input("\n𝗣𝗿𝗲𝘀𝘀 𝗘𝗻𝘁𝗲𝗿 𝗧𝗼 𝗥𝗲𝘁𝘂𝗿𝗻 𝗧𝗼 𝗧𝗵𝗲 𝗠𝗲𝗻𝘂")


def main():
    while True:
        choice = menu()

        if choice == "1":
            run_script_python("X/NM.py")
        elif choice == "2":
            run_script_nodejs("X/OT.js")
        elif choice == "3":
            run_script_nodejs("X/PB.js")
        elif choice == "4":
            run_script_nodejs("X/ZIV.js")
        elif choice == "5":
            run_script_nodejs("X/hat.js")
        elif choice == "6":
            run_script_nodejs("X/pcx.js")
        elif choice == "7":
            run_script_nodejs("X/nm.js")
        elif choice == "8":
            run_script_nodejs("X/dark.js")
        elif choice == "0":
            os.system('clear')
            print("Script Has Ended. \nThank For Using This Module \n- BOOS DEV TEAM - \n")
            
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang valid.")

if __name__ == "__main__":
    main()
