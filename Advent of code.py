
# coding: utf-8

### Ex1a

# In[1]:

r=0
o='('
i=0
f = open('ex1.txt', 'r')
while True:
    ch=f.read(1)
    if not ch: break
    if ch=='(':
        r=r+1
    if ch==')':
        r=r-1
r


### Ex1b

# In[2]:

r=0
o='('
i=0
f = open('ex1.txt', 'r')
while True:
    ch=f.read(1)
    if not ch: break
    if ch=='(':
        r=r+1
    if ch==')':
        r=r-1
    i=i+1
    if r<0: break
        
i    


### Ex2a

# In[3]:

import numpy as np
import math


f = open('ex2a.txt', 'r')
dim=[1,2,3]
A=[1,0,0]
i=0
temp='0'
Area=0
Area_tot=0

while True:
    ch=f.read(1)
    if not ch: break
    if ch!='\n' and ch!='x':
        temp=temp+ch
    if ch=='x': 
        dim[i]=int(temp)
        temp=''
        i=i+1
    if ch=='\n': 
        dim[i]=int(temp)
        temp=''
        i=0
        A[0]=2*dim[0]*dim[1]
        A[1]=2*dim[0]*dim[2]
        A[2]=2*dim[1]*dim[2]
        Area=np.sum(A)+np.min(A)/2
        Area_tot=Area_tot+Area
        
Area_tot

        
    


### Ex2b

# In[4]:

import numpy as np
import math


f = open('ex2a.txt', 'r')
dim=[1,2,3]
P=[1,0,0]
i=0
temp='0'
P2=0
P2_tot=0

while True:
    ch=f.read(1)
    if not ch: break
    if ch!='\n' and ch!='x':
        temp=temp+ch
    if ch=='x': 
        dim[i]=int(temp)
        temp=''
        i=i+1
    if ch=='\n': 
        dim[i]=int(temp)
        temp=''
        i=0
        P[0]=2*(dim[0]+dim[1])
        P[1]=2*(dim[0]+dim[2])
        P[2]=2*(dim[1]+dim[2])
        P2=np.min(P)+(dim[0]*dim[1]*dim[2])
        P2_tot=P2_tot+P2
        
P2_tot


### Ex 3a

# In[5]:

import numpy as np
import math
s=(8193,8193)
houses=np.zeros(s)
houses[0,0]=0
i=int(np.sqrt(8193))
j=i
houses[i,j]=1

f = open('ex3a.txt', 'r')
a=np.zeros(s)
while True:
    ch=f.read(1)
    if not ch: break
    if ch=='^': i=i+1
    if ch=='v': i=i-1
    if ch=='>': j=j+1
    if ch=='<': j=j-1
    houses[i,j]=houses[i,j]+1
how_many=np.sum(houses>0)
print(how_many)


### Ex3b 

# In[8]:

import numpy as np
import math
s=(8193,8193)
houses_santa=np.zeros(s)
houses_robot=np.zeros(s)
houses=np.zeros(s)
i_s=int(np.sqrt(8193))
j_s=i

i_r=int(np.sqrt(8193))
j_r=i

tot=0

houses_santa[i_s,j_s]=1
houses_robot[i_r,j_r]=1
f = open('ex3a.txt', 'r')
a=np.zeros(s)
while True:
    ch=f.read(1)
    if not ch: break
        
    tot=tot+1
    if (np.mod(tot,2)==0): 
        if ch=='^': i_r=i_r+1
        if ch=='v': i_r=i_r-1
        if ch=='>': j_r=j_r+1
        if ch=='<': j_r=j_r-1
        houses_robot[i_r,j_r]=houses_robot[i_r,j_r]+1

    
    if (np.mod(tot,2)>0):
        if ch=='^': i_s=i_s+1
        if ch=='v': i_s=i_s-1
        if ch=='>': j_s=j_s+1
        if ch=='<': j_s=j_s-1
        houses_santa[i_s,j_s]=houses_santa[i_s,j_s]+1
how_many=np.sum((houses_santa+houses_robot)>0)

 


# In[9]:

print how_many


# In[ ]:




# In[ ]:



