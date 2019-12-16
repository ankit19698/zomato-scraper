from bs4 import BeautifulSoup
import requests
from selenium import webdriver


def score(site):
	
	url = requests.get(site,headers={'User-Agent':'Mozilla/5.0'}).text
	soup = BeautifulSoup(url,'html.parser')



	ls = []
	num = []
	add = []




	for j in soup.findAll('a', attrs={'class':'item res-snippet-ph-info'}):

				num.append(j['data-phone-no-str'])
				ls.append(j['data-res-name'])


	for i in soup.findAll('div', attrs={'class':'col-m-16 search-result-address grey-text nowrap ln22'}):
		if i:
			add.append(i.text.strip())

	return ls,num,add


site = input("Paste the zomato page: Example>> https://www.zomato.com/city_name/restaurents/...<< URL+space : ")

ls,num,add = score(site)
for i in range(len(ls)):
	print("Name : ",ls[i])
	print("Contact : ",num[i])
	print("Address : ",add[i])
	print("------------------------------------------------------------------")
