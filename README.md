# Inverse Design of Plasmonics Nanoparticles using Tandem and cVAE Networks

This repository is a part of *Leveraging Generative Neural Networks for Accurate, Diverse, and Robust Nanoparticle Design*, DOI:###.

## Introduction

## Table of Contents

1. Getting Started

    - Prerequisites
    - How to Use

2. Repository Structure

3. Dataset Generation

4. Model Training

5. Model Testing

## Getting Started

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

### How to Use

1. Clone the repository.

        git clone https://github.com/tanzim-rahman/plasmonics-inverse-design.git

2. Generate the training dataset. This can be done by either,

    - Unzipping **training_dataset.7z** in the Dataset directory.
    - Running **dataset_generation.py**.

3. Train the models. The notebooks for training are available in the Training Notebooks directory.

4. Test the models. This can be done with the **model_prediction_and_testing.ipynb** notebook.

### Repository Structure

Directories:

- Dataset: Contains the dataset required for model training.

- Models: Contains the trained models.

- Refractive index interpolated: Contains refractive indices of the materials used during the project. Required for calculating the plasmonics response using Mie theory.

- Spectra: Contains the experimentally obtained absorption spectrum for a Au@Ag core-shell nanoparticle. Used for testing the models.

- Training Notebooks: Contains the notebooks for training the various models.

Files:

- DataGen.py: Uses the python module *scattnlay* to calculate the plasmonics response of a multi-layered nanoparticle using Mie theory. The file can be used to generate as well as normalize the extinction, scattering and absorption cross-sections.

- dataset_generation.py: Allows for the manual generation of a new training dataset.

- model_prediction_and_testing.ipynb: Notebook that allows for the testing of the trained models.
