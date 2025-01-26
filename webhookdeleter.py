import requests
from colorama import Fore
import os
os.system("cls")

hook = input(" Webhook to delete : ")
msg = input(" Deletion Message :  ")

if hook == None and msg == None:
    print("You didn't input anything.")
    input("Press enter to close")

try:
    requests.post(hook, data={"content": f"{msg}"})
    requests.delete(hook)
    print(f"Sent {Fore.LIGHTBLUE_EX}{msg} {Fore.RESET}and deleted webhook : {Fore.LIGHTBLUE_EX}{hook}")
    input(" Press enter to close : ")
except Exception as e:
    print(Fore.LIGHTRED_EX + "Invalid webhook or doesn't exist.")

