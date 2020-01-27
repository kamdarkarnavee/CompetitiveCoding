N = [5,4,3,2,1,4,7,8,9,10]
K = 4
# N = [1,4,3,2,5,4]
ans = []
max = []

def solution(N, K):
  """Your solution goes here."""
  def compare(l1, l2):
    for i in range(K):
        if l1[i] != l2[i]:
            if l1[i] > l2[i]:
                return l1
            else:
                return l2
        else:
            return l1

  if len(N) >= K:
    max = N[:K]

  for i in range(len(N)-K):
    j = i+1
    l1 = N[j:j+K]
    ans = compare(max, l1)
    max = compare(ans, max)

  return max

print(solution(N,K))