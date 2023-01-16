# -*- coding: utf-8 -*-
from psychopy import visual, core, event,gui,logging
import os, random, time, csv 
import pandas as pd
from os.path import join
from threading import Thread
from queue import Queue
import time

#define some global variables
score_dir = './score/'
video_dir = 'C:\\Humanstudy\\videos\\all_vid\\'
video_list_dir = 'C:\\ASLStudy\\list'
# csv for each particant, different csv , name of the video 


def train():
    video_dir = 'C:\\Humanstudy\\videos\\sample_vids\\'

    video_list = ['nasa1.mp4','nasa2.mp4']
    
    for video in video_list:
        cmd = "\"C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe\"  {}".format(join(video_dir,video))
        print(cmd)
        os.system(cmd)
        win = visual.Window(size=SCREEN_SIZE, fullscr=True)  
        win.mouseVisible = True
        rating = visual.RatingScale(win=win, name='rating', precision = '100', marker='triangle', 
textColor = 'black',textSize = 0.8,markerColor='DarkRed', showValue = False,mouseOnly= True, 
tickHeight = 0, size=1.0, pos=[0, 0], low=1, high=100, labels=[u'Bad',u' Excellent'], 
scale=u'Please provide a video quality score.')
        text_1 = visual.TextStim(win, text = u'Poor           Fair           Good',
                             pos=(-0.003, -0.07), height=0.05, wrapWidth=1.5, ori=0,
                             color=u'black', colorSpace='rgb', opacity=1,
                             depth=0.0)

        while rating.noResponse:
            rating.draw()
            text_1.draw()
            win.flip()
        print('rating:',rating.getRating())
        rating.reset()
        win.close()


def study():
    df_score = None
    for video in video_list:
        cmd = "\"C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe\"  {}".format(join(video_dir,video))
        # time this command to catch cheaters who close the video player
        os.system(cmd)
        win = visual.Window(size=SCREEN_SIZE, fullscr=True)  
        win.mouseVisible = True
        rating = visual.RatingScale(win=win, name='rating', precision = '100', marker='triangle', 
textColor = 'black',textSize = 0.8,markerColor='DarkRed', showValue = False,mouseOnly= True, 
tickHeight = 0, size=1.0, pos=[0, 0], low=1, high=100, labels=[u'Bad',u' Excellent'], 
scale=u'Please provide a video quality score.') # add progress bar here
        text_1 = visual.TextStim(win, text = u'Poor           Fair           Good',
                             pos=(-0.003, -0.07), height=0.05, wrapWidth=1.5, ori=0,
                             color=u'black', colorSpace='rgb', opacity=1,
                             depth=0.0)
        while rating.noResponse:
            rating.draw()
            text_1.draw()
            win.flip()
        print('rating:',rating.getRating())
        score = rating.getRating()
        df_score = pd.concat([df_score,pd.DataFrame([video,score]).transpose()])
        # df_score.reset_index(drop=True)
        df_score.to_csv(join(score_dir,session_scorefile))
        rating.reset()
        win.close()



df_score = None
# Open id and session selection interface
info = {'id':'', 'session':''}
infoDlg = gui.DlgFromDict(dictionary = info, title = u'info', order = ['id','session'])
if infoDlg.OK == False:
    core.quit()
    
name = info['id']
session = info['session']


if name == "":
    print("Subject did not enter id, exiting.")
    core.quit()

if session == "":
    print("Subject did not enter session #, exiting.")
    core.quit()


session_scorefile  = 'score_{}_{}.csv'.format(name,session)
session_listfile  = 'list_{}_{}.csv'.format(name,session)



if session == "2":
    sesson1_file_name = 'score_{}_{}.csv'.format(name,1)
    if not os.path.exists(join(score_dir, sesson1_file_name)):
        print("Please complete session 1 first.")
        core.quit()

if os.path.exists(join(score_dir,session_scorefile)):
    print("File already exists")
    core.quit()

# read the video list for the session
df_list = pd.read_csv(join(video_list_dir,session_listfile),header=None)
video_list = list(df_list[0])
print (len(video_list) )
# SCREEN_SIZE = (960,540)
SCREEN_SIZE = (3840,2160)

