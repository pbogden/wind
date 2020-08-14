# Note: To run python scripts with a conda environment, the following works, but I'm not sure why. 
# I got the hint from SFO: https://stackoverflow.com/questions/53382383/makefile-cant-use-conda-activate

CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

data.json:
	($(CONDA_ACTIVATE) pynio_env; python app.py)

# Print metadata (including the date of the forecast)
metadata:
	($(CONDA_ACTIVATE) pynio_env; python metadata.py)

# Print a list of all the variables in the GRIB file
list:
	($(CONDA_ACTIVATE) pynio_env; python list.py)

# Get latest GRIB file
latest:
	cp ../gfs/data/gfs.t06z.pgrb2.1p00.anl.gr data
