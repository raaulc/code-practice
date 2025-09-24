def all_the_subsequence(mystring, target, answer, index=0):
    if index >= len(mystring):
        # when to stop and get the subsequence 
        answer.append(target)
        return
    
    # my case 
    # one char operation - include or exclude
    ch = mystring[index]
    # recursion 
    # include
    all_the_subsequence(mystring, target + ch , answer, index+1)
    # exclude
    all_the_subsequence(mystring, target , answer, index+1)
    
answer = []
all_the_subsequence("hello", "", answer)
print(answer)