
%macro a 2
    mov eax,%1
    %%abc: mov ebx,%2
	%macro e 2
        	mov eax,%1
	        mov ebx,%1
			%macro c 2
			    mov eax,%1
				mov ebx,%2
			%endmacro
	        add eax,ebx
	%endmacro
	jmp %%abc
%endmacro


%macro b 2
   mov eax,2
%endmacro   


section .text
     global main
main:
     mov eax,1
     mov ebx,3
     a 12,13
     a 12,15
     
    

