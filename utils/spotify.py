import urllib2, json
from pprint import pprint

clientID = "ce08603068aa48df9e531d9734322d0a"
clientSecret = "2770e587a1b6411298fa239d05fe0355"

def keywordSearch(artist,track):

    retList = []
    a = artist.replace(" ","+")
    t = track.replace(" ","+")
    
    if not (a == "" and t == ""):

        #searching for only an artist returns the artist's top tracks    
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

        #searching for only a track returns tracks with the same name but by different artists
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

        #searching for both an artist and a track returns the top three versions of that song
        else:
            url = "https://api.spotify.com/v1/search?q=" + t + "&type=track"
            request = urllib2.urlopen(url)
            result = request.read()
            d = json.loads(result)
            d = d["tracks"]
            counter = 0
            for t in d["items"]:
                for a in t["artists"]:
                    if a["name"] == artist:
                        retList.append( t["external_urls"]["spotify"] )
                        counter += 1
                        if counter == 3:
                            return retList

                                    
        return retList


#test cases
pprint( keywordSearch("Maroon 5","Sunday Morning") )
#this returns ["spotify url1","spotify url2", ...]
print()
print()
#pprint( keywordSearch("Maroon 5","") )
#this returns [["track1","spotify url1"], ["track2","spotify url2"], ...]
print()
print()
#pprint( keywordSearch("","Sunday Morning") )
#this returns [["artist1,artist2,...","spotify url1"], ["artist1,artist2,...","spotify url2"], ...]

