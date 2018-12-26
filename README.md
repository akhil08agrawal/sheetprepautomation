# sheetprepautomation
The initial csv file is not optimally organised and there may be many assets which are not present locally/remotely. So, the task is to map out a better organised csv file and let the user know about the missing assets which are to be used in the campaign. It also covers fuzzy search as there may be small error in the name of the assets due to human error and this process will allow the user to look into the suggested assets present in the remote/local storage system. The user then can authenticate the suggested asset name changes and this will update the sheet. 
Data Structure
The input will be a sheet and a folder which will contain  all the assets in the specified folders. Output can be in the form of a json which could be something like as follow : 
Stats
Image:
{  Completeness_Score: % availability
    tuple for unavailable files:
    {  (the name in the csv file , (suggested asset to be used , score)),
       .
       .
     }
}
Video:
...
Audio:
...
Fonts:
...
Others:
...


The fuzzy score can be achieved in four different ways:
Simple Ratio:
Partial Ratio:
Token Sort Ratio:
Token Set Ratio:
What are we doing?
Currently we are creating buckets for image, video, audio, text and others. And for each bucket we are creating a single vector of items in all the columns in that sub data file. And at the same time, we also create a single list consisting of all the filenames in the assets in the local/remote system. 
Then for each item in the list of items we compare it with each item in the assets_list and then combining it with the item with maximum fuzzy score. We have the freedom to choose the scoring method. A sample output is as follows:

[('image', ('FHM KBag jpg', 35)), 
('occasion image', ('TSG Vacation jpg', 47)),
 ('UTB Brunch M jpg', ('UTB Brunch M jpg', 100)), 
('UTB Brunch M jpg', ('UTB Brunch M jpg', 100)), 
('UTB Workwear M jpg', ('UTB Workwear M jpg', 100)),
 ('UTB Workwear M', ('UTB Workwear M jpg', 88)), 
('UTB Workwear M', ('UTB Workwear M jpg', 88)), 
('UTB Party jpg', ('UTB Party jpg', 100)), 
('SP WorkWear', ('TSG WorkWear jpg', 74)),
('SP Fitness jpg', ('SP Jeans jpg', 69))
('UVS Festival M jpg', ('UVS Festival F jpg', 89)),
('SP WorkWear', ('TSG WorkWear jpg', 74))
('SP WorkWear', ('TSG WorkWear jpg', 74)), 
('SP Fitness jpg', ('SP Jeans jpg', 69)),]

Problem of traversing through the directory and having the assets at the designated folder. 

Other issues to look at:
1) How to take care of assets being present in a particular designated folder. How to check for that. Currently the model just tells whether the asset is available or not, irrespective of its presence at a particular location.
2) The model is for a local system. Need to be mirrored for the remove system.
3) The current model makes bucket as per the col names and so there may be problems when we encounter new set of col names.
4) How to process the sheet columns simultaneously, when the sheet is too large?

Approach:

1) Using the columns names divide the original csv file into 4 sub files, namely images, video, audio and others.
2) Add the col which has the directory name to all the above sub-dataframes
3) Group the data by the directory names so that the list of assets is not made multiple times for the same directory. (this is done using the walk function)
4) To each element in the sub-data, lets say imagelist, the output is the perfect match in that directory sub-folder and in case when there is not a perfect match then we make a list of the assets in all the sister folders in the main folder and then check for any fuzzy matches. 
5) The same is repeated for the sub-dataframe created for videos, audio, etc.
