amount = []

count = int(input("enter the total spending categories:"))

for categories in range(count):
  spending = int(input(f"Enter expense {categories + 1} :"))
  amount.append(spending)

print(amount)

def total_amount():
  total = 0
  for i in amount:
    total += i
  return total

total_amount_value = total_amount()

print(f"Total expense is {total_amount_value}")


def highest():
  h_value = amount[0]
  i = 1
  for i in range(len(amount)):
    if amount[i] > h_value:
      h_value = amount[i]
  return h_value

maximum_amount = highest()   

print(f"Highest expense is {maximum_amount}")

def average():

  avg = total_amount_value/len(amount)
  return avg

avg_value = average()

print(f"The average spending is {avg_value}")

