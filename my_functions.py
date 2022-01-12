# to get arbitrary number of integer from input command
def my_get_int(split_char=' '):
    a = list(map(int, input().split(split_char)))
    return a


# this is a function used for slicing in 2D python list
def list_2D_slicing(l_2D,row_start,num_row,col_start,num_col):
    res=[]
    for i in range(num_row):
        for j in range(num_col):
            res.append(l_2D[row_start+i][col_start+j])
    return(res)

# to check if a list is included in a bigger list
def Sub_list(main_list,sub_list):
    count=0
    for x in sub_list:
        if x in main_list:
            count+=1
    if count==len(sub_list):
        return 1
    else:
        return 0
		

# to find number of times that a string(key) is repeated into another string(s)
def num_of_substr(s,key,start):
    num=0
    flag=len(s)

    while flag:

        ind=s.find(key,start)
        if ind>=0 :
            num+=1
            start=ind+1
        else:
            flag=0
    return(num)


# how to create a 2D empty array with a specific size
def array_2D_empty(n,m):
    
    res=[]
    for i in range(n):
        res.append([[]]*m)

    return(res)

def fibo(n):
    res=[]
    if n==1:
        res.append(1)
    elif n==2:
        res.append(1)
        res.append(1)
    else:
        res=[1,1]
        for i in range(2,n):
            res.append(res[-1]+res[-2])
    return(res)




if __name__ == "__main__":
    
    a=my_get_int()
    print(a)