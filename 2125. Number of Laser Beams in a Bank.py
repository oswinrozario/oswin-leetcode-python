class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # # method - 1, simple iterate
        # answer = 0
        # previous_row_count_one = 0
        # for i in range(0,len(bank)):
        #     count_one = 0
        #     for j in range(len(bank[i])):
        #         if(bank[i][j] == '1'):
        #             count_one += 1
        #     if(count_one > 0):
        #         answer += (count_one * previous_row_count_one)
        #         previous_row_count_one = count_one
        # return answer

        # method - 2, shorter solution
        previous_row_count_one = 0
        answer = 0
        for s in bank:
            count_one = s.count('1')
            if(count_one):
                answer += (count_one * previous_row_count_one)
                previous_row_count_one = count_one
        return answer

        