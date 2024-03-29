# Physics Informed Masked Autoencoder (PI-MAE)

![Physical Mask](https://github.com/luke-mcevoy/PI-MAE/blob/main/Figures/With-White-Background/PI-MAE-Physical-Mask-Data-Acquisition.png)

![PIMAE vs MAE](https://github.com/luke-mcevoy/PI-MAE/blob/main/Figures/With-White-Background/PI-MAE-vs-MAE-Architecture.png
)

![PIMAE Physical Mask Results](https://github.com/luke-mcevoy/PI-MAE/blob/main/Figures/With-White-Background/PI-MAE-Physical-Mask-Results.png)

![PIMAE Noise Mask Results](https://github.com/luke-mcevoy/PI-MAE/blob/main/Figures/With-White-Background/PI-MAE-Noise-Mask-Results.png)

## Abstract

Imaging technology based on detecting individual photons has seen tremendous progress in recent years, with broad
applications in autonomous driving, biomedical imaging, astronomical observation, and more. Comparing with conventional
methods, however, it takes much longer time and relies on sparse and noisy photon-counting data to form an image. Here
we introduce Physics-Informed Masked Autoencoder (PI-MAE) as a fast and efficient approach for data acquisition and
image reconstruction through hardware implementation of the MAE (Masked Autoencoder). We examine its performance on
a single-photon LiDAR system when trained on digitally masked MNIST data. Our results show that, with 1.8 × 10−6 or less
detected photons per pulse and down to 9 detected photons per pixel, it achieves high-quality image reconstruction on unseen
object classes with 90% physical masking. Our results highlight PI-MAE as a viable hardware accelerator for significantly
improving the performance of single-photon imaging systems in photon-starving applications.

## Authors

Luke McEvoy, Daniel Tafone, Yong Meng Sua, Yuping Huang

## Development Enviornment

PI-MAE was developed using Tensorflow (version 2) with Python (version 3.10) on an AWS SageMaker instance with one NVIDIA T4 16GB GPU.

## [Code](https://github.com/luke-mcevoy/PI-MAE/tree/main/Code)

- Software for beam steering is in `MEMs-Code/` folder.
  - `Direct.py` controls the LiDAR system, given a scanning pattern as input
  - `Scan-Pattern-Creation.ipynb` creates randomly masked scanning patterns
  - `Direct-Scripts-Executed-for-PI-MAE.py` automates the LiDAR data acquisition process, as it executes all the scanning patterns in `Direct-scripts.txt`.

- Software for processing raw photon counts is in `Data-Processing\` folder.
  - `Photon-Counts-To-Images.ipynb` turns raw photon counts into images.
  - `What-is-Average-Photon-Count.ipynb` computes photon statistics on raw photon counts.
  - `Noise-Mask-PI-MAE.ipynb` creates noise masks is

- Software for PI-MAE is in `PI-MAE-Model\` folder.
  - `PI-MAE-Scans\` folder has data for you to run PI-MAE
    - `NOISE-MASK\` folder has noise mask scans, which is used by PI-MAE for reconstruction of 75% and 90% noise mask data
    - `PHYSICAL-MASK\` folder has physical mask scans, which is used by PI-MAE for reconstruction of 75% and 90% physical mask data
    - `Results-From-Running-Model\` is where PI-MAE output is written when you run the model yourself
      - `75-Physical-Results` holds the results from 75% physical mask reconstruction when you run PI-MAE
      - `90-Physical-Results` holds the results from 90% physical mask reconstruction when you run PI-MAE
      - `75-Noise-Results` holds the results from 75% noise mask reconstruction when you run PI-MAE
      - `90-Noise-Results` holds the results from 90% noise mask reconstruction when you run PI-MAE
  - Notebooks:
    - `PI-MAE-physical75mask.ipynb` is PI-MAE code to reconstruct 75% physical mask scans
    - `PI-MAE-physical90mask.ipynb` is PI-MAE code to reconstruct 90% physical mask scans
    - `PI-MAE-noise75mask.ipynb` is PI-MAE code to reconstruct 75% noise mask scans
    - `PI-MAE-noise90mask.ipynb` is PI-MAE code to reconstruct 90% noise mask scans
  - HTML:
    - `PI-MAE-physical75mask.html` is PI-MAE code to reconstruct 75% physical mask scans
    - `PI-MAE-physical90mask.html` is PI-MAE code to reconstruct 90% physical mask scans
    - `PI-MAE-noise75mask.html` is PI-MAE code to reconstruct 75% noise mask scans
    - `PI-MAE-noise90mask.html` is PI-MAE code to reconstruct 90% noise mask scans

## Data

- Raw single photon counts are in `Raw-Photon-Counts\` folder.
  - Letters:
    - 75% physically masked letters are in `LETTERS-75\` folder.
    - 90% physically masked letters are in `LETTERS-90\` folder.
  - Numbers:
    - 75% physically masked numbers are in `NUMBERS-75\` folder.
    - 90% physically masked numbers are in `NUMBERS-90\` folder.
- Raw single photon counts processed into images are in `Photon-Counts-as-Images\PI-MAE-Scans\` folder.
  - 75% physically masked letters are in `PHYSICAL-MASK\75mask-physical\` folder.
  - 90% physically masked letters are in `PHYSICAL-MASK\90mask-physical\` folder.
  - 75% noise masked numbers are in `NOISE-MASK\75mask-noise\` folder.
  - 90% noise masked numbers are in `NOISE-MASK\90mask-noise\` folder.

## Results

- `physicalmask75\` has PI-MAE reconstructions of 75% physically masked LiDAR scans.
- `physicalmask90\` has PI-MAE reconstructions of 90% physically masked LiDAR scans.
- `noisemask75\` has PI-MAE reconstructions of 75% noise masked LiDAR scans.
- `noisemask90\` has PI-MAE reconstructions of 90% noise masked LiDAR scans.
