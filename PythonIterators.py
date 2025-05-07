nums = [1, 2, 3, 4, 5, 6]

for i in nums:
    print(i)

iterate = iter(nums)
print(iterate)
print(iterate.__next__())
print(iterate.__next__())
print(iterate.__next__())
print(next(iterate))

string = "WsCube Tech"

for j in string:
    print(j)

str_iterate = iter(string)    
print(str_iterate.__next__())
print(next(str_iterate))
print(next(str_iterate))


class Fantastic_Five:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        # if self.num<=10:
        if self.num<=5:
            value = self.num
            self.num+=1
            return value
        else:
            raise StopIteration
        
FF = Fantastic_Five()
print(FF)

for k in FF:
    print(k)