.text
.globl staircase_slow
staircase_slow:
    addi    $t0, $zero, 2
    slt     $t0, $a0, $t0
    addi    $t1, $zero, 1
    bne     $t0, $zero, staircase_slow_end

staircase_slow_rec:
    addi    $sp, $sp, -12
    sw      $ra, 8($sp)

    sw      $a0, 0($sp)
    addi    $a0, $a0, -1
    jal     staircase_slow
    sw      $v0, 4($sp)

    lw      $a0, 0($sp)
    addi    $a0, $a0, -2
    jal     staircase_slow

    lw      $t0, 4($sp)
    add     $t1, $t0, $v0

    lw      $ra, 8($sp)
    addi    $sp, $sp, 12

staircase_slow_end:
    add     $v0, $t1, $zero
    jr      $ra