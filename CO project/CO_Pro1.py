def error_gen(flag2):
    #flag2= False
    return flag2
def instruction(ls,ln,l,dic,var_dic):
    flag2=True
    if len(l)==5:
        if ":" in l[0]:
            lst10=[]
            for k in range(1,len(l)):
                lst10.append(l[k])
            # print(lst10)
            instruction(ls,ln,lst10,dic,var_dic)  
        else:
                print("syntax error")
                f2.write("syntax error")
                flag2= False
                error_gen(flag2)
    if len(l)==4:
        d1={"add":"00000","sub":"00001","mul":"00110","xor":"01010","or":"01011","and":"01100"}
        if l[0] in d1:
            f2.write(d1[l[0]])
            f2.write("00")
            if l[1] in dic:
                f2.write(dic[l[1]])
                if l[2] in dic:
                    f2.write(dic[l[2]])
                    if l[3] in dic:
                        f2.write(dic[l[3]])
                    else:
                        print("syntax error")
                        f2.write("syntax error")
                        flag2= False
                        error_gen(flag2)
                        
                else:
                    print("syntax error")
                    f2.write("syntax error")
                    flag2= False
                    error_gen(flag2)
            else:
                print("syntax error")
                f2.write("syntax error")
                flag2= False
                error_gen(flag2)
        elif ":" in l[0]:
            lst10=[]
            for k in range(1,len(l)):
                lst10.append(l[k])
            # print(lst10)
            instruction(ls,ln,lst10,dic,var_dic)  
        else:
                print("syntax error")
                f2.write("syntax error")
                flag2= False
                error_gen(flag2)
        
    elif len(l)==2:
        # type E
        array={"jmp":"01111" ,"jlt":"11100","jgt":"11101","je":"11111"}
        if l[0] in array:
            # f2.write(array[l[0]])
            # f2.write("0000")
            # f2.write(l[1])
            new_list1=[]
            for read in ls:
                # new_list=list(map(str,read.split()))
                new_list1.append(list(map(str,read.split())))
            for j in range(0,len(new_list1)):
                if l[1] == new_list1[j][0][:-1]:
                    # print(ln[j])
                    # f2.write(str(ln[j]))
                    flag2=True
                    f2.write(array[l[0]])
                    f2.write("0000")
                    for i in ln[j]:
                        f2.write(str(i))
                    break
                else:
                    flag2=False
            if flag2==False:
                print("syntax error")
                f2.write("syntax error")
                flag2= False
                error_gen(flag2)  

            # f2.write("\n")
        if ":" in l[0]:
            if(l[1]=="hlt"):
                f2.write("11010")
                f2.write("00000000000")
            else:
                print("syntax error")
                f2.write("syntax error")
                flag2= False
                error_gen(flag2)  
        if l[0] not in array and ":" not in l[0]:
            print("syntax error")
            f2.write("syntax error")
            flag2= False
            error_gen(flag2)
    elif len(l)==1:
        if l[0]=="hlt":
            f2.write("11010")
            f2.write("00000000000")
        elif ":" in l[0]:
            pass
        else:
                print("syntax error")
                f2.write("syntax error")
                flag2= False
                error_gen(flag2)

    elif len(l)==3:

        if "$" in l[2]:
            
            d3={"mov":"00010","rs":"01000","ls":"01001"}          
            # for i in d3:
            if l[0] in d3:
                f2.write(d3[l[0]])
                f2.write("0")
                if l[1] in dic:
                    f2.write(dic[l[1]])
                    # f2.write("_")
                    if l[2][1:].isnumeric():
                        cd=int(l[2][1:])
                        cd1=bin(cd).replace("0b","")
                        cd1=list(cd1)
                        if len(cd1)<=7:
                            while(len(cd1)<7):
                                cd1.insert(0,0)
                                # print(cd1)
                            
                            for i in cd1:
                                #f2.write(cd1)
                                
                                f2.write(str(i))
                        else:
                            print("syntax error")
                            f2.write("syntax error")
                            error_gen(flag2)
                    else:
                        print("syntax error")
                        f2.write("syntax error")
                        error_gen(flag2)
                else:
                    print("syntax error")
                    f2.write("syntax error")
                    error_gen(flag2)
            else:
                    print("syntax error")
                    f2.write("syntax error")
                    error_gen(flag2)
            
        else:
            # TYPE C
            d4={"mov":"00011","ld":"00100","st":"00101","div":"00111","not":"01101","cmp":"01110"}
            if(len(l)==3):
                if l[0] in d4:
                    # f2.write(d4[l[0]])
                    if l[1] in dic:
                        # f2.write(dic[l[1]])
                        if l[2] in dic:
                            f2.write(d4[l[0]])
                            f2.write("00000")
                            f2.write(dic[l[1]])
                            f2.write(dic[l[2]])
                        elif l[2] in var_dic:
                            # f2.write(str(var_dic[l[2]]))
                            f2.write(d4[l[0]])
                            f2.write("0")
                            f2.write(dic[l[1]])
                            for i in var_dic[l[2]]:
                                f2.write(str(i))
                        else:
                            print("syntax error")
                            f2.write("syntax error")
                            flag2= False
                            error_gen(flag2)
                    else:
                        print("syntax error")
                        f2.write("syntax error")
                        flag2= False
                        error_gen(flag2)
                elif ":" in l[0]:
                    lst10=[]
                    for k in range(1,len(l)):
                        lst10.append(l[k])
                    # print(lst10)
                    instruction(ls,ln,lst10,dic,var_dic)  
                else:
                        print("syntax error")
                        f2.write("syntax error")
                        flag2= False
                        error_gen(flag2)  



f = open("test.txt","r")
red=f.readlines()
f.close()
f2=open("output.txt","w")
dic={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
line_number={}
var_dic={}
k=0
j=0
flag=True
new_list11=[]
# for k in red:
#     r=list(map(str,k.split()))
#     for m in k:
#         for 
count=0     
for j in range(0,len(red)):
    cd1=bin(j).replace("0b","")
    cd1=list(cd1)
    while(len(cd1)<7):
        cd1.insert(0,0)
        # print(cd1)
    line_number[j]=cd1
    lst=list(map(str,red[j].split()))
    new_list11.append(lst)
    if lst[0]=="var":
        if j==k:
            var_dic[lst[1]]=line_number[k]
            k+=1
        else:
            # class goto1(Exception):
            #     print("syntax error")
            count=j
            flag=False
    j+=1
flag2=True

for i in range(0,len(red)):
    if len(red[i]) ==2:
        for j in range(0,len(new_list11[i])):
            if new_list11[i][1]=="hlt":
                if i!=len(new_list11)-1:
                    print("syntax error")
                    flag=False
                    break
    elif len(red[i]) ==1:
        for j in range(0,len(new_list11[i])):
            if new_list11[i][0]=="hlt":
                if i!=len(new_list11)-1:
                    print("syntax error")
                    flag=False
                    break
        
# if flag==True:
for i in range(k,len(red)):
    if error_gen(flag2)==True :
        l=list(map(str,red[i].split()))
        if l[0]!="var":
            instruction(red,line_number,l,dic,var_dic)
            f2.write("\n") 
        else:
            print("syntax error")
            f2.write("syntax error\n")
            

    else:
        print("syntax error")
        f2.close()
        flag=False
        break

