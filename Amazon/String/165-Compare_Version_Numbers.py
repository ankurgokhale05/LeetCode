# String Manipulation problem
# We split the string by '.' and then check integer value of every part of the string. 
# We also add trailing zeros at the end of version depending upon whether they are smaller in length when compared with other version number.
# Time Complexity: O(n) as we iterate through atleast 1 version.
# Space Complexity: O(n) as we take zeroadd array.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        zeroadd = []
        version1 = version1.split('.')
        version2 = version2.split('.')
        n = len(version1)
        if len(version1) > len(version2):
            zeroadd = [0] * (len(version1) - len(version2))
            version2 += zeroadd
        if len(version2) > len(version1):
            zeroadd = [0] * (len(version2) - len(version1))
            version1 += zeroadd
        for i in range(len(version1)):
            if int(version1[i]) == int(version2[i]) and i != n-1:
                continue
            if int(version1[i]) > int(version2[i]):
                return 1
            if int(version1[i]) < int(version2[i]):
                return -1
        return 0
            