# Author: Kyle Kroboth kjk5884@psu.edu
# Collaborator: Shravani Samala sjs7049@psu.edu
# Collaborator: Mackenzie Johnson mlj5382@psu.edu
# Collaborator: Luke Bowman lkb5453@psu.edu
# Section: 2
# Breakout: 1

def sum_n(n):
  if n==0:
    return(0)
  else:
    return(n + sum_n(n-1))

def print_n(s,n):
  if n==0:
    return(0)
  else:
    print(s)
    print_n(s, n-1)
def run():
  total = int(input("Enter an int: "))
  print("sum is: " + str(sum_n(total)))
  words = input("Enter a string: ")
  print_n(words,total)


if __name__ == "__main__":
  run()