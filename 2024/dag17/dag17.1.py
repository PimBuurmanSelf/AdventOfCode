import math
import operator

total = 0

def combo(op):
    if op >= 0 and op <= 3:
        return op
    if op >= 4 and op <= 6:
        return reg[op - 4]
        
def pow2(y):
    x = 1
    for i in range(y):
        x *= 2
    return x
    
out = []
with open('dag17input.txt', encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')

    reg = [0] * 3
    for line in data:
        if line.startswith('Register A:'):
            reg[0] = int(line.split()[-1])
        if line.startswith('Register B:'):
            reg[1] = int(line.split()[-1])
        if line.startswith('Register C:'):
            reg[2] = int(line.split()[-1])
        if line.startswith('Program:'):
            prog = [int(i) for i in line[9:].split(',')]
            
    idx = 0
    while idx < len(prog) // 2:
        opcode = prog[2 * idx]
        operand = prog[2 * idx + 1]
        if opcode == 0:
            op2 = pow2(combo(operand))
            reg[0] = reg[0] // op2
        elif opcode == 1:
            reg[1] = operator.xor(reg[1], operand)
        elif opcode == 2:
            reg[1] = combo(operand) % 8
        elif opcode == 3:
            if reg[0] != 0:
                idx = operand
                continue
        elif opcode == 4:
            reg[1] = operator.xor(reg[1], reg[2])
        elif opcode == 5:
            out.append(combo(operand) % 8)
        elif opcode == 6:
            op2 = pow2(combo(operand))
            reg[1] = reg[0] // op2
        elif opcode == 7:
            op2 = pow2(combo(operand))
            reg[2] = reg[0] // op2
        idx += 1
        
    print(out, ','.join([str(i) for i in out]))
            