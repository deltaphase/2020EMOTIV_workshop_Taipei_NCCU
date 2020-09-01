# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 00:04:04 2020

@author: KC
"""
import mne
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("open eyes 2min_26.08.20_14.26.14.csv",skiprows=1)
df = pd.DataFrame.drop(df, labels = ['EEG.Counter','Timestamp','EEG.Interpolated', 'EEG.RawCq', 'EEG.Battery', 'MarkerIndex', 'MarkerType', 'MarkerValueInt', 'EEG.MarkerHardware', 'CQ.AF3', 'CQ.F7', 'CQ.F3', 'CQ.FC5','CQ.P7','CQ.O1','CQ.O2','CQ.P8','CQ.T8','CQ.FC6','CQ.F4','CQ.F8','CQ.AF4', 'CQ.T7', 'CQ.Overall'], axis = 1)
df
ch_name=list(df.columns)
# Sampling rate of the Nautilus machine
sfreq = 128  # Hz

# Create the info structure needed by MNE
info = mne.create_info(ch_name, sfreq,ch_types ='eeg')

# Finally, create the Raw object
raw = mne.io.RawArray(np.transpose(np.array(df)), info)

# Plot it!
raw.plot(scalings= {'eeg':128})
