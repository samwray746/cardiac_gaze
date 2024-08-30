# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:21:17 2024

@author: bsms9zh8
"""

import psychopy
from psychopy import visual 
import os.path as op

def create_experimental_stimuli(win): 
    
    ### PATHS ### 
    images_path = 'D:\\PhD\\cardiac_gaze\\images_crop_resize'
    
    ### COLOURS ### 
    grey = '#808080'
    
    ### FIXATION CROSS ### 
    horiz_line_fixation_start = [-25, 0]
    horiz_line_fixation_end = [25, 0]

    vert_line_fixation_start = [0, 25]
    vert_line_fixation_end = [0, -25]
     
    fixation_cross_vertical = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=grey)

    fixation_cross_horizontal = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=grey)

    fixation_cross_vertical.start = vert_line_fixation_start
    fixation_cross_vertical.end = vert_line_fixation_end

    fixation_cross_horizontal.start = horiz_line_fixation_start
    fixation_cross_horizontal.end = horiz_line_fixation_end
    
    ### VARIOUS STIMULI FOR TASK ### 
    
    ### INSTRUCTIONS ### 
    
    training_instructions_one = visual.TextStim(win, text='Welcome to the experiment!\n\nDuring the experiment, faces will quickly appear that are gazing in different directions.\n\n\nPress spacebar to continue.', height = 25)
    training_instructions_two = visual.TextStim(win, text='After viewing a face, you will be asked where you thought the face was gazing.\n\n\nPress spacebar to continue.', height = 25)
    training_instructions_three = visual.TextStim(win, text='A white circle and red marker will be presented.\n\n\nUse the arrow keys to move the marker where you think the face is gazing, and spacebar to make your choice.\n\n\nPress spacebar to continue.', height = 25)
    training_instructions_four = visual.TextStim(win, text='For instance, moving the marker to the furthest left part of the circle means you judged the face to be looking as far to YOUR left as possible.\n\n\nPress spacebar to continue.', height = 25)
    training_instructions_five = visual.TextStim(win, text='You will then be asked to give a confidence rating on your gaze response.\n\n\nThe confidence rating gauges the extent to which you thought your response matched the gaze direction.', height = 25)
    training_instructions_six = visual.TextStim(win, text='The two extreme ends of the confidence rating are EXTREMELY CONFIDENT and NOT CONFIDENT AT ALL.\n\n\nExtremely confident would mean you were sure that your response matched the gaze direction.\n\n\nMeanwhile, not confident at all means you were very underconfident in your gaze response matching the gaze direction.', height = 25)
    training_instructions_seven = visual.TextStim(win, text='The experiment consists of 3 blocks, which each feature a different face. You can take a break in-between blocks.\n\n\nPress the spacebar to continue.', height = 25)
    training_instructions_eight = visual.TextStim(win, text='If you have any questions, ask the researcher now.\n\n\nPress the spacebar to continue.', height = 25)
    training_instructions_nine = visual.TextStim(win, text="Let's do a few training trials.\n\n\nPress the spacebar to continue.", height = 25)
    
    training_complete = visual.TextStim(win, text="Training block complete. Well done!\n\n\nIf you have any questions, ask the researcher now. Otherwise, press spacebar to start the first experimental block.", height = 25)
    
    block_complete = visual.TextStim(win, text="Experimental block complete. Well done!\n\n\nTake a rest, and press the spacebar to begin the next block.", height = 25)
    
    confidence_instructions = visual.TextStim(win, text = 'How well do you think your answer matched the true gaze direction?', height = 25, pos = [0, 200])
    high_confidence = visual.TextStim(win, text = "Extremely confident", height = 25, pos = [130, 125])
    low_confidence = visual.TextStim(win, text = "Not confident at all", height = 25, pos = [130, -125])
    
    ### VERTICAL LINE FOR CONFIDENCE RESPONSE ### 
    
    # Define the length of the vertical line
    line_length = 250  # Length of the vertical line in pixels

    vertical_line = visual.Line(
        win,
        start=(0, -line_length / 2),
        end=(0, line_length / 2),
        lineColor='white')
    
                                 
    ### FACE ONE ### 
    face_1_path = op.join(images_path, 'face_1')
    face_1_list = ['0018_2m_0P_0V_0H.png', '0018_2m_0P_0V_5H.png', '0018_2m_0P_0V_-5H.png', '0018_2m_0P_0V_10H.png', '0018_2m_0P_0V_-10H.png',
                 '0018_2m_0P_0V_15H.png', '0018_2m_0P_0V_-15H.png', '0018_2m_0P_10V_0H.png', '0018_2m_0P_-10V_0H.png',
                  '0018_2m_0P_10V_5H.png', '0018_2m_0P_10V_-5H.png', '0018_2m_0P_-10V_5H.png', '0018_2m_0P_-10V_-5H.png', '0018_2m_0P_10V_10H.png',
                  '0018_2m_0P_10V_-10H.png', '0018_2m_0P_-10V_10H.png', '0018_2m_0P_-10V_-10H.png', '0018_2m_0P_10V_15H.png', '0018_2m_0P_10V_-15H.png',
                  '0018_2m_0P_-10V_15H.png', '0018_2m_0P_-10V_-15H.png']
    
    f1_0v_0h_p = op.join(face_1_path, face_1_list[0])
    f1_0v_0h = visual.ImageStim(win, f1_0v_0h_p, pos = (10, -67))
    
    f1_0v_5h_p = op.join(face_1_path, face_1_list[1])
    f1_0v_5h = visual.ImageStim(win, f1_0v_5h_p, pos = (10, -67))
    
    f1_0v_m5h_p = op.join(face_1_path, face_1_list[2])
    f1_0v_m5h = visual.ImageStim(win, f1_0v_m5h_p, pos = (10, -67))
    
    f1_0v_10h_p = op.join(face_1_path, face_1_list[3])
    f1_0v_10h = visual.ImageStim(win, f1_0v_10h_p, pos = (10, -67))
    
    f1_0v_m10h_p = op.join(face_1_path, face_1_list[4])
    f1_0v_m10h = visual.ImageStim(win, f1_0v_m10h_p, pos = (10, -67))
    
    f1_0v_15h_p = op.join(face_1_path, face_1_list[5])
    f1_0v_15h = visual.ImageStim(win, f1_0v_15h_p, pos = (10, -67))
    
    f1_0v_m15h_p = op.join(face_1_path, face_1_list[6])
    f1_0v_m15h = visual.ImageStim(win, f1_0v_m15h_p, pos = (10, -67))
    
    f1_10v_0h_p = op.join(face_1_path, face_1_list[7])
    f1_10v_0h = visual.ImageStim(win, f1_10v_0h_p, pos = (10, -67))
    
    f1_m10v_0h_p = op.join(face_1_path, face_1_list[8])
    f1_m10v_0h = visual.ImageStim(win, f1_m10v_0h_p, pos = (10, -67))
    
    f1_10v_5h_p = op.join(face_1_path, face_1_list[9])
    f1_10v_5h = visual.ImageStim(win, f1_10v_5h_p, pos = (10, -67))
    
    f1_10v_m5h_p = op.join(face_1_path, face_1_list[10])
    f1_10v_m5h = visual.ImageStim(win, f1_10v_m5h_p, pos = (10, -67))
    
    f1_m10v_5h_p = op.join(face_1_path, face_1_list[11])
    f1_m10v_5h = visual.ImageStim(win, f1_m10v_5h_p, pos = (10, -67))
    
    f1_m10v_m5h_p = op.join(face_1_path, face_1_list[12])
    f1_m10v_m5h = visual.ImageStim(win, f1_m10v_m5h_p, pos = (10, -67))
    
    f1_10v_10h_p = op.join(face_1_path, face_1_list[13])
    f1_10v_10h = visual.ImageStim(win, f1_10v_10h_p, pos = (10, -67))
    
    f1_10v_m10h_p = op.join(face_1_path, face_1_list[14])
    f1_10v_m10h = visual.ImageStim(win, f1_10v_m10h_p, pos = (10, -67))
    
    f1_m10v_10h_p = op.join(face_1_path, face_1_list[15])
    f1_m10v_10h = visual.ImageStim(win, f1_m10v_10h_p, pos = (10, -67))
    
    f1_m10v_m10h_p = op.join(face_1_path, face_1_list[16])
    f1_m10v_m10h = visual.ImageStim(win, f1_m10v_m10h_p, pos = (10, -67))
    
    f1_10v_15h_p = op.join(face_1_path, face_1_list[17])
    f1_10v_15h = visual.ImageStim(win, f1_10v_15h_p, pos = (10, -67))
    
    f1_10v_m15h_p = op.join(face_1_path, face_1_list[18])
    f1_10v_m15h = visual.ImageStim(win, f1_10v_m15h_p, pos = (10, -67))
    
    f1_m10v_15h_p = op.join(face_1_path, face_1_list[19])
    f1_m10v_15h = visual.ImageStim(win, f1_m10v_15h_p, pos = (10, -67))
    
    f1_m10v_m15h_p = op.join(face_1_path, face_1_list[20])
    f1_m10v_m15h = visual.ImageStim(win, f1_m10v_m15h_p, pos = (10, -67))
    
### FACE TWO ### 
    face_2_path = op.join(images_path, 'face_2')
    face_2_list = ['0033_2m_0P_0V_0H.png', '0033_2m_0P_0V_5H.png', '0033_2m_0P_0V_-5H.png', '0033_2m_0P_0V_10H.png', '0033_2m_0P_0V_-10H.png',
                   '0033_2m_0P_0V_15H.png', '0033_2m_0P_0V_-15H.png', '0033_2m_0P_10V_0H.png', '0033_2m_0P_-10V_0H.png',
                   '0033_2m_0P_10V_5H.png', '0033_2m_0P_10V_-5H.png', '0033_2m_0P_-10V_5H.png', '0033_2m_0P_-10V_-5H.png', '0033_2m_0P_10V_10H.png',
                   '0033_2m_0P_10V_-10H.png', '0033_2m_0P_-10V_10H.png', '0033_2m_0P_-10V_-10H.png', '0033_2m_0P_10V_15H.png', '0033_2m_0P_10V_-15H.png',
                   '0033_2m_0P_-10V_15H.png', '0033_2m_0P_-10V_-15H.png']
    
    f2_0v_0h_p = op.join(face_2_path, face_2_list[0])
    f2_0v_0h = visual.ImageStim(win, f2_0v_0h_p, pos = (0, -60))
    
    f2_0v_5h_p = op.join(face_2_path, face_2_list[1])
    f2_0v_5h = visual.ImageStim(win, f2_0v_5h_p, pos = (0, -60))
    
    f2_0v_m5h_p = op.join(face_2_path, face_2_list[2])
    f2_0v_m5h = visual.ImageStim(win, f2_0v_m5h_p, pos = (0, -60))
    
    f2_0v_10h_p = op.join(face_2_path, face_2_list[3])
    f2_0v_10h = visual.ImageStim(win, f2_0v_10h_p, pos = (0, -60))
    
    f2_0v_m10h_p = op.join(face_2_path, face_2_list[4])
    f2_0v_m10h = visual.ImageStim(win, f2_0v_m10h_p, pos = (0, -60))
    
    f2_0v_15h_p = op.join(face_2_path, face_2_list[5])
    f2_0v_15h = visual.ImageStim(win, f2_0v_15h_p, pos = (0, -60))
    
    f2_0v_m15h_p = op.join(face_2_path, face_2_list[6])
    f2_0v_m15h = visual.ImageStim(win, f2_0v_m15h_p, pos = (0, -60))
    
    f2_10v_0h_p = op.join(face_2_path, face_2_list[7])
    f2_10v_0h = visual.ImageStim(win, f2_10v_0h_p, pos = (0, -60))
    
    f2_m10v_0h_p = op.join(face_2_path, face_2_list[8])
    f2_m10v_0h = visual.ImageStim(win, f2_m10v_0h_p, pos = (0, -60))
    
    f2_10v_5h_p = op.join(face_2_path, face_2_list[9])
    f2_10v_5h = visual.ImageStim(win, f2_10v_5h_p, pos = (0, -60))
    
    f2_10v_m5h_p = op.join(face_2_path, face_2_list[10])
    f2_10v_m5h = visual.ImageStim(win, f2_10v_m5h_p, pos = (0, -60))
    
    f2_m10v_5h_p = op.join(face_2_path, face_2_list[11])
    f2_m10v_5h = visual.ImageStim(win, f2_m10v_5h_p, pos = (0, -60))
    
    f2_m10v_m5h_p = op.join(face_2_path, face_2_list[12])
    f2_m10v_m5h = visual.ImageStim(win, f2_m10v_m5h_p, pos = (0, -60))
    
    f2_10v_10h_p = op.join(face_2_path, face_2_list[13])
    f2_10v_10h = visual.ImageStim(win, f2_10v_10h_p, pos = (0, -60))
    
    f2_10v_m10h_p = op.join(face_2_path, face_2_list[14])
    f2_10v_m10h = visual.ImageStim(win, f2_10v_m10h_p, pos = (0, -60))
    
    f2_m10v_10h_p = op.join(face_2_path, face_2_list[15])
    f2_m10v_10h = visual.ImageStim(win, f2_m10v_10h_p, pos = (0, -60))
    
    f2_m10v_m10h_p = op.join(face_2_path, face_2_list[16])
    f2_m10v_m10h = visual.ImageStim(win, f2_m10v_m10h_p, pos = (0, -60))
    
    f2_10v_15h_p = op.join(face_2_path, face_2_list[17])
    f2_10v_15h = visual.ImageStim(win, f2_10v_15h_p, pos = (0, -60))
    
    f2_10v_m15h_p = op.join(face_2_path, face_2_list[18])
    f2_10v_m15h = visual.ImageStim(win, f2_10v_m15h_p, pos = (0, -60))
    
    f2_m10v_15h_p = op.join(face_2_path, face_2_list[19])
    f2_m10v_15h = visual.ImageStim(win, f2_m10v_15h_p, pos = (0, -60))
    
    f2_m10v_m15h_p = op.join(face_2_path, face_2_list[20])
    f2_m10v_m15h = visual.ImageStim(win, f2_m10v_m15h_p, pos = (0, -60))
    
### FACE THREE ### 
    face_3_path = op.join(images_path, 'face_3')
    face_3_list = ['0031_2m_0P_0V_0H.png', '0031_2m_0P_0V_5H.png', '0031_2m_0P_0V_-5H.png', '0031_2m_0P_0V_10H.png', '0031_2m_0P_0V_-10H.png',
                   '0031_2m_0P_0V_15H.png', '0031_2m_0P_0V_-15H.png', '0031_2m_0P_10V_0H.png', '0031_2m_0P_-10V_0H.png',
                   '0031_2m_0P_10V_5H.png', '0031_2m_0P_10V_-5H.png', '0031_2m_0P_-10V_5H.png', '0031_2m_0P_-10V_-5H.png', '0031_2m_0P_10V_10H.png',
                   '0031_2m_0P_10V_-10H.png', '0031_2m_0P_-10V_10H.png', '0031_2m_0P_-10V_-10H.png', '0031_2m_0P_10V_15H.png', '0031_2m_0P_10V_-15H.png',
                   '0031_2m_0P_-10V_15H.png', '0031_2m_0P_-10V_-15H.png']
    
    f3_0v_0h_p = op.join(face_3_path, face_3_list[0])
    f3_0v_0h = visual.ImageStim(win, f3_0v_0h_p, pos = (17, -70))
    
    f3_0v_5h_p = op.join(face_3_path, face_3_list[1])
    f3_0v_5h = visual.ImageStim(win, f3_0v_5h_p, pos = (17, -70))
    
    f3_0v_m5h_p = op.join(face_3_path, face_3_list[2])
    f3_0v_m5h = visual.ImageStim(win, f3_0v_m5h_p, pos = (17, -70))
    
    f3_0v_10h_p = op.join(face_3_path, face_3_list[3])
    f3_0v_10h = visual.ImageStim(win, f3_0v_10h_p, pos = (17, -70))
    
    f3_0v_m10h_p = op.join(face_3_path, face_3_list[4])
    f3_0v_m10h = visual.ImageStim(win, f3_0v_m10h_p, pos = (17, -70))
    
    f3_0v_15h_p = op.join(face_3_path, face_3_list[5])
    f3_0v_15h = visual.ImageStim(win, f3_0v_15h_p, pos = (17, -70))
    
    f3_0v_m15h_p = op.join(face_3_path, face_3_list[6])
    f3_0v_m15h = visual.ImageStim(win, f3_0v_m15h_p, pos = (17, -70))
    
    f3_10v_0h_p = op.join(face_3_path, face_3_list[7])
    f3_10v_0h = visual.ImageStim(win, f3_10v_0h_p, pos = (17, -70))
    
    f3_m10v_0h_p = op.join(face_3_path, face_3_list[8])
    f3_m10v_0h = visual.ImageStim(win, f3_m10v_0h_p, pos = (17, -70))
    
    f3_10v_5h_p = op.join(face_3_path, face_3_list[9])
    f3_10v_5h = visual.ImageStim(win, f3_10v_5h_p, pos = (17, -70))
    
    f3_10v_m5h_p = op.join(face_3_path, face_3_list[10])
    f3_10v_m5h = visual.ImageStim(win, f3_10v_m5h_p, pos = (17, -70))
    
    f3_m10v_5h_p = op.join(face_3_path, face_3_list[11])
    f3_m10v_5h = visual.ImageStim(win, f3_m10v_5h_p, pos = (17, -70))
    
    f3_m10v_m5h_p = op.join(face_3_path, face_3_list[12])
    f3_m10v_m5h = visual.ImageStim(win, f3_m10v_m5h_p, pos = (17, -70))
    
    f3_10v_10h_p = op.join(face_3_path, face_3_list[13])
    f3_10v_10h = visual.ImageStim(win, f3_10v_10h_p, pos = (17, -70))
    
    f3_10v_m10h_p = op.join(face_3_path, face_3_list[14])
    f3_10v_m10h = visual.ImageStim(win, f3_10v_m10h_p, pos = (17, -70))
    
    f3_m10v_10h_p = op.join(face_3_path, face_3_list[15])
    f3_m10v_10h = visual.ImageStim(win, f3_m10v_10h_p, pos = (17, -70))
    
    f3_m10v_m10h_p = op.join(face_3_path, face_3_list[16])
    f3_m10v_m10h = visual.ImageStim(win, f3_m10v_m10h_p, pos = (17, -70))
    
    f3_10v_15h_p = op.join(face_3_path, face_3_list[17])
    f3_10v_15h = visual.ImageStim(win, f3_10v_15h_p, pos = (17, -70))
    
    f3_10v_m15h_p = op.join(face_3_path, face_3_list[18])
    f3_10v_m15h = visual.ImageStim(win, f3_10v_m15h_p, pos = (17, -70))
    
    f3_m10v_15h_p = op.join(face_3_path, face_3_list[19])
    f3_m10v_15h = visual.ImageStim(win, f3_m10v_15h_p, pos = (17, -70))
    
    f3_m10v_m15h_p = op.join(face_3_path, face_3_list[20])
    f3_m10v_m15h = visual.ImageStim(win, f3_m10v_m15h_p, pos = (17, -70))
    
    ### Parameters for the response stimuli ### 
    
    circle_radius = 150 
    cross_size = 25
    
    
    return fixation_cross_horizontal, fixation_cross_vertical, training_instructions_one, training_instructions_two, training_instructions_three, training_instructions_four, training_instructions_five, training_instructions_six, training_instructions_seven, training_instructions_eight, training_instructions_nine, training_complete, block_complete, confidence_instructions, high_confidence, low_confidence, vertical_line, line_length, f1_0v_0h, f1_0v_5h, f1_0v_m5h, f1_0v_10h, f1_0v_m10h, f1_0v_15h, f1_0v_m15h, f1_10v_0h, f1_m10v_0h, f1_10v_5h, f1_10v_m5h, f1_m10v_5h, f1_m10v_m5h, f1_10v_10h, f1_10v_m10h, f1_m10v_10h, f1_m10v_m10h, f1_10v_15h, f1_10v_m15h, f1_m10v_15h, f1_m10v_m15h, f2_0v_0h, f2_0v_5h, f2_0v_m5h, f2_0v_10h, f2_0v_m10h, f2_0v_15h, f2_0v_m15h, f2_10v_0h, f2_m10v_0h, f2_10v_5h, f2_10v_m5h, f2_m10v_5h, f2_m10v_m5h, f2_10v_10h, f2_10v_m10h, f2_m10v_10h, f2_m10v_m10h, f2_10v_15h, f2_10v_m15h, f2_m10v_15h, f2_m10v_m15h, f3_0v_0h, f3_0v_5h, f3_0v_m5h, f3_0v_10h, f3_0v_m10h, f3_0v_15h, f3_0v_m15h, f3_10v_0h, f3_m10v_0h, f3_10v_5h, f3_10v_m5h, f3_m10v_5h, f3_m10v_m5h, f3_10v_10h, f3_10v_m10h, f3_m10v_10h, f3_m10v_m10h, f3_10v_15h, f3_10v_m15h, f3_m10v_15h, f3_m10v_m15h, circle_radius, cross_size
 
 

