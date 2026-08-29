class Solution(object):
    def ispossible(self,nums,days,mid):
        load=0
        rdays=1
        for w in nums:
            if load+w <=mid:
                load+=w
            else:
                load=w
                rdays+=1
        return rdays<=days
    def shipWithinDays(self, nums, days):
        l=max(nums)
        h=sum(nums)
        while l<h:
            mid=(l+h)//2
            nd= self.ispossible(nums,days,mid)
            if nd:
                h=mid
            else:
                l=mid+1
        return h