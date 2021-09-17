#!/usr/bin/env python
# coding: utf-8

# In[40]:


# Import dependencies
import pandas as pd
import os


# In[41]:


# Read file into DataFrame
file_path = os.path.join('../','Resources', 'ratings_and_sentiments.csv')
coffee_shop_review_df = pd.read_csv(file_path)
coffee_shop_review_df.head()


# In[42]:


# Find all reviews with a number rating greater than or equal to 4.
coffee_shop_review_df[coffee_shop_review_df['num_rating'] >= 4]


# In[43]:


# Find all the coffee shops with a overall sentiment greater than or equal to 4.
coffee_shop_review_df[coffee_shop_review_df['overall_sent'] >= 4]


# In[44]:


# Find all the coffee shops with an overall sentiment greater than or equal to 4 and an overall rating greater than 4.
review_count = coffee_shop_review_df[(coffee_shop_review_df['overall_sent'] >= 4) & (coffee_shop_review_df['num_rating'] > 4)]
review_count


# In[45]:


len(review_count)


# In[46]:


coffee_shop_review_df = coffee_shop_review_df.rename(columns={"review_text":"review"})
coffee_shop_review_df.head()


# In[47]:


# Change the name of the bool_HIGH column to bool_high
coffee_shop_review_df = coffee_shop_review_df.rename(columns={"bool_HIGH":"bool_high"})
coffee_shop_review_df.head()


# In[48]:


# Save your changes to the file as a pipe delimited file.
coffee_shop_review_df.to_csv('coffee_shop_reviews.txt', sep = '|')

