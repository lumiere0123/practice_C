d=[{1:10}, {2:20}, {1:30}]
# {1:[10,30], 2:[20]}

new_d={}

#for item in d:
#    for key in item:
#        if key not in new_d:
#            new_d[key] = [item[key]]
#        else:
#            new_d[key].append(item[key])
#


for item in d:
    for key in item:
        new_d.setdefault(key, []).append(item[key])


print(new_d)



d2=[[1,10], [2,20], [1,30]]
# {1:[10,30], 2:[20]}

new_d2={}


for item in d2:
    new_d2.setdefault(item[0],[]).append(item[1])



print(new_d2)





