
def num_to_8bit_bin(num):
    arr = ['0','0','0','0','0','0','0','0']
    arr[0]='1'

    x = ''.join(arr)
    print(x)
    temp = int(num) #if passing num as string
    print(arr)


def rev_str(str):
    return str[::-1]



a = '192.168.1.10'
b = '255.255.255.0'
str = 'hi there'

num_to_8bit_bin(10)
# print(f'reverse of string: {rev_str(str)}')

lst1 = a.split(sep='.')
lst2 = b.split(sep='.')


# for x in range(0,len(lst1)):
#     print(lst1[x])
#     print(type(lst1[x]))