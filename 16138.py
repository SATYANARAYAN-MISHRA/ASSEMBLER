import sys

class mdt:
    def __init__(self):
        self.index=0
        self.ins=[]
    def SHOW(self):
        print self.ins


class mnt:
    def __init__(self):
        self.lst=[]
    def SHOW(self):
        for i in self.lst:
            print i




def Search(line,mnt):
    ff=([x for x in mnt.lst if x[0]==line[1] and x[1]==line[2]])
    n=len(ff)
    if n>0:
        return 1
    else:
        return 0




def Proces(lines,i,macro_index,mnt,mdt,n):
    macro_count=0
    index=0
    flag=0
    l=0
    for k in range(i,n):
        line = lines[k]
        m=len(line)
        if line[0]=='section':
            l=k
            break
        elif line[0]=='section' and flag==1:
            print "< syntax error in macros >"
            sys.exit()
        elif m==3 and line[0] == '%macro' and flag==0:
           if Search(line,mnt):
               print "< macro > "+line[1]+" < Redefined Inside itself with same no of arguments or other else>"
               sys.exit()
           else:
               mnt.lst+=[[line[1],line[2],mdt.index+1]]
               index=mdt.index
               flag=1
        elif m==3 and line[0] == "%macro" and flag==1:
            macro_count+=1
            if k not in macro_index:
                macro_index.insert(0,k)
        elif m==1 and line[0] == "%endmacro" and macro_count==0 and flag==1:
            #index+=1
            mdt.index=index
            mnt.lst[-1]+=[index]
            mnt.lst[-1]+=[0]
            flag=0
            l=k
            break
        elif m==1 and line[0] == "%endmacro" and macro_count!=0 and flag==1:
            macro_count-=1
        else:
            print line
            if flag==1 and macro_count==0:
                mdt.ins+=[line]
                index+=1

    return (macro_index,l)



def tokenize(line):
    line=filter(lambda x:x!='',line)
    n=len(line)
    if n==2:
        line[0]=line[0].split(':')
        line[1]=line[1].split(',')
    elif n==3:
        line[0]=line[0].split(':')
        line[1]=[line[1]]
        line[2]=line[2].split(',')
    elif n==4:
        line[0].split(':')
        line[1].split(',')
        line[2]=(''.join(line[2:])).split(',')
    line = filter(lambda a:a!='',[x for j in line for x in j])
    return line



def convert(mdt,k,line,cnt,mnt,z):
    n=len(line)
    x=[]
    m=mnt.lst.index(z)
    mnt.lst[m][4]+=1


    ins=mdt.ins[k]
    for i in ins:
        if i[0]=="%" and i[1]=="%%":
            x+=[i+str(cnt)]
        elif i[0]=="%" and i[0]!="%":
            print i,line
            x+=[line[int(i[1:])]]
        else:
            x+=[i]
    return x





def Proces2(Expended,line,mnt,mdt):
    print line[0]

    z=[x for x in mnt.lst if x[0]==line[0]]
    if z!=[]:
        for k in range(z[0][2]-1,z[0][3]-1):
            Expended+=[convert(mdt,k,line,z[0][1],mnt,z[0])]
    else:
        Expended+=[line]
    return Expended



mnt=mnt()
mdt=mdt()
file = open(sys.argv[1])
#file = make(sys.argv[1])
text = file.read()
lines = text.split('\n')
n = len(lines)


z=map(lambda y:filter(lambda c:c!='',y),map(lambda x:x.split(' '),lines))
lines=map(lambda a:map(lambda f:filter(lambda v:v!='\t',f),a),(filter(lambda x:x!=[],z)))
print lines
lines=filter(lambda x:x!=[],lines)
j=0
n=len(lines)
macro_index=[0]
while(macro_index):
    i = macro_index.pop()
    tup=Proces(lines,i,macro_index,mnt,mdt,n)
    macro_index=tup[0]
    if lines[tup[1]][0]=='section':
        j=tup[1]
        break
    elif macro_index==[]:
        macro_index+=[tup[1]]


m=lines.index(['main:'])
Expended=[]
Expended+=map(lambda x:tokenize(x),lines[m:])
mdt.ins=map(lambda x:tokenize(x),mdt.ins)



for i in range(m+1,n):


    lines[i]=filter(lambda x:x!='',lines[i])
    Expended=Proces2(Expended,lines[i],mnt,mdt)

print Expended


mnt.SHOW()
mdt.SHOW()











