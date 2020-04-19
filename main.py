import time
from collections import OrderedDict

class redis(object):
    def __init__(self):
        self.item={}
    
    def set(self,key,value):
        flag="NULL"
        if 1==1:
            self.item[key]=value
            flag="OK"
        return flag
        
    def get(self,key):
        if key not in self.item:
            return "NIL"
        elif type(self.item[key])!=str:
            return "ERROR"
        else:
            return self.item[key]
            
    def expire(self,key,t):
        time.sleep(t)
        del self.item[key]
        
    def zadd(self,key,score,value):
        if key not in self.item:
            self.item[key]=OrderedDict()
            temp=self.item[key]
            temp[score]=[]
            temp[score].append(value)
        else:
            self.item[key][score].append(value)
            
    def zrank(self,key,value):
        if key not in self.item:
            return "NILL"
        flag="NILL"
        count=0
        for i in self.item[key]:
            if value in self.item[key][i]:
                return count
            count+=1
        return flag
        
    def zrange(self,key,start,end):
        if key not in self.item:
            return "NILL"
        l=self.item[key]
        ans=""
        for i in l:
            ans+='\n'.join(l[i])
        return ans
        
    def exists(self,key):
        if key in self.item:
            return 1
        else:
            return 0
            
    def append(self,key,value):
        if key in self.item:
            self.item[key]+=value
        else:
            self.item[key]=value
        
    def delete(self,key):
        if key in self.item:
            del self.item[key]
            
        

            
        
        
        
        
        
        
