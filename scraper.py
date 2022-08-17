import requests, math
from replit import db
from bs4 import BeautifulSoup
group_tag = "group-89904"

#obtain html of my group
def getHTML():
  html_text = requests.get('https://secure.runescape.com/m=hiscore_oldschool_ironman/group-ironman/?groupName=Bath+NinjaZ').text
  soup = BeautifulSoup(html_text,'lxml')  
  return(soup)

#turn lxml into a split string of my group
def myGroup():
  soup = getHTML()
  my_group = soup.find('tr',attrs={'data-test': group_tag})
  my_group = my_group.text.split()
  return(my_group)

#find and return searched group lxml as split string
def search(rank, size = 4):
  
  if ((rank % 20) == 0):
    page = math.floor(rank/20)
  else:
    page = math.floor(rank/20)+1
    
  html_search = requests.get('https://secure.runescape.com/m=hiscore_oldschool_ironman/group-ironman/?groupSize={}&page={}'.format(size,page)).text
  html_search = BeautifulSoup(html_search,'lxml')
  
  if rank > 1000:
    rank = str(rank)
    rank = rank[0] + ',' + rank[1] + rank[2]+ rank[3]
  sResult = html_search.find('td', text = rank).parent
  sResult = sResult.text.split()
  return sResult
  
  
def printGroup(group):
  rank = group[0]
  level = group[-2]
  exp = group[-1]
  i = -3
  name = ""
  while (group[0] != group[i]):
    name = group[i].capitalize() + " " + name
    i = i-1
    
  s = "Name: {}\nRank: {}\nTotal Level: {}\nExp: {} ".format(name ,rank ,level ,exp)
  return s


  