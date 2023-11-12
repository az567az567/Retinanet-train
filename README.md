The method to install 
------
https://github.com/fizyr/keras-retinanet  
1) Clone this repository.  
2) In the repository, execute `pip install . --user`.  
   Note that due to inconsistencies with how `tensorflow` should be installed,  
   this package does not define a dependency on `tensorflow` as it will try to install that (which at least on Arch Linux results in an incorrect installation).
   Please make sure `tensorflow` is installed as per your systems requirements.  
3) Alternatively, you can run the code directly from the cloned  repository, however you need to run `python setup.py build_ext --inplace` to compile Cython code first.
4) Optionally, install `pycocotools` if you want to train / test on the MS COCO dataset by running `pip install --user  
 git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI`.  

Convert txt to xml files  
------ 
cd C:\Users\az567\txt2xml  
python txt2xml.py  
python setup.py build_ext –inplace  
pip install tensorflow==2.8   
pip install keras==2.6.0  
pip install progressbar2  
pip install keras_resnet  
C:\keras-retinanet\keras_retinanet\preprocessing\pascal_voc to change classes  

Train the model
------
cd C:/keras-retinanet  
python keras_retinanet/bin/train.py pascal “C:/keras-retinanet/dataset”  

convert your model from the training model to the inference model
------
change resnet50_pascal_01.h5  to  training.h5 & create folder retinamodels  
cd C:/keras-retinanet  
python keras_retinanet/bin/convert_model.py “C:/keras-retinanet/retinamodels/training.h5” “C:/keras-retinanet/retinamodels/inference.h5”  

Test the model
------
cd C:/keras-retinanet/examples  
python resnet50_retinanet.py  

Direct run C:/keras-retinanet/examples/resnet50_retinanet.py  




