# COproject_Grp2
Assembler

In this project we used Python language to write the program for our assembler. 
We made use live share feature of vs code to collaborate on the code at the same time. 
We defined a function that would test each instruction on basis of instruction length. By doing this we could divide all instructions in 5 categories by length. In each category we made subcategories according to need.
We used print statements to identify where the error is and then modified the code according to that error.
We read the instructions from a file and then made a nested list in which each element was a list which contained the instruction. This list is used to check the labels since each nested list is a instruction and that instruction is given a line number , outer_list[inside_list[0]] is compared with the label statement given after opcode. 
We also used dictionaries to give opcodes and register numbers in binary for the machine code conversion.
We also used dictionary to give each instruction a line number which we used in machine code for "jmp" ,"je" and similar instructions.
We assigned binary number of 7 bits to variables according to the line numbers.
In built python functions are also used like isnumeric(),len() etc.
