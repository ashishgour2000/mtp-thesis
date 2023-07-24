#1mg

import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
import requests
import pandas as pd
import time

#Path for chrome driver in local machine
#Change it accordingly
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver1 = webdriver.Chrome(PATH)

def get_url(search_term):
	template = 'https://www.1mg.com/search/all?name={}'
	#only one word querries
	#search_term = search_term.replace(' ','+')
	return template.format(search_term)

data_list = []
rank = 0

que_list = ['malaria', 'antiseptic', 'multivitamins', 'pain']


for que in que_list:
	url = get_url(que)

	#Change range to increase the no of pages to traverse
	for page in range(1, 2):
		print('Processing query: ', que, ' ****************************************************************************************')
		driver.get(url)
		soup = BeautifulSoup(driver.page_source, 'html.parser')

		#for every row
		results = soup.find_all('div',{'class': 'col-xs-12 col-md-10 col-sm-9'})
		for result in results:
			divs = result.find_all('div',{'class': 'col-md-3 col-sm-4 col-xs-6 style__container___jkjS2'})

			for div_tab in divs:
				element_list = []
				rank = rank+1
				atags = div_tab.find_all('a',{'class': 'style__product-link___1hWpa'})
				desc_tag = div_tab.find('div',{'class': 'style__product-description___zY35s'})
				productname_tag = desc_tag.find('div',{'class': 'style__pro-title___3G3rr'})
				producttitle = productname_tag.text
				#element_list.append(rank)
				element_list.append(producttitle)
				#print(producttitle)
				for a in atags:
					product_url = 'https://www.1mg.com' + a.get('href')
					element_list.append(product_url)
					driver1.get(product_url)
					soup1 = BeautifulSoup(driver1.page_source, 'html.parser')
					ufs = soup1.find_all('div',{'id': 'user_feedback'})
					user_feedback = []
					for uf in ufs:
						tag1 = uf.find('div',{'class': 'style__container___H5Qpz'})
						tag2 = tag1.find_all('div',{'class': 'row'})
						for rows in tag2:
							tag3 = rows.find_all('div',{'class': 'style__container___1nARz'})
							for tag_ in tag3:
								feedback_ = []
								que_tag = tag_.find('span',{'class': 'style__title___2XWdV'})
								question = que_tag.text
								feedback_.append(question)
								ans_tags = tag_.find_all('div',{'class': 'style__container___3DWmB'})
								for anstag in ans_tags:
									sol_list=[]
									val_tag = anstag.find('div',{'class': 'style__details-text___3mMMv'})
									val = val_tag.text
									perc_tag = anstag.find('div',{'class': 'style__percentage___1FkC_'})
									per = perc_tag.text
									sol_list.append(val)
									sol_list.append(per)
									feedback_.append(sol_list)
								user_feedback.append(feedback_)
				element_list.append(user_feedback)
				data_list.append(element_list)

	#frame = pd.DataFrame(data_list, columns = ['Rank', 'Product Title', 'URL', 'User feedback'])
	frame = pd.DataFrame(data_list, columns = ['Product Title', 'URL', 'User feedback'])
	file_name_save = que + '_userfeedback_page1.csv'
	frame.to_csv(file_name_save)