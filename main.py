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
    # Base case: If the list has only one element
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    mid = len(mylist) // 2
    left = longest_run_recursive(mylist[:mid], key)
    right = longest_run_recursive(mylist[mid:], key)

    # Check if the longest sequence can be extended from the left to the right
    longest_size = max(left.longest_size, right.longest_size, left.right_size + right.left_size)

    # Check if the entire range is a continuous sequence of the key
    is_entire_range = left.is_entire_range and right.is_entire_range and mylist[0] == key and mylist[-1] == key

    return Result(longest_size, left.left_size, right.right_size, is_entire_range)



