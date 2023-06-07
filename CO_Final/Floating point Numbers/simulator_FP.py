# Register Address
# R0 000
# R1 001
# R2 010
# R3 011
# R4 100
# R5 101


# Register Address
# R0 000
# R1 001
# R2 010
# R3 011
# R4 100
# R5 101
# R6 110
# FLAGS 111
import math
bias = 3
print_list = []
pc = 0
label_flag = True
hlt_flag = True
rf_dic = {"000": "0000000000000000", "001": "0000000000000000", "010": "0000000000000000", "011": "0000000000000000",
          "100": "0000000000000000", "101": "0000000000000000", "110": "0000000000000000", "111": "0000000000000000"}
reg_names = {"R0": "000", "R1": "001", "R2": "010", "R3": "011",
             "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}
# s

ayana = []
# plus="0000000"
# while True:
#     try:
#         line=input()
#         ayana.append(line)
#         plus=int(plus,2)+1
#         cd=bin(plus).replace("0b","")
#         item=""
#         while(len(cd)<7):
#             cd.insert(0,0)
#         for i in cd:
#             item+=str(i)

#     except:
#         break


# mem
decimal_numbers = [i for i in range(0, 128)]
binary_numbers = [bin(j) for j in decimal_numbers]
# print(binary_numbers)
memory_address = {}
for k in binary_numbers:
    cd1 = k.replace("0b", "")
    cd1 = list(cd1)
    item = ""
    while (len(cd1) < 7):
        cd1.insert(0, 0)
    for i in cd1:
        item += str(i)
    memory_address[item] = "0000000000000000"
# print(memory_address)
# instruction in mem
# print(memory_address)
key = [i for i in memory_address]


temp = 0
while True:
    # print("hell0")
    try:
        line = input()
        ayana.append(line)
    except:
        break
# pc


def Execution_engine(instruction):
    global pc
    global label_flag
    global hlt_flag
    global bias
    if (len(instruction) == 16):
        if (instruction.isdigit()):
            # for i in range(len(instruction)):
            #     if(instruction[i]==0 or instruction[i]==1):
            if '0' and '1' in instruction:
                opcode = instruction[:5]
                if opcode == '00000':  # ADD
                    rdb, rs1b, rs2b = instruction[7:10], instruction[10:13], instruction[13:]
                    # rd=rf_dic[rdb]
                    rs1 = rf_dic[rs1b]
                    rs2 = rf_dic[rs2b]
                    rs1, rs2 = int(rs1, 2), int(rs2, 2)
                    rrd = rs1+rs2

                    if rrd > 65535:
                        rf_dic['111'] = "0000000000001000"
                    else:
                        rf_dic['111'] = "0000000000000000"
                    rrd = bin(rrd)
                    cd2 = rrd.replace("0b", "")

                    cd2 = list(cd2)
                    if len(cd2) > 16:
                        rrd = cd2[1:]
                        rf_dic[rdb] = "0000000000000000"
                    else:

                        while (len(cd2) < 16):
                            cd2.insert(0, 0)
                        item2 = ""
                        for j in cd2:
                            item2 += str(j)
                        rf_dic[rdb] = item2
                    # print("add done")
                    return

                    # print(rd)
                elif opcode == '00001':  # SUB
                    rdb, rs1b, rs2b = instruction[7:10], instruction[10:13], instruction[13:]
                    rs1 = rf_dic[rs1b]
                    rs2 = rf_dic[rs2b]
                    rs1, rs2 = int(rs1, 2), int(rs2, 2)

                    rrd = rs1-rs2
                    if rrd < 0:
                        rf_dic['111'] = "0000000000001000"
                        rf_dic[rdb] = "0000000000000000"
                    else:
                        rrd = bin(rrd)
                        cd2 = rrd.replace("0b", "")
                        cd2 = list(cd2)
                        item2 = ""
                        while (len(cd2) < 16):
                            cd2.insert(0, 0)
                        for j in cd2:
                            item2 += str(j)
                        rf_dic[rdb] = item2
                        rf_dic['111'] = "0000000000000000"
                    # print("sub done")
                    return

                    # print(rrd)
                elif opcode == '00110':  # MUL

                    rdb, rs1b, rs2b = instruction[7:10], instruction[10:13], instruction[13:]
                    # rd=rf_dic[rdb]
                    rs1 = rf_dic[rs1b]
                    rs2 = rf_dic[rs2b]
                    rs1, rs2 = int(rs1, 2), int(rs2, 2)
                    rrd = rs1*rs2
                    if rrd > 65535:
                        rf_dic['111'] = "0000000000001000"
                    rf_dic['111'] = "0000000000000000"
                    rrd = bin(rrd)
                    cd2 = rrd.replace("0b", "")
                    cd2 = list(cd2)
                    if len(cd2) > 16:
                        rf_dic[rdb] = "0000000000000000"
                    else:
                        while (len(cd2) < 16):
                            cd2.insert(0, 0)
                        for j in cd2:
                            item2 += str(j)
                        rf_dic[rdb] = item2
                    # print("mul done")
                    return
                elif opcode == '00010':
                    rd = instruction[6:9]
                    imm = instruction[9:]
                    l1 = []
                    for i in range(0, len(imm)):
                        l1.append(int(imm[i]))
                    while len(l1) < 16:
                        l1.insert(0, 0)
                    val = ""
                    for u in l1:
                        val += str(u)
                    rf_dic[rd] = val
                    rf_dic['111'] = "0000000000000000"
                    return

                elif opcode == '00011':  # MOV reg1 reg2
                    # rd,rs1,=int(instruction[10:13],2),int(instruction[13:],2)
                    # rd=rs1
                    # print(rd)
                    rd = instruction[10:13]
                    rs1 = instruction[13:]
                    rf_dic[rd] = rf_dic[rs1]
                    rf_dic['111'] = "0000000000000000"
                    # print("mov reg1 to reg2")
                    return

                elif opcode == '00100':  # load
                    rd = instruction[6:9]
                    memory_addr = instruction[9:16]
                    rf_dic[rd] = memory_address[memory_addr]
                    rf_dic['111'] = "0000000000000000"
                    # print("load done")
                    return

                elif opcode == '00101':  # store
                    rd = instruction[6:9]
                    md = instruction[9:16]
                    memory_address[md] = rf_dic[rd]
                    rf_dic['111'] = "0000000000000000"
                    # print("store done")
                    return

                elif opcode == '00111':  # DIVIDE
                    # rdb=instruction[10:13]
                    # rdb1=instruction[13:]
                    # rs1=int(int(instruction[10:13],2))
                    # rs2=int(int(instruction[13:],2))
                    rdb, rs1b = instruction[10:13], instruction[13:]
                    rs1 = rf_dic[rdb]
                    rs2 = rf_dic[rs1b]
                    rs1, rs2 = int(rs1, 2), int(rs2, 2)

                    rrd1 = rs1//rs2
                    rrd2 = rs1 % rs2

                    rrd1 = bin(rrd1)
                    cd2 = rrd1.replace("0b", "")
                    cd2 = list(cd2)
                    rrd2 = bin(rrd2)
                    cd21 = rrd2.replace("0b", "")
                    cd21 = list(cd21)

                    if rs2 == '0':
                        rf_dic["111"] = "0000000000001000"
                        rf_dic[rdb] = "0000000000000000"
                        rf_dic[rs1b] = "0000000000000000"

                    else:
                        while (len(cd2) < 16):
                            cd2.insert(0, 0)
                        item2 = ''
                        for j in cd2:
                            item2 += str(j)
                        rf_dic[rdb] = item2

                        while (len(cd21) < 16):
                            cd21.insert(0, 0)
                        item3 = ''
                        for j in cd21:
                            item3 += str(j)
                        rf_dic[rs1b] = item3
                        rf_dic['111'] = "0000000000000000"
                    # print("divide done")
                    return

                elif opcode == '01000':  # right shift
                    rs1b = instruction[6:9]
                    imm = instruction[9:]
                    imm1 = int(int(imm, 2))
                    rs1 = list(rf_dic[rs1b])
                    for i in range(imm1):
                        rs1.insert(0, 0)
                    item = ""
                    for i in rs1:
                        item += str(i)
                    rs1 = item
                    rrd = rs1[:16]
                    rf_dic[rs1b] = rrd
                    rf_dic['111'] = "0000000000000000"
                    # print("right shift done")
                    return

                elif opcode == '01001':  # left shift

                    rs1b = instruction[6:9]
                    imb = instruction[9:16]
                    rs1 = rf_dic[rs1b]
                    im = int(imb, 2)
                    imm = int(im)
                    rs1 = list(rs1)
                    for i in range(0, imm):
                        rs1.insert(len(rs1), 0)
                        # rs1=rs1[1:]
                    # rrd=rs1
                    item = ""
                    for i in rs1:
                        item += str(i)
                    rs1 = item
                    rrd = rs1[-16:]
                    rf_dic[rs1b] = rrd
                    rf_dic['111'] = "0000000000000000"
                    # print("left shift")
                    return

                # Performs bitwise
                # XOR of reg2 and
                # reg3. Stores the
                # result in reg1.
                elif opcode == '01010':  # EXCLUSIVE OR
                    # rd,rs1,rs2=int(int(instruction[7:10],2)),int(int(instruction[10:13],2)),int(int(instruction[13:],2))
                    rd = instruction[7:10]
                    rs1 = instruction[10:13]
                    rs2 = instruction[13:]
                    temp = ""
                    for i in range(0, len(rs1)):
                        if rs1[i] == rs2[i]:
                            temp += '0'
                        else:
                            temp += '1'
                    rf_dic[rd] = temp
                    rf_dic['111'] = "0000000000000000"
                    # print("exclusive or done")
                    return

                elif opcode == "01011":  # OR
                    rd = instruction[7:10]
                    rs1 = instruction[10:13]
                    rs2 = instruction[13:]
                    temp = ""
                    for i in range(0, len(rs1)):
                        if rs1[i] == '0' and rs2[i] == '0':
                            temp += '0'
                        else:
                            temp += '1'
                    rf_dic[rd] = temp
                    rf_dic['111'] = "0000000000000000"
                    # print("or done")
                    return

                elif opcode == "01100":  # AND
                    rd = instruction[7:10]
                    rs1 = instruction[10:13]
                    rs2 = instruction[13:]
                    temp = ""
                    for i in range(0, len(rs1)):
                        if rs1[i] == '1' and rs2[i] == '1':
                            temp += '1'
                        else:
                            temp += '0'
                    rf_dic[rd] = temp
                    rf_dic['111'] = "0000000000000000"
                    # print("and done")
                    return

                elif opcode == '01101':       # INVERT
                    rd = instruction[10:13]
                    rs1 = instruction[13:]

                    temp = ""
                    for i in range(0, len(rs1)):
                        if rs1[i] == '0':
                            temp += '1'
                        else:
                            temp += '0'
                    rf_dic[rd] = temp
                    rf_dic['111'] = "0000000000000000"
                    # print("invert done")
                    return

                # Compares reg1 and
                # reg2 and sets up
                # the FLAGS
                # register.

                elif opcode == "01110":  # COMPARE
                    rs1b = instruction[10:13]
                    rs2b = instruction[13:]
                    rs1 = int(int(instruction[10:13]))
                    rs2 = int(int(instruction[13:]))
                    if rf_dic[rs1b] == rf_dic[rs2b]:
                        rf_dic['111'] = "0000000000000001"
                    elif rf_dic[rs1b] > rf_dic[rs2b]:
                        rf_dic['111'] = "0000000000000010"
                    elif rf_dic[rs1b] < rf_dic[rs2b]:
                        rf_dic['111'] = "0000000000000100"
                    else:
                        rf_dic['111'] = "0000000000000000"
                    # print("compare done")
                    return

               # Jumps to mem_addr,
                # where mem_addr is
                # a memory address.
                elif opcode in ["01111", "11100", "11111", "11101"]:
                    mem = instruction[9:]
                    if opcode == "11100":  # jump if less than
                        if rf_dic['111'] == "0000000000000100":
                            # print("jump if less than")

                            pc = mem

                    elif opcode == "11111":  # jump if equal
                        if rf_dic['111'] == "0000000000000001":
                            # print("jump if equal")
                            pc = mem

                    elif opcode == "11101":  # jump if greater than
                        if rf_dic['111'] == "0000000000000010":
                            # print("jump if greater than")
                            pc = mem

                    else:  # unconditional jump ,opcode

                        # print("uncondditional jump")
                        pc = mem

                    rf_dic['111'] = "0000000000000000"
                    # print("jump done")
                    label_flag = False
                    return

                elif opcode == "11010":  # halt
                    rf_dic['111'] = "0000000000000000"
                    hlt_flag = False
                    return
                # 10000 F_Addition
                # 10001 F_Subtraction
                # 10010 MoveF_Immediate
                elif opcode == "10000":  # F_Addition
                    rd = instruction[7:10]
                    rs1 = instruction[10:13]
                    rs2 = instruction[13:16]
                    fp1 = rf_dic[rs1][-8:]
                    fp2 = rf_dic[rs2][-8:]
                    # rs1 ki pehli 3 values E hai
                    # hme E-bias bias=3
                    # baki 5 values mantissa hai uske liye for loop usme 2^-1 se shuru krke
                    # 2^-5 tak loop chalega mantissa me +1
                    # multiply krdo mantissa ki new vaue ko 2^X
                    e1 = fp1[0:3]
                    m1 = fp1[3:]
                    e1 = int(e1, 2)
                    e1 = e1-bias
                    e2 = fp2[0:3]
                    m2 = fp2[3:]
                    e2 = int(e2, 2)
                    e2 = e2-bias
                    mantissa1 = 0
                    mantissa2 = 0
                    for i in range(1, 6):
                        x = math.pow(2, (-1)*i)
                        mantissa1 += (int(m1[i-1])*x)
                    mantissa1 += 1
                    x = math.pow(2, e1)
                    fp_num1 = mantissa1*x
                    for i in range(1, 6):
                        x = math.pow(2, (-1)*i)
                        mantissa2 += (int(m2[i-1])*x)
                    mantissa2 += 1
                    x = math.pow(2, e2)
                    fp_num2 = mantissa2*x
                    if fp_num1+fp_num2 > 31.5 or fp_num1+fp_num2 < 0.25:
                        rf_dic['111'] = "0000000000001000"
                        rf_dic[rd] = "0000000000000000"
                    else:
                        temp = fp_num1+fp_num2
                        temp2 = str(temp)
                        fp_lst = list(map(str, temp2.split(".")))

                        # denormal range [0.00390625,0.12109375]
                        if temp < 0.12109376 and temp > 0.00390624:
                            cd1 = int(fp_lst[0])
                            cd1 = bin(cd1).replace("0b", "")
                            binary_num = ""
                            cd2 = (fp_lst[1])
                            x = math.pow(10, len(cd2))
                            cd2 = int(cd2)
                            cd2 = cd2/x
                            while cd2 != 0:
                                new = cd2*2
                                floor = math.floor(new)
                                binary_num += str(floor)
                                cd2 = new-floor
                            fp_1 = cd1+"."+binary_num

                            # print(fp_1)

                            fp_1 = list(fp_1)
                            mantissa = ""
                            for i in range(5, 10):
                                mantissa += fp_1[i]
                            exponent = "000"

                            # print(mantissa)

                            # print(exponent)
                            converted_imm = exponent+mantissa

                        else:
                            cd1 = int(fp_lst[0])
                            cd1 = bin(cd1).replace("0b", "")
                            binary_num = ""
                            cd2 = (fp_lst[1])
                            x = math.pow(10, len(cd2))
                            cd2 = int(cd2)
                            cd2 = cd2/x
                            while cd2 != 0:
                                new = cd2*2
                                floor = math.floor(new)
                                binary_num += str(floor)
                                cd2 = new-floor
                            fp_1 = cd1+"."+binary_num

                            fp_1 = list(fp_1)
                            for i in range(len(fp_1)):
                                if fp_1[i] == "1":
                                    idx1 = i
                                    break
                            for i in range(len(fp_1)):
                                if fp_1[i] == ".":
                                    idxdot = i
                                    break
                            length = idx1-idxdot
                            if length > 0:
                                exponent = ((-1)*length)+3
                                mantissa = ""
                                i = idx1+1
                                if len(fp_1)-i-1 >= 5:
                                    while len(mantissa) < 5:
                                        mantissa += fp_1[i]
                                        i += 1

                                else:
                                    for j in range(i, len(fp_1)):
                                        mantissa += fp_1[j]
                                    while len(mantissa) < 5:

                                        mantissa += "0"
                            else:
                                exponent = ((-1)*(length+1))+3
                                mantissa = ""
                                i = idx1+1
                                if len(fp_1)-i-1 >= 5:
                                    while len(mantissa) < 5:
                                        if fp_1[i] != ".":
                                            mantissa += fp_1[i]

                                            i += 1

                                        else:
                                            i += 1
                                else:

                                    for j in range(i, len(fp_1)):
                                        if fp_1[j] != ".":
                                            mantissa += fp_1[j]

                                    while len(mantissa) < 5:
                                        mantissa += "0"

                            # print(mantissa)
                            exponent = bin(exponent).replace("0b", "")

                            if len(exponent) < 3:
                                exponent = list(exponent)
                                while len(exponent) < 3:
                                    exponent.insert(0, 0)
                            temp = ""
                            for i in range(3):
                                temp += str(exponent[i])
                            exponent = temp

                            #

                            converted_imm = exponent+mantissa
                            rf_dic['111'] = "0000000000000000"

                        converted_imm = "00000000"+converted_imm
                        rf_dic[rd] = converted_imm
                        # rf_dic['111'] = "0000000000000000"
                        return

                elif opcode == "10001":  # F_Subtraction
                    rd = instruction[7:10]
                    rs1 = instruction[10:13]
                    rs2 = instruction[13:16]
                    fp1 = rf_dic[rs1][-8:]
                    fp2 = rf_dic[rs2][-8:]
                    e1 = fp1[0:3]
                    m1 = fp1[3:]
                    e1 = int(e1, 2)
                    e1 = e1-bias
                    e2 = fp2[0:3]
                    m2 = fp2[3:]
                    e2 = int(e2, 2)
                    e2 = e2-bias
                    mantissa1 = 0
                    mantissa2 = 0
                    for i in range(1, 6):
                        x = math.pow(2, (-1)*i)
                        mantissa1 += (int(m1[i-1])*x)
                    mantissa1 += 1
                    x = math.pow(2, e1)
                    fp_num1 = mantissa1*x
                    # print(fp_num1)
                    for i in range(1, 6):
                        x = math.pow(2, (-1)*i)
                        mantissa2 += (int(m2[i-1])*x)
                    mantissa2 += 1
                    x = math.pow(2, e2)
                    fp_num2 = mantissa2*x
                    # print(fp_num2)
                    if fp_num1-fp_num2 > 31.5 or fp_num1-fp_num2 < 0.25:
                        rf_dic['111'] = "0000000000001000"
                        rf_dic[rd] = "0000000000000000"
                    else:
                        temp = fp_num1-fp_num2
                        temp2 = str(temp)
                        fp_lst = list(map(str, temp2.split(".")))

                        # denormal range [0.00390625,0.12109375]
                        if temp < 0.12109376 and temp > 0.00390624:
                            cd1 = int(fp_lst[0])
                            cd1 = bin(cd1).replace("0b", "")
                            binary_num = ""
                            cd2 = (fp_lst[1])
                            x = math.pow(10, len(cd2))
                            cd2 = int(cd2)
                            cd2 = cd2/x
                            while cd2 != 0:
                                new = cd2*2
                                floor = math.floor(new)
                                binary_num += str(floor)
                                cd2 = new-floor
                            fp_1 = cd1+"."+binary_num

                            # print(fp_1)

                            fp_1 = list(fp_1)
                            mantissa = ""
                            for i in range(5, 10):
                                mantissa += fp_1[i]
                            exponent = "000"

                            # print(mantissa)

                            # print(exponent)
                            converted_imm = exponent+mantissa

                        else:
                            cd1 = int(fp_lst[0])
                            cd1 = bin(cd1).replace("0b", "")
                            binary_num = ""
                            cd2 = (fp_lst[1])
                            x = math.pow(10, len(cd2))
                            cd2 = int(cd2)
                            cd2 = cd2/x
                            while cd2 != 0:
                                new = cd2*2
                                floor = math.floor(new)
                                binary_num += str(floor)
                                cd2 = new-floor
                            fp_1 = cd1+"."+binary_num

                            fp_1 = list(fp_1)
                            for i in range(len(fp_1)):
                                if fp_1[i] == "1":
                                    idx1 = i
                                    break
                            for i in range(len(fp_1)):
                                if fp_1[i] == ".":
                                    idxdot = i
                                    break
                            length = idx1-idxdot
                            if length > 0:
                                exponent = ((-1)*length)+3
                                mantissa = ""
                                i = idx1+1
                                if len(fp_1)-i-1 >= 5:
                                    while len(mantissa) < 5:
                                        mantissa += fp_1[i]
                                        i += 1

                                else:
                                    for j in range(i, len(fp_1)):
                                        mantissa += fp_1[j]
                                    while len(mantissa) < 5:

                                        mantissa += "0"
                            else:
                                exponent = ((-1)*(length+1))+3
                                mantissa = ""
                                i = idx1+1
                                if len(fp_1)-i-1 >= 5:
                                    while len(mantissa) < 5:
                                        if fp_1[i] != ".":
                                            mantissa += fp_1[i]

                                            i += 1

                                        else:
                                            i += 1
                                else:

                                    for j in range(i, len(fp_1)):
                                        if fp_1[j] != ".":
                                            mantissa += fp_1[j]

                                    while len(mantissa) < 5:
                                        mantissa += "0"
                            exponent = bin(exponent).replace("0b", "")
                            # print(mantissa)
                            if len(exponent) < 3:
                                exponent = list(exponent)
                                while len(exponent) < 3:
                                    exponent.insert(0, 0)
                            temp = ""
                            for i in range(3):
                                temp += str(exponent[i])
                            exponent = temp
                            #

                            converted_imm = exponent+mantissa

                        converted_imm = "00000000"+converted_imm
                        rf_dic[rd] = converted_imm
                        rf_dic['111'] = "0000000000000000"
                        return

                elif opcode == "10010":  # MoveF_Immediate
                    rd = instruction[5:8]
                    f_imm = instruction[8:]
                    l = list(f_imm)

                    f_imm = ""
                    for i in l:
                        f_imm += str(i)
                    rf_dic[rd] = "00000000"+f_imm
                    rf_dic['111'] = "0000000000000000"
                    return


for i in range(0, len(ayana)):
    memory_address[key[i]] = ayana[i]
# print(memory_address)
# print(red)


def call_pc(mem_addr_key):
    # print("pc before execution",pc)
    Execution_engine(memory_address[mem_addr_key])
    # PRINTING PC
    instruction = memory_address[mem_addr_key]

    opcode = instruction[0:5]
    # if opcode not in ["01111","11100","11111","11101"]:

    # print(pc, end="        ")
    print_list.append(pc)
    print_list.append("      ")
    # PRINTING REGISTER FILE
    for i in rf_dic:
        # print(rf_dic[i], end=" ")
        print_list.append(rf_dic[i])
    # print()
    print_list.append("\n")
    return


for i in range(0, len(ayana)):
    # print("for new inst")
    # print("pc before execution",pc)
    if hlt_flag == True:
        # if memory_address[key[i-1]] == "1101000000000000":

        #     break
        if label_flag == True:
            pc = key[i]
            call_pc(pc)
        # elif memory_address[key[i]-1] == "1101000000000000":
        #     break
        else:
            # print("inside else")
            label_flag = True
            call_pc(pc)
    else:
        break

# MEMORY DUMP
for i in print_list:
    if i != "\n":
        print(i, end=" ")
    else:
        print()
for i in memory_address:
    print(memory_address[i])
# instruction=ayana[0]

# def EE():
#     address=pc()
#     a=memory_address(address)
