import os
with open("c.txt",'rb') as f:
    a1 = reversed(f.readlines())
for line in a1:
    line=(line.strip())
    line = line.decode(encoding='big5', errors='ignore').strip()
    print (line)
    line=line.strip()
    cur_path = os.path.abspath(os.curdir)
    line = line.replace('C:', '\C')
    line = line.replace('D:', '\D')
    line = line.replace('E:', '\E')
    print (line)
    all=cur_path+line
    (a, b) = os.path.split(all)
    c = os.path.exists(a)
    if "." in b:
        if not c:
            #try:
                os.makedirs(a)
           # except IOError:
                #pass
            #try:
                file = open(all, 'w')
                file.close()
            #except IOError:
               # pass
        else:
            #try:
                file = open(all, 'w')
                file.close()
            #except IOError:
                #pass

    else:
        continue


