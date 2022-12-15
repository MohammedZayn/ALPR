## python version preffered 3.7.4
##https://carnet.ai/ they predict the make of the car

import os
import streamlit as st 
import subprocess
from PIL import Image
import time

def load_image(image):
    img = Image.open(image)
    return img

# cmdOne = 'pip install -r requirements.txt'
# processOne = subprocess.Popen(cmdOne, stdout=subprocess.PIPE)
# stdout,stderr = processOne.communicate()

# cmdTwo = 'python save_model.py --weights ./data/custom.weights --output ./checkpoints/custom-416 --input_size 416 --model yolov4'
# processTwo = subprocess.Popen(cmdTwo, shell=True)
# stdout,stderr = processTwo.communicate()

# cmdThree = 'python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --dont_show True --images ./data/images/car2.jpg --plate'
# processThree = subprocess.Popen(cmdThree, stdout=subprocess.PIPE)
# stdout,stderr = processThree.communicate()
# print(str(stdout))
# plateNumber = stdout[17:]
# print(plateNumber)

# APP-ALPR
st.title("ALPR Application")
st.markdown(" This application allows you to upload your car image and reads the number plate for you ")
st.markdown("---")


image = st.file_uploader("Upload Your Picture Here: ", type=['jpg','png','jpeg'])

if image is not None:
    path_in = image.name
    
    ####### saving file #######
    file_details = {"FileName":image.name,"FileType":image.type}
    img = load_image(image)
    #dividing page into two columns
    col1,col2= st.columns(2)
    col1.markdown("<h3 style='text-align: center; color: black;'>Input Image</h3>", unsafe_allow_html=True)
    col2.markdown("<h3 style='text-align: center; color: black;'>Output Image</h3>", unsafe_allow_html=True)
    col1.image(image)
    with open(os.path.join("./data/images",image.name),"wb") as f: 
      f.write(image.getbuffer())         
    ####### Running script #######
    progress_bar = st.progress(0)
    for perc_completed in range(100):
        time.sleep(0.05)
        progress_bar.progress(perc_completed+1)

    cmdThree = f'python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --dont_show True --images ./data/images/{path_in} --plate'
    processThree = subprocess.Popen(cmdThree, stdout=subprocess.PIPE)
    stdout,stderr = processThree.communicate()
    ####### Input on the input feild #######   
    plateNumber = str(stdout[17:-2])
    plateNumber = plateNumber[2:-1]
    license_plate = st.text_input("License Plate: ", plateNumber)

    # time.sleep(2)
    output_file_path = Image.open(r"C:\Users\HP\PycharmProjects\yolov4-custom-functions-master\detections\detection1.png")
    col2.image(output_file_path)
    
    






    # st.write(str(stdout))
    # plateNumber = str(stdout[17:-2])
    # plateNumber = plateNumber[2:-1]
    # st.write(plateNumber)
    