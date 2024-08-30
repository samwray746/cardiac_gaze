# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:46:20 2024

@author: bsms9zh8
"""

from psychopy import core


def experiment_variables(win):
    
    ### VARIABLES, PATHS, FUNCTIONS ### 

    pport_address_spike = 16360
    trigger_code_spike = 255

    experiment_clock = core.MonotonicClock() # the main clock used in the experiment 
    countdown = core.CountdownTimer()
    
    fr = win.getActualFrameRate() # getting frame rate of the monitor 
    one_frame = 1/fr
    inc = 0.5 # variable controlling the rating scale 

    # variables defining the number of ticks and their spacing in the confidence scale 
    num_ticks = 11
    tick_length = 20  # Length of each horizontal tick in pixels
    spacing = 25  # Spacing between ticks
    
    ### SETTING UP THE EXPERIMENT STRUCTURE ### 

    # 21 different gaze directions per face
    # In each 'rep' we'll present the 21 different gaze directions at both systole and diastole i.e., 42 trials 
    # We will then repeat each 'rep' 5 times, so that a given gaze direction is presented 5 times at both systole and diastole

    task_order_1 = [1,2,2,1,2,1,1,2,1,2,2,1,2,1,2,1,1,2,1,2,2,1,2,1,1,2,1,2,1,2,2,1,2,1,1,2,1,2,2,1,2,1] # 1 = systole, 2 = diastole 
    task_order_2 = [2,1,1,2,1,2,2,1,2,1,1,2,1,2,1,2,2,1,2,1,1,2,1,2,2,1,2,1,2,1,1,2,1,2,2,1,2,1,1,2,1,2] 

    rep_length = len(task_order_1) # the number of trials in a rep 
    number_reps = 5
    trials_per_block = len(task_order_1) * number_reps

    order_1_structure = [task_order_1, task_order_2, task_order_1, task_order_2, task_order_1] # will counterbalance 
    order_2_structure = [task_order_2, task_order_1, task_order_2, task_order_1, task_order_2]

    # Strings for recording gaze directions 
    str_0v_0h = '0v_0h'
    str_0v_5h = '0v_5h'
    str_0v_m5h = '0v_m5h'
    str_0v_10h = '0v_10h'
    str_0v_m10h = '0v_m10h'
    str_0v_15h = '0v_15h'
    str_0v_m15h = '0v_m15h'
    str_10v_0h = '10v_0h'
    str_m10v_0h = 'm10v_0h'
    str_10v_5h = '10v_5h'
    str_10v_m5h = '10v_m5h'
    str_m10v_5h = 'm10v_5h'
    str_m10v_m5h = 'm10v_m5h'
    str_10v_10h = '10v_10h'
    str_10v_m10h = '10v_m10h'
    str_m10v_10h = 'm10v_10h'
    str_m10v_m10h = 'm10v_m10h'
    str_10v_15h = '10v_15h'
    str_10v_m15h = '10v_m15h'
    str_m10v_15h = 'm10v_15h'
    str_m10v_m15h = 'm10v_m15h'
    
    return pport_address_spike, trigger_code_spike, experiment_clock, countdown, fr, one_frame, inc, num_ticks, tick_length, spacing, task_order_1, task_order_2, rep_length, number_reps, trials_per_block, order_1_structure, order_2_structure, str_0v_0h, str_0v_5h, str_0v_m5h, str_0v_10h, str_0v_m10h, str_0v_15h, str_0v_m15h, str_10v_0h, str_m10v_0h, str_10v_5h, str_10v_m5h, str_m10v_5h, str_m10v_m5h, str_10v_10h, str_10v_m10h, str_m10v_10h, str_m10v_m10h, str_10v_15h, str_10v_m15h, str_m10v_15h, str_m10v_m15h