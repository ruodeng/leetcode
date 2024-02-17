from collections import namedtuple
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        Job = namedtuple('Job', ('start','end','profit'))
        jobs = sorted([Job(startTime[i], endTime[i], profit[i]) for i in range(n)])



        nextPossJob = [n]*n
        # startorder_i will iterate through jobs in order of startTime (how jobs is ordered)
        # endorder_i will iterate through jobs in order of endTime
        startorder_i = 0
        for endorder_i in sorted(range(n), key=lambda x:jobs[x].end):
            while startorder_i < n and jobs[endorder_i].end > jobs[startorder_i].start:
                startorder_i += 1
            if startorder_i == n:
                break
            nextPossJob[endorder_i] = startorder_i

        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            # Two possibilities: use the current job at i or skip to next job
            dp[i] = max(jobs[i].profit + dp[nextPossJob[i]], dp[i+1])
        return dp[0]  