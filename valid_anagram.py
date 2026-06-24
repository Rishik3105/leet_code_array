class Solution(object):
    def isAnagram(self, s, t):
        s_sorted=sorted(s)
        t_sorted=sorted(t)
        if s_sorted == t_sorted:
            return True
        else:
            return False
        
