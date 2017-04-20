def hanoi(n,a,b,c):  
  
    if n==1:  
        print(a,'->',c)  
    else:  
        hanoi(n-1,a,c,b)    #前n-1个由a借助b移动到c 递归借用hanoi函数  
        hanoi(1,a,b,c)  
        hanoi(n-1,b,a,c)  
x=int(input("shurupanzishu: "))  
  
hanoi(x,'a','b','c')  
