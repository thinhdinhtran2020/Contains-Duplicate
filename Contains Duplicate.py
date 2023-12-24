class Solution:
    def containsDuplicate(self, nums):
        nums_sorted = sorted(nums)
        for i in range(len(nums_sorted)):
            if (i+1) != len(nums_sorted):
                if nums_sorted[i] == nums_sorted[i+1]:
                    return True
        return False

def main():
    solution = Solution()
    print(solution.containsDuplicate([1,2,3,4]))
main()