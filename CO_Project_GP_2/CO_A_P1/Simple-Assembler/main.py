def error_gen(flag2):
    return flag2
def instruction(ls,ln,l,dic,var_dic,extra_var):
    flag2=True
    if len(l)==5:
        if ":" in l[0]:
            lst10=[]
            for k in range(1,len(l)):
                lst10.append(l[k])
            
            instruction(ls,ln,lst10,dic,var_dic,extra_var)  
        else:
                print("syntax error")
                flag2= False
                error_gen(flag2)
    if len(l)==4:
        d1={"add":"00000","sub":"00001","mul":"00110","xor":"01010","or":"01011","and":"01100"}
        if l[0] in d1:
            print(d1[l[0]],end="")
            print("00",end="")
            if l[1] in dic:
                print(dic[l[1]],end="")
                if l[2] in dic:
                    print(dic[l[2]],end="")
                    if l[3] in dic:
                        print(dic[l[3]])
                    else:
                        print("syntax error : wrong register name")
                        flag2= False
                        error_gen(flag2)
                        
                else:
                    print("syntax error : wrong register")
                    flag2= False
                    error_gen(flag2)
            else:
                print("syntax error: wrong register name")
                flag2= False
                error_gen(flag2)
        elif ":" in l[0]:
            lst10=[]
            for k in range(1,len(l)):
                lst10.append(l[k])
            instruction(ls,ln,lst10,dic,var_dic,extra_var)  
        else:
                print("syntax error: Instruction not supported by ISA")
                flag2= False
                error_gen(flag2)
        
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
                    print(array[l[0]],end="")
                    print("0000",end="")
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
                        print(i,end="")
                    print()
                    break
                
                else:
                    flag2=False
            if flag2==False:
                print("syntax error: Label not defined!!")
                flag2= False
                error_gen(flag2)  
        if ":" in l[0]:
            if(l[1]=="hlt"):
                
                print("1101000000000000")
                
            else:
                print("syntax error: Invalid instruction after label")
                flag2= False
                error_gen(flag2)  
        if l[0] not in array and ":" not in l[0]:
            print("syntax error: Instruction not supported by ISA")
            
            flag2= False
            error_gen(flag2)
    elif len(l)==1:
        if l[0]=="hlt":
           
            print("1101000000000000")
        elif ":" in l[0]:
            pass
        else:
                print("syntax error: Instruction does not exist")
                
                flag2= False
                error_gen(flag2)

    elif len(l)==3:

        if "$" in l[2]:
            
            d3={"mov":"00010","rs":"01000","ls":"01001"}          
            
            if l[0] in d3:
                
                print(d3[l[0]],end="")
                print("0",end="")
                if l[1] in dic:
                    
                    print(dic[l[1]],end="")

                   
                    if l[2][1:].isnumeric():
                        cd=int(l[2][1:])
                        cd1=bin(cd).replace("0b","")
                        cd1=list(cd1)
                        if len(cd1)<=7:
                            while(len(cd1)<7):
                                cd1.insert(0,0)
                                
                            
                            for i in cd1:
                               
                                print(i,end="")
                            print()
                        else:
                            print("syntax error: Immediate value exceeded 7 bits")
                            
                            error_gen(flag2)
                    else:
                        print("syntax error: Invalid immediate(not integer)")
                       
                        error_gen(flag2)
                else:
                    print("syntax error: Invalid register name")
                   
                    error_gen(flag2)
            else:
                    print("syntax error: Instruction not supported by ISA")
                    
                    error_gen(flag2)
            
        else:
            # TYPE C
            d4={"mov":"00011","ld":"00100","st":"00101","div":"00111","not":"01101","cmp":"01110"}
            if(len(l)==3):
                if l[0] in d4:
                   
                    if l[1] in dic:
                      
                        if l[2] in dic:
                           
                            print(d4[l[0]],end="")
                            print("00000",end="")
                            print(dic[l[1]],end="")
                            print(dic[l[2]])
                        elif l[2] in var_dic:
                            print(d4[l[0]],end="")
                            print("0",end="")
                            print(dic[l[1]],end="")
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
                                
                                print(i,end="")
                            print()
                        else:
                            print("syntax error: Invalid register name or invalid variable name")
                           
                            flag2= False
                            error_gen(flag2)
                    else:
                        print("syntax error: Invalid register name")
                        
                        flag2= False
                        error_gen(flag2)
                elif ":" in l[0]:
                    lst10=[]
                    for k in range(1,len(l)):
                        lst10.append(l[k])
                    
                    instruction(ls,ln,lst10,dic,var_dic,extra_var)  
                else:
                        print("syntax error: Instruction not supported by ISA")
                       
                        flag2= False
                        error_gen(flag2)  


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
        else:
           
            count=j
            flag=False
    
    j+=1
flag2=True

for i in range(0,len(red)):
    if len(red[i]) ==2:
        for j in range(0,len(new_list11[i])):
            if new_list11[i][1]=="hlt":
                if i!=len(new_list11)-1:
                    print("syntax error: hlt should be defined at last")
                    flag=False
                    break
    elif len(red[i]) ==1:
        for j in range(0,len(new_list11[i])):
            if new_list11[i][0]=="hlt":
                if i!=len(new_list11)-1:
                    print("syntax error: hlt should be defined at last")
                    flag=False
                    break
        

for i in range(k,len(red)):
    if error_gen(flag2)==True :
        l=list(map(str,red[i].split()))
        if l[0]!="var":
            instruction(red,line_number,l,dic,var_dic,k)
        else:
            print("syntax error: Variable can not be defined in between")
    else:
        print("syntax error")
        
        flag=False
        break