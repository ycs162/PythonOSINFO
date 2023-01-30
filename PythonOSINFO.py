#!/usr/bin/python3

#This script is created by:
#Name: Yap Ching Siong
#Student code: S14
#Class: CFC2407
#Lecturer: James

# This script is created to automate the display of operating system information.
# The following information will be displayed after executing this script:
# 1. OS version
# 2. Private IP address, Public IP address and Default Gateway.
# 3. Display hard disk size, free and used space.
# 4. Display Top five directories and their size (the directories involve in calculation depends on the path user executes this script).
# 5. Display cpu usage; refresh every 10seconds.
 
# Reference:
# https://www.geeksforgeeks.org/python-os-system-method/
# https://unix.stackexchange.com/questions/88644/how-to-check-os-and-version-using-a-linux-command
# https://phoenixnap.com/kb/linux-check-disk-space
# https://phoenixnap.com/kb/check-cpu-usage-load-linux
# https://www.cyberciti.biz/faq/how-do-i-find-the-largest-filesdirectories-on-a-linuxunixbsd-filesystem/

import os

print("OS version: ")
os.system("uname -a")
print("\n")
os.system("sleep 2")

print("Private IP Address: ")
os.system("ifconfig | grep broadcast | awk '{print $2}'")
print("\n")
os.system("sleep 2")

print("Public IP Address: ")
os.system("curl ifconfig.io")
print("\n")
os.system("sleep 2")

print("Default Gateway: ")
os.system("route | grep UG | awk '{print $2}' | uniq")
print("\n")
os.system("sleep 2")

print("Hard Disk Size: ")
os.system("df -h")
print("\n")
os.system("sleep 2")

print("Top Five Largest Directories And Their Size: ")
os.system("du -h | sort -h | tail -n 5")
print("\n")
os.system("sleep 2")

print("CPU Usage (Ctrl + C to Exit): ")
os.system("top -d 10")
