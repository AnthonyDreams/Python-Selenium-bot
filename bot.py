from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from random import randint
import json as Json
import win10toast
import traceback
import logging
import time
import re
import os
import sys



delay = 20
toaster = win10toast.ToastNotifier()

def Chrome():
	global driver
	driver = webdriver.Chrome(os.path.basename('chromedriver'))

def forceToStop():
	exit('terminado')

def CloseChrome():
	sys.exit('finalizado')

def Finalizado():
	CloseChrome()
	toaster.show_toast('Terminado', 'Bot Finalizado por el dia de hoy, espere mañana por favor.')


def main():
	RE_INT = re.compile(r'^[-+]?([1-9]\d*|0)$')
	count = 0
	global card
	with open('count.txt', 'r') as count:
		count = int(count.readline());
		
	with open('count.txt', 'w') as countwrite:
		countwrite.write(str(int(count) + 1))



	global data
	states = {
		"AL": "Alabama",
		"AK": "Alaska",
		"AS": "American Samoa",
		"AZ": "Arizona",
		"AR": "Arkansas",
		"CA": "California",
		"CO": "Colorado",
		"CT": "Connecticut",
		"DE": "Delaware",
		"DC": "District Of Columbia",
		"FM": "Federated States Of Micronesia",
		"FL": "Florida",
		"GA": "Georgia",
		"GU": "Guam",
		"HI": "Hawaii",
		"ID": "Idaho",
		"IL": "Illinois",
		"IN": "Indiana",
		"IA": "Iowa",
		"KS": "Kansas",
		"KY": "Kentucky",
		"LA": "Louisiana",
		"ME": "Maine",
		"MH": "Marshall Islands",
		"MD": "Maryland",
		"MA": "Massachusetts",
		"MI": "Michigan",
		"MN": "Minnesota",
		"MS": "Mississippi",
		"MO": "Missouri",
		"MT": "Montana",
		"NE": "Nebraska",
		"NV": "Nevada",
		"NH": "New Hampshire",
		"NJ": "New Jersey",
		"NM": "New Mexico",
		"NY": "New York",
		"NC": "North Carolina",
		"ND": "North Dakota",
		"MP": "Northern Mariana Islands",
		"OH": "Ohio",
		"OK": "Oklahoma",
		"OR": "Oregon",
		"PW": "Palau",
		"PA": "Pennsylvania",
		"PR": "Puerto Rico",
		"RI": "Rhode Island",
		"SC": "South Carolina",
		"SD": "South Dakota",
		"TN": "Tennessee",
		"TX": "Texas",
		"UT": "Utah",
		"VT": "Vermont",
		"VI": "Virgin Islands",
		"VA": "Virginia",
		"WA": "Washington",
		"WV": "West Virginia",
		"WI": "Wisconsin",
		"WY": "Wyoming"
	}
	global phone
	with open('addresses-us-all.json', 'r') as json:
		data = Json.loads(json.read())
		data = data['addresses'][randint(0, len(data['addresses']))]

	with open('file.json', 'r') as phones:
		phone = Json.loads(phones.read())
		phone = phone['phones'][randint(0, len(phone['phones']))]
	phone_set = ""


	for a in phone['PhoneNumber']:
		try:
			int(a)
			phone_set += a
		except ValueError:
			pass


	def nameGenerator():
		global first_name
		global last_name

		with open('name.json', 'r') as name_list:
			name = Json.loads(name_list.read())
			first_name = name['names'][randint(0, len(name['names']))]
			last_name = name['names'][randint(0, len(name['names']))]
	
	nameGenerator()

	
	def gettingCard():
		with open('11-21.json', 'r') as cards:
			card = Json.loads(cards.read())
			card = card['cards'][count]['card']
			time.sleep(5)
			credicard = driver.find_element_by_id('paymentForm:j_id_16_5:creditCardNumber')
			credicard.send_keys(''+card)
		globals()['card'] = card
	def GoToInfo():
		driver.set_page_load_timeout(80)
		driver.get('https://www.fanatics.com/mlb/san-diego-padres/san-diego-padres-stripe-team-crew-socks-brown/o-3487+t-47121193+p-81073822173+z-9-1887779471?_ref=p-SRP:m-GRID:i-r2c1:po-7')
		element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[4]/div[2]/div[11]/div/div/div[5]/div/div[2]/div/div[1]/div/button')))
		driver.execute_script("arguments[0].click();", element)
		second_button =  WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/header/div[1]/div[3]/a')))
		driver.execute_script("arguments[0].click();", second_button)
		time.sleep(5)
		guestUserCheckout = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div[4]/button')))
		driver.execute_script("arguments[0].click();", guestUserCheckout)

	def AddingAddress():
		
		firstName = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div[1]/div/form/div[1]/div[1]/div/div[1]/div/div/input')))
		firstName.send_keys("first_name")
		lastName = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div[1]/div/form/div[1]/div[1]/div/div[2]/div/div/input')))
		lastName.send_keys(last_name)
		# select = Select(driver.find_element_by_id('shippingForm:j_id_11:country'))
		# select.select_by_visible_text('United States')
		# street = driver.find_element_by_id('shippingForm:j_id_11:street')
		# street.send_keys(data['address1'])
		# time.sleep(2)
		# postalCode = driver.find_element_by_id('shippingForm:j_id_11:zipcode')
		# postalCode.send_keys(int(data['postalCode']))
		# city = driver.find_element_by_id('shippingForm:j_id_11:city')
		# city.send_keys(data['city'])
		# time.sleep(5)
		# select_states = Select(driver.find_element_by_id('shippingForm:j_id_11:whatever'))
		# select_states.select_by_visible_text(states[data['state']])
		# phone = driver.find_element_by_id('shippingForm:j_id_11:telephone')
		# phone.send_keys(phone_set)
		# time.sleep(4)
		# element_ = driver.find_element_by_id('shippingForm:j_id_11:cart_next')
		# driver.execute_script("arguments[0].click();", element_)
		
	def BankInfo():
		
		gettingCard()

		email = driver.find_element_by_id('paymentForm:j_id_17:emailAddress')
		email.send_keys(first_name+last_name + '@yopmail.com')
		time.sleep(2)
		holder = driver.find_element_by_id('paymentForm:j_id_16_5:creditCardHolderName')
		holder.send_keys(first_name+ ' ' + last_name)


		time.sleep(5)

		expirationMonth = Select(driver.find_element_by_id('paymentForm:j_id_16_5:creditCardExpirationMonth'))
		expirationMonth.select_by_visible_text('11')

		expirationYear = Select(driver.find_element_by_id('paymentForm:j_id_16_5:creditCardExpirationYear'))
		expirationYear.select_by_visible_text('2021')
		time.sleep(4)
		element__ = driver.find_element_by_id('paymentForm:cart_next')
		driver.execute_script("arguments[0].click();", element__)
		element__2 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'j_id_w:j_id_4m:b0-cart_next')))
		driver.execute_script("arguments[0].click();", element__2)

	def save():
		try:
			driver.find_element_by_id('payVaultError')
		except:
			with open('workingcard.txt', 'a') as file:
				file.write(globals()['card'] + '\n')



	GoToInfo()
	AddingAddress()
	time.sleep(3)
	BankInfo()
	save()

def exception():
	count_ = 0
	driver.quit()
	logging.error(traceback.format_exc())
	toaster.show_toast('bot error', 'Ha habido un error, el script se reiniciará.')
	with open('count.txt', 'r') as count:
		count_ = int(count.readline());

	with open('count.txt', 'w') as countwrite:
	    countwrite.write(str(int(count_) - 1))
	with open('logs.txt', 'a') as log:
	    log.write(traceback.format_exc() + '\n')

	os.execv(sys.executable, ['python'] + sys.argv + ["restart"])

if __name__ == '__main__':

	Chrome()
	try:
		main()
	except Exception as e:
		driver.quit()
		logging.error(traceback.format_exc())
		toaster.show_toast('bot error', 'Ha habido un error, el script se reiniciará.')
		with open('count.txt', 'w') as countwrite:
			countwrite.write(str(int(count) - 1))
		with open('logs.txt', 'a') as log:
			log.write(traceback.format_exc() + '\n')
		print('python' + sys.argv + " restart")
		os.execv(sys.executable, ['python'] + sys.argv + [" restart"])
