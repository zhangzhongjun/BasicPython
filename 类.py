# coding=utf-8

# 定义一个Person类
class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1,lambda p1,p2:cmp(p1.name,p2.name))

print L2[0].name
print L2[1].name
print L2[2].name

# __开头的属性，私有属性，不能被外界访问到
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print p.name
# 静态属性
class Person(object):
    count=0
    def __init__(self,name):
        self.name = name
        Person.count = Person.count + 1

p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count

# 在前面加上__ ,静态属性__count，使得无法从外部获取到静态属性
class Person(object):
    __count = 0
    def __init__(self, name):
        self.name = name
        Person.__count += 1
        print Person.__count
p1 = Person('Bob')
p2 = Person('Alice')

# 私有属性__grade，使用一个内部的实例方法get_grade()访问
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    def get_grade(self):
        if self.__score>=90:
            return "A"
        elif self.__score>60:
            return 'B'
        else:
            return "C"
p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)
print p1.get_grade()
print p2.get_grade()
print p3.get_grade()

# 利用@classmethod定义类方法
class Person(object):
    __count = 0
    @classmethod
    def how_many(cls):
        return cls.__count
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        Person.__count += 1
print Person.how_many()
p1 = Person('Bob',u"女")
print Person.how_many()
# 总是继承一个类，如果没有，就继承object
# 函数super(Student,self)返回Student的父类，即Person类
class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender);
        self.score = score
s = Student("John",u"男",123)
print s.name
print s.gender
print s.score
# 使用getattr获得某个实例上的某属性的值 setattr设置某个实例上的某属性的值
print getattr(s,"name")
setattr(s,"name","Mark")
print getattr(s,"name")
# 多态，动态语言，不检查类型
import json
class Students(object):
    def read(self):
        return r'["Tim","Bob","Alice"]'

s = Students()
print json.load(s)
# 可以接收无限多参数的构造方法
class Person(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k,v in kw.iteritems():
            setattr(self,k,v)

p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course
#python中的特殊方法
# 用于print()的__str__()方法 用于len()的__len__()方法 用于cmp()的__cmp__()方法
# __repr__()方法和__str__()方法的作用类似，前者是给开发人员用的，后者是给用户用的
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def __str__(self):
        return "<Student:%s, %s, %i>" %(self.name,self.gender,self.score)
        
    def __repr__(self):
        return "<Student:%s, %s, %s>" %(self.name,self.gender,self.score)
s = Student('Bob', 'male', 88)
print s

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__
    def __cmp__(self, s):
        if self.score<s.score:
            return 1
        elif self.score>s.score:
            return -1
        else: return cmp(self.name,s.name)

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)
# __len__()方法使得类表现的像一个List一样
class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print f
print len(f)
# 有理数的加减乘除 需要实现__add__() __sub__() __mul__() __div__()
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)
    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)
    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)
    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2
#
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return float(self.p) / self.q
print int(Rational(7,2))
print float(Rational(7, 2))
print float(Rational(1, 3))
# 使用__slot__()方法来限制一个类的属性
class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    __slots__ = ('name','gender','score')

    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score = score

s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score
# __call__()方法可以使得类变成一个可调用对象
class Fib(object):
    def __call__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        return L

f = Fib()
print f(10)

# __init__()方法可以对对象进行初始化
class Person(object):
    def __init__(self,name,score,**kw):
        self.name = name
        self.score = score
        for k,v in kw.iteritems():
            setattr(self,k,v)
p=Person("John",123,sex=u'男')
p1 = Person("Mark",12,job=u'经理')
print p.sex
print p1.job
