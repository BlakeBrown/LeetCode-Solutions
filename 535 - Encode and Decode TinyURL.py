# Solution 1: Use two hashtables so we can lookup longUrl and shortUrl in O(1)
# To encode we can just increment a counter

# Problems with this approach (creds to StefanPochmann in LeetCode discussions):
# - People can find out how many URLs have already been encoded. Not sure I want them to know.
# - People might try to get special numbers by spamming me with repeated requests shortly before their desired number comes up.
# - Only using digits means the codes can grow unnecessarily large. Only offers a million codes with length 6 (or smaller). Using six digits or lower or upper case letters would offer (10+26*2)6 = 56,800,235,584 codes with length 6.
class Codec:
    def __init__(self):
        self.count = 0
        self.longLookup = {}
        self.shortLookup = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.longLookup:
            return self.longLookup[longUrl]
        else:
            self.longLookup[longUrl] = self.count
            self.shortLookup[self.count] = longUrl
            self.count += 1
            return self.count-1

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.shortLookup[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

# Solution 2: Better to use random strings as keys. If we've generate a random string
# that we've previously encountered, just generate a new one.
