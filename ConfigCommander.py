import os, sys, logging, inquirer
from inquirer import questions

import python_inquirer
osinfo = sys.platform
from python_inquirer import *
from inquirer import *
#patch this up 


def BackupApps(path='/var/log/apt/history.log'):
    """
    This backs up apps. 
    """
    print("So just to be clear, this only backs up things that are installed via apt/yum/pkg. If you need stuff in other folders, try using rsync.")
    input("Please type what folders you want to have ")
    # try:
    #     if os.path.exists(path):
    #         sucesslist = []
    #         failist = []  
    #         read_data = []
    #         with open(path,'r') as f:
    #             for line in f:
    #                 read_data.append(line)
    #         f.close()
    #         #Close here of course 
    #         test = 'test forty five'
    #         for i in read_data:  
    #             if i.startswith('Command') and 'remove' not in i:
    #                 logging.info(f"Doing Line {i}")
    #                 try:
    #                     i = i.partition('install')[2]
    #                     sucesslist.append(i)
    #                     logging.info("%i sucessfully added",i)
    #                 except:
    #                     i = i.partition('get')[2]
    #                     sucesslist.append(i)
    #                     logging.info("%i sucessfully added",i)
    #             elif i.startswith('Commmand') and 'remove' in i:
    #                 sucesslist.remove(i)
    #         print("The Following Apps Have been backed Up: ")
    #         [print(i) for i in sucesslist]
    #         print("The Following Apps Have NOT been backed Up")
    #         [print(i) for i in failist]
        
    #     elif os.path.exists('/var/log/dnf'):
    #         print("Not a feature yet!")
            
    #     elif os.path.exists('/var/log/pkg'):
    #         print("Not a feature yet!")

    #     else:
    #         print("failed")
    #         pass
    
    
    # except:
    #     print("Failed")
    #     pass
    
    

def RestoreApps(parameter_list):
    pass

def BackupSettings(parameter_list):
    pass
def RestoreSettings(parameter_list):
    pass
optionsdict = {'Backup Apps': BackupApps, 'Restore Apps': 'RestoreApps', 'Backup Settings': 'BackupSettings', 'Restore Settings': 'RestoreSettings'}

def main():
    if osinfo.lower() == 'linux':
        print('Fun Linux Distro Fact: Did you know that the actual Ubuntu mascot is a trans foxgirl?')
        
    elif osinfo.lower() == 'freebsd':
        print('<3 FreeBSD')

    elif osinfo.lower() == 'OneFS':
        print("Why are you using this with OneFS? What possible reason could you have to use this with OneFS? I am really, really confused.")

    else:
        print(f'Sorry, your version is {osinfo} and I don\'t really support that right now. ^^;')

    
    #Let's do this here then 
    # while True:

        # choice = input()
        # if choice in optionsdict.keys():
        #     optionsdict[choice]()
    
    questions = [
        inquirer.List('Options',
                      message="Which do you wish to choose?",
                      choices=['Backup Apps', 'Restore Apps', 'Backup Settings', 'Restore Settings']
                      )
    ]
    answers = inquirer.prompt(questions)
    
    choice = (answers['Options'])

    if answers['Options'] in optionsdict.keys():
        optionsdict[choice]()
        print("yes")

if __name__ == "__main__":
    main()
