import re
import requests

data = requests.get('http://www.columbia.edu/~fdc/sample.html')

patern = r'[<][h][3].*[h][3][>]'
patern_2 = r'[<].*?[>]'
cutter = re.findall(patern, data.text)
solution = re.sub(patern_2, '', str(cutter))

print(solution)  # так тоже можно

# NOTE обратите внимание и на такой способ решения этой задачи
req_site = requests.get('http://www.columbia.edu/~fdc/sample.html')
result = re.findall(r'<h3.*>(.*)</h3>', req_site.text)
print(result)
