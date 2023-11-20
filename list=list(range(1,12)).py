proviness =['广东','四川','山东']
cities=['广州','深圳','惠州','珠海'],['成都','内江','乐山','绵阳'],['青岛','济南','德州','菏泽']
def findCities(p):
    c=[]
    for i in range(0,len(proviness)):
        if p in cities[i]:
            return proviness[i]
    return c

print(findCities('山东'))
print(findCities('青岛'))                   