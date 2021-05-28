# lp3thw p.141

for i in (1, 2, 3, 4,):
  print("\ni =", end=' ')
  print(i, end='')

print("\ni after the for loop =", i)

for j in (1, 2, 3, 4,):
  print("\nj =", end=' ')
  if 2 < j:
    continue
  print(j, end='')

print("\nj after the for loop =", j)
