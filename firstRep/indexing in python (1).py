#!/usr/bin/env python
# coding: utf-8

# # indexing

# In[1]:


# make a string
a= "Samosa,Pakoda"
a


# In[2]:


a[0]


# In[3]:


a[2]


# In[4]:


len(a)


# In[5]:


a[0:6]


# In[10]:


a[-6:13]


# In[11]:


food="biryani"
food


# # string method

# In[12]:


food


# In[13]:


len(food)


# In[14]:


food.capitalize()


# In[15]:


# uppercase letters
food. upper()


# In[16]:


# lowercase letters
food.lower()


# In[19]:


# Replace
food.replace("b", "sh")


# In[21]:


#counting a specific alphabet in a string
name="baba_aamar with Dr Aamar Tufail"
name


# In[22]:


name.count("a")


# # finding an index number in string
# 
# 

# In[23]:


name="baba_aamar with Dr Aamar Tufail "
name


# In[26]:


name.find("D")


# # Basic data structure in python
# 1.Tuple
# 2.list
# 3.Dictionaries
# 4.set

# ## 1-Tuple
# .order collection of elements
# .enclosed in () braces/paranthesis
# .Different type of elements can be stored
# .once elements are stored you can not change them(unmutable)

# In[1]:


tuple1=(1,"python",True,2.5)
tuple1


# In[2]:


#type of a tuple
type(tuple1)


# # indexing in Tuple

# In[3]:


tuple1[1]


# In[4]:


tuple1[2]


# In[5]:


#Last element is exclusive
tuple1[0:3]


# In[6]:


#count of elements in tuple
len(tuple1)


# In[7]:


tup2=(2,"babaAamar",3.5,False)
tup2


# In[8]:


tuple1+tup2


# In[9]:


tuple1*2+tup2


# In[10]:


tup3=(20,50,30,60,79,85)
tup3


# In[11]:


#minimum
min(tup3)


# In[12]:


max(tup3)


# In[13]:


tup3*2


# # 2 list in pythn
# .ordered collection of elements
# .enclosed in [] square braces/bracket
# .Mutateable,mean you can change the values

# In[15]:


li1=[2,"babaAamar",False,3.4]
li1


# In[16]:


type(li1)


# In[17]:


len(li1)


# In[18]:


li2=[3,5,"babaAamar","Codanics",478,53.3,False]
li2


# In[19]:


li1+li2


# In[20]:


li1*2


# In[23]:


li1.reverse()
li1


# In[26]:


li1.append("Codanics Youtube channel")
li1


# In[32]:


li1.count("a")
li1


# In[33]:


li3=[20,30,35,50,40,12,15,11,10,356,56,886]
li3


# In[34]:


#Sorting a list
li3.sort()
li3


# # 3-Dictionaries
# -An unorderd collection of elements
# -Key and value
# -Curly braces or brackets{}
# -Mutateable/changes the value

# In[36]:


#Food and their prices
d1={"samosa":30, "Pakora":100, "Raita":20, "Salad":50,}
d1


# In[37]:


type(d1)


# In[38]:


d1.keys()


# In[39]:


values=d1.values()
values


# In[43]:


#adding new element
d1["Tikki"]=10
d1


# In[45]:


d2={"Dates":50, "Chocolates":200, "Swayyan":1000}
d2


# In[46]:


#concatinate
d1.update(d2)


# In[47]:


d1


# # 4-Set
# -unordered and unindexed
# -Curly braces are used{}
# -No Duplicates allowed

# In[50]:


s1={1,2.2,5.3,"Aamar","Codanics","Faisalabad",True}
s1


# In[52]:


s1.add("Aamar1")


# In[53]:


s1


# In[58]:


s1.remove("Aamar1")
s1


# In[ ]:





# In[ ]:




