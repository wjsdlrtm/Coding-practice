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
        num = multiple_check(30, num)
        num = multiple_check(15, num)
        num = multiple_check(10, num)
        num = multiple_check(5, num)
        num = multiple_check(3, num)
        num = multiple_check(2, num)

        if(num==1):
            return True

        else:
            return False

