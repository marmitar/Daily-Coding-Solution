.text
.globl staircase_many
#
#    a0 -> staircase size
#    a1 -> set size
#    a2 -> set pointer
#
#    v0 <- ways to climb
#
staircase_many:

    add     $t0, $a2, $zero     # t0: set position (pointer)
    sll     $t1, $a1, 2
    add     $t1, $t1, $a2       # t1: set end (pointer)
    add     $t2, $zero, $zero   # t2: set maximum

staircase_get_max:
    beq     $t0, $t1, staircase_memo_init

    lw      $t3, 0($t0)         # t3: current value in set
    slt     $t4, $t3, $t2
    bne     $t4, $zero, staircase_get_max_next

    add     $t2, $t3, $zero     # new maximum

staircase_get_max_next:
    addi    $t0, $t0, 4
    beq     $zero, $zero, staircase_get_max


staircase_memo_init:
    add     $v0, $zero, $zero
    beq     $t2, $zero, staircase_end_normal

    addi    $sp, $sp, -12
    sw      $s0, 0($sp)
    sw      $s1, 4($sp)
    sw      $s2, 8($sp)

    sll     $s0, $t2, 2         # s0: memo size (in bytes)

    sub     $sp, $sp, $s0       # sp: memo pointer

    add     $s1, $zero, $zero   # s1: memo position (bytes)

    addi    $t0, $zero, 1
    add     $t4, $sp, $s1
    sw      $t0, 0($t4)
    addi    $s1, $s1, 4

staircase_memo_loop:
    beq     $s1, $s0, staircase_calc

    add     $t4, $sp, $s1
    sw      $zero, 0($t4)

    addi    $s1, $s1, 4
    beq     $zero, $zero, staircase_memo_loop


staircase_calc:
    addi    $s1, $zero, 4       # reset memo ptr
    add     $t0, $zero, $zero   # t0: staircase step

    sll     $t2, $a1, 2
    add     $t2, $t2, $a2       # t2: set end (pointer)

staircase_calc_loop:
    beq     $t0, $a0, staircase_end_normal

    addi    $t0, $t0, 1

    add     $t1, $a2, $zero     # t1: set position (pointer)

    add     $t7, $zero, $zero   # t7: ways to climb to this step

staircase_calc_set_loop:
    beq     $t1, $t2, staircase_calc_loop_end

    lw      $t3, 0($t1)         # t3: current value in set
    add     $t1, $t1, 4

    slt     $t4, $t0, $t3
    bne     $t4, $zero, staircase_calc_set_loop

    sll     $t3, $t3, 2
    sub     $t3, $s1, $t3       # t3: position in memo to get

    slt     $t4, $t3, $zero
    beq     $t4, $zero, staircase_calc_set_loop_after_cycle
    add     $t3, $t3, $s0       # cycle if necessary

staircase_calc_set_loop_after_cycle:
    add     $t3, $t3, $sp
    lw      $t3, 0($t3)         # t3: value from memo

    add     $t7, $t7, $t3

    beq     $zero, $zero, staircase_calc_set_loop

staircase_calc_loop_end:

    add     $t3, $sp, $s1
    sw      $t7, 0($t3)

    addi    $s1, $s1, 4
    bne     $s1, $s0, staircase_calc_loop

    add     $s1, $zero, $zero
    beq     $zero, $zero, staircase_calc_loop


staircase_end_normal:
    bne     $s1, $zero, staircase_end_normal_skip
    add     $s1, $s0, $zero

staircase_end_normal_skip:
    addi    $s1, $s1, -4

    add     $t4, $sp, $s1
    lw      $v0, 0($t4)

    add     $sp, $sp, $s0
    lw      $s0, 8($sp)
    lw      $s1, 4($sp)
    lw      $s2, 0($sp)
    addi    $sp, $sp, 12

staircase_end:
    jr      $ra
