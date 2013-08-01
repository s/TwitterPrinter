# -*- coding: utf-8 -*-

#################################################
# app.py     							        
# 01 Aug 2013
# Said ÖZCAN									
# Twitter Printer
#################################################

from classes.Api import Api

try:
	if __name__ == '__main__':	
		Api()

except KeyboardInterrupt:
	
	print '>>InstagramPrinter: Application will shut down.'