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

		print '>>TwitterPrinter: Connecting To Api'
		
		self.apiConnectionFlag = 1

		try:
			
			t = Twitter(auth=OAuth(self.accessToken, self.accessTokenSecret, self.consumerKey, self.consumerSecret))

			#print self.searchHashtag

			data = t.search.tweets(q=self.searchHashtag)

			self.process_data( data['statuses'] )
		
		except Exception as exc:

			print '>>TwitterPrinter: An Exception Raised During Connecting To Api:' + str(exc)

			sys.exit(0)




	##################
	# method process_data
	# the process_data method
	# @param self
	# @return void
	##################
	def process_data(self, response):
		
		print '>>TwitterPrinter: Processing Data'

		try:

			if len( response ):

				for r in response:
						
					self.save_data_as_html( r )

			else: 
				
				print '>>TwitterPrinter: No tweets fetched'

		except Exception as exc:

			print '>>TwitterPrinter: An Exception Raised During process_data:' + str(exc)

			sys.exit(0)
				





	##################
	# method save_data_as_html
	# the save_data_as_html method
	# @param self
	# @return void
	##################
	def save_data_as_html(self, data ):
		
		print '>>TwitterPrinter: Will Generate HTML if not exists before'	

		self.apiConnectionFlag = 0

		fileName = str( data['id'] ) + '.html'

		source = self.outputDirectory + 'templates/' + self.templateFileName
		
		destination = self.outputDirectory + 'views/#' + self.searchHashtag + '/'

		if not os.path.exists( destination ):
			os.makedirs( destination )
			os.chmod( destination, 0777)

		#user data
		user = data['user']
		
		if True == os.path.exists( destination + fileName):
			
			print '>>TwitterPrinter: File ' + fileName + ' already exists. Will pass this time.'		
			
			return 
		else:
			
			try:
				
				with open( source ) as file:

					template = file.read()

			except Exception as exc:

				print '>>TwitterPrinter: An Exception Raised During generating view:' + str(exc)

				sys.exit(0)
			
			
			template = template.replace( '{$title}', self.pageTitle )

			template = template.replace( '{$postOwnerUsername}', '@' + user['screen_name'] )

			template = template.replace( '{$postOwnerName}', user['name'] )

			template = template.replace( '{$userAvatar}', user['profile_image_url'])

			template = template.replace( '{$tweetDate}', data['created_at'] )

			tweetText = data['text']

			originalTweetText = tweetText

			for hashtag in data['entities']['hashtags']:

				hashtagIndices = hashtag['indices']

				hashtag['text'] = '#' + hashtag['text']

				tweetText = tweetText.replace( tweetText[hashtagIndices[0]:hashtagIndices[1]], '<span class=\'hrefColor\'>' + hashtag['text'] + '</span>' )

			tweetText = tweetText.replace( originalTweetText, tweetText )

			startOfMedia = template.index( '{$photo}' ) + len( '{$photo}' )

			endOfMedia = template.index( '{/$photo}', startOfMedia )

			mediaBlock = template[ startOfMedia:endOfMedia ]

			originalMediaBlock = mediaBlock

			if 'media' in data['entities']:

				media = data['entities']['media'][0]

				mediaBlock = mediaBlock.replace( '{$photoUrl}', media['media_url'] )

				mediaBlock = mediaBlock.replace( '{$photoWidth}', str( media['sizes']['small']['w'] ) )

				mediaBlock = mediaBlock.replace( '{$photoHeight}', str( media['sizes']['small']['h'] ) )

				#print tweetText[media['indices'][0]:media['indices'][1]]

				tweetText = tweetText.replace( media['url'], '<span class=\'hrefColor\'>' + media['url'] + '</span>' )

			else:

				mediaBlock = ''
				
			template = template.replace( '{$photo}' + originalMediaBlock + '{/$photo}' , mediaBlock )

			template = template.replace( '{$tweetText}', tweetText )

			newFilePath = destination + str(data['id']) + '.html'
			
			if True == os.path.exists(newFilePath):
				os.remove(newFilePath)
				
			
			newFile = open( newFilePath, 'w+' )
			
			newFile.write( template.encode('utf8') )
			
			newFile.close()

			print '>>TwitterPrinter: ' + str(data['id']) + '.html has been generated.' 




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

			self.templateFileName = data['templateFileName']
	
			configurations.close()
		
		except KeyError as exc:
			
			print '>>TwitterPrinter: Validation error. Check credientals'

			sys.exit(0)