"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
  if x <= 1:
      return x
  else:
      return foo(x-1) + foo(x-2)
    

def longest_run(mylist, key):
    ### TODO
    length = 0
    count = 0
    for num in mylist:
      if num == key:
        count+=1
        length = max(length, count)
      else:
        count = 0
    return length
        

  

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    ### TODO
    if len(mylist) == 1:
      if mylist[0] == key:
          return Result(1, 1, 1, 1)
      else:
          return Result(0, 0, 0, 0)
    mid = len(mylist)//2
    left = longest_run_recursive(mylist[:mid], key)
    right = longest_run_recursive(mylist[mid:], key)

    longest = max(left.longest, right.longest, left.right_run + right.left_run)
    left_run = left.left_run if left.left_run == mid else 0
    right_run = right.right_run if right.right_run == len(mylist) - mid else 0
    total_run = left.total_run + right.total_run

    return Result(longest, left_run, right_run, total_run)


