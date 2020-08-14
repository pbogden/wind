import Nio
#
# NOTE: To run this code
#
#    conda activate pynio_env
#    python mdata.py
#    conda deactivate
#

filepath = "data/gfs.t06z.pgrb2.1p00.anl.gr"
f = Nio.open_file(filepath, mode='r', options=None, history='', format='')

# Print long names of all the variables the file
keys = f.variables.keys()
for i, key in enumerate(keys):
    try:
        print(i, key, f.variables[key].long_name + ", " + f.variables[key].level_type)
    except:
        print('NO LEVEL TYPE', i, key, f.variables[key].long_name)
