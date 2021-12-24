#!/usr/bin/env python
# coding: utf-8

# In[2]:


import turtle


# In[3]:


#Testing if the import works with simple turtle commands


# In[7]:


turtle.bgcolor("black")
turtle.pensize("2")
turtle.color("red")


# In[8]:


#simple square

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.done()


# In[10]:


#Second simple test

turtle.bgcolor("black")
turtle.pensize("2")
turtle.color("red")


# In[11]:


for colours in ["blue","green","yellow"]:
    turtle.color(colours)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
turtle.done()


# In[13]:


#Cool graphics using turtle

turtle.bgcolor("black")
turtle.pensize("2")
turtle.color("red")


# In[ ]:


turtle.speed(20)

for i in range(12):
    for colours in ["blue", "purple", "red", "orange", "yellow", "green"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(5)
turtle.done()


# In[ ]:




