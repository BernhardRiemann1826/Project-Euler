def sum_of_multiples(limit, p1=3, p2=5):
  n, sum = 1, 0
  while n < limit:
    if n % p1 * p2 == 0 or n % p1 == 0 or n % p2 == 0:
      sum += n
    n += 1
  print(sum)
  
sum_of_multiples(1000)
