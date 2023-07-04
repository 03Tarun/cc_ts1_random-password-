#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import string

def generate_password(length=8):
    """Function to generate a random password."""
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Usage example
password_length = 10
random_password = generate_password(password_length)
print("Random Password:", random_password)


# In[ ]:





# In[ ]:




