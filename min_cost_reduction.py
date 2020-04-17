import heapq


def reductionCost(num):
    # Write your code here
    heapq.heapify(num)
    summ = []

    while len(num) > 1:
        first_num = heapq.heappop(num)
        second_num = heapq.heappop(num)
        summ.append(first_num + second_num)
        heapq.heappush(num, first_num + second_num)

    return sum(summ)


num = [1, 2, 3, 4]
print(reductionCost(num))
