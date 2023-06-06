print_list=[]
import math
def instruction(ls,ln,l,dic,var_dic,extra_var,line_number):
    d1={"add":"00000","sub":"00001","mul":"00110","xor":"01010","or":"01011","and":"01100"}
    d3={"mov":"00010","rs":"01000","ls":"01001"}  
    array={"jmp":"01111" ,"jlt":"11100","jgt":"11101","je":"11111"}
    d4={"mov":"00011","ld":"00100","st":"00101","div":"00111","not":"01101","cmp":"01110"}
    flag2=True
    if len(l)==5:
        if ":" in l[0]:
            lst10=[]
            for k in range(1,len(l)):
                lst10.append(l[k])
            instruction(ls,ln,lst10,dic,var_dic,extra_var,line_number)  
        else:
                print_list.append("False")
                print("SyntaxError",line_number,":Instruction not supported")
                flag2=False
               
    if len(l)==4:
        d1={"add":"00000","sub":"00001","mul":"00110","xor":"01010","or":"01011","and":"01100","addf":"10000","subf":"10001","mod":"10011","nor":"10100","nand":"10101","xnor":"10110"}
        if l[0] in d1:
            # print(d1[l[0]],end="")
            # print("00",end="")

            print_list.append(d1[l[0]])
            print_list.append("00")

            if l[1] in dic  :
                # print(dic[l[1]],end="")

                print_list.append(dic[l[1]])

                if l[2] in dic :
                    # print(dic[l[2]],end="")

                    print_list.append(dic[l[2]])

                    if l[3] in dic :
                        # print(dic[l[3]])

                        print_list.append(dic[l[3]])
                        print_list.append("\n")
                   

                    else:
                        print_list.append("False")
                        print("Error line number",line_number+1,":",l[3],"->wrong register name")
                        flag2=False
              
                else:
                    print_list.append("False")
                    print("Error line number",line_number+1,":",l[2],"->wrong register name")
                    flag2=False
            elif l[1]=="FLAGS":
                print_list.append("False")
                print("Error line number",line_number+1,":",l[2],"->wrong register name")
                flag2=False
            else:
                print_list.append("False")
                print("Error line number",line_number+1,":",l[1],"->wrong register name")
                flag2=False
        elif ":" in l[0]:
            lst10=[]
            for k in range(1,len(l)):
                lst10.append(l[k])
            instruction(ls,ln,lst10,dic,var_dic,extra_var,line_number)  
        else:
            print_list.append("False")
            print("Error line number",line_number+1,": Instruction not supported by ISA")
            flag2=False
    
    elif len(l)==2:
        # type E
        array={"jmp":"01111" ,"jlt":"11100","jgt":"11101","je":"11111"}
        if l[0] in array:
            new_list1=[]
            for read in ls:
                new_list1.append(list(map(str,read.split())))
            for j in range(0,len(new_list1)):
                if l[1] == new_list1[j][0][:-1]:
                    flag2=True

                    # print(array[l[0]],end="")
                    # print("0000",end="")

                    print_list.append(array[l[0]])
                    print_list.append("0000")

                    cs=""
                    for item in ln[j]:
                        cs+=str(item)
                    xt=int(cs,2)-(extra_var)  
                    xtt=bin(xt).replace("0b","")
                    
                    xtt=list(xtt)
                    if len(xtt)<=7:
                        while(len(xtt)<7):
                            xtt.insert(0,0)
                    for i in xtt:
                        # print(i,end="")
                        print_list.append(i)
                    # print()
                    print_list.append("\n")
                    break
                
                else:
                    flag2="False"
            if flag2=="False":
                print_list.append("False")
                print("Error line number",line_number+1,": Label not defined!!")
                flag2=False
                 
        if ":" in l[0]:
            if(l[1]=="hlt"):
                # print("1101000000000000")
                print_list.append("1101000000000000")
                print_list.append("\n")
            else:
                print_list.append("False")
                print("Error line number",line_number+1,": Invalid instruction after label")
                flag2=False
                 
        if l[0] not in array and ":" not in l[0]:
            print_list.append("False")
            print("Error line number",line_number+1,": Instruction not supported by ISA")
            flag2=False
    elif len(l)==1:
        if l[0]=="hlt":
            # print("1101000000000000")
            print_list.append("1101000000000000")
            print_list.append("\n")
        elif ":" in l[0]:
            pass
        else:
            print_list.append("False")
            # if l[0] not in dic or l[0] not in d1 or l[0] not in array or l[0] not in d3 or l[0] not in d4:
            if l[0].strip() in dic or l[0].strip() in d1:
                
                print("Error line number",line_number+1,": Instruction not supported by ISA")
                flag2= False
            else:
                 print("Error line number",line_number+1,":",l[0],"->Instruction not supported by ISA")
               

    elif len(l)==3:

        if "$" in l[2]:
            
            d3={"mov":"00010","rs":"01000","ls":"01001","movf":"10010"}          
            
            if l[0] in d3:
                
                # print(d3[l[0]],end="")
                # print("0",end="")

                print_list.append(d3[l[0]])
                

                if l[1] in dic:                
                    # print(dic[l[1]],end="") 
                                   
                    if l[2][1:].isnumeric():
                        print_list.append("0")
                        print_list.append(dic[l[1]])   
                        cd=int(l[2][1:])
                        cd1=bin(cd).replace("0b","")
                        cd1=list(cd1)
                        if len(cd1)<=7:
                            while(len(cd1)<7):
                                cd1.insert(0,0)                           
                            for i in cd1:                             
                                # print(i,end="")
                                print_list.append(i)
                            # print()
                            print_list.append("\n")
                        else:
                            print_list.append("False")
                            print("Error line number",line_number+1,": Immediate value exceeded 7 bits") 

                    elif "." in l[2]: 
                        print_list.append(dic[l[1]])        
                        fp_lst=list(map(str,l[2][1:].split(".")))
                        
                        cd1=int(fp_lst[0])
                        cd1=bin(cd1).replace("0b","")
                        binary_num = ""
                        cd2=(fp_lst[1])
                        x=math.pow(10,len(cd2))
                        cd2=int(cd2)
                        cd2=cd2/x
                        while cd2!=0:
                            new=cd2*2
                            floor=math.floor(new)
                            binary_num+=str(floor)
                            cd2=new-floor
                        fp_1=cd1+"."+binary_num
                        
                        
                        
                        fp_1=list(fp_1)
                        for i in range(len(fp_1)):
                            if fp_1[i]=="1":
                                idx1=i
                                break
                        for i in range(len(fp_1)):
                            if fp_1[i]==".":
                                idxdot=i
                                break
                        length=idx1-idxdot
                        if length >0:
                            exponent=((-1)*length)+3
                            mantissa=""
                            i=idx1+1
                            if len(fp_1)-i-1>=5: 
                                while len(mantissa)<5:
                                    mantissa+=fp_1[i]
                                    i+=1
                                    
                            else:
                                for j in range(i,len(fp_1)):
                                    mantissa+=fp_1[j]
                                while len(mantissa)<5:
                                   
                                    mantissa+="0"
                        else:
                            exponent=((-1)*(length+1))+3
                            mantissa=""
                            i=idx1+1
                            if len(fp_1)-i-1>=5:
                                while len(mantissa)<5: 
                                    if fp_1[i]!=".":
                                        mantissa+=fp_1[i]
                                        
                                        i+=1
                                      
                                    else:
                                        i+=1
                            else:
                                
                                for j in range(i,len(fp_1)):
                                    if fp_1[j]!=".":
                                        mantissa+=fp_1[j]

                                while len(mantissa)<5:
                                    mantissa+="0"
                               
                        print(mantissa)
                        exponent=bin(exponent).replace("0b","")
                        print(exponent)
                        converted_imm=exponent+mantissa
                        print_list.append(converted_imm)
                        print_list.append("\n")
                                        

                    else:
                        print_list.append("False")
                        print("Error line number",line_number+1,":",l[2][1:],"->Invalid immediate(not integer)")                
                else:
                    print_list.append("False")
                    print("Error line number",line_number+1,":",l[1],"->Invalid register name") 
           


            else:
                print_list.append("False")
                print("Error line number",line_number+1,": Instruction not supported by ISA")
      
        else:
            # TYPE C
            d4={"mov":"00011","ld":"00100","st":"00101","div":"00111","not":"01101","cmp":"01110","square":"10111"}
            if(len(l)==3):
                if l[0] in d4:
                   
                    if l[1] in dic:
                      
                        if l[2] in dic :
                            print_list.append(d4[l[0]])
                            print_list.append("00000")
                            print_list.append(dic[l[1]])
                            print_list.append(dic[l[2]])
                            print_list.append("\n")

                        elif l[2] in var_dic:
                            print_list.append(d4[l[0]])
                            print_list.append("0")
                            print_list.append(dic[l[1]])

                            cs=""
                            for item in var_dic[l[2]]:
                                cs+=str(item)
                            xt=int(cs,2)+(len(ls)-extra_var)  
                            xtt=bin(xt).replace("0b","")
                            
                            xtt=list(xtt)
                            if len(xtt)<=7:
                                while(len(xtt)<7):
                                    xtt.insert(0,0)
                                   
                            for i in xtt:
                                
                                # print(i,end="")
                                print_list.append(i)
                            print_list.append("\n")
                            # print()
             
                        else:
                            print_list.append("False")
                            print("Error line number",line_number+1,":",l[2],"->Invalid register name or invalid variable name")
                            flag2=False
                 
                    else:
                        print_list.append("False")
                        print("Error line number",line_number+1,":",l[1],"->Invalid register name")
                        flag2=False
                elif ":" in l[0]:
                    lst10=[]
                    for k in range(1,len(l)):
                        lst10.append(l[k])
                    instruction(ls,ln,lst10,dic,var_dic,extra_var,line_number)  
                else:
                    print_list.append("False")
                    print("Error line number",line_number+1,": Instruction not supported by ISA")
                    flag2=False
                   
                       


