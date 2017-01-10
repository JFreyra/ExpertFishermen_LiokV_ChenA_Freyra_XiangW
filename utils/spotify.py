import urllib2, json
from pprint import pprint

clientID = "ce08603068aa48df9e531d9734322d0a"
clientSecret = "2770e587a1b6411298fa239d05fe0355"

def keywordSearch(artist,track):
    
    if track == "" and artist == "":
        retList = []
        
    elif track == "":
        newQuery = artist.replace(" ","+")
        url = "https://api.spotify.com/v1/search?q=" + newQuery + "&type=artist"
        request = urllib2.urlopen(url)
        result = request.read()
        d = json.loads(result)
        d = d["artists"]["items"][0]["id"]
        url = "https://api.spotify.com/v1/artists/" + d + "/top-tracks?country=US"
        request = urllib2.urlopen(url)
        result = request.read()
        d = json.loads(result)
        retList = []
        for t in d["tracks"]:
            retList.append( t["name"] )
    
    #else if artist == "":
        

    else:
        retList = [] #placeholder
        
    return retList

pprint( keywordSearch("Adam","") )
