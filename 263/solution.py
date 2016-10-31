class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num==0):
            return False
        while(num % 30 == 0):
            num = num/30
        while(num % 15 == 0):
            num = num/15
        while(num % 10 == 0):
            num = num/10
        while(num % 6 == 0):
            num = num/6

        while(num % 5 == 0):
            num = num/5

        while(num % 3 ==0):
            num = num/3

        while(num % 2 ==0):
            num = num/2

        if(num==1):
            return True

        else:
            return False

