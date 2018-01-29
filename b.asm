section .data
	a dd 12,232,3676,41,5,6,7
	i dq 1.2,2.3
        string db "this is my string",9,0
	len equ $-string
	count dq 1.0
section .bss
	b resd 1
section .text
	global main
	extern puts
main:
	mov ebx,24
        mov ebx,ecx
        mov dword[b],12
	mov dword[b],ebx
	mov eax,ebx
        mov ecx,edx
        mov edx,12
        mov ecx,edx
	dec edi
	jmp lp
	
lp:	 mov ebx,dword[b]
lp1:     add eax,ebx
         sub eax,ebx
        
