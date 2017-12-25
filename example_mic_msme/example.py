import BrukerMRI2 as bruker
import pylab as pl
import os


MainDir = os.getcwd()+os.sep
ExpNum = 56

# load FLASH experiment and reconstruct raw data
Experiment = bruker.ReadExperiment(MainDir, ExpNum)
Experiment.ReconstructKspace()

im = Experiment.reco_data[:,:,0]

# show the resulting images
pl.figure(figsize= (8,8))
pl.subplot(111)
pl.imshow(im, cmap=pl.cm.gray, aspect='auto')

#pl.subplot(132)
#pl.imshow(abs(Experiment.reco_data[:,:,1]))
#
#pl.subplot(133)
#pl.imshow(abs(Experiment.reco_data[:,:,2]))

#pl.suptitle("MRI method: " + Experiment.method["Method"] + \
#            ", Matrix: " + str(Experiment.method["PVM_Matrix"][0]) + \
#            " x " + str(Experiment.method["PVM_Matrix"][1]))

pl.show()
