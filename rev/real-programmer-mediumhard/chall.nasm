section .data
    prompt db "YO YO YO, I BET YOU CANT GET THIS SUPER NEAT FLAG!111!1!11!!", 0xa, ">>> ", 0
    prompt_len equ $ - prompt

    correct db "Correct", 0

    interesting db 0x89, 0xab, 0xf2

    secret db 0xed, 0xcb, 0x93, 0xff, 0xcf, 0x8b, 0xc0, 0xc5, 0xc3, 0xd8, 0xd1, 0xc3, 0xec, 0x9d, 0xa1, 0xdb, 0x9c, 0xa0, 0xbc, 0xdb, 0xaf, 0xef, 0x9d, 0xc3, 0xdc, 0xf6, 0x9e, 0xbb, 0x9e, 0xaf, 0xe7, 0x9c, 0x9b, 0xbc, 0xf6, 0xc7, 0xc3, 0x9c, 0x83, 0xd8, 0x9d, 0x9e, 0xbc, 0xd8
    secret_len equ $ - secret          ; Calculate the length of the secret byte string

section .bss
    flag resb 128

section .text
    global _start                ; Entry point for the program

_start:
    ; Print the prompt (>>>)
    mov rax, 1                    ; sys_write system call number (1)
    mov rdi, 1                    ; File descriptor 1 (stdout)
    mov rsi, prompt               ; Pointer to the prompt string
    mov rdx, prompt_len           ; Length of the prompt string
    syscall                       ; Call kernel (syscall)

    ; Read user input (up to 128 bytes)
    mov rax, 0                    ; sys_read system call number (0)
    mov rdi, 0                    ; File descriptor 0 (stdin)
    mov rsi, flag                 ; Pointer to the buffer where input will be stored
    mov rdx, 128                  ; Max number of bytes to read
    syscall                       ; Call kernel (syscall)

    ; r15 will be the current index
    mov r15, 0
a:
    ; mod operation, ends up being in edx
    ; Load dividend and divisor into registers
    mov rax, r15  ; Load dividend into eax
    mov ebx, 3   ; Load divisor into ebx

    ; Perform the division
    xor edx, edx         ; Clear edx (important for division to prevent overflow)
    div ebx              ; eax = eax / ebx, edx = eax % ebx (remainder)

    ; Now the remainder is in edx

    ; get the current character
    xor rax, rax
    mov al, [flag + r15]

    ; xor the character then add two
    mov bl, [interesting + edx]
    xor al, bl
    add al, 2

    ; compare current character with flag
    mov bl, [secret + r15]
    cmp bl, al

    jne exit

    xor rax, rax
    
    ; comparison for the loop
    inc r15
    cmp r15, secret_len
    jl a

    ; print correct
    mov rax, 1
    mov rdi, 1
    mov rsi, correct
    mov rdx, 8
    syscall

    ; Exit the program
exit:
    mov rax, 60                  ; sys_exit system call number (60)
    xor rdi, rdi                 ; Return code 0
    syscall                      ; Call the kernel (system call)

