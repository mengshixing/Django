#sort 折半插入排序,用于对一个已经排序完毕的数组 加入一个新元素

#折半插入排序
def insertsort(timearr,item):
    if len(timearr)==1:
        timearr.append(item) if item>timearr[0] else timearr.insert(0,item)
    else:
        middle(timearr,0,len(timearr)-1,item)
#折半插入排序递归方法        
def middle(timearr,start,end,item):
    if end-start==1:
        if item>timearr[start]:
            timearr.append(item) if item>timearr[end] else timearr.insert(end,item)
        else:
            timearr.insert(start,item)
    else:
        middle(timearr,start,(start+end)//2,item) if timearr[(start+end)//2]>item else middle(timearr,(start+end)//2,end,item)