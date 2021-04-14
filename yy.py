import requests,random
def lt() :
  url = "https://cdn.jsdelivr.net/gh/space78/source/list.txt"
  r = requests.get(url)
  r=r.text
  w=r.split('\n')
  f=random.choice(w)
  print(f)
  return f
a = lt()