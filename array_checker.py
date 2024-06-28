
class Checker(object):
    def __init__(self, array):
        self.array = array
    
    def max_sums(self, start, end):
        #  Find the max_crossing_sum
        def find_max_csum(start, mid, end):
            # Initialize the left_sum, right_sum and temporary sum
            left_sum = float('-inf')
            right_sum = float('-inf')
            sum = 0
            
            # Find the maximum subarray sum on the left side of the midpoint
            for i in range(mid, start-1, -1):
                sum += self.array[i]
                if sum > left_sum:
                    left_sum = sum
            
            sum = 0
            # Find the maximum subarray sum on the right side of the midpoint
            for i in range(mid + 1, end + 1):
                sum += self.array[i]
                if sum > right_sum:
                    right_sum = sum
            
            return max(0, left_sum + right_sum)
        
        # Base case: single element
        if start == end:
            return max(0, self.array[start])
        
        mid = (start + end) // 2

        # Find the maximum recursively
        return max(self.max_sums(start, mid), self.max_sums(mid+1, end), find_max_csum(start, mid, end))
