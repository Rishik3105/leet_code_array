class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if i[-1] == target:
                return target
            elif i[-1] > target:
                mid=len(i)/2
                if i[mid] == target:
                    return target
                elif i[mid] > target:
                    while mid !=0:
                        if i[mid] == target:
                            return target
                        mid -=1
                    if i[0] == target:
                        return target
                elif i[mid] < target:
                    while mid < len(i):
                        if i[mid] == target:
                            return target
                        mid+=1
