# coding = utf-8
#!/usr/bin/python
L = range(1, 101)

print L[0:10]
print L[2::3]
print L[4:51:5]

L = range(1, 101)
print L[-10::]
print L[-46::5]

def firstCharUpper(s):
    return s[0:1:1].upper()+s[1::1]

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')