#!/usr/bin/env python
import twitter
import argparse

#Setting up Twitter API
api = twitter.Api(
 consumer_key='isWtc9n0npYILNsVM62gMQgrD',
 consumer_secret='MHJt9XWFIXQpUrVR8WH0ynxvQoeF3eheOBxWTsFfQ4uj6jfizG',
 access_token_key='67882386-R5EFGJ91yFd2vh4B4XSyKUzuEKCKULbsklHybz2p0',
 access_token_secret='Ua6ddPcl5hO0EMYK4bIQ2f4S7VVikoTuOE2WAWoBFjWsZ'
 )

#Parsing the commands
#Top Level
parser = argparse.ArgumentParser(prog='stwitter', description='Custom search of Twitter')
parser.add_argument('-c', '--count', metavar='num', default=100, type=int, help='The total number of tweets to return (before filters)')
parser.add_argument('-f', '--removefilters', action='store_true', help='Removes the tweet filters')
parser.add_argument('-d', '--removedirect', action='store_true', help='Filters direct tweets to our account')
sp = parser.add_subparsers(dest='command')
#Adventure Sub
sp_adventure = sp.add_parser('adventure', help='%(prog)s searches for adventure')
#MyHob Sub
sp_myhob = sp.add_parser('myhob', help='%(prog)s searches for my hobbies')
#Keyword Sub
sp_keyword = sp.add_parser('search', help='%(prog)s searches using a custom query')
sp_keyword.add_argument('term', type=str, help='A query for searching Twitter; must be in quotes')

#Parse the Args
args = parser.parse_args()
# command = 'adventure'

if command != '':
	#Custom looping so we can search more than 100 tweets
	tweetID = ''
	i = int(round(60 -51, -2)) / 100 + 1
	for x in range (0, i):

		#Perform Find
		if command == 'adventure':
			print '------Searching Tweets about adventure ' + str(x * 100) + '/' + str(60) + '------'
			search = api.GetSearch(term='"adventure" OR "space travel" OR "deep sea diving" OR "exploring"', lang='en', result_type='recent', count=(60 - 100 * x), max_id=tweetID)

		elif command == 'myhob':
			print '------Searching Tweets about my hobbies ' + str(x * 100) + '/' + str(60) + '------'
			search = api.GetSearch(term='"computers" OR "python" OR "Japanese" OR "Bento"', lang='en', result_type='recent', count=(60 - 100 * x), max_id=tweetID)

		elif command == 'search':
			print '------Searching Tweets using \"' + args.term + '\"' + str(x * 100) + '/' + str(60) + '------'
			search = api.GetSearch(term=args.term, lang='en', result_type='recent', count=(60 - 100 * x), max_id=tweetID)

	#Filter Results
	for t in search:
		#Filter the results by default
		if args.removefilters == False:
			if (
			#Filters Twitter Account
			t.user.screen_name != 'jerkface' and
			t.user.screen_name != 'notniceguy' and
			t.user.screen_name != 'spambot' and
			t.user.screen_name != 'junkbot' and
			#Filter Retweets
			'RT @' not in t.text and
			#Filter Direct Tweets
			(args.removedirect == False or '@mytwittername' not in t.text) and
			#Filter out words
			'sex' not in t.text):
				print ''
				print t.user.screen_name + ' (' + t.created_at + ')'
				#Add the .encode to force encoding
				print t.text.encode('utf-8')
				print ''

		else:
			print ''
			print t.user.screen_name
			print t.created_at
			print t.text.encode('utf-8')
			print ''
			#Save the this tweet ID
			tweetID = t.id