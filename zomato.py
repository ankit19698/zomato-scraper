from bs4 import BeautifulSoup
import requests
from selenium import webdriver


def score(site):
	
	url = requests.get(site,headers={'User-Agent':'Mozilla/5.0'}).text
	soup = BeautifulSoup(url,'html.parser')



	ls = []
	num = []
	add = []
	#rate = []



	for j in soup.findAll('a', attrs={'class':'item res-snippet-ph-info'}):

				num.append(j['data-phone-no-str'])
				ls.append(j['data-res-name'])


	for i in soup.findAll('div', attrs={'class':'col-m-16 search-result-address grey-text nowrap ln22'}):
		if i:
			add.append(i.text.strip())

	return ls,num,add


site = input("Paste the zomato page: Example>> https://www.zomato.com/city_name/restaurents/...<< URL+space : ")

ls,num,add = score(site)

f = open("record.txt","w")


###

for i in range(len(ls)):
	print("Name : ",ls[i])
	f.write(str("Name : ")+ls[i]+str("\n"))
	print("Contact : ",num[i])
	f.write(str("Contact : ")+num[i]+str("\n"))
	print("Address : ",add[i])
	f.write(str("Address : ")+add[i]+str("\n"))
	f.write(str("-"*2*len(max(add))))
	f.write(str("\n"))
	print("-"*2*len(max(add)))



print(len(ls),len(num),len(add))



