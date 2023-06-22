class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        def check_array(num_array):
            result =  True
            for i in range(len(num_array)):
                result = result and num_array[0] <= num_array[i]
                if not result:
                    return False
            return result
        
        for window in range(1,n + 1):
            #print "window"+str(window)
            for i in range(n - window +1):
                #print nums[i:i + window]
                if window == 1:
                    result.append(nums[i])
                else:
                    if check_array(nums[i:i + window]):
                        result.append(nums[i:i + window])
        
        left = right = 0
        for left in range(n):
            for right in range(left, n):
                #result.append(nums[right])
                #print "left" +str(nums[left])
                #print "right"+str(nums[right])
                if nums[left] <= nums[right]:
                    result.append(nums[left:right+1])
                else:
                    break
        """
        n = len(nums)
        # stack with number and index
        stack = []
        answer = 0
        # going from right to left
        for i in range(n-1, -1, -1):
            # compare nums[i] against the num on stack [-1] (index 1 is the idx)
            while stack and nums[i] <= stack[-1][0]:
                stack.pop()
            # notice we grab all the sub arrays between both indexes n- i and stack - i
            if stack:
                answer += stack[-1][1] - i
            else:
                answer += n - i
            stack.append([nums[i], i])
        return answer