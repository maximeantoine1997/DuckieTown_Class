#!/usr/bin/env python
# coding: utf-8

# In[1]:


def DT_TOKEN():
    # todo change this to your duckietown token
    dt_token = "dt1-3nT8KSoxVh4MguChczKWnzfKkqdXH3f1DY4fH8sGXRkBRbi-43dzqWFnWd8KBa1yev1g3UKnzVxZkkTbfUmR7d8Uzhhdn4TfiUt3dZ8L4tTfvsmnKx"
    return dt_token

def MODEL_NAME():
    # todo change this to your model's name that you used to upload it on google colab.
    # if you didn't change it, it should be "yolov5"
    return "yolov5"

# In[2]:


def NUMBER_FRAMES_SKIPPED():
    # todo change this number to drop more frames
    # (must be a positive integer)
    return 0

# In[8]:


# `class` is the class of a prediction
def filter_by_classes(clas):
    # Right now, this returns True for every object's class
    # Change this to only return True for duckies!
    # In other words, returning False means that this prediction is ignored.  
    return True

# In[9]:


# `scor` is the confidence score of a prediction
def filter_by_scores(scor):
    # Right now, this returns True for every object's confidence
    # Change this to filter the scores, or not at all
    # (returning True for all of them might be the right thing to do!)
    if scor > 0.85:
        return True
    return False

# In[13]:


# `bbox` is the bounding box of a prediction, in xyxy format
# So it is of the shape (leftmost x pixel, topmost y pixel, rightmost x pixel, bottommost y pixel)
def filter_by_bboxes(bbox):
    # Like in the other cases, return False if the bbox should not be considered.
    print(f"bbox 0: {bbox[0]}")
    print(f"bbox 2: {bbox[2]}")
    
    y = 416
    x = 416
    
    # if leftmost x is on the right side of the image. consider it
    if bbox[2] > x/2:
        # if topmost y is below 1/3 of the image. consider it
        if bbox[0] > y/3:
            return True
    
    return False

