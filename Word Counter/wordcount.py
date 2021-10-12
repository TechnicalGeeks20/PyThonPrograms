import time
### Uncomment this to input file ###
try:
    file=input("Enter File Name : ")
    print("Retriving",file,"....")
    lines=open(file).read()
except:
    print("File Not Found")
    lines=str()
### End ###

### Uncomment below to input string ###
#lines=input("Enter the String : ")
### End ###


### This is code to count the word ###
words=lines.split()
counts=dict()
count=0
t1=time.time()
for word in words:
    word=word.lower()
    ### Using Exception Handling ###
    try:
        counts[word]=counts[word]+1
    except:
        counts[word]=1
    ### END ###
    # ### Usual Way ###
    # if word in counts:
    #    counts[word]=counts[word]+1
    # else:
    #    counts[word]=1
    # ### END ###
    # ### Fastest Way ###
    # counts[word]=counts.get(word,0)+1
    # ### END ###
    count=count+1
### End ###
t2=time.time()
print("Evaluation Time : ",t2-t1)    
print("Total Words :",count)

#print("Word Frequency : \n",counts)


### Uncomment this to search count number of any word ###
#key=input("Enter Word :")
#if key in counts:
#    print(key,":",counts[word])
#else: print(key,"Not Found")
### End ###