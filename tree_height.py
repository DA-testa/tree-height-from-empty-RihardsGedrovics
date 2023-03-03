#def compute_height(n, parents):
    # Write this function
#    max_height = 0
    # Your code here
#    return max_height

#def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
#    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.

#main()
# print(numpy.array([1,2,3]))

import os
import sys
import threading

def height(tree):
    depth_list = [1]*len(tree)
    for i, n in enumerate(tree):
        while n != -1:
            depth_list[i] += 1
            n = tree[n]
               
    return max(depth_list)

def main():
    try:
        inp=str(input())

        if "I" in inp:
            nodes=int(input())
            parents = list(map(int, input().split(" ")))
                        
            return print(height(parents))
    
        if "F" in inp:
            file_name = input()
        
            if "a" not in file_name:
                script_dir=os.path.dirname(os.path.abspath("__file__"))
                rel_path="test/"+file_name
                with open(rel_path, "r") as f:
                    lines=f.readlines()
                
                    # if 1<=int(lines[0])<=105:
                    nodes=lines[0]
                    parents= lines[1]
                    lst=[int(x) for x in parents.strip().split(" ")]
                    return print(height(lst))
                                
            else:
                pass
    except EOFError as e:
        pass
            
main()
         
sys.setrecursionlimit(10**8)  # max depth of recursion
threading.stack_size(2**28)   # new thread will get stack of such size
threading.Thread(target=main).start()