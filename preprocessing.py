# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:00:58 2017

@author: ishchorry
"""




#ability_to_display_data()
#
#normalize_data_if_needed()
#
#for frame in data:
#    vocoder_1st_dim,vocoder_2nd_dim = run_network(frame)
#
def get_data():
    import pyworld as pw
    import os
    import soundfile as sf
    cwd = os.getcwd()
    raw_folder = os.path.join(cwd,'data','raw')
    processed_folder = os.path.join(raw_folder,'processed')
    
    #create processed items folder
    if not os.path.exists(processed_folder):
        os.makedirs(processed_folder)
    
    for i,filename in enumerate(os.listdir(raw_folder)):
        if filename.endswith(".raw"): 
            # print(os.path.join(directory, filename))
            
            
            print("hree",i)
            data, samplerate = sf.read(os.path.join(raw_folder,filename), channels=1, endian='LITTLE',dtype='float',subtype='PCM_16',samplerate=48000)
            print("here2, data",data,"rate",samplerate)
            f0, sp, ap = pw.wav2world(data, fs=48000)
            
            print("passed through vocoder successfully. f0",f0)
            
            print("")
            print("")
            print("")
            print("sp",sp)
            print("")
            print("")
            print("")
            print("ap",ap)
            new_file_folder_path = os.path.join(processed_folder,str(i))
            if not os.path.exists(new_file_folder_path):
                os.makedirs(new_file_folder_path)
            
            new_proccesed_file_path = os.path.join(new_file_folder_path,'f0')
            f = open(new_proccesed_file_path,'w')
            f.write(f0)
            f.close()
            
            new_proccesed_file_path = os.path.join(new_file_folder_path,'sp')
            f = open(new_proccesed_file_path,'w')
            f.write(sp)
            f.close()
            
            new_proccesed_file_path = os.path.join(new_file_folder_path,'ap')
            f = open(new_proccesed_file_path,'w')
            f.write(ap)
            f.close()
            
    # Convert speech into features (using default options)
    
#def front_end():
#    receive_phonemes_from_ui()
#    prev,cur,_next = one_hot_encode_phonemes
#    pass
#
#def run_network(frame):
#    #a single neural network predicts the params of multivariate conditional distribution
#    #corresponding to acoustic features of a single frame
#    #this was chosen because features produced by parametric vocoder have 2 time frequency dimensions.
#    #therefore, we model the features as 1D with multiple channels.
#    #the prediction of each features in current frame depends on ALL of the features of all past frames
#    #within a receptive field (the range of input samples that affect a single output sample)
#    #all input channels of the intiial causal conv contribute to all resulting feature maps, and so one
#    #for the other convs
#    #this model shares most of architecture with WaveNet
#    #more details later
#    pass
    
get_data()