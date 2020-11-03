#!/usr/bin/python3
import os
import sys
os.system("tput setaf 7")
os.system("figlet -f slant -w 100 -c Welcome to A-MATE")
os.system("tput setaf 1")
option =0
while option != 5:
    

    print("\t\t\t\t WHAT DO YOU WANT TO DO")
    os.system("tput setaf 2")
    print("\t\t\t Press 1 for Installing The Hadoop")
    os.system("tput setaf 3")
    print("\t\t\t Press 2 For Setting LVM")
    os.system("tput setaf 4")
    print("\t\t\t Press 3 To Reduce the Size of LVM")
    os.system("tput setaf 5")
    print("\t\t\t Press 4 To Increase The Size Of LVM")
    os.system("tput setaf 6")
    print("\t\t\t Press 5 For Exit")
    os.system("tput setaf 7")
    option = int(input("\t\t\t Enter Your Choice: "))
    os.system("tput setaf 7")
    


    if option == 1:
            os.system("ansible-playbook Hadoop_setup.yaml")
    elif option == 2:
            os.system("ansible-playbook Creation.yaml")
    elif option == 3:
            os.system("ansible-playbook reduce.yaml")
    elif option == 4:
            os.system("ansible-playbook extend.yaml")
    elif option == 5:
            os.system("exit")
    else: 
        os.system("tput setaf 1")
        print("\n\t\t\t\t     InValid Choice\n\n\n")
