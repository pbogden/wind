import Nio
import numpy as np
#
# NOTE: To run this code
#
#    conda activate pynio_env
#    python appm.py
#    conda deactivate
#

filepath = "data/gfs.t06z.pgrb2.1p00.anl.gr"
f = Nio.open_file(filepath, mode='r', options=None, history='', format='')

# Print wind metadata for 8 level types
key = 'UGRD_P0_L6_GLL0'     # maximum wind level -- (1)
#key = 'UGRD_P0_L7_GLL0'     # tropopause -- (1)
#key = 'UGRD_P0_L100_GLL0'   # isobaric surface -- (31)
#key = 'UGRD_P0_L102_GLL0'   # specified height above sea level -- (3) -- lv_AMSL1: [1829..3658] 
#key = 'UGRD_P0_L103_GLL0'   # specified height above ground (m) -- (6) -- lv_HTGL7: [20..100]
#key = 'UGRD_P0_L104_GLL0'  # $igma level (sigma value) -- (1)
#key = 'UGRD_P0_2L108_GLL0' # Level at specified pressure difference from ground to level (Pa) -- (1)
#key = 'UGRD_P0_L109_GLL0'  # Potential vorticity (K m2 kg-1 s-1) -- (2)

udata = f.variables[key].get_value()
vdata = f.variables['V' + key[1:]].get_value()
print(udata.size)
print(udata.shape)
print(type(udata))

import json

udata = udata.tolist()
vdata = vdata.tolist()
with open("data.json", "w") as f:
    json.dump(json.loads(json.dumps([udata, vdata]), parse_float=lambda x: round(float(x), 2)), f)
