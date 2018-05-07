alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
database = {}

class Codec():
    
    import string
    import random
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        global alphabet
        global database
        
        shortUrl = 'http://tinyurl.com/'+''.join((random.choice(alphabet)) for x in range(6))
        database[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return database[shortUrl]
        

# Your Codec object will be instantiated and called as such:
#codec = Codec()
#codec.decode(codec.encode(url))

'''
Notes
1. Attention to the scope of variable. alphabet and database should be declared outside the class to be a global variable
'''