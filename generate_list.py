# import os
# from shutil import copyfile
# import glob
# import pandas as pd
# import random

# def swapPositions(vidlist, pos1, pos2):
     
#     vidlist[pos1], vidlist[pos2] = vidlist[pos2], vidlist[pos1]
#     return vidlist

# def remove_adjacent_content(df):
#     flag = 0
#     vidlist = list(df['video'])
#     new_df = df.sample(frac=1).reset_index(drop=True)
#     for i in range(len(vidlist)-2):
#         if(new_df['content'].iloc[i]==new_df['content'].iloc[i+1]):
#             row1,row2 = new_df.iloc[i+1,:].copy(),new_df.iloc[i+2,:].copy()
#             new_df.iloc[i+1,:],new_df.iloc[i+2,:] = row2,row1
#             flag = 1
#     return new_df,flag

# def randomize_group(df):
#     filenames = list(df['video'])

#     outfolder = './lists/'
#     flag = 1
#     count = 0
#     temp_list = filenames
#     while(flag):
#         df,flag = remove_adjacent_content(df)
#         count=count+1
#         if(count>20):
#             break

#     return df
    

# def sep_sessions(df,seed):
#     contents = df['content']
#     unique_contents = list(set(contents))
#     first_session_contents = random.Random(seed).sample(unique_contents,int(len(unique_contents)//2))
#     second_session_contents = [i for i in unique_contents if i not in first_session_contents]
#     first_session_df = df[df['content'].isin(first_session_contents)]
#     second_session_df = df[df['content'].isin(second_session_contents)]
#     return first_session_df,second_session_df

# def get_lists(df):
#     for seed in range(1,80):
#         first_session_df,second_session_df = sep_sessions(df,seed)
#         first_session_randomized_df = randomize_group(first_session_df)
#         second_session_randomized_df = randomize_group(second_session_df)
#         list1_filename = './lists/list_{}_{}.csv'.format(seed,1)
#         list2_filename = './lists/list_{}_{}.csv'.format(seed,2)
#         first_session_randomized_df.to_csv(list1_filename,index=0)
#         second_session_randomized_df.to_csv(list2_filename,index=0)

# df = pd.read_csv('../metadata.csv')
# get_lists(df)



