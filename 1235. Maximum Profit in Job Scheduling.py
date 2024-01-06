from ast import List, Tuple
from bisect import bisect_left


class Solution:

    def max_profit(self, index, totalJobs, jobs: List[Tuple[int, int]], startTime: List[int], dp: List[int]):
        if(index >= totalJobs):
            return 0
        if(dp[index] != -1):
            return dp[index]
        next_job = bisect_left(startTime,jobs[index][1])
        profitIncludingCurrJob = jobs[index][2] + self.max_profit(next_job, totalJobs, jobs, startTime, dp)
        profitNotIncCurrJob = self.max_profit(index+1,totalJobs, jobs, startTime, dp)

        dp[index] = max(profitIncludingCurrJob,profitNotIncCurrJob)
        return dp[index]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        totalJobs = len(startTime)
        dp = [-1] * totalJobs
        jobs = sorted(zip(startTime, endTime, profit))
        startTime.sort()
        return self.max_profit(0, totalJobs, jobs, startTime, dp)

        