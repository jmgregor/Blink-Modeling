"""
Senior Project: Blink Modeling
Jared Gregor (jmg2586@rit.edu)
BlinkDetection_Functions.py

This file holds all of the helper functions used inside the Blink Detection Notebook

"""

# ----------------------------------------------------------------------
""" Dataset Stats """
# --Return number of videos in eye dataset-- #
def datasetStats(directory_main):
    # Import Libraries
    import os 
    import numpy as np
    import csv

    # Read in data set of videos to get stats
    names = []
    for folder in os.listdir(directory_main):
        names.append(folder)
    directory_right = directory_main + names[0]
    directory_left = directory_main + names[1]

    # Intialize output matrix
    output = [["Person", "L_T1", "L_T2", "L_T3", "L_T4", "R_T1", "R_T2", "R_T3", "R_T4", "L_Tot", "R_Tot"]]
    data = np.zeros((23,11), dtype=int)
    for i in range(23):
        data[i][0] = i+1

    # Get left eye stats
    for folder in os.listdir(directory_left):
        # Get current person and trial
        person, trial = splitNameTrial(folder)
        # Fill with number of images
        data[person-1][trial] = len(os.listdir(directory_left + "/" + folder))
        
    # Get right eye stats
    for folder in os.listdir(directory_right):
        # Get current person and trial
        person, trial = splitNameTrial(folder)
        # Fill with number of images
        data[person-1][trial+4] = len(os.listdir(directory_right + "/" + folder))
        
    # Compute and return dataset stats
    for row in data:
        row[9] = row[1] + row[2] + row[3] + row[4]
        row[10] = row[5] + row[6] + row[7] + row[8]
        output.append(row)
        
    # Save to CSV
    with open('../data/outputs/datasetStats.csv', 'w', newline='') as csv_output:
        writer = csv.writer(csv_output)
        writer.writerows(output)

# ----------------------------------------------------------------------
""" Split Trial name """
# --- Returns the trial name and number from foldername --- #
def splitNameTrial(name):
    #Find person number
    loc1 = name.find("_") + 1
    loc2 = name.find("_", loc1)
    personNum = name[loc1:loc2]
    #Find Trial number
    loc3 = name.find("_", loc2+1) + 1
    trialNum = name[loc3:]    
    return int(personNum), int(trialNum)

# ----------------------------------------------------------------------
""" Rotate Whole Video """
# --- Rotates a folder of videos 180 degrees --- # 
def rotateVideos(path_video):
    import os
    import cv2
    import numpy as np

    for folder in os.listdir(path_video):
        for video in os.listdir(path_video + '/' + folder):
            #Read in current video
            cap = cv2.VideoCapture(path_video + '/' + video)
            #Setup output
            fps = 300
            framesize = (int(cap.get(3)), int(cap.get(4)))
            out = cv2.VideoWriter(path_video + '/' + video, cv2.VideoWriter_fourcc('M','J','P','G'),fps, framesize)
            #Read until video is completed
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    #rotate frame
                    frame = np.rot90(frame,2)
                    #save frame
                    out.write(frame)
                else:
                    break
                
            #Free objects
            cap.release()
            out.release()

# ----------------------------------------------------------------------
""" Rotate Extracted Frames """
# --- Rotates a folder of images 180 degrees --- #
def rotateFrames(path_frames):
    import cv2
    import os
    import numpy as np

    # Loop through images in folder
    for blink in os.listdir(path_frames):
        for frame in os.listdir(path_frames + '/' + blink):
            # Read in image
            img = cv2.imread(path_frames + '/' + blink + '/' + frame)
            # Rotate 180 degrees
            dst = np.rot90(img,2)
            # Save Image
            cv2.imwrite(path_frames + '/' + blink + '/' + frame, dst)

# ----------------------------------------------------------------------
""" Combine left and right videos into one place """
def mixData(path):
    import os

    for eye in os.listdir(path):
        # Left vs Right eye
        if(eye == 'right'):
            mix = True
            eye_pos = '_Eye_1'
        elif (eye == 'left'):
            mix = True
            eye_pos = '_Eye_0'
        else:
            mix = False

        if (os.path.isdir(path + '/' + eye) and mix):
            # Get Person and Trial Number
            for folder in os.listdir(path + '/' + eye):
                # Get Blink Number
                for blink in os.listdir(path + '/' + eye + '/' + folder):
                    if (blink[-3:] == 'avi'):
                        nameOld = path + '/' + eye + '/' + folder + '/' + blink
                        nameNew = path + '/mixed/' + folder + eye_pos + '_Blink_' + blink[0:blink.find('_blink')] + '.avi'
                        # Rename Files
                        if not os.path.isfile(nameNew):
                            os.rename(nameOld, nameNew)
                        
