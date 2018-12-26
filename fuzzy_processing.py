from __future__  import unicode_literals

import numpy as np
import pandas as pd
import csv
import nltk

import re
import os
import operator
import gensim
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from os import listdir
from os.path import isfile, join
from os import walk


def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    # s = re.sub(r"\s+", '-', s)

    return s

# Prints: I-cant-get-no-satisfaction"
# print(urlify("I can't get no satisfaction!"))

def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2))

data = data.replace(np.nan,' ' )
print(os.getcwd())
path = "/home/akhil/Downloads/Kubric_winter_internship"
os.chdir(path)
print(os.getcwd())

row_count = len(data.index)
col_count = len(data.columns)

print(row_count)
print(col_count)


#image
imagelist = [i for i in fuzzy_data.columns if "image" in i or "Image" in i or "img" in i or "logo" in i or "Logo" in i or "Img" in i or "logo" in i]
fuzzy_image = fuzzy_data.loc[:,imagelist]

#video
videolist = [i for i in fuzzy_data.columns if "video" in i or "effect" in i or "vo" in i or "box_call_out" in i or "VO" in i]
fuzzy_video = fuzzy_data.loc[:,videolist]

#audio
audiolist = [i for i in fuzzy_data.columns if "audio" in i or "music" in i or "bg" in i and "video" not in i]
fuzzy_audio = fuzzy_data.loc[:,audiolist]

#text
textlist = [i for i in fuzzy_data.columns if "text" in i and "effect" not in i or "product_name" in i or "price" in i and fuzzy_data[i].dtype == object or "location" in i or "Location" in i or "Campaign" in i or "gender" in i or "name" in i]
fuzzy_text = fuzzy_data.loc[:,textlist]

#int and float columns
droplist_one = [i for i in fuzzy_data.columns if fuzzy_data[i].dtype == float or fuzzy_data[i].dtype == int]

#others
#to create others bucket we will simply delete the cols which have been used above
fuzzy_random = fuzzy_data.copy()
droplist = imagelist + videolist + audiolist + textlist + droplist_one
fuzzy_random.drop(droplist,axis=1,inplace=True)


#fuzzy_image
raw_image_documents = []
for i in list(range(1,len(imagelist))):
    raw_image_documents.extend(fuzzy_image.iloc[:,i])
print("length of image vector is ",len(raw_image_documents))
print("the length of image list is ", len(imagelist))

raw_image_documents[0]

list_aa = []
aaa = 0
bbb= 0
for directories in os.listdir("/home/akhil/Downloads/Kubric_winter_internship/assets_folder_one/"): 
    mypath = "/home/akhil/Downloads/Kubric_winter_internship/assets_folder_one/" + directories + "/"
    for (dirpath, dirnames, filenames) in walk(mypath):
        list_aa.extend(filenames)
        aaa = aaa+1
        break
for directories in os.listdir("/home/akhil/Downloads/Kubric_winter_internship/assets_folder_two/"): 
    mypath2 = "/home/akhil/Downloads/Kubric_winter_internship/assets_folder_two/" + directories + "/"
    for (dirpath, dirnames, filenames) in walk(mypath2):
        list_aa.extend(filenames)
        bbb = bbb +1
        break
               
print("The number of folders in the assets_folder_one are ",aaa)
print("The number of folders in the assets_folder_two are ",bbb)
print("\n")    
# print(list_aa)
# print("\n") 
print("the length of list_aa is", len(list_aa))
#     dir = os.path.join('/home/akhil/Downloads/Kubric_winter_internship/assets_folder_one', directories)
#     os.chdir(dir)
#     current = os.path.dirname(dir)
#     new = str(current).split("-")[0]
#     print(new)

solutions = []
for i in range(0,len(raw_image_documents)):
    #print("The input query is",raw_image_documents[i])
    solutions.append(process.extractOne(raw_image_documents[i], list_aa, scorer=fuzz.token_sort_ratio))
print(solutions)

#raw_image_documents
print(len(raw_image_documents))
print(len(solutions))
list(zip(raw_image_documents , solutions))

# a=[]
# for i in list(range(1,len(f))):
#     a.append(fuzz.token_set_ratio(f[i],raw_image_documents[8]))
#     #print("the token set ratio is ",a)
    
# print(a)









