# SR4X for image super-resolution @ NTIRE 2024 Challenge

## To download the code repository

```bash
git clone https://github.com/CeviKle/KLETech-CEVI_Lowlight_Hypnotise_SRx4.git
cd KLETech-CEVI_Lowlight_Hypnotise_SRx4
```

## System Requirements
NVIDIA GPU (minimum 24-32 GB for testing)
### Installation/setup 
```
docker pull niksx/image-superresolution
```
Download the weights from this [Drive link](https://drive.google.com/drive/folders/1RZ3BPlZck_sUutaE6OP-f_N5URFQZ-L3?usp=sharing), and paste under ```HAT/``` folder

## To test the code with LR images 
```bash
cd KLETech-CEVI_Lowlight_Hypnotise_SRx4/HAT
```
Paste the testing images under ```HAT/test_images``` folder and then run, 

```bash
CUDA_VISIBLE_DEVICES=0 python -m torch.distributed.launch --nproc_per_node=1 hat/test.py -opt options/test/HAT_SRx4_ImageNet-LR.yml --launch pytorch
```