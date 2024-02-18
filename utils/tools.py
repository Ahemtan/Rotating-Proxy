import os
import random

def userAgents():
   with open(f"{os.getcwd()}\\user-agents.txt") as f:
    agents = f.read().split("\n")
    return random.choice(agents)


with open("../data/valid_proxy.txt", "r") as f:
    proxies = f.read().split("\n")

proxy = random.choice(proxies)