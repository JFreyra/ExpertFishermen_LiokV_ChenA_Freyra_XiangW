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
                tempList = [ t["name"] , t["external_urls"]["spotify"] ]
                retList.append( tempList )
    
        elif a == "":
            url = "https://api.spotify.com/v1/search?q=" + t + "&type=track"
            request = urllib2.urlopen(url)
            result = request.read()
            d = json.loads(result)
            d = d["tracks"]
            for t in d["items"]:
                collabs = ""
                for a in t["artists"]:
                    collabs += a["name"] + ","
                collabs = collabs[:-1]
                retList.append( [collabs,t["external_urls"]["spotify"]] )
                                
        else:
            retList = [] #placeholder
        
    return retList

pprint( keywordSearch("","Sunday Morning") )
