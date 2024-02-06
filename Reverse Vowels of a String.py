
    
def lv(s):
    v=[]
    for i in s : 
        if i.lower() in {'a', 'e', 'i', 'o', 'u'} :
            v.append(i)
    return v


def vreve(s):
    r=""
    lvs=lv(s)
    #print(lvs)
    for i in s :
        if i.lower() not in {'a', 'e', 'i', 'o', 'u'}  :
            r= r + i
        else : 
            r+=lvs[-1]
            lvs.pop()
     #       print(lvs)
    return r



class Solution(object):
    def reverseVowels(self, s):
        return vreve(s)
        

    
        
