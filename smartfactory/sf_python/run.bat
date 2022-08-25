
call "C:\Demo\open_model_zoo\.venv\Scripts\activate"

call "C:\Program Files (x86)\Intel\openvino_2022.1.0.643\setupvars.bat"

python object_detection_demo.py -m model/model.xml -d CPU -t 0.7 -at ssd -nireq 1 --labels labels.txt -i 0