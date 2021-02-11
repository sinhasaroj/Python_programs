import re

x ='Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.'

# clnstr = re.sub(r'\W',' ',x)

# res = Counter(x)

# print(res)

# # print(clnstr)

res = x.split()

str2 = []

d = {}

for i in res:
    if i not in str2:
        str2.append(i)

for i in range(len(str2)):
    # print(f'{str2[i]}:{res.count(str2[i])}')
    x_ = str2[i]
    y_ = res.count(str2[i])

    d[x_] = y_

# print(d)

# result = sorted(d,key = lambda i:d[i],reverse=True)

# print(result)

sort_values = sorted(d.items() , key = lambda kv : kv[1], reverse=True)

print(dict(sort_values))