# Window full or not
win = visual.Window(size=SCREEN_SIZE,#size=(800,600),
                    fullscr=True)            
                    
#win.recordFrameIntervals = True
#logging.console.setLevel(logging.WARNING)

win.mouseVisible = False


if session == "1":
    text_1 = visual.TextStim(win, text = u'Thank you for your participation!\n\n\
You will be watching a set of videos one after the other.\n\n\
At the end of each video, a rating screen will be presented to you.\n\n\
For each video, please provide an overall quality score by choosing on the continuous rating bar.\n\n\
If you have any questions please ask them now.\n\n\
Hit Enter to start the training!',
                             font=u'Arial',
                             pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0,
                             color=u'black', colorSpace='rgb', opacity=1,
                             depth=0.0)
    text_1.draw()
    win.flip()
    core.wait(0)
    k_1 = event.waitKeys(keyList = ['return'])
    win.mouseVisible = False
elif session =="2":
    text_10 = visual.TextStim(win, text = u'Thank you for your participation!\n\n\
You will be watching a set of videos one after the other.\n\n\
At the end of each video, a rating screen will be presented to you.\n\n\
For each video, please provide an overall quality score by choosing on the continuous rating bar.\n\n\
If you have any questions please ask them now.\n\n\
Since this is the second session, there will be no training.\n\n\
Hit Enter to start the testing!',
                             font=u'Arial',
                             pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0,
                             color=u'black', colorSpace='rgb', opacity=1,
                             depth=0.0)
    text_10.draw()
    win.flip()
    core.wait(0)
    k_10 = event.waitKeys(keyList = ['return'])
    win.mouseVisible = False
else:
    print("Invalid session")
    core.quit()        


rating = visual.RatingScale(win=win, name='rating', precision = '100', marker='triangle', 
textColor = 'black',textSize = 0.8,markerColor='DarkRed', showValue = False,mouseOnly= True, 
tickHeight = 0, size=1.0, pos=[0, 0], low=1, high=100, labels=[u'Bad',u' Excellent'], 
scale=u'Please provide a video quality score.')



win.close()



if session == '1':
    train()
    win = visual.Window(size=SCREEN_SIZE, fullscr=True)  
    text_study = visual.TextStim(win, text = u'Study begins! Press Enter!',
                             font=u'Arial',
                             pos=(0, 0), height=0.15, wrapWidth=1.5, ori=0,
                             color=u'black', colorSpace='rgb', opacity=1,
                             depth=0.0);
    text_study.draw()
    win.flip()
    core.wait(0)
    k_10 = event.waitKeys(keyList = ['return'])
    win.close()
    study()
    win = visual.Window(size=SCREEN_SIZE, fullscr=True)  
    text_study = visual.TextStim(win, text = u'Study ends!\n Thanks very much for your participation!',
                             font=u'Arial',
                             pos=(0, 0), height=0.15, wrapWidth=1.5, ori=0,
                             color=u'black', colorSpace='rgb', opacity=1,
                             depth=0.0);
    text_study.draw()
    win.flip()
    core.wait(0)
    k_10 = event.waitKeys(keyList = ['return'])
    win.close()

if session == '2':

    study()
    win = visual.Window(size=SCREEN_SIZE, fullscr=True)  
    text_study = visual.TextStim(win, text = u'Study ends!\n Thanks very much for your participation!',
                             font=u'Arial',
                             pos=(0, 0), height=0.15, wrapWidth=1.5, ori=0,
                             color=u'black', colorSpace='rgb', opacity=1,
                             depth=0.0);
    text_study.draw()
    win.flip()
    core.wait(0)
    k_10 = event.waitKeys(keyList = ['return'])
    win.close()
    pass

if session == '3':

    study()
    win = visual.Window(size=SCREEN_SIZE, fullscr=True)  
    text_study = visual.TextStim(win, text = u'Study ends!\n Thanks very much for your participation!',
                             font=u'Arial',
                             pos=(0, 0), height=0.15, wrapWidth=1.5, ori=0,
                             color=u'black', colorSpace='rgb', opacity=1,
                             depth=0.0);
    text_study.draw()
    win.flip()
    core.wait(0)
    k_10 = event.waitKeys(keyList = ['return'])
    win.close()
    pass

win.close()
core.quit()

