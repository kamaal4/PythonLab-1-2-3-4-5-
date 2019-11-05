# Name: Mohd Mustafa Kamaal
# Roll no: 34
# Enrl no: A180571
# Batch: 1
C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(C," is a number list.\n")
def list_slice(S, step):
    return [S[i::step] for i in range(step)]
print(list_slice(C,3),"is a splited list.")
#S and step are arguments for function "list_slice"
#S is used for name of number list and step is used for Nth element.
