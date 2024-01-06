class Solution:

    # logic -- 
    # if odd
    # 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39
    # - 1 2 3 3 4  5  5  6  7  7. 8. 9  9  10 11 11 12 13 13

    # if even
    # 2 4 6 8 10 12 14 16 18 20
    # also works for even

    # if n%3 == 0 
    #     then 
    #         ans = n/3
    # else 
    #     n-2 % 3 == 0
    #         ans = (n-2)/3 + 1
    # else 
    #     (n-4)/3 + 2

    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        element_frequencies = Counter(nums)
        for key,value in element_frequencies.items():
            if value == 1:
                answer = -1
                break
            else:
                if value%3 == 0:
                    answer += value/3
                elif (value-2)%3 == 0:
                    answer += ((value-2)/3 + 1)
                else:
                    answer += ((value-4)/3 + 2)
        return int(answer)


        