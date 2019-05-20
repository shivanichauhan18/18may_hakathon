mainStr="the quick brown fox jumped over the lazy dog . the dog slept over the verandah."
b=mainStr.split(' ')
print b 
subStr="over"
replacementStr="on"

l=len(b)

i=0
while i<len(b):
    if b[i]==subStr:
        b.remove(b[i])
        b.insert(i,replacementStr)
    i=i+1
print " ".join(b)