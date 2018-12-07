import csv
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


nParticles = range(1024, 1050*1024, 50*1024)
print(list(nParticles))
macDeltaAVG = [0.01666313322320933,
             0.016669596322222223,
             0.016710319878619154,
             0.016791540854504756,
             0.016740562819297266,
             0.01675225565159129,
             0.016765589674860335,  # 300
             0.01677531982783678,
             0.016815878380392158,
             0.017055597033541783,
             0.017055597033541783,  # 500
             0.017702301910914455,
             0.018156345525105866,
             0.018917457172761665,
             0.020678066824948313,
             0.021838193104803495,
             0.02072899031767956,
             0.021352422585765123,
             0.024282678817152105,
             0.024285034014563105,
             0.026674477915555554] # 1000

dskDeltaAVG = [0.01666032583786785,
               0.01665657976692564,
               0.016661457480288727,
               0.0166576731804553,
               0.016660707977790117,
               0.016661652617990005,
               0.016667850585,
               0.016661656273181565,
               0.01666213000777346,
               0.016690951087875418,
               0.01666813620888889,
               0.016667265199444444,
               0.016672738858333334,
               0.016667449045555557,
               0.01669970823539232,
               0.018095459215922795,
               0.019277836292228644,
               0.02043790190667575,
               0.021782747466618287,
               0.022964473337413926,
               0.02393489324082935]

macFPSAVG = []
for val in macDeltaAVG:
    macFPSAVG.append(1.0 / val)

macFPSAVG = np.array(macFPSAVG).astype(np.float)

dskFPSAVG = []
for val in dskDeltaAVG:
    dskFPSAVG.append(1.0 / val)

dskFPSAVG = np.array(dskFPSAVG).astype(np.float)

plt.plot(nParticles, macFPSAVG)
plt.plot(nParticles, dskFPSAVG)

plt.show()
