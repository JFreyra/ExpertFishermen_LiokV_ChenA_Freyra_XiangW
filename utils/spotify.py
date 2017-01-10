import urllib2, json
from pprint import pprint

clientID = "ce08603068aa48df9e531d9734322d0a"
clientSecret = "2770e587a1b6411298fa239d05fe0355"

def keywordSearch(artist,track):

    retList = []
    a = artist.replace(" ","+")
    t = track.replace(" ","+")
    
    if not (a == "" and t == ""):
            
        if t == "":
            url = "https://api.spotify.com/v1/search?q=" + a + "&type=artist"
            request = urllib2.urlopen(url)
            result = request.read()
            d = json.loads(result)
            d = d["artists"]["items"][0]["id"]
            url = "https://api.spotify.com/v1/artists/" + d + "/top-tracks?country=US"
            request = urllib2.urlopen(url)
            result = request.read()
            d = json.loads(result)
            for t in d["tracks"]:
                tempList = [ t["name"] , t["id"] ]
                retList.append( tempList )
    
        elif a == "":
            url = "https://api.spotify.com/v1/"
            request = urllib2.urlopen(url)
            result = request.read()
            d = json.loads(result)
    
        else:
            retList = [] #placeholder
        
    return retList

pprint( keywordSearch("Sam Smith","") )
