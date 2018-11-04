# coding=utf-8
def get_num(source_list):
    ret_list = []
    if not isinstance(source_list,list):
        print("please enter list type parameter")
    else:
        for i in source_list:
            if not isinstance(i,int):
                print('list memter must int type')
            elif i%2==0:
                ret_list.append(i)
    return ret_list
tmp = get_num([2,4,6,8])
print(tmp)
print('122')
