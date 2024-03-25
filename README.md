# SR4X for image super-resolution @ NTIRE 2024 Challenge

## To download the code repository

```bash
git clone https://github.com/CeviKle/KLETech-CEVI_Lowlight_Hypnotise_SRx4.git
cd KLETech-CEVI_Lowlight_Hypnotise_SRx4
```
### Installation
Install Pytorch first.
Then,
```
pip install -r requirements.txt
python setup.py develop
```

## To test the code with LR images 

Without implementing the codes, [chaiNNer](https://github.com/chaiNNer-org/chaiNNer) is a nice tool to run our models.

Otherwise, 
- Refer to `./options/test` for the configuration file of the model to be tested, and prepare the testing data and pretrained model.  
-  Download pretrained weights from [Drive Link](https://drive.google.com/drive/folders/1RZ3BPlZck_sUutaE6OP-f_N5URFQZ-L3?usp=sharing) and place under ```model_zoo``` folder
- Then run the following codes (taking `model_zoo/20_SR4X.pth` as an example):
```
python models/test.py -opt options/test/HAT_SRx4_ImageNet-pretrain.yml
```
The testing results will be saved in the `./results` folder.  

- Refer to `./options/test/HAT_SRx4_ImageNet-LR.yml` for **inference** without the ground truth image.

**Note that the tile mode is also provided for limited GPU memory when testing. You can modify the specific settings of the tile mode in your custom testing option by referring to `./options/test/HAT_tile_example.yml`.**