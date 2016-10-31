class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        one = 0
        two = 0
        two = n/2
        one = n%2
        def factorial(n):
            fac = 1
            for i in range(1, n + 1):
                fac *= i
            return fac
        for i in range(0, two+1):
            result += (factorial(one+two)/(factorial(one)*factorial(two)))

            two -= 1
            one += 2

        return result
