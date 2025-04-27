
# coding: utf-8

# # Introduction to Jupyter Notebooks
# 
# [Jupyter Notebooks](https://jupyter.org/) are an enviornment allowing you to code and to take notes in one same document. That means that in this notebook you can:
# - write cells like this one in [markdown](https://en.wikipedia.org/wiki/Markdown) (try and press `Enter` when this cell is selected, it will show you the code for it... press `Ctrl-Enter` or `Shift-Enter` and it's back to how it was!);
# - write code cells like the one just below (press `Ctrl-Enter` or `Shift-Enter` to run it as well):

# In[3]:


print("Hello Jupyter!")


# ## Shortcuts
# 
# The Jupyter environment is full of shortcuts and great things that make your life easier. 
# 
# A quick list:
# - press `Enter` to start typing into a cell, `Escape` to navigate your notebook (you can then press `j` or `k`, or the arrow keys, to go up and down;
# - when navigating (not typing in a cell), you can press `a` to create a new cell above, `b` for below;
# - if a cell is selected (but you are not typing in it), you can press `m` to turn it into a `markdown` cell, and `y` to make it a code cell;
# - if you press `Ctrl-Enter`, you will run the cell and stay on it, whereas if you press `Shift+Enter`, you go one cell below (and if it is the last one, a new one will be created);
# - if a cell is selected, you can press `x` to cut it, `c` to copy it, and then `v` to paste after the current cell, and `V` to paste before it;
# - **Many** other shortcuts, which you can also customise, check in the menu above "Help" > "Keyboard Shortcuts".
# 
# ---

# ## Markdown
# 
# Markdown is an easy way to write text in a web context without going for the full html syntax. 
# 
# You can check out [this cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). 
# 
# Basic things:
# - Separate paragraphs with an empty line, or two spaces at the end of the line;
# - italic with `*asterisks*` or `_underscores_`, bold with `**two**` or `__two__`, (the two can be combined);
# - lists, numbered or unnumbered, like so:
# 
# ```
# unnumbered list with a line starting with -
# numbered list with 1., 2., etc.
# ```
# 
# - code snippets using this the grave accent \`, multiline with three of them \`\`\`;
# - titles (h1-6) using `#` starting the line, from just one to six;
# - three stars `***` or dashes `---` give you a horizontal line like tihs one (it needs to be at the start of the line): 
# ---
# - links are generated like so: `[text](link.com)`;
# - images similarly: `![image text](image.jpg)`;
# 
# For more details, check out the cheatsheet!

# ---
# 
# # Simple coding
# 
# As seen in the videos, any code cell allows you to input code and get results immediately.

# In[2]:


x = 10
y = x + 2
y


# Notice that if you run a cell with a variable at the end of it, it will act like a print out of that variable.

# In[3]:


print(y) # same as above, and our y still exist!


# You can do all sorts of nice things now in Python!

# In[9]:


mylist = [1,2,3,4]
mylist_squared = [element**2 for element in mylist] # nice and Pythonic list comprehension syntax
print(mylist_squared)
print(max(mylist_squared)) # the maximum element


# When in doubt, ask for help! It can be quite dry at first but if you get used to how it's written, it's a goldmine of information!

# In[8]:


help(max)


# Don't ever forget to press the `TAB` button as well, which allows you to access both the autocomplete (for variables, classes and functions names) and methods (in-built functionality from libraries).
# 
# In the cell below, put your cursor at the end of each of those, press `TAB` and look at the list of options. (These will only work if you have run the cells defining the variables `mylist` and `mylist_squared` above!)
# 
# Beware! These cells are now incomplete, and will throw an error if you run them like that!

# In[12]:


my # put your cursor after y and hit `TAB`: you will be able to choose between the two variables starting by these letters


# In[ ]:


mylist. # hitting `TAB` after the . will show all list methods that Python has (many!)


# ---
# ## Now a Data Science example!

# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib # remember in Python you have to import the relevant libraries

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0.1,10) # return evenly spaced numbers over a specified interval, from 0.1 to 10 (see the help below)

line = plt.plot(x, np.log(x),'--',linewidth = 1) # plot these evenly spaced numbers against their logarithm
                                                 # use '--' as line (try with just one for instance), 
                                                 # and control the width


# In[10]:


help(np.linspace)

