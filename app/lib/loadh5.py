import numpy as np
import h5py
"""
# Load data from HDF5
with h5py.File('../testData/data.h5', 'r') as hf:
    players = [i for i in hf['descs']]
    test = players[0:2]

    for i in test:
        print np.array(hf['descs'][i])

    item = hf['kps']

    print isinstance(item, h5py.File)
    print isinstance(item, h5py.Group)
    print isinstance(item, h5py.Dataset)


    print item.id      # for example: <GroupID [1] (U) 33554473>
    print item.ref     # for example: <HDF5 object reference>
    print item.parent  # for example: <HDF5 group "/Configure:0000/Run:0000/CalibCycle:0000" (5 members)>
    print item.file    # for example: <HDF5 file "cxi80410-r0587.h5" (mode r, 3.5G)>
    print item.name    # for example: /Configure:0000/Run:0000/CalibCycle:0000/Camera::FrameV1
    print item.attrs          # for example: <Attributes of HDF5 object at 230141696>
    print item.attrs.keys()   # for example: ['start.seconds', 'start.nanoseconds']
    print item.attrs.values() # for example: [1297608424L, 627075857L]
    print len(item.attrs)
    #print item.items()
"""
h5db = []
with h5py.File('../testData/data.h5', 'r') as hf2:
    for i in hf2['kps/']:
        k = hf2['kps/' + i][:]
        d = hf2['descs/' + i][:]
        h5db.append({"file": i, "desc": (k, d)})
print h5db
