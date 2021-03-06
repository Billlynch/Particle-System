import csv
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


nParticles = range(1024, 1050*1024, 50*1024)
nParticles = list(nParticles)
nParticles.append(2000 * 1024)
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
             0.026674477915555554,
             0.05345559514946619] # 1000

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
               0.02393489324082935,
               0.04832476530434783]

clDeltaAVG = [0.016660368549694615,
              0.01666193456579678,
              0.01665977139422543,
              0.016665720051637977,
              0.016664339638534146,
              0.016663931932259856,
              0.016662518528595224,
              0.016661815821765687,
              0.016663563740144365,
              0.016669727140555556,
              0.016668110898888887,
              0.016665673478622987,
              0.01666557541476957,
              0.01669103201446051,
              0.016671310388333332,
              0.01666679612777778,
              0.0167159226005571,
              0.016673475000555556,
              0.016671003384444445,
              0.016674599009444444,
              0.016671623603333335,
              0.016954884544632766]

macFPSAVG = []
for val in macDeltaAVG:
    macFPSAVG.append(1.0 / val)

macFPSAVG = np.array(macFPSAVG).astype(np.float)

dskFPSAVG = []
for val in dskDeltaAVG:
    dskFPSAVG.append(1.0 / val)

dskFPSAVG = np.array(dskFPSAVG).astype(np.float)

clFPSAVG = []
for val in clDeltaAVG:
    clFPSAVG.append(1.0 / val)

clFPSAVG = np.array(clFPSAVG).astype(np.float)

mac = plt.plot(nParticles, macFPSAVG)
dsk = plt.plot(nParticles, dskFPSAVG)
cl = plt.plot(nParticles, clFPSAVG)

plt.title('Average Frame Rate vs Particle Count')
plt.ylabel('Frame Rate (FPS)')
plt.xlabel('Number of Particles')
plt.legend((mac[0], dsk[0], cl[0]), ('Macbook Pro mid 2014', 'Gaming Desktop CPU', 'Gaming Desktop GPU (OpenCL enabled)'))

plt.show()

