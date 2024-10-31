# Inverse Design of Plasmonics Nanoparticles using Tandem and cVAE Networks

## Introduction

This repository is a part of *Leveraging Generative Neural Networks for Accurate, Diverse, and Robust Nanoparticle Design*, DOI:###.

## Table of contents

1. [Getting started](#getting-started)

    - [Prerequisites](#prerequisites)
    - [How to use](#how-to-use)

2. [Repository structure](#repository-structure)

3. [Dataset structure](#dataset-structure)

    - [Material IDs](#material-ids)
    - [Thickness](#thickness)
    - [Dielectric host medium](#dielectric-host-medium)
    - [Absorption cross-sections](#absorption-cross-sections)
    - [Dataset generation](#dataset-generation)

4. [Model training](#model-training)

5. [Model prediction and testing](#model-prediction-and-testing)

## Getting started

### Prerequisites

All codes available in the repository are written in [Python3](https://www.python.org/). Additionally, it is highly recommended to use [Jupyter Notebook](https://jupyter.org/) for the training and testing of the ML models since it allows for the execution of small batches of code instead of running the entire script.

In order to calculate plasmonics resonance using Mie theory, [Scattnlay](https://github.com/ovidiopr/scattnlay) is used.

For data analysis, we used [Numpy](https://numpy.org/) and [Pandas](https://pandas.pydata.org/). For data visualization purposes, we employed the [Matplotlib](https://matplotlib.org/) library (particularly the Pyplot submodule).

The training process is performed using the [Keras API](https://keras.io/) with a [TensorFlow backend](https://www.tensorflow.org/).

Listed below are the versions of the various modules used during the project.

- Python - 3.10.5
- Scattnlay - 2.2.0
- Numpy - 1.25.2
- Pandas - 2.0.3
- Matplotlib - 3.7.1
- Tensorflow - 2.15.0
- Keras - 2.15.0

The Tensorflow version should be at least 2.15.0. The versions of the other modules does not seem crucial, however we still suggest using the latest versions available.

### How to use

1. Clone the repository.

        git clone https://github.com/tanzim-rahman/plasmonics-inverse-design.git

2. Generate the training dataset. This can be done by either,

    - Unzipping **training_dataset.7z** in the Dataset directory.
    - Running **dataset_generation.py**.

3. Train the models. The notebooks for training are available in the **Training Notebooks** directory.

4. Test the models. This can be done with the **model_prediction_and_testing.ipynb** notebook.

### Repository structure

Directories:

- **Dataset**: Contains the dataset required for model training.

- **Models**: Contains the trained models.

- **Refractive index interpolated**: Contains refractive indices of the materials used during the project. Required for calculating the plasmonics response using Mie theory.

- **Spectra**: Contains the experimentally obtained absorption spectrum for a Au@Ag core-shell nanoparticle. Used for testing the models.

- **Training Notebooks**: Contains the notebooks for training the various models.

Files:

- **DataGen.py**: Uses the python module *scattnlay* to calculate the plasmonics response of a multi-layered nanoparticle using Mie theory. The file can be used to generate as well as normalize the extinction, scattering and absorption cross-sections.

- **dataset_generation.py**: Allows for the manual generation of a new training dataset.

- **model_prediction_and_testing.ipynb**: Notebook that allows for the testing of the trained models.

## Dataset structure

The dataset is contained in a *CSV* file that holds **205** columns. Each row of the dataset signifies a unique nanosphere with column properties specified in the table below.

|Column(s)|Value|Description                      |
|---------|-----|---------------------------------|
|1        |m1   |Material ID of core layer.       |
|2        |m2   |Material ID of shell layer.      |
|3        |t1   |Thickness of core layer (in nm). |
|4        |t2   |Thickness of shell layer (in nm).|
|5        |host |Dielectric host medium.          |
|6-205    |Acs  |Absorption cross-sections.       |

### Material IDs

The material IDs are assigned based on the table below:

|Material|None|Ag|Al|Au|Cu|GaAs|InAs|InP|Mo|Si|SiO2|
|--------|----|--|--|--|--|----|----|---|--|--|----|
|ID      |0   |1 |2 |3 |4 |5   |6   |7  |8 |9 |10  |

In our work, we only considered the core-shell particles. The dataset also contains bulk nanospheres where column 2 is set as 0 (None).

### Thickness

The thickness represents the distance between the outer and the inner walls of each layer. Hence, for the core layer, it is simply the radius of the nanosphere upto the beginning of the shell layer. In case of the shell layer, the thickness is the core thickness subtracted from the total sphere radius.

### Dielectric host medium

The medium that the nanospheres exist in. 0 denotes air medium while 1 denotes water medium. For our purposes, we used **water** as the dielectric host. However, our dataset also includes results for air as the host medium.

### Absorption cross-sections

The final **200** columns of a particular row in the dataset consist of the absorption cross-section spectra of the nanosphere defined by the first **5** columns of that row. **200** points of wavelength are linearly sampled in the range of **300-800 nm** (inclusive) and their respective cross-sections are calculated and recorded.

### Dataset generation

Inside the **Dataset** directory is a zipped file that contains an already generated dataset. A new dataset can be produced by using the **dataset_generation.py** script. The script works by selecting all possible combinations of *m1*, *m2*, *t1*, *t2* and *host* (as specified by the constrains mentioned below) and calculating the absorption cross-section for a nanosphere with those properties.

- The material IDs *m1* and *m2* are varied from **1-10**. However, an initial run is done where *m2* is set as **0** in order to calculate the cross-sections for single-layered nanospheres.

- The dielectric host is varied from **0** (air) to **1** (water).

- The thicknesses *t1* and *t2* are varied from **1-100**. Additionally, another condition is specified which restricts their sum (*t1* + *t2*) to less than **100**.

## Model training

## Model prediction and testing

Inside the **model_prediction_and_testing.ipynb** notebook are the codes for testing the trained models. This includes prediction of nanospheres based on random cross-section inputs as well as experimentally obtained inputs using both Tandem and cVAE models. Further details are included inside the notebook.
