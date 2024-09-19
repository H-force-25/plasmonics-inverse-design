# Inverse Design of Plasmonics Nanoparticles using Tandem and cVAE Networks

This repository is a part of *Leveraging Generative Neural Networks for Accurate, Diverse, and Robust Nanoparticle Design*, DOI:###.

## Table of Contents

- Getting Started
- Dataset Generation
- Model Training
- Model Testing

## Getting Started

### Prerequisites

All codes available in the repository are written in [Python3](https://www.python.org/). Additionally, it is highly recommended to use [Jupyter Notebook](https://jupyter.org/) for the training and testing of the ML models since it allows for the execution of small batches of code instead of running the entire script.

In order to calculate plasmonics resonance using Mie theory, [Scattnlay](https://github.com/ovidiopr/scattnlay) is used.

For data analysis, we used [Numpy](https://numpy.org/) and [Pandas](https://pandas.pydata.org/). For data visualization purposes, we employed the [Matplotlib](https://matplotlib.org/) library (particularly the Pyplot submodule).

The training process is performed using the [Keras API](https://keras.io/) with a [TensorFlow backend](https://www.tensorflow.org/).

Listed below are the versions of the various modules used during the project.

- Python - 3.10.5
- Scattnlay - 2.2.0
- Numpy - #
- Pandas - #
- Matplotlib - #
- Tensorflow - 2.15.0
- Keras - #

The Tensorflow version should be at least 2.15.0. The versions of the other modules does not seem crucial, however we still suggest using the latest versions available.

### How to Use

1. Clone the repository.

        git clone https://github.com/tanzim-rahman/plasmonics-inverse-design.git

2. Generate the training dataset. This can be done by either,

    - Unzipping **training_dataset.7z** in the Dataset directory.
    - Running **dataset_generation.py**.

3. Train the models.
