import pandas as pd 
import os
import glob
import shutil


DIRECTORY = "/Volumes/drive1/12_18s/"
# print(os.listdir(DIRECTORY))
# files = [x[0] for x in os.walk(DIRECTORY)]
# folders = ['/Volumes/drive1/12_18s/45', '/Volumes/drive1/12_18s/45_0.8', '/Volumes/drive1/12_18s/45_1280_720_0.25', '/Volumes/drive1/12_18s/45_1280_720_0.8', '/Volumes/drive1/12_18s/45_1280_720_2', '/Volumes/drive1/12_18s/45_2', '/Volumes/drive1/12_18s/45_640_360_0.8', '/Volumes/drive1/12_18s/45_852_480_0.25', '/Volumes/drive1/12_18s/45_852_480_0.8', '/Volumes/drive1/12_18s/45_852_480_2']
# # print(len(folders))
# files = glob.glob("/Volumes/drive1/12_18s/*", recursive = True)
# # print(files)
# # files = glob.glob("C:\\HDRStudy\\videos\\*.mp4")
# base_list = []
# content_list = []
# bitrate_list = []
# resolution_list = []

# for folder in folders:
#     files = glob.glob(folder + "/*.avi")
#     if len(folder.split("/")[-1].split("_")) == 1:
#         resolution = "1080"
#         bitrate = "reference"
#     elif len(folder.split("/")[-1].split("_")) == 2:
#         resolution = "1080"
#         bitrate = folder.split("/")[-1].split("_")[-1]
#     else:
#         resolution = folder.split("/")[-1].split("_")[-2]
#         bitrate = folder.split("/")[-1].split("_")[-1]
    
#     for file in files:
#         base = os.path.basename(file)
#         base_list.append(base)
#         content = base.split(".")[0]
#         content_list.append(content)
#         filename = content + "_res=" + resolution + "_bitrate=" + bitrate + ".avi"
#         full_filename = folder + "/" + filename
#         os.rename(file, full_filename)
#         shutil.copy(full_filename, "/Volumes/drive1/12_18s/videos")


VIDEOS = "/Volumes/drive1/12_18s/videos"
files = glob.glob(VIDEOS + "/*.avi")

base_list = []
content_list = []
resolution_list = []
bitrate_list = []

for file in files:
    base = os.path.basename(file)
    base_list.append(base)
    content_a = base.split("_")[:-2]
    content = "_".join(content_a)
    content_list.append(content)
    resolution_list.append(base.split("_")[-2].split("=")[-1])
    bitrate_list.append(base.split("_")[-1].replace(".avi", "").split("=")[-1])


df = pd.DataFrame(list(zip(base_list,content_list, resolution_list, bitrate_list)),\
                    columns = ['video','content','resolution','bitrate' ])
print(df)
df.to_csv('metadata.csv',index=False)