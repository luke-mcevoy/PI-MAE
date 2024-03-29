# PI-MAE

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

# Code

Software for beam steering is in `MEMs-Code` folder. In this folder there is the code that controls LiDAR system `Direct.py` given a scanning pattern, code to create scanning patterns `Scan-Pattern-Creation.ipynb`, and an python script to automate the execution of many scanning patterns called `Direct-Scripts-Executed-for-PI-MAE.py`.

Software for turning raw photon counts (CSV) into images (PNG) is `Photon-Counts-To-Images.ipynb`.

Software for computing photon statistics on raw photon counts is `What-is-Average-Photon-Count.ipynb`.

Software for creating noise masks is `Noise-Mask-PI-MAE.ipynb`

Software for PI-MAE is under `` folder.
