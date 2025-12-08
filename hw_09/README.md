## How to use

If you want to run the notebook you have to install:

* PIL: pip install pillow
* onnx: pip install onnx
* onnxruntime: pip install onnxruntime

Note: Create a new environment so onnx does not mess up any tensorflow dependencies

Once packages are installed download:
* hair_classifier_v1.onnx
* hair_classifier_v1.onnx.data

Also from the dockerimage agrigorev/model-2025-hairstyle:v1, get:
* hair_classifier_empty.onnx
* hair_classifier_empty.onnx.data

Files have to be placed inside of ntbk folder, or if you change the location
adjust the corresponding paths in the notebook file
