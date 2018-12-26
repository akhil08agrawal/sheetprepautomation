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
from os import walk    #to get the list of files on the local machine


def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    # s = re.sub(r"\s+", '-', s)
    return s

# Prints: I-cant-get-no-satisfaction"
# print(urlify("I can't get no satisfaction!"))

#This is to check the intersection of two lists. In this whether the imagelist,videolist, audiolist and random
#has any similar column or not
def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2))


data = data.replace(np.nan,' ' )
#This is important as when there are nan values the loop actions were leading to an error

print(os.getcwd())
#Define the path to the assets folder
path = "/home/akhil/Downloads/Kubric_winter_internship"
os.chdir(path)
print(os.getcwd())

row_count = len(data.index)
col_count = len(data.columns)

print(row_count)
print(col_count)

image_fuzzy_words = ["image","Image","img","logo","Logo","Img"]
video_fuzzy_words = ["video","effect", "vo","box_call_out", "VO"]
audio_fuzzy_words = ["audio","music","bg","Audio","AUDIO"]
text_fuzzy_words = ["text","effect","product_name", "price" ,"location", "Location", "Campaign", "gender","name"]
image_extensions = [".jpg", ".jpeg", ".png" ,".PNG" , ".JPEG" ,".Jppeg","jppeg" ]
video_extensions = [".mov" , ".mp4" , ".MP4" ,".MOV"]

imagelist = []
videolist = []
audiolist = []
textlist = []

#######################################################
# Making list of columns for different genre of files #
#######################################################
#image
imagelist = [i for i in fuzzy_data.columns if any(ext in i for ext in image_fuzzy_words)]
fuzzy_image = fuzzy_data.loc[:,imagelist]

#video
videolist = [i for i in fuzzy_data.columns if any(ext in i for ext in image_fuzzy_words)]
fuzzy_video = fuzzy_data.loc[:,videolist]

#audio
audiolist = [i for i in data.columns if any(ext in i for ext in audio_fuzzy_words) and "video" not in i]
fuzzy_audio = fuzzy_data.loc[:,audiolist]

#text
textlist = [i for i in fuzzy_data.columns if any(ext in i for ext in text_fuzzy_words)]
fuzzy_text = fuzzy_data.loc[:,textlist]

#int and float columns
droplist_one = [i for i in fuzzy_data.columns if fuzzy_data[i].dtype == float or fuzzy_data[i].dtype == int]

#others
#to create others/the random bucket we will simply delete the cols which have been used above
fuzzy_random = fuzzy_data.copy()
droplist = imagelist + videolist + audiolist + textlist + droplist_one
fuzzy_random.drop(droplist,axis=1,inplace=True)

#Now adding the directory columns to all the sub-dataframes

data = data.reset_index()
fuzzy_image = fuzzy_image.reset_index()
fuzzy_video = fuzzy_video.reset_index()
fuzzy_audio = fuzzy_audio.reset_index()
fuzzy_text = fuzzy_text.reset_index()
fuzzy_random = fuzzy_random.reset_index()

data.index = fuzzy_image.index

#Adding the directory column to all the sub-dataframes
fuzzy_image['directory'] = data['directory']
fuzzy_video['directory'] = data['directory']
fuzzy_audio['directory'] = data['directory']
fuzzy_text['directory'] = data['directory']


#fuzzy_image
raw_image_documents = []
for i in list(range(1,len(imagelist))):
    raw_image_documents.extend(fuzzy_image.iloc[:,i])
print("length of image vector is ",len(raw_image_documents))
print("the length of image list is ", len(imagelist))

raw_image_documents[0]

#######################################################
# Making one list for all the files in the local directory#
#######################################################
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
print("the length of list_aa is", len(list_aa))

#######################################################
# Comparing each element in the list with the filenames 
# directory and returning the closet match with a fuzzy score#
#######################################################
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

#######################################################
# To directly create a list of image elements in the csv sheet #
#######################################################
imagelist = []
videolist = []

for j in range(0,col_count):
    garbage = []
    garbage= [i for i in data.iloc[:,j] if any(ext in i for ext in image_extensions)]
    imagelist.extend(garbage)
#print("The list of images with image input\n",imagelist)
for j in range(0,col_count):
    garbage = []
    garbage= [i for i in data.iloc[:,j] if any(ext in i for ext in video_extensions)]
    videolist.extend(garbage)

##########################
# Search for validation #
##########################

#To check whether the cols with number output have numbers in a desired range or not






















