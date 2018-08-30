.data

in_text: .align 2
.asciiz "In: "

out_text: .align 2
.asciiz "Out: "

newline: .align 2
.asciiz "\n"

set_size:
.word 3
set:
.word 1
.word 3
.word 5


.text
.globl main
main:
    la      $a0, in_text
    addi    $v0, $zero, 4
    syscall

    addi    $v0, $zero, 5
    syscall
    add     $s0, $v0, $zero

    add     $a0, $s0, $zero
    lw      $a1, set_size
    la      $a2, set
    jal     staircase_many
    add     $s0, $v0, $zero

    la      $a0, out_text
    addi    $v0, $zero, 4
    syscall

    add     $a0, $s0, $zero
    addi    $v0, $zero, 1
    syscall

    la      $a0, newline
    addi    $v0, $zero, 4
    syscall

    addi    $v0, $zero, 10
    syscall
