#Search in a Rotated Sorted Array

class Solution(object):
    def search(self, nums, target):

        def pivotpoint(nums):
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return i+1
                
            return -1
                
        def bin(nums,target):
            
            left = 0
            right= len(nums)-1
            
            while(left<=right):
                mid = int(left + (right-left)/2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                
            return -1
            
            
        pivot = pivotpoint(nums)
        
        if target == nums[0]:
            ans = 0
        elif target == nums[len(nums)-1]:
            ans = len(nums)-1
        
        elif pivot == -1:
            ans = bin(nums,target)
        
        elif target < nums[0]:
            ans = bin(nums[pivot:],target)
            print(ans)
            if ans != -1:
                ans = ans + len(nums[:pivot])
        elif target > nums[len(nums)-1]:
            ans = bin(nums[:pivot],target)
        
        else:
            return -1
        return ans