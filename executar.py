
"""
amplification_factor: the amplification factor, with 0 being no change.
fl: low cutoff frequency.
fh: high cutoff frequency.
fs: sampling rate of the video.
n_filter_tap: number of filter tap to use.
filter_type: Type of filter to use. Can be one of "fir", "butter", or "differenceOfIIR". 
For "differenceOfIIR", fl and fh specifies rl and rh coefficients as in Wadhwa et al.
"""

import os
import numpy as np

print("\r")
print("Iniciando sequencia de simulação por TensorFlow!")
print("\r")

step = 0.1

amplification_factor = 10

fs = 240

n_filter_tap = 1

filter_type = "fir"  # voce pode escolher: butter (butterworth), 
                        # fir, differenceOfIIR, yes (dynamic mode) 
                        # or no (static mode)

vidio_in = 'vid_20221202_cam_0_a'

neural_net = "o3f_hmhm2_bg_qnoise_mix4_nl_n_t_ds3" 

#fl = 0.05
#fh = 15
if filter_type == ("yes" or "no"):

    if filter_type == "yes":

        print("\r")
        print("dynamic video")
        print("\r")

    else:
        print("\r")
        print("static video")
        print("\r")


    for i in range(1) :
        #amplification_factor = i
        print("\r")
        print("The amplification factor is:",amplification_factor)
        print("\r")
        os.system("sh run_on_test_videos.sh  "
                   + neural_net + " " 
                   + vidio_in + " "
                   + str(amplification_factor) + " "
                   + filter_type) 

elif (filter_type == 'butter' or 'differenceOfIIR' or 'fir') :
    for i in np.arange(0.5,25,step):
        print("\r")
        fl = i
        print("\r")
        print(fl)
        print("\r")
        fh = fl + step
        print("\r")
        print(fh)
        print("\r")
        #n_filter_tap = i
        #print(n_filter_tap)
        print("\r")
        os.system("sh run_temporal_on_test_videos.sh "
                + neural_net + " "
                + vidio_in + " "
                + str(amplification_factor) + " " 
                + str(fl) + " " 
                + str(fh) + " " 
                + str(fs) + " " 
                + str(n_filter_tap) + " "
                + filter_type)

else:
    print("\r")
    print("erro")
    print("\r") 

    
