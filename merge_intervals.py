
def merge(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort()

    ans = []
    current_interval = intervals[0]
    ans.append(current_interval)

    for i in intervals:
        if current_interval[1] >= i[0]:
            current_interval[1] = max(current_interval[1], i[1])
        else:
            current_interval = i
            ans.append(current_interval)
    return ans




print(merge([[1,4],[0,2],[3,5]]))
print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))