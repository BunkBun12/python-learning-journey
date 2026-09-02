# 2 x 2 matrix

matrix_a = [
  [1,2],
  [2,1]
]

matrix_b = [
  [1,2],
  [4,3]
]

result = [
  [0,0],
  [0,0]
]

print(matrix_a)
print(matrix_b)

for i in range(len(matrix_a)):
  for j in range(len(matrix_b)):
    result[i][j] = matrix_a[i][j] + matrix_b[i][j]

print(result)