red=[]

while True:
    try:
        line=input()
        red.append(line)
    except:
        break


dic={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
line_number={}
var_dic={}
k=0
j=0
flag=True
new_list11=[]

count=0     
for j in range(0,len(red)):
    cd1=bin(j).replace("0b","")
    cd1=list(cd1)
    while(len(cd1)<7):
        cd1.insert(0,0)
        
    line_number[j]=cd1
    lst=list(map(str,red[j].split()))
    new_list11.append(lst)
    if lst[0]=="var":
        if j==k:
            var_dic[lst[1]]=line_number[k]
            k+=1
    j+=1
flag2=True


for i in range(0,len(red)):
    if len(new_list11[i]) ==2:
        for j in range(0,len(new_list11[i])):
            if new_list11[i][1]=="hlt":
                if i!=len(new_list11)-1:
                    print_list.append("False")
                    print("Error: hlt should be defined at last")
                    flag="False"
                    break
    elif len(new_list11[i]) ==1:
        for j in range(0,len(new_list11[i])):
            if new_list11[i][0]=="hlt":
                if i!=len(new_list11)-1:
                    print("Error: hlt should be defined at last")
                    print_list.append("False")
                    flag="False"
                    break

if "hlt" not in new_list11[len(new_list11)-1]:
    print_list.append("False")
    print("Error: hlt statement not found at last")
    flag="False"
    
for i in range(k,len(red)):
    l=list(map(str,red[i].split()))
    if l[0]!="var":
        instruction(red,line_number,l,dic,var_dic,k,i)
    else:
        print_list.append("False")
        print("Error line number",i+1,": Variable can not be defined in between")
if "False" not in print_list:
    # print(":::::::::::::::::::::::")
    for i in range(0,len(print_list)):
        # if print_list[i]!="\n":
            print(print_list[i],end="")

