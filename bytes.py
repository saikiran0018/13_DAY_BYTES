a=b"python"
print(a,type(a))                       # b'python' <class 'bytes'>
print(list(a))                          # [112, 121, 116, 104, 111, 110] 
print(tuple(a))                         # (112, 121, 116, 104, 111, 110)  
print(set(a))                           # {104, 110, 111, 112, 116, 121}

a=b"array"
print(list(a))                             # [97, 114, 114, 97, 121]

y=b"python"
for i in y:
    print(i)                              # vertical 112 121 116 104 111 110

print(ord('p'))                               # 112
print(chr(80))                                 # p

p=b"python"
p[0]=80                                      # TypeError: 'bytes' object does not support item assignment

a=b'[1,2,3]'
print(list(a))                                 # [91, 49, 44, 50, 44, 51, 93]

print(ord('['))                                # 91
print(ord(','))                                # 44
print(chr(91))                                 # [
m=bytearray(b"python")
print(m)                                       # bytearray(b'python')
print(m[0])                                    # 112
m[0]=80
print(m)                                       # bytearray(b'Python')

m=bytearray("pyton")
print(m)                                        # TypeError: string argument without an encoding




