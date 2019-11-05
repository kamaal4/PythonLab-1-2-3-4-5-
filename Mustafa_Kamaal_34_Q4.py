# Name: Mohd Mustafa Kamaal
# Roll no: 34
# Enrl no: A180571
# Batch: 1
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print("Sorted list is :",sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
