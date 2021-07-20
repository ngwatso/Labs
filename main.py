# Find all the pairs of two integers in an unsorted array that sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.

def findSum(arr, S):

  res = []
  pair = []

  for i in arr:

    for j in arr:

      if j == i:
        continue
      
      if i + j == S:
        pair.append(i)
        pair.append(j)

        res.append(pair)
        pair = []
      
        arr.remove(i)
        arr.remove(j)

  return res

print(findSum([3, 5, 2, -4, 8, 11], 7))