# -*- coding: utf-8 -*-

#################################################
# Api.py     							        
# 01 Aug 2013
# Said ÖZCAN									
# Twitter Printer
#################################################

from twitter import *

import httplib, urllib2, json, time, sys, shutil, os, stat, re, datetime, yaml

class Api:

	############ static members ############

	#Api connection flag
	#if methods below can't finish it's job within delay time, this flag will prevent send second request
	apiConnectionFlag = 0


	#Output directory
	outputDirectory = 'outputs/'





	
	############ dynamic members from config.yaml ############

	#Twitter api consumer key
	consumerKey = ''


	#Twitter api consumer secret
	consumerSecret = ''


	#Twitter api access token
	accessToken = ''


	#Twitter api access token secret
	accessTokenSecret = 	''


	#Api connection delay time
	delayTime = 0


	#Html file page title
	pageTitle = 'TwitterPrinter'


	#Hashtag to search
	searchHashtag = ''
	



	##################
	# method __init__
	# the __init__ method
	# @param self
	# @return void
	##################
	def __init__(self):
		
		self.get_configurations()		

		if True is self.check_network():

			while 1:

				while self.apiConnectionFlag is 1:
					pass

				self.connect_to_api()

				print '>>TwitterPrinter: Application will sleep for ' + str(self.delayTime) + ' seconds.'

				time.sleep( self.delayTime )
		else:

			print '>>TwitterPrinter: No network connection'






	##################
	# method connect_to_api
	# the connect_to_api method
	# @param self
	# @return void
	##################
	def connect_to_api(self):
		t = Twitter(auth=OAuth(self.accessToken, self.accessTokenSecret, self.consumerKey, self.consumerSecret))

		data = t.search.tweets(q=self.searchHashtag)
		
		print data




	##################
	# method process_data
	# the process_data method
	# @param self
	# @return void
	##################
	def process_data(self):
		pass





	##################
	# method save_data_as_html
	# the save_data_as_html method
	# @param self
	# @return void
	##################
	def save_data_as_html(self):
		pass





	##################
	# method check_network
	# the check_network method
	# @param self
	# @return void
	##################
	def check_network(self):

		try:

			response=urllib2.urlopen('http://google.com',timeout=1)

			return True

		except:

			return False





	##################
	# method get_configurations
	# this method gets the configurations of application from config.yaml
	# @param self
	# @return void
	##################
	def get_configurations(self):		
		
		try:
		
			configurations = open('config.yaml')
		
			data = yaml.safe_load(configurations)

			self.consumerKey = data['consumerKey']

			self.consumerSecret = data['consumerSecret']

			self.accessToken = data['accessToken']

			self.accessTokenSecret = data['accessTokenSecret']

			self.delayTime = data['delayTime']

			self.pageTitle = data['pageTitle']

			self.searchHashtag = data['searchHashtag']
	
			configurations.close()
		
		except KeyError as exc:
			
			print '>>TwitterPrinter: Validation error. Check credientals'

			sys.exit(0)