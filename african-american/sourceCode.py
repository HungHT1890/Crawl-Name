import requests,re
for x in range(1,11):
    api = f'https://www.behindthename.com/submit/names/usage/african-american/{x}'
    getName = requests.get(api)
    name = re.findall(r'<a href="/name/(.*?)/submitted"',getName.text)
    for  i in name:
        print(i)
        with open('african-american.txt','a',encoding='utf-8') as saveName:
            saveName.write(i+'\n')