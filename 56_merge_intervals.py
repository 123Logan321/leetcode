import sys

intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()
ans = []
ans.append(intervals[0])

for i in intervals[1:]:
    if ans[-1][0] <= i[0] <= ans[-1][-1]:
        ans[-1][-1] = max(i[-1], ans[-1][-1])
    else:
        ans.append(i)

print(ans)