try:
    from urllib.request  import urlopen
except ImportError:
    from urllib2 import urlopen
try:
    from urllib.parse  import quote, unquote
except ImportError:
    from urllib2 import quote, unquote
import json

#Description: User Input is used to find a similar musical artists events based on
#Last.FM's and BandsInTown's APIs. This data is used to populate MySQL database 
#using a user input on what band they want.
#
#For more information go to Github:
#https://github.com/cs327e-spring2016/SupremeNova


def artistparse(bandName):

	# user inputs artist name
	name = str(bandName)

	# replaces string with HTML format to fit API convention
	name = quote(name)

	# there is some type of API error when someone types a string '. H' (REALLY STRANGE ERROR)
	if ('.' and 'H') in name:
		name = name.replace('.','')

	# calls the last.fm API 
	lastfm_url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=&api_key=809d15fdb258f92ffd60f361dcf84feb&format=json'
	lastfm_url = lastfm_url[:66] + (name) + lastfm_url[66:]
	response = urlopen(lastfm_url)
	
	# convert bytes to string type and string type to dict
	lfm_string = response.read().decode('utf-8')
	lfm_json_obj = json.loads(lfm_string)

	# calls the last.fm genre API 
	lastfm_genre = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&artist=&api_key=809d15fdb258f92ffd60f361dcf84feb&format=json'
	lastfm_genre = lastfm_genre[:66] + (name) + lastfm_genre[66:]
	resp_genre = urlopen(lastfm_genre)

	# converts bytes to string type and string type to dict
	lfm_genre = resp_genre.read().decode('utf-8')
	lfm_genre_json = json.loads(lfm_genre)

	# for function bandList for the original band
	if len(lfm_genre_json) != 0:
		try:
			bandList(str(unquote(name)), str(lfm_genre_json['toptags']['tag'][0]['name']), cur, conn)
		except:
			#print("Error could not add")
			print()
	else:
		try:
			bandList(str(unquote(name)), 'None', cur, conn)
		except:
			print()
			#print("Error could not add")

	# to check if no artist is empty 
	if ('error' not in lfm_string) and (len(lfm_json_obj['similarartists']['artist']) != 0):

		# creates artist list, last artist, and artist index
		artistList =[]
		artistLast = lfm_json_obj['similarartists']['artist'][-1]['name']
		artist_index = 0

		# iterates through the list and uses the last artist to prevent going out of index
		while lfm_json_obj['similarartists']['artist'][artist_index]['name'] is not artistLast:
			artistList.append((lfm_json_obj['similarartists']['artist'][artist_index]['name']))
			artist_index += 1

		# adds the last artist parsing through list
		artistList.append(artistLast)
		#print(artistList)
		print()
		return artistList

		# Scraping the Bandsintown API
		i = 0
		while i < len(artistList):
			artistList[i] = quote(str(artistList[i]))
			# insert 
			i += 1

		# Calling bandsintown url (bit = BandsinTown)
		for band in artistList:
			bit_url = 'http://api.bandsintown.com/artists//events.json?api_version=2.0&app_id=BandAdvocate'
			bit_url = bit_url[:35] + str(band) + bit_url[35:]
			try:
				response2 = urlopen(bit_url)
				# convert bytes to string type and string type to dict
				bit_string = response2.read().decode('utf-8')
				bit_json_obj = json.loads(bit_string)
			except:
				print("Unable to Parse BandsinTown")

			# Parses through all of the artists venues, formatted location, formatted datetime
			print(str(unquote(band)))
			
			# calls the last.fm GENRE API 
			lastfm_genre = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&artist=&api_key=809d15fdb258f92ffd60f361dcf84feb&format=json'
			lastfm_genre = lastfm_genre[:66] + str(band) + lastfm_genre[66:]
			try:
				resp_genre = urlopen(lastfm_genre)
			except: 
				print("Unable to Parse LastFM")

			# converts bytes to string type and string type to dict
			lfm_genre = resp_genre.read().decode('utf-8')
			try:
				lfm_genre_json = json.loads(lfm_genre)
			except:
				print("Unable to Parse LastFM")

			# for function the bandList for the original band
			if len(lfm_genre_json) != 0:
				try:
					bandList(str(unquote(band)), str(lfm_genre_json['toptags']['tag'][0]['name']), cur, conn)
					similarBands(str(unquote(name)), str(unquote(band)), str(lfm_genre_json['toptags']['tag'][0]['name']), cur, conn)
				except:
					pass
			else:
				try:
					similarBands(str(unquote(name)), str(unquote(band)), 'None', cur, conn)
				except:
					pass
			
			#Prints Artist's Events
			if len(bit_json_obj) != 0:
				for item in bit_json_obj :
					print(item['formatted_location'])
					print(item['formatted_datetime'])
					print(item['venue']['name'])
					print()
					try:
						event(unquote(band), state, city, date, time, venue, cur, conn)
					except:
						pass
					
			else:
				print('There are no events for this artist')
				print()
				
	# when no artist is found 
	else:
		print()
		print('Similar Artists Not Found')
		print()





