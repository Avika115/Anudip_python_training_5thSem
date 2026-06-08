#WAP to input a setence from user and count the number of special characters present in the sentence 

sentence = input("enter a sentence")
count = 0
for ch in sentence:
    if ch.isalnum()==False:
        count+1
print("the number of special characters", count)
