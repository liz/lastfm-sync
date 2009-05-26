from models import *
import time, datetime
from django.contrib.contenttypes.models import ContentType
import urllib, dateutil.parser, dateutil.tz
from xml2dict import XML2Dict

class LastfmSyncr:
	def syncposts(self, user, chart):		
		url = 'http://ws.audioscrobbler.com/1.0/user/%s/%s.xml' % (user, chart)
		data = urllib.urlopen(url).read()
		x = XML2Dict()
		r1 = x.fromstring(data)
		if chart == 'weeklytrackchart':
			user_name = r1['weeklytrackchart']['user']['value']
			week_start = r1['weeklytrackchart']['from']['value']
			week_end = r1['weeklytrackchart']['to']['value']
			for track in r1['weeklytrackchart']['track']:
				syncweeklytrack(track, user_name, week_start, week_end, chart)
		elif chart == 'weeklyalbumchart':
			user_name = r1['weeklyalbumchart']['user']['value']
			week_start = r1['weeklyalbumchart']['from']['value']
			week_end = r1['weeklyalbumchart']['to']['value']
			for album in r1['weeklyalbumchart']['album']:
				syncweeklyalbum(album, user_name, week_start, week_end, chart)
		elif chart == 'recenttracks':
			user_name = r1['recenttracks']['user']['value']
			for track in r1['recenttracks']['track']:
				syncrecenttrack(track, user_name, chart)
		elif chart == 'recentlovedtracks':
			user_name = r1['recentlovedtracks']['user']['value']
			for track in r1['recentlovedtracks']['track']:
				syncrecentlovetrack(track, user_name, chart)
		else:
			user_name = r1['weeklyartistchart']['user']['value']
			week_start = r1['weeklyartistchart']['from']['value']
			week_end = r1['weeklyartistchart']['to']['value']
			for artist in r1['weeklyartistchart']['artist']:
				syncweeklyartist(artist, user_name, week_start, week_end, chart)
				

			
def syncweeklytrack(track, user_name, week_start, week_end, chart):
	default_dict = {'week_start' : week_start, 'week_end' : week_end, 'artist' : track['artist']['value'], 'track' : track['name']['value'], 'chart_position' : track['chartposition']['value'], 'play_count' : track['playcount']['value'], 'url' : track['url']['value'], 'user_name' : user_name, 'chart' : chart }
	ctype = ContentType.objects.get_for_model(LastfmPost)
	created = LastfmPost.objects.get_or_create(content_type=ctype, **default_dict)
	
def syncweeklyartist(artist, user_name, week_start, week_end, chart):
	default_dict = {'week_start' : week_start, 'week_end' : week_end, 'artist' : artist['name']['value'], 'chart_position' : artist['chartposition']['value'], 'play_count' : artist['playcount']['value'], 'url' : artist['url']['value'], 'user_name' : user_name, 'chart' : chart  }
	ctype = ContentType.objects.get_for_model(LastfmPost)
	created = LastfmPost.objects.get_or_create(content_type=ctype, **default_dict)
	
def syncweeklyalbum(album, user_name, week_start, week_end, chart):
	default_dict = {'week_start' : week_start, 'week_end' : week_end, 'album' :  album['name']['value'],   'artist' : album['artist']['value'], 'chart_position' : album['chartposition']['value'], 'play_count' : album['playcount']['value'], 'url' : album['url']['value'], 'user_name' : user_name, 'chart' : chart  }
	ctype = ContentType.objects.get_for_model(LastfmPost)
	created = LastfmPost.objects.get_or_create(content_type=ctype, **default_dict)

def syncrecenttrack(track, user_name, chart):
	default_dict = {'track' :  track['name']['value'],   'artist' : track['artist']['value'], 'url' : track['url']['value'], 'user_name' : user_name, 'chart' : chart  }
	ctype = ContentType.objects.get_for_model(LastfmPost)
	created = LastfmPost.objects.get_or_create(content_type=ctype, **default_dict)
	
def syncrecentlovetrack(track, user_name, chart):
	default_dict = {'track' :  track['name']['value'],   'artist' : track['artist']['value'], 'url' : track['url']['value'], 'user_name' : user_name, 'chart' : chart  }
	ctype = ContentType.objects.get_for_model(LastfmPost)
	created = LastfmPost.objects.get_or_create(content_type=ctype, **default_dict)
