

#file=file, --makefile=FILE
import sys
import a.json
import macros.py from macro.asm
import ASSEMLER  from b.asm
from tab_errer import


def my_make(lst):
    for i in range(lst):
        if lst[i]=='':
            print 'error'
        elif lst[i]=='python ASSEMLER.PY':
            if 'b.asm' in lst:
                print 'a.out'
        elif lst[i]=='macros.py':
            print 'give a asm file'
        elif lst[i]=='macros.py macro.asm':

    while(macro_index):
        i = macro_index.pop()
        tup=Proces(lines,i,macro_index,mnt,mdt,n)
        macro_index=tup[0]

        if lines[tup[1]][0]=='section':
         j=tup[1]
         break
     elif macro_index==[]:
         macro_index+=[tup[1]]



#file=file, --makefile=FILE
file = open(sys.argv[1])
makefile = file
my_make(makefile)
