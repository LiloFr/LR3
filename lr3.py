def input_f():
  while True:
    n=int(input('Введите натуральное число'))
    if n>0:
      break
    print('Неверные данные')
  return n



def x2(n):
  return collatz(n//2)


def x3_1(n):
  return collatz(n * 3 + 1)


def collatz(n):
  num = [n]
  if n == 1:
    pass
  elif n % 2 == 0:
    num.extend(x2(n))
  else:
    num.extend(x3_1(n))
  return num


if __name__ == '__main__':
  x = input_f()
  print(collatz(x))
