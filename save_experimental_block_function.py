# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:23:15 2024

@author: bsms9zh8
"""


def save_experimental_block(data_wb, face_number_str, gaze_directions, systole_diastole, perceptual_responses_x, perceptual_responses_y, distances_from_direct, confidence_responses, r_peak_times_lists, predicted_rr_intervals_list, mean_rr_intervals_list, trials_per_block):
    
    data_sheet = data_wb[face_number_str]
    
    # Adding data to worksheet 

    for trial in range(trials_per_block):
        # Adding gaze direction data for a trial 
        data_sheet.cell(trial+2, 1, gaze_directions[trial])
        # Adding systole/diastole data for a trial 
        data_sheet.cell(trial+2, 2, systole_diastole[trial])
        # Adding perceptual rating, x-coordinate
        data_sheet.cell(trial+2, 3, perceptual_responses_x[trial])
        # Adding perceptual rating, y-coordinate
        data_sheet.cell(trial+2, 4, perceptual_responses_y[trial])
        # Adding perceptual rating, distance from centre 
        data_sheet.cell(trial+2, 5, distances_from_direct[trial])
        # Adding confidence rating 
        data_sheet.cell(trial+2, 6, confidence_responses[trial])
        
        if systole_diastole[trial] == 1: # 5 r-peaks detected during a systole trial 
            
            data_sheet.cell(trial+2, 7, r_peak_times_lists[trial][0]) # first R-peak
            data_sheet.cell(trial+2, 8, r_peak_times_lists[trial][1]) # second R-peak...
            data_sheet.cell(trial+2, 9, r_peak_times_lists[trial][2]) 
            data_sheet.cell(trial+2, 10, r_peak_times_lists[trial][3]) 
            data_sheet.cell(trial+2, 11, r_peak_times_lists[trial][4]) 
        
        elif systole_diastole[trial] == 2: # 4 r-peaks detected during a diastole trial 
            
            data_sheet.cell(trial+2, 7, r_peak_times_lists[trial][0]) # first R-peak
            data_sheet.cell(trial+2, 8, r_peak_times_lists[trial][1]) # second R-peak...
            data_sheet.cell(trial+2, 9, r_peak_times_lists[trial][2]) 
            data_sheet.cell(trial+2, 10, r_peak_times_lists[trial][3]) 
            data_sheet.cell(trial+2, 13, predicted_rr_intervals_list[trial]) # predicted RR-interval added

        data_sheet.cell(trial+2, 12, mean_rr_intervals_list[trial]) # mean rr_interval added 
        