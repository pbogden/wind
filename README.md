
# wind

Visualize GFS winds from NOMADS file in GRIB format

* [wind](https://observablehq.com/d/a4fac32b8ae69138) -- notebook
* [particle trails](https://observablehq.com/@pbogden/particle-trails) -- notebook

There are 2 code options for processing GRIB data: NCAR or ECMWF (both have Python APIs). I'm using the NCAR code, PyNIO.

* [Data](#data) -- description of GRIB data format
* [PyNIO](#pynio) -- instructions to install and run

### Process GRIB file

To create data.json with wind vectors

    $ make

To print some metadata (including date of the forecast)

    $ make metadata

To list all the variables in the GRIB file

    $ make list 

### Source data 

* GRIB 
    * The date part of the filename.
    * GRIB files have wind for 8 level types. Relevant metadata is in the filename. For example:
        * UGRD_P0_L6_GLL0     # maximum wind level -- (1)
        * UGRD_P0_L7_GLL0     # tropopause -- (1)
        * UGRD_P0_L100_GLL0   # isobaric surface -- (31)
        * UGRD_P0_L102_GLL0   # specified altitude above sea level (m) -- (3) -- lv_AMSL1: [1829..3658]
        * UGRD_P0_L103_GLL0   # specified height above ground (m) -- (6) -- lv_HTGL7: [20..100]
        * UGRD_P0_L104_GLL0   # Sigma level (sigma value) -- (1)
        * UGRD_P0_2L108_GLL0  # Level at specified pressure difference from ground to level (Pa) -- (1)
        * UGRD_P0_L109_GLL0   # Potential vorticity (K m2 kg-1 s-1) -- (2)
    * Two levels: height of maximum wind, height of tropopause
    * Height of maximum wind is available in pressure (Pa) and ICAO standard atmosphere reference height (m)
    * Height of maximum wind and height of tropopoause in (m) use ICAO standard atmosphere reference height
* ICAO
    * The International Civil Aviation Organization (ICAO) published an "ICAO Standard Atmosphere" in 1993. 
    * It has the same model as the ISA, but extends the altitude coverage to 80 kilometers (262,500 feet)
    * The ICAO Standard Atmosphere, like the ISA, does not contain water vapor.

### PyNIO

Installed [PyNIO](http://www.pyngl.ucar.edu/Nio.shtml) as directed with a separate conda environment.
The [PyNIO github site](https://github.com/NCAR/pynio#pynio) is well documented.

    $ conda create --name pynio_env --channel conda-forge pynio
    $ source activate pynio_env

To use it, first activate the environment, and deactivate when done:

    $ conda activate pynio_env
    $ python
    >>> import Nio
    >>> print(Nio.__version)
    >>> print(Nio.__doc__)
    $ conda deactivate

* [PyNIO API docs](http://www.pyngl.ucar.edu/Nio.shtml) -- ucar.edu
    * Filename extension indicates expected format
    * For GRIB 1 & 2: .gr, .gr1, .grb, .grib, .grb1, .grib1, .gr2, .grb2, .grib2 

### References

* GRIB encoding
    * [GRIB2 encoding details](https://www.weather.gov/mdl/grib_design) -- weather.gov
* turbulence, etc.
    * Unnoficial display of [World Area Forecast System (WAFS)](https://aviationweather.cp.ncep.noaa.gov/wafs) -- noaa.gov
        * APPROVED ACCESS ONLY for data
    * [North American Rapid Refresh Ensemble (NARRE)](https://nomads.ncep.noaa.gov/txt_descriptions/NARRE_doc.shtml) -- noaa.gov
        * Has icing, turbulence, jet streem convection from ensemble models
    * [NEXRAD radar](https://www.ncdc.noaa.gov/data-access/radar-data/nexrad-products) -- NCDC products
    * [assessment of graphical turbulence](https://repository.library.noaa.gov/view/noaa/18086/noaa_18086_DS1.pdf?) (PDF) -- noaa.gov
* [GRIB](https://en.wikipedia.org/wiki/GRIB) -- wikipedia
* [ecCodes](https://confluence.ecmwf.int/display/ECC) -- ecmwf.int
    * ECMWF tools for GRIB, BUFR and WMS GTS (documentation uses Atlassian)
    * These tools need to be compiled with cmake. Python bindings exist. Linux recommended; no Windows support.
    * [Python 3 interface for ecCodes](https://confluence.ecmwf.int/display/ECC/Python+3+interface+for+ecCodes) -- ecmf.int
    * [GRIB tools (deprecated)](https://confluence.ecmwf.int//display/GRIB/Grib+tools) -- ecmwf.int
* [NOMADS](https://nomads.ncep.noaa.gov/) -- ncep.noaa.gov
    * [model changes](https://www.emc.ncep.noaa.gov/gmb/STATS/html/model_changes.html)
    * [GFS documentation](https://nomads.ncep.noaa.gov/txt_descriptions/GFS_doc.shtml)
    * [Performance statistics](https://www.emc.ncep.noaa.gov/gmb/STATS_vsdb/)
* [podpac](https://github.com/creare-com/podpac) -- github
    * [gfs.ipynb](https://github.com/creare-com/podpac-examples/blob/master/notebooks/demos/gfs.ipynb) -- github
* [pynio](https://github.com/NCAR/pynio#pynio) -- github
    * [PyNIO](http://www.pyngl.ucar.edu/Nio.shtml) -- ucar.edu
    * Includes install instructions using conda
* [grib2json](https://github.com/cambecc/grib2json) -- github
    * older java implementation
* [PyNGL](http://www.pyngl.ucar.edu/) -- ucar.edu
    * 2D visualization of climate and weather data in Python
    * [pyngl](https://github.com/NCAR/pyngl) -- github
    * [PYNGL gallery](http://www.pyngl.ucar.edu/Examples/gallery.shtml) -- gallery
* [Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) -- docs.conda.io
* [International Standard Atmosphere (ISA)](https://en.wikipedia.org/wiki/International_Standard_Atmosphere)
* Visualization
    * [cambecc earth](https://github.com/cambecc/earth) -- github
    * [Esri version](https://github.com/Esri/wind-js) -- github
* [GRIB WW3 data viz with python](https://polar.ncep.noaa.gov/waves/examples/usingpython.shtml#example_2() -- ncep.noaa.gov
