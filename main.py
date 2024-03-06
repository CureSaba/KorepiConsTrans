import re
import requests
from time import sleep

file_name = "a.txt"

def get(character):
    url = f"https://genshin-impact.fandom.com/wiki/{character}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    response = requests.get(url, headers=headers)

    text=response.text
    try:
        print(re.findall(r'<b>Japanese<\/b><\/td><td><span lang="ja">(.*?)<\/span>', text)[0])
        return re.findall(r'<b>Japanese<\/b><\/td><td><span lang="ja">(.*?)<\/span>', text)[0]
    except:
        print(re.findall(r'<td><ruby><span lang="ja">.*?<\/td>', text))
        return "".join(re.findall(r'<span lang="ja">(.*?)<\/span>', re.findall(r'<td><ruby><span lang="ja">.*?<\/td>', text)[0])[::2])
    


with open(file_name, encoding="utf-8") as f:
    data = f.read()

#data = re.sub(r'C6', r'完凸', data)
data = re.sub(r'C1:', r'1凸:', data)
data = re.sub(r'[^\n🟦🟨🟥？?]*C(.):', r'  \1凸:', data)
data = re.sub(r'🟦', r'🟢', data)
data = re.sub(r'🟨', r'🟡', data)
data = re.sub(r'🟥', r'🔴', data)
data = re.sub(r'？|\?', r'⚪', data)
data = re.sub(r'5-Star', r'星5', data)
data = re.sub(r'4-Star', r'星4', data)
for i in re.findall(r'- ([^\n]*)', data):
    data = data.replace(i, get(i))

with open(file_name, mode="w", encoding="utf-8") as f:
    f.write(data)