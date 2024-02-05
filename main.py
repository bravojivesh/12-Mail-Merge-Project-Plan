#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Letters/starting_letter.txt") as letter:
    content= letter.read()

with open ("./Input/Names/invited_names.txt") as names:
    names_lis= names.readlines() #this is different from "readline()". Singular, Plural.
    # print (names_lis) #db: we get a list of lines from the file. Entire List. When read the \n will be ignored.

    for single_name in names_lis:
        stripped_sing_name= single_name.strip()
        new_content=content.replace("[name]", stripped_sing_name)
        path ="./Output/ReadyToSend/"
        with open (f"{path}{stripped_sing_name}.txt", mode="w") as output:
            output.write(new_content)

        # print (stripped_sing_name) #this is for debugging