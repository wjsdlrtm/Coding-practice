class Solution(object):


    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def multiple_check(divider, target):
            while(target % divider ==0):
                target = target/divider
            return target
        if (num==0):
            return False
        dividers = [30, 15, 10, 5, 3, 2]
        for divider in dividers:
            num = multiple_check(divider, num)

        if(num==1):
            return True

        else:
            return False



