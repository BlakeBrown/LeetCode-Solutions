# In my first attempt I tried converting the ip to binary and back, however it is a lot
# easier to work in decimal. The reason why decimal works really well
# is because once we determine how many addresses we can use for a given block,
# we can simply add to get to our next starting point.

# Solution 1: Create two functions to convert between CIDR and a decimal number
# Create the biggest CIDR block we can, add it to our answers list,
# update our base ip in decimal and repeat.
class Solution:
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        ans = []
        # Start by converting ip to decimal number
        number = self.ipToNumber(ip)
        while n > 0:
            # 1. Find number of addresses we can use
            addresses = 1
            for i in range(0, 31):
                if (addresses & number) or (addresses*2 > n):
                    break
                addresses *= 2
            # 2. Create a new CIDR block
            ans.append(self.numberToIp(number, 32-i))
            # 3. Increase decimal number and reduce n
            number += addresses
            n -= addresses
        return ans
        
    def ipToNumber(self, ip):
        nums = ip.split(".")
        total = 0
        for i in range(len(nums)):
            nums[i] = int(nums[i])
            total += (nums[i] << (24-i*8))
        return total
        
    def numberToIp(self, number, prefixBits):
        ip = ""
        bit = 1
        total = 0
        for i in range(0, 33):
            if i%8 == 0:
                if i == 8:
                    ip = str(total)
                elif i > 8:
                    ip = str(total) + "." + ip
                total = 0
            if bit & number:
                total += 2**(i%8)
            bit *= 2
        return ip + "/" + str(prefixBits)

# Solution 2 - We can simplify numberToIp to be more efficient
class Solution:
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        ans = []
        # Start by converting ip to decimal number
        number = self.ipToNumber(ip)
        while n > 0:
            # 1. Find number of addresses we can use
            addresses = 1
            for i in range(0, 31):
                if (addresses & number) or (addresses*2 > n):
                    break
                addresses *= 2
            # 2. Create a new CIDR block
            ans.append(self.numberToIp(number, 32-i))
            # 3. Increase decimal number and reduce n
            number += addresses
            n -= addresses
        return ans
        
    def ipToNumber(self, ip):
        nums = ip.split(".")
        total = 0
        for i in range(len(nums)):
            nums[i] = int(nums[i])
            total += (nums[i] << (24-i*8))
        return total
        
    def numberToIp(self, number, prefixBits):
        return str(number>>24 & 255) + "." + str(number>>16 & 255) + "." + str(number>>8 & 255) + "." + str(number&255) + "/" + str(prefixBits)