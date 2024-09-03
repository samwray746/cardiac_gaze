# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:40:35 2024

@author: bsms9zh8
"""
from main_script import listenforHR_basic
from is_within_circle_function import is_within_circle
from intart_functions import sendParallelTrigger
import random
import psychopy
from psychopy import core, visual, event
from statistics import mean
import keyboard as k 

def experimental_block(countdown, fixation_cross_horizontal, fixation_cross_vertical, win, one_frame, number_reps, g0v_0h, g0v_5h, g0v_m5h, g0v_10h, g0v_m10h, g0v_15h, g0v_m15h, g10v_0h, gm10v_0h, g10v_5h, g10v_m5h, gm10v_5h, gm10v_m5h, g10v_10h, g10v_m10h, gm10v_10h, gm10v_m10h, g10v_15h, g10v_m15h, gm10v_15h, gm10v_m15h, order, order_1_structure, order_2_structure, rep_length, task_order_1, task_order_2, str_0v_0h, str_0v_5h, str_0v_m5h, str_0v_10h, str_0v_m10h, str_0v_15h, str_0v_m15h, str_10v_0h, str_m10v_0h, str_10v_5h, str_10v_m5h, str_m10v_5h, str_m10v_m5h, str_10v_10h, str_10v_m10h, str_m10v_10h, str_m10v_m10h, str_10v_15h, str_10v_m15h, str_m10v_15h, str_m10v_m15h, experiment_clock, pport_address_spike, trigger_code_spike, circle_radius, cross_size, vertical_line, confidence_instructions, high_confidence, low_confidence, num_ticks, line_length, spacing, tick_length):
    
    gaze_directions = [] # containing gaze directions per trial for a block
    systole_diastole = [] # whether the trial is systole or diastole for a block
    perceptual_responses_x = [] # perceptual responses per trial for a block, x-coordinate
    perceptual_responses_y = [] # perceptual responses per trial for a block, y-coordinate 
    distances_from_direct = [] # perceptual response, direct from centre 
    confidence_responses = [] # confidence responses per trial for a block
    r_peak_times_lists = [] # r-peak times per trial for a block
    mean_rr_intervals_list = [] # rr-intervals per trial for a block 
    predicted_rr_intervals_list = [] # Predicted RR-intervals per trial for a block 
    
    countdown.reset()

    fixation_cross_horizontal.draw()
    fixation_cross_vertical.draw()

    win.flip()
    
    while True:
        if countdown.getTime() < (-2 + one_frame):
            break 
    
    for rep in range(number_reps): # each gaze direction is shown five times per systole/diastole i.e., 5 reps per face     
        
        face_stim_s = [g0v_0h, g0v_5h, g0v_m5h, g0v_10h, g0v_m10h, g0v_15h, g0v_m15h, g10v_0h, gm10v_0h, g10v_5h, g10v_m5h, gm10v_5h, gm10v_m5h, g10v_10h, g10v_m10h, gm10v_10h, gm10v_m10h, g10v_15h, g10v_m15h, gm10v_15h, gm10v_m15h]
        face_stim_d = [g0v_0h, g0v_5h, g0v_m5h, g0v_10h, g0v_m10h, g0v_15h, g0v_m15h, g10v_0h, gm10v_0h, g10v_5h, g10v_m5h, gm10v_5h, gm10v_m5h, g10v_10h, g10v_m10h, gm10v_10h, gm10v_m10h, g10v_15h, g10v_m15h, gm10v_15h, gm10v_m15h]

        if order == 1: # the order in which this rep occurs 
            rep_order = order_1_structure[rep]
        elif order == 2:
            rep_order = order_2_structure[rep]
            
        # Entering the main stimulus presentation 
        for trial in range(rep_length):
            
            r_peak_counter = 0 # for tracking how many R-peaks have been detected this trial so far - remove when collecting actual data 
            
            r_peak_times = [] # the list that we'll use for each trial to measure R-peak times
            rr_intervals = [] 
            
            if ((rep_order == task_order_1) and (task_order_1[trial] == 1)) or ((rep_order == task_order_2) and task_order_2[trial] == 1): # a systole trial 
            
                face_this_trial = random.choice(face_stim_s) # choosing which stimulus will be presented this trial
                face_stim_s.remove(face_this_trial) # removing the chosen simulus, so that it won't be presented this rep again 
                face_this_trial.draw() # drawing the chosen stimulus 
                
                systole_diastole.append(1) # systole = 1, diastole = 2
                
                # Adding to the gaze direction list the face direction presented this trial
                
                if face_this_trial == g0v_0h:
                    gaze_directions.append(str_0v_0h)
                elif face_this_trial == g0v_5h:
                    gaze_directions.append(str_0v_5h)
                elif face_this_trial == g0v_m5h:
                    gaze_directions.append(str_0v_m5h)
                elif face_this_trial == g0v_10h:
                    gaze_directions.append(str_0v_10h)
                elif face_this_trial == g0v_m10h:
                    gaze_directions.append(str_0v_m10h)
                elif face_this_trial == g0v_15h:
                    gaze_directions.append(str_0v_15h)
                elif face_this_trial == g0v_m15h:
                    gaze_directions.append(str_0v_m15h)
                elif face_this_trial == g10v_0h:
                    gaze_directions.append(str_10v_0h)
                elif face_this_trial == gm10v_0h:
                    gaze_directions.append(str_m10v_0h)
                elif face_this_trial == g10v_5h:
                    gaze_directions.append(str_10v_5h)
                elif face_this_trial == g10v_m5h:
                    gaze_directions.append(str_10v_m5h)
                elif face_this_trial == gm10v_5h:
                    gaze_directions.append(str_m10v_5h)
                elif face_this_trial == gm10v_m5h:
                    gaze_directions.append(str_m10v_m5h)
                elif face_this_trial == g10v_10h:
                    gaze_directions.append(str_10v_10h)
                elif face_this_trial == g10v_m10h:
                    gaze_directions.append(str_10v_m10h)
                elif face_this_trial == gm10v_10h:
                    gaze_directions.append(str_m10v_10h)
                elif face_this_trial == gm10v_m10h:
                    gaze_directions.append(str_m10v_m10h)
                elif face_this_trial == g10v_15h:
                    gaze_directions.append(str_10v_15h)
                elif face_this_trial == g10v_m15h:
                    gaze_directions.append(str_10v_m15h)
                elif face_this_trial == gm10v_15h:
                    gaze_directions.append(str_m10v_15h)
                elif face_this_trial == gm10v_m15h:
                    gaze_directions.append(str_m10v_m15h)

                
                 ### R-PEAK DETECTION ### 
                 
                 # For diastole trials we're going to be gathering 3 RR-intervals, so waiting for 4 R-peaks, then presenting
                 # the stimulus just before the 5th R-peak. 
                 
                 # We'll do the same for systole trials to keep the ISIs similar, i.e., detecting 5 R-peaks, and presented 250ms after the 5th  
                 
                for peak in range(5): 
                     r_peak_time = listenforHR_basic()
                     r_peak_times.append(r_peak_time)
                     countdown.reset()
                     r_peak_counter += 1 
                     
                     # A potential problem has been that when the threshold is crossed (i.e., an R-peak), the listenforHR_basic doesn't only send once, but during the
                     # whole time that the signal crosses the threshold. So I'm introducing a delay during the sensing period, in order to pause everything
                     # Until the signal has gone back below the threshold 
                     
                     if r_peak_counter < 5:
                         core.wait(0.5)
                 
                while True: # waiting 250ms after R-peak has been detected
                     if countdown.getTime() < (-0.250 + one_frame):
                         break
                 
                win.flip()  
                countdown.reset()
                sendParallelTrigger(pport_address_spike, trigger_code_spike)
             
                while True:
                     if countdown.getTime() < (-0.04 + one_frame): #40ms presentation 
                         break
                     
                win.flip() # remove stimulus
            
                ### FOR SYSTOLE TRIALS, CALCULATING THE MEAN RR-INTERVAL AND ADDING RR-INTERVALS TO LIST ### 
                
                for peak in range(len(r_peak_times) - 1): # going through the R-peak list
                    rr_interval = r_peak_times[peak + 1] - r_peak_times[peak] # R-peak, index + 1, minus R-peak, index
                    rr_intervals.append(rr_interval)
                    
                mean_rr_int = mean(rr_intervals)
    
            elif ((rep_order == task_order_1) and (task_order_1[trial] == 2)) or ((rep_order == task_order_2) and (task_order_2[trial] == 2)): # a diastole trial 
            
                face_this_trial = random.choice(face_stim_d) # choosing which stimulus will be presented this trial
                face_stim_s.remove(face_this_trial) # removing the chosen simulus, so that it won't be presented this rep again 
                face_this_trial.draw()  # drawing the chosen stimulus 
                
                systole_diastole.append(2)    
                
                if face_this_trial == g0v_0h:
                    gaze_directions.append(str_0v_0h)
                elif face_this_trial == g0v_5h:
                    gaze_directions.append(str_0v_5h)
                elif face_this_trial == g0v_m5h:
                    gaze_directions.append(str_0v_m5h)
                elif face_this_trial == g0v_10h:
                    gaze_directions.append(str_0v_10h)
                elif face_this_trial == g0v_m10h:
                    gaze_directions.append(str_0v_m10h)
                elif face_this_trial == g0v_15h:
                    gaze_directions.append(str_0v_15h)
                elif face_this_trial == g0v_m15h:
                    gaze_directions.append(str_0v_m15h)
                elif face_this_trial == g10v_0h:
                    gaze_directions.append(str_10v_0h)
                elif face_this_trial == gm10v_0h:
                    gaze_directions.append(str_m10v_0h)
                elif face_this_trial == g10v_5h:
                    gaze_directions.append(str_10v_5h)
                elif face_this_trial == g10v_m5h:
                    gaze_directions.append(str_10v_m5h)
                elif face_this_trial == gm10v_5h:
                    gaze_directions.append(str_m10v_5h)
                elif face_this_trial == gm10v_m5h:
                    gaze_directions.append(str_m10v_m5h)
                elif face_this_trial == g10v_10h:
                    gaze_directions.append(str_10v_10h)
                elif face_this_trial == g10v_m10h:
                    gaze_directions.append(str_10v_m10h)
                elif face_this_trial == gm10v_10h:
                    gaze_directions.append(str_m10v_10h)
                elif face_this_trial == gm10v_m10h:
                    gaze_directions.append(str_m10v_m10h)
                elif face_this_trial == g10v_15h:
                    gaze_directions.append(str_10v_15h)
                elif face_this_trial == g10v_m15h:
                    gaze_directions.append(str_10v_m15h)
                elif face_this_trial == gm10v_15h:
                    gaze_directions.append(str_m10v_15h)
                elif face_this_trial == gm10v_m15h:
                    gaze_directions.append(str_m10v_m15h)
                    
                ### R-PEAK DETECTION AND RR-INTERVAL CALCULATION ### 
                
                for peak in range(4): # gathering 4 R-peaks
                    r_peak_time = listenforHR_basic()
                    r_peak_times.append(r_peak_time)
                    countdown.reset()
                    r_peak_counter += 1
                
                    
                    if peak < r_peak_counter < 4: # again stopping multiple signals being sent per R-peak 
                        core.wait(0.5)

                ### CALCULATING RR-INTERVALS ### 
                
                for peak in range(len(r_peak_times) - 1): # going through the R-peak list
                    rr_interval = r_peak_times[peak + 1] - r_peak_times[peak] # R-peak, index + 1, minus R-peak, index
                    rr_intervals.append(rr_interval)
                    
                mean_rr_int = mean(rr_intervals) # this is useful to know to check for faulty trials 
                
                predicted_rr_int = (rr_intervals[-1]*0.5) + (rr_intervals[-2]*0.3) + (rr_intervals[-3]*0.2)
                # ^ I'm calculating the predicted RR-interval by weighting the calculated RR-intervals, most recent with the highest weighting 
                
                ### DOING SOME BASIC ADJUSTMENTS BASED OFF THE MEAN RR-INTERVALS ### 
                
                if predicted_rr_int >= 1: # i.e., less than 60bpm
                
                    while True:
                        if countdown.getTime() < (-predicted_rr_int + 0.150 + one_frame): # we present the stimulus 150ms before the next predicted R-peak
                            break
                
                elif (1 > predicted_rr_int) and (predicted_rr_int >= 0.86): #i.e., between 60 and 70bpm
                    
                    while True:
                        if countdown.getTime() < (-predicted_rr_int + 0.135 + one_frame): # present the stimulus 0.135ms before the next predicted R-peak
                            break
                        
                elif predicted_rr_int < 0.86: # i.e., greater than 70bpm
                
                    while True: 
                        if countdown.getTime() < (-predicted_rr_int + 0.125 + one_frame): # present the stimulus 0.125ms before the next predicted R-peak 
                            break                
                
                win.flip() # Presenting the face 
                countdown.reset() # resetting the countdown timer now
                sendParallelTrigger(pport_address_spike, trigger_code_spike)
                
                
                while True:
                    if countdown.getTime() < (-0.04 + one_frame):
                        break
                
                win.flip()
            
        ### GETTING GAZE DIRECTION RESPONSE ### 

            countdown.reset()
            
            circle = psychopy.visual.Circle(win, fillColor = "white", radius = circle_radius)
            cross = psychopy.visual.shape.ShapeStim(win, fillColor = "red", vertices = 'cross', size = cross_size)
            
            cross_pos = [0,0]
            cross.setPos(cross_pos)
            
            while True:
                if countdown.getTime() < (-0.250 + one_frame): # A blank screen for 250ms after the presentation of the face 
                    break
                
            cross.draw()
            circle.draw()
            win.flip()
            
            while True:
            
                if k.is_pressed("left"):
                    new_pos = [cross_pos[0] - 3, cross_pos[1]]
                elif k.is_pressed("right"):
                    new_pos = [cross_pos[0] + 3, cross_pos[1]]
                elif k.is_pressed("up"):
                    new_pos = [cross_pos[0], cross_pos[1] + 3]
                elif k.is_pressed("down"):
                    new_pos = [cross_pos[0], cross_pos[1] - 3]
                elif k.is_pressed("space"):
                    break
                else:
                    new_pos = cross_pos
                
                # Check if the new position is within the circle
                if is_within_circle(new_pos, circle_radius):
                    cross_pos = new_pos
                    cross.setPos(cross_pos)
            
                # Draw the circle and the cross
                circle.draw()
                cross.draw()
                win.flip()
               
            response_coords_x = cross_pos[0]
            response_coords_y = cross_pos[1]
            
            distance_from_direct = (response_coords_x**2 + response_coords_y**2)**0.5 
            
            ### GETTING CONFIDENCE RESPONSE ### 
            
            countdown.reset()
          
            while True:
                if countdown.getTime() < (-0.25 + one_frame): # A blank screen for 250ms after the first perceptual rating 
                    break
                
            # Followed by the confidence rating scale 
            
            triangle_position = 0
            space_pressed = False
            while space_pressed == False:
                
                # Draw the vertical line and confidence instructions
                vertical_line.draw()
                confidence_instructions.draw()
                high_confidence.draw()
                low_confidence.draw()
                triangle = visual.Polygon(win, edges = 3, radius = 15, pos = [-50, triangle_position])
                triangle.draw()
                
                for i in range(num_ticks):
                     # Calculate the y position of each tick
                     y_pos = -line_length / 2 + i * spacing
                     # Create the horizontal tick
                     tick = visual.Line(
                         win,
                         start=(-tick_length / 2, y_pos),
                         end=(tick_length / 2, y_pos),
                         lineColor='white')
                     # Draw the tick
                     tick.draw()
                 
                win.flip()
                
                # Updating position of the triangle according to the key pressed 
                
                keys = event.waitKeys(keyList = ['up', 'down', 'space'])
                
                if (keys[0] == 'up') and (triangle_position != 125):
                    triangle_position += 25
                    
                elif (keys[0] == 'up') and (triangle_position == 125):
                    triangle_position = 125
                    
                elif (keys[0] == 'down') and (triangle_position != -125):
                    triangle_position -= 25
                
                elif (keys[0] == 'down') and (triangle_position == -125):
                    triangle_position == -25
                    
                elif keys[0] == 'space':
                    break 
             
            # Recording the confidence rating response 
            if triangle_position == 0:
                confidenceRating = 5
            elif triangle_position == 25:
                confidenceRating = 6
            elif triangle_position == 50:
                confidenceRating = 7
            elif triangle_position == 75:
                confidenceRating = 8
            elif triangle_position == 100:
                confidenceRating = 9
            elif triangle_position == 125:
                confidenceRating = 10
            elif triangle_position == -25:
                confidenceRating = 4
            elif triangle_position == -50:
                confidenceRating = 3
            elif triangle_position == -75:
                confidenceRating = 2
            elif triangle_position == -100:
                confidenceRating = 1
            elif triangle_position == -125:
                confidenceRating = 0 
                    
            # Drawing the fixation cross for the next trial, will be shown for the next R-peak sensing period     
            
            win.flip()
            
            fixation_cross_horizontal.draw()
            fixation_cross_vertical.draw()
            
            # Recording the info for this trial 
            
            perceptual_responses_x.append(response_coords_x)
            perceptual_responses_y.append(response_coords_y)
            distances_from_direct.append(distance_from_direct)
            confidence_responses.append(confidenceRating)
            r_peak_times_lists.append(r_peak_times)
            mean_rr_intervals_list.append(mean_rr_int)
            
            if systole_diastole[-1] == 1: # a systole trial 
                predicted_rr_intervals_list.append(0) # just to fill the list (during systole trials we don't calculate a predicted rr int)
            
            elif systole_diastole[-1] == 2: # a diastole trial 
                predicted_rr_intervals_list.append(predicted_rr_int)
                
            win.flip()
                
            core.wait(1.5) # giving an opportunity for the ECG to settle before the next trial starts 
            
    return gaze_directions, systole_diastole, perceptual_responses_x, perceptual_responses_y, distances_from_direct, confidence_responses, r_peak_times_lists, predicted_rr_intervals_list, mean_rr_intervals_list
            
