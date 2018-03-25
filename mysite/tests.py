from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTestCase(LiveServerTestCase):

	def setUp(self):
		self.selenium=webdriver.Chrome()
		super(LoginTestCase,self).setUp()

	def tearDown(self):
		self.selenium.quit()
		super(LoginTestCase,self).tearDown()

	def test_login_option1(self):
		selenium=self.selenium
		#Open the link
		selenium.get('http://127.0.0.1:8000/accounts/login')
		#Delay
		try:
			#Find the form element
			username = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "username")))
			password = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "password")))
			login = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "login")))
			'''
			username=selenium.find_element_by_id('username')
			password=selenium.find_element_by_id('password')
			login=selenium.find_element_by_id('login')
			'''
			#Fill the form data
			username.send_keys('raksha')
			password.send_keys('ayurveda')

			#Submit the form
			login.send_keys(Keys.RETURN)
			#Check the result
			assert 'Cart' in selenium.page_source
		finally:
			selenium.quit()

	def test_login_option2(self):
		selenium=self.selenium
		#Open the link
		selenium.get('http://127.0.0.1:8000/accounts/login')
		#Delay
		try:
			#Find the form element
			username = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "username")))
			password = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "password")))
			login = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "login")))
			'''
			username=selenium.find_element_by_id('username')
			password=selenium.find_element_by_id('password')
			login=selenium.find_element_by_id('login')
			'''
			#Fill the form data
			username.send_keys('raksha')
			password.send_keys('abc')

			#Submit the form
			login.send_keys(Keys.RETURN)
			#Check the result
			assert 'Username' in selenium.page_source
		finally:
			selenium.quit()

	def test_login_option3(self):
		selenium=self.selenium
		#Open the link
		selenium.get('http://127.0.0.1:8000/accounts/login')
		#Delay
		try:
			#Find the form element
			username = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "username")))
			password = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "password")))
			login = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "login")))
			'''
			username=selenium.find_element_by_id('username')
			password=selenium.find_element_by_id('password')
			login=selenium.find_element_by_id('login')
			'''
			#Fill the form data
			username.send_keys('abc')
			password.send_keys('abc')

			#Submit the form
			login.send_keys(Keys.RETURN)
			#Check the result
			assert 'Username' in selenium.page_source
		finally:
			selenium.quit()

	def test_login_option4(self):
		selenium=self.selenium
		#Open the link
		selenium.get('http://127.0.0.1:8000/accounts/login')
		#Delay
		try:
			#Find the form element
			username = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "username")))
			password = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "password")))
			login = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "login")))
			'''
			username=selenium.find_element_by_id('username')
			password=selenium.find_element_by_id('password')
			login=selenium.find_element_by_id('login')
			'''
			#Fill the form data
			username.send_keys('abc')
			password.send_keys('ayurveda')

			#Submit the form
			login.send_keys(Keys.RETURN)
			#Check the result
			assert 'Username' in selenium.page_source
		finally:
			selenium.quit()
		
		