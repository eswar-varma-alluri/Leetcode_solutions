class Solution(object):
    def subarraySum(self, nums, k):
        p=0
        a=0
        freq={0:1}
        for num in nums:
            p+=num
            n=p-k
            if n in freq:
                a+=freq[n]
            if p in freq:
                freq[p]+=1
            else:
                freq[p]=1
        return a