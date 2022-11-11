import re
import requests

data = requests.get('http://www.columbia.edu/~fdc/sample.html')

patern = r'[<][h][3].*[h][3][>]'
patern_2 = r'[<].*?[>]'
cutter = re.findall(patern, data.text)
solution = re.sub(patern_2, '', str(cutter))

print(solution)