# lost-data-chaser
For the '[Chasers of the Lost Data](https://2019.spaceappschallenge.org/challenges/planets-near-and-far/raiders-lost-data/details)' 
challenge for the [SpaceApps 2019 Hackathon](https://www.spaceappschallenge.org/).

**The Challenge**
> Help find ways to improve the performance of machine learning and predictive models by filling in gaps in the 
> datasets prior to model training. This entails finding methods to computationally recover or approximate data that 
> is missing due to sensor issues or signal noise that compromises experimental data collection. This work is 
> inspired by data collection during additive manufacturing (AM) processes where sensors capture build characteristics in-situ, but it has applications across many NASA domains.

# Installation
## Linux
### Conda 
To install in development mode:
1. Navigate to `/lost-data-chaser`
2. Run `conda env create -f environment.yml`

### Setup.py
1. Navigate to `/lost-data-chaser`
2. Run `python setup.py install` or `python setup.py develop` for development mode.

# Dataset download
To run the notebooks, ensure you have downloaded the following challenge files.

An auxiliary file will also be required, to download this run

`$ python data_chaser/utils/nsidc-download_SNEX17_SSD.001_2019-10-19.py` 

And extract the file `SnowEx17_snowdepth_15min_V2.csv` to your data directory.