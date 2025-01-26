
# https://github.com/OmicronFlare/pysources

import requests
import os
from colorama import Fore

os.system("cls")

hook = input(" Webhook : ")
message = input(" Message : ")
amount = int(input(" Amount : "))

for i in range(amount):
    try:
        requests.post(hook, data={"content": f"{message}"})
        print(Fore.LIGHTBLUE_EX + f"Sent {Fore.LIGHTBLACK_EX}{message}")
    except Exception as e:
        print(Fore.LIGHTRED_EX + "Webhook invalid or doesn't exist.")

input()
