import os
for i in range(10000):
    with open(str(i)+".txt","w") as f:
        for a in range(50):
            f.write(str(a))


import os
list=os.listdir()
for i in list:
    os.remove(i)