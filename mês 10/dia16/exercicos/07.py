def fibonacci(n):
  fib_list = [0, 1]
  while len(fib_list) < n:
    next_num = fib_list[-1] + fib_list[-2]
    fib_list.append(next_num)

  return fib_list

print(fibonacci(10))