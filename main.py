import requests
from utils.tools import userAgents, proxy

url = "https://www.daraz.com.np"

res = requests.get(url, proxies={"http":f"http://{proxy}"}, headers={"User-Agent": f"{userAgents}"})