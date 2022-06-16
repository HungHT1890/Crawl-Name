import requests,re
for x in range(1,9):
    api = f'https://www.behindthename.com/submit/names/usage/thai/{x}'
    getName = requests.get(api)
    name = re.findall(r'<a href="/name/(.*?)/submitted"',getName.text)
    for  i in name:
        print(i)
        with open('Thailand Name.txt','a',encoding='utf-8') as saveName:
            saveName.write(i+'\n')