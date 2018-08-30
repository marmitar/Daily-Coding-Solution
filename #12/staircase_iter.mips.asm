.text
.globl staircase
staircase:
    addi    $t0, $zero, 1
    addi    $t1, $zero, 0
    addi    $t3, $zero, 0

staircase_loop:
    beq     $t3, $a0, staircase_end

    add     $t2, $t0, $zero
    add     $t0, $t0, $t1
    add     $t1, $t2, $zero

    addi    $t3, $t3, 1
    beq     $zero, $zero, staircase_loop

staircase_end:
    add     $v0, $t0, $zero
    jr      $ra
