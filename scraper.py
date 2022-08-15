import requests
from bs4 import BeautifulSoup
group_tag = "group-89904"

def getHTML():
  html_text = requests.get('https://secure.runescape.com/m=hiscore_oldschool_ironman/group-ironman/?groupName=Bath+NinjaZ').text
  soup = BeautifulSoup(html_text,'lxml')  
  return(soup)

def ironmanGroup():
  soup = getHTML()
  my_group = soup.find('tr',attrs={'data-test': group_tag})
  my_group = my_group.text.split()
  s = "Name: {} {}\nRank: {}\nTotal Level: {}\nExp: {} ".format(my_group[1], my_group[2],my_group[0], my_group[3],my_group[4] )
  return(s)

  
