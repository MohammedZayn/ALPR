## python version preffered 3.7.4
##https://carnet.ai/ they predict the make of the car

import os
import streamlit as st 
import subprocess
from PIL import Image
import time
import cvzone
from cvzone.ClassificationModule import Classifier
import cv2

def load_image(image):
    img = Image.open(image)
    return img
    
def CarClassifier(img):
    myClassifier = Classifier('classifModels/keras_model.h5','classifModels/labels.txt')
    predictions = myClassifier.getPrediction(img)
        #  print(predictions[1])
    if predictions[1] == 0:
        car = 'Acura Integra Type R 2001'
    elif predictions[1] == 1:
        car ='Acura RL Sedan 2012'
    elif predictions[1] == 2:
        car ='Class 3'
    elif predictions[1] == 3:
        car = 'Acura TL Type-S 2008'
    elif predictions[1] == 4:
        car = 'Acura TSX Sedan 2012'
    elif predictions[1] == 5:
        car = 'Acura ZDX Hatchback 2012'
    elif predictions[1] == 6:
        car = 'AM General Hummer SUV 2000'
    elif predictions[1] == 7:
        car = 'Aston Martin V8 Vantage Convertible 2012'
    elif predictions[1] == 8:
        car = 'Aston Martin V8 Vantage Coupe 2012'
    elif predictions[1] == 9:
        car = 'Aston Martin Virage Convertible 2012'

    elif predictions[1] == 10:
        car = 'Aston Martin Virage Coupe 2012'
    elif predictions[1] == 11:
        car = 'Audi 100 Sedan 1994'
    elif predictions[1] == 12:
        car = 'Audi 100 Wagon 1994'
    elif predictions[1] == 13:
        car = 'Audi A5 Coupe 2012'
    elif predictions[1] == 14:
        car = 'Audi R8 Coupe 2012'
    elif predictions[1] == 15:
        car = 'Audi RS 4 Convertible 2008'
    elif predictions[1] == 16:
        car = 'Audi S4 Sedan 2007'
    elif predictions[1] == 17:
        car = 'Audi S4 Sedan 2012'
    elif predictions[1] == 18:
        car = 'Audi S5 Convertible 2012'
    elif predictions[1] == 19:
        car = 'Audi S5 Coupe 2012'

    elif predictions[1] == 20:
        car = 'Audi S6 Sedan 2011'
    elif predictions[1] == 21:
        car = 'Audi TT Hatchback 2011'
    elif predictions[1] == 22:
        car = 'Audi TT RS Coupe 2012'
    elif predictions[1] == 23:
        car = 'Audi TTS Coupe 2012'
    elif predictions[1] == 24:
        car = 'Audi V8 Sedan 1994'
    elif predictions[1] == 25:
        car = 'Bentley Arnage Sedan 2009'
    elif predictions[1] == 26:
        car = 'Bentley Continental Flying Spur Sedan 2007'
    elif predictions[1] == 27:
        car = 'Bentley Continental GT Coupe 2007'
    elif predictions[1] == 28:
        car = 'Bentley Continental GT Coupe 2012'
    elif predictions[1] == 29:
        car = 'Bentley Continental Supersports Conv. Convertible'

    elif predictions[1] == 30:
        car = 'Bentley Mulsanne Sedan 2011'
    elif predictions[1] == 31:
        car = 'BMW 1 Series Convertible 2012'
    elif predictions[1] == 32:
        car = 'BMW 1 Series Coupe 2012'
    elif predictions[1] == 33:
        car = 'BMW 3 Series Sedan 2012'
    elif predictions[1] == 34:
        car = 'BMW 3 Series Wagon 2012'
    elif predictions[1] == 35:
        car = 'BMW 6 Series Convertible 2007'
    elif predictions[1] == 36:
        car = 'BMW ActiveHybrid 5 Sedan 2012'
    elif predictions[1] == 37:
        car = 'BMW M3 Coupe 2012'
    elif predictions[1] == 38:
        car = 'BMW M5 Sedan 2010'
    elif predictions[1] == 39:
        car = 'BMW M6 Convertible 2010'

    elif predictions[1] == 40:
        car = 'BMW X3 SUV 2012'
    elif predictions[1] == 41:
        car = 'BMW X5 SUV 2007'
    elif predictions[1] == 42:
        car = 'BMW X6 SUV 2012'
    elif predictions[1] == 43:
        car = 'BMW Z4 Convertible 2012'
    elif predictions[1] == 44:
        car = 'Bugatti Veyron 16.4 Convertible 2009'
    elif predictions[1] == 45:
        car = 'Bugatti Veyron 16.4 Coupe 2009'
    elif predictions[1] == 46:
        car = 'Buick Enclave SUV 2012'
    elif predictions[1] == 47:
        car = 'Cadillac CTS-V Sedan 2012'
    elif predictions[1] == 48:
        car = 'Cadillac Escalade EXT Crew Cab 2007'
    elif predictions[1] == 49:
        car = 'Cadillac SRX SUV 2012'

    elif predictions[1] == 50:
        car = 'Chevrolet Avalanche Crew Cab 2012'
    elif predictions[1] == 51:
        car = 'Chevrolet Camaro Convertible 2012'
    elif predictions[1] == 52:
        car = 'Chevrolet Cobalt SS 2010'
    elif predictions[1] == 53:
        car = 'Chevrolet Corvette Convertible 2012'
    elif predictions[1] == 54:
        car = 'Chevrolet Corvette Ron Fellows Edition Z06 2007'
    elif predictions[1] == 55:
        car = 'Chevrolet Corvette ZR1 2012'
    elif predictions[1] == 56:
        car = 'Chevrolet Express Cargo Van 2007'
    elif predictions[1] == 57:
        car = 'Chevrolet Express Van 2007'
    elif predictions[1] == 58:
        car = 'Chevrolet HHR SS 2010Chevrolet HHR SS 2010'
    elif predictions[1] == 59:
        car = 'Chevrolet Impala Sedan 2007'

    elif predictions[1] == 60:
        car = 'Chevrolet Malibu Hybrid Sedan 2010'
    elif predictions[1] == 61:
        car = 'Chevrolet Malibu Sedan 2007'
    elif predictions[1] == 62:
        car = 'Chevrolet Monte Carlo Coupe 2007'
    elif predictions[1] == 63:
        car = 'Chevrolet Silverado 1500 Classic Extended Cab 2007'
    elif predictions[1] == 64:
        car = 'Chevrolet Silverado 1500 Extended Cab 2012'
    elif predictions[1] == 65:
        car = 'Chevrolet Silverado 1500 Hybrid Crew Cab 2012'
    elif predictions[1] == 66:
        car = 'Chevrolet Silverado 1500 Regular Cab 2012'
    elif predictions[1] == 67:
        car = 'Chevrolet Silverado 2500HD Regular Cab 2012'
    elif predictions[1] == 68:
        car = 'Chevrolet Sonic Sedan 2012'
    elif predictions[1] == 69:
        car = 'Chevrolet Tahoe Hybrid SUV 2012'

    elif predictions[1] == 70:
        car = 'Chevrolet TrailBlazer SS 2009'
    elif predictions[1] == 71:
        car = 'Chevrolet Traverse SUV 2012'
    elif predictions[1] == 72:
        car = 'Chrysler 300 SRT-8 2010'
    elif predictions[1] == 73:
        car = 'Chrysler Aspen SUV 2009'
    elif predictions[1] == 74:
        car = 'Chrysler Crossfire Convertible 2008'
    elif predictions[1] == 75:
        car = 'Chrysler PT Cruiser Convertible 2008'
    elif predictions[1] == 76:
        car = 'Chrysler Sebring Convertible 2010'
    elif predictions[1] == 77:
        car = 'Chrysler Town and Country Minivan 2012'
    elif predictions[1] == 78:
        car = 'Daewoo Nubira Wagon 2002'
    elif predictions[1] == 79:
        car = 'Dodge Caliber Wagon 2007'

    elif predictions[1] == 80:
        car = 'Dodge Caliber Wagon 2012'
    elif predictions[1] == 81:
        car = 'Dodge Caravan Minivan 1997'
    elif predictions[1] == 82:
        car = 'Dodge Challenger SRT8 2011'
    elif predictions[1] == 83:
        car = 'Dodge Charger Sedan 2012'
    elif predictions[1] == 84:
        car = 'Dodge Charger SRT-8 2009'
    elif predictions[1] == 85:
        car = 'Dodge Dakota Club Cab 2007'
    elif predictions[1] == 86:
        car = 'Dodge Dakota Crew Cab 2010'
    elif predictions[1] == 87:
        car = 'Dodge Durango SUV 2007'
    elif predictions[1] == 88:
        car = 'Dodge Durango SUV 2012'
    elif predictions[1] == 89:
        car = 'Dodge Journey SUV 2012'

    elif predictions[1] == 90:
        car = 'Dodge Magnum Wagon 2008'
    elif predictions[1] == 91:
        car = 'Dodge Ram Pickup 3500 Crew Cab 2010'
    elif predictions[1] == 92:
        car = 'Dodge Ram Pickup 3500 Quad Cab 2009'
    elif predictions[1] == 93:
        car = 'Dodge Sprinter Cargo Van 2009'
    elif predictions[1] == 94:
        car = 'Eagle Talon Hatchback 1998'
    elif predictions[1] == 95:
        car = 'Ferrari 458 Italia Convertible 2012'
    elif predictions[1] == 96:
        car = 'Ferrari 458 Italia Coupe 2012'
    elif predictions[1] == 97:
        car = 'Ferrari California Convertible 2012'
    elif predictions[1] == 98:
        car = 'Ferrari FF Coupe 2012'
    elif predictions[1] == 99:
        car = 'FIAT 500 Abarth 2012'

    elif predictions[1] == 100:
        car = 'FIAT 500 Convertible 2012'
    elif predictions[1] == 101:
        car = 'Class 103'
    elif predictions[1] == 102:
        car = 'Ford Edge SUV 2012'
    elif predictions[1] == 103:
        car = 'Ford E-Series Wagon Van 2012'
    elif predictions[1] == 104:
        car = 'Ford Expedition EL SUV 2009'
    elif predictions[1] == 105:
        car = 'Ford F-150 Regular Cab 2007'
    elif predictions[1] == 106:
        car = 'Ford F-150 Regular Cab 2012'
    elif predictions[1] == 107:
        car = 'Ford F-450 Super Duty Crew Cab 2012'
    elif predictions[1] == 108:
        car = 'Ford Fiesta Sedan 2012'
    elif predictions[1] == 109:
        car = 'Ford Focus Sedan 2007'

    elif predictions[1] == 110:
        car = 'Ford Freestar Minivan 2007'
    elif predictions[1] == 111:
        car = 'Ford GT Coupe 2006'
    elif predictions[1] == 112:
        car = 'Ford Mustang Convertible 2007'
    elif predictions[1] == 113:
        car = 'Ford Ranger SuperCab 2011'
    elif predictions[1] == 114:
        car = 'Geo Metro Convertible 1993'
    elif predictions[1] == 115:
        car = 'GMC Acadia SUV 2012'
    elif predictions[1] == 116:
        car = 'GMC Canyon Extended Cab 2012'
    elif predictions[1] == 117:
        car = 'GMC Savana Van 2012'
    elif predictions[1] == 118:
        car = 'GMC Terrain SUV 2012'
    elif predictions[1] == 119:
        car = 'GMC Yukon Hybrid SUV 2012'

    elif predictions[1] == 120:
        car = 'Honda Accord Coupe 2012'
    elif predictions[1] == 121:
        car = 'Honda Accord Sedan 2012'
    elif predictions[1] == 122:
        car = 'Honda Odyssey Minivan 2007'
    elif predictions[1] == 123:
        car = 'Honda Odyssey Minivan 2012'
    elif predictions[1] == 124:
        car = 'HUMMER H2 SUT Crew Cab 2009'
    elif predictions[1] == 125:
        car = 'HUMMER H3T Crew Cab 2010'
    elif predictions[1] == 126:
        car = 'Hyundai Accent Sedan 2012'
    elif predictions[1] == 127:
        car = 'Hyundai Azera Sedan 2012'
    elif predictions[1] == 128:
        car = 'Hyundai Elantra Sedan 2007'
    elif predictions[1] == 129:
        car = 'Hyundai Elantra Touring Hatchback 2012'

    elif predictions[1] == 130:
        car = 'Hyundai Genesis Sedan 2012'
    elif predictions[1] == 131:
        car = 'Hyundai Santa Fe SUV 2012'
    elif predictions[1] == 132:
        car = 'Hyundai Sonata Hybrid Sedan 2012'
    elif predictions[1] == 133:
        car = 'Hyundai Sonata Sedan 2012'
    elif predictions[1] == 134:
        car = 'Hyundai Tucson SUV 2012'
    elif predictions[1] == 135:
        car = 'Hyundai Veloster Hatchback 2012'
    elif predictions[1] == 136:
        car = 'Hyundai Veracruz SUV 2012'
    elif predictions[1] == 137:
        car = 'Infiniti G Coupe IPL 2012'
    elif predictions[1] == 138:
        car = 'Infiniti QX56 SUV 2011'
    elif predictions[1] == 139:
        car = 'Isuzu Ascender SUV 2008'

    elif predictions[1] == 140:
        car = 'Jaguar XK XKR 2012'
    elif predictions[1] == 141:
        car = 'Jeep Compass SUV 2012'
    elif predictions[1] == 142:
        car = 'Jeep Grand Cherokee SUV 20122'
    elif predictions[1] == 143:
        car = 'Jeep Liberty SUV 2012'
    elif predictions[1] == 144:
        car = 'Jeep Patriot SUV 2012'
    elif predictions[1] == 145:
        car = 'Jeep Wrangler SUV 2012'
    elif predictions[1] == 146:
        car = 'Lamborghini Aventador Coupe 2012'
    elif predictions[1] == 147:
        car = 'Lamborghini Diablo Coupe 2001'
    elif predictions[1] == 148:
        car = 'Lamborghini Gallardo LP 570-4 Superleggera 2012'
    elif predictions[1] == 149:
        car = 'Lamborghini Reventon Coupe 2008'

    elif predictions[1] == 150:
        car = 'Land Rover LR2 SUV 2012'
    elif predictions[1] == 151:
        car = 'Land Rover Range Rover SUV 2012'
    elif predictions[1] == 152:
        car = 'Class 154'
    elif predictions[1] == 153:
        car = 'Maybach Landaulet Convertible 2012'
    elif predictions[1] == 154:
        car = 'Mazda Tribute SUV 2011'
    elif predictions[1] == 155:
        car = 'McLaren MP4-12C Coupe 2012'
    elif predictions[1] == 156:
        car = 'Mercedes-Benz 300-Class Convertible 1993'
    elif predictions[1] == 157:
        car = 'Mercedes-Benz C-Class Sedan 2012'
    elif predictions[1] == 158:
        car = 'Mercedes-Benz E-Class Sedan 2012'
    elif predictions[1] == 159:
        car = 'Mercedes-Benz S-Class Sedan 2012'

    elif predictions[1] == 160:
        car = 'Mercedes-Benz SL-Class Coupe 2009'
    elif predictions[1] == 161:
        car = 'Mercedes-Benz Sprinter Van 2012'
    elif predictions[1] == 162:
        car = 'MINI Cooper Roadster Convertible 2012'
    elif predictions[1] == 163:
        car = 'Mitsubishi Lancer Sedan 2012'
    elif predictions[1] == 164:
        car = 'Nissan 240SX Coupe 1998'
    elif predictions[1] == 165:
        car = 'Nissan Juke Hatchback 2012'
    elif predictions[1] == 166:
        car = 'Nissan Leaf Hatchback 2012'
    elif predictions[1] == 167:
        car = 'Nissan NV Passenger Van 2012'
    elif predictions[1] == 168:
        car = 'Plymouth Neon Coupe 1999'
    elif predictions[1] == 169:
        car = 'Porsche Panamera Sedan 2012'

    elif predictions[1] == 170:
        car = 'Rolls-Royce Ghost Sedan 2012'
    elif predictions[1] == 171:
        car = 'Rolls-Royce Phantom Drophead Coupe Convertible 201'
    elif predictions[1] == 172:
        car = 'Rolls-Royce Phantom Sedan 2012'
    elif predictions[1] == 173:
        car = 'Class 175'
    elif predictions[1] == 174:
        car = 'smart fortwo Convertible 2012'
    elif predictions[1] == 175:
        car = 'Spyker C8 Convertible 2009'
    elif predictions[1] == 176:
        car = 'Spyker C8 Coupe 2009'
    elif predictions[1] == 177:
        car = 'Suzuki Aerio Sedan 2007'
    elif predictions[1] == 178:
        car = 'Suzuki Kizashi Sedan 2012'
    elif predictions[1] == 179:
        car = 'Suzuki SX4 Hatchback 2012'

    elif predictions[1] == 180:
        car = 'Suzuki SX4 Sedan 2012'
    elif predictions[1] == 181:
        car = 'Tesla Model S Sedan 2012'
    elif predictions[1] == 182:
        car = 'Toyota 4Runner SUV 2012'
    elif predictions[1] == 183:
        car = 'Toyota Camry Sedan 2012'
    elif predictions[1] == 184:
        car = 'Toyota Corolla Sedan 2012'
    elif predictions[1] == 185:
        car = 'Toyota Sequoia SUV 2012'
    elif predictions[1] == 186:
        car = 'Volkswagen Beetle Hatchback 2012'
    elif predictions[1] == 187:
        car = 'Volkswagen Golf Hatchback 1991'
    elif predictions[1] == 188:
        car = 'Volkswagen Golf Hatchback 2012'
    elif predictions[1] == 189:
        car = 'Volvo 240 Sedan 1993'

    elif predictions[1] == 190:
        car = 'Volvo C30 Hatchback 2012'
    elif predictions[1] == 191:
        car = 'Volvo XC90 SUV 2007'
    
    return car
        
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
    ################ classifying image ############################
    # imagepath = f'\data/images\{path_in}'
    output_file_path = Image.open(r"C:\Users\HP\PycharmProjects\yolov4-custom-functions-master\detections\detection1.png")
    col2.image(output_file_path)

    imgclassify = cv2.imread(r"C:\Users\HP\PycharmProjects\yolov4-custom-functions-master\detections\detection1.png")
    text1 = CarClassifier(imgclassify)
    # print(text1)
    CarMake = st.text_input("Vehicle Make: ", text1)

    # time.sleep(2)
    
    
    






    # st.write(str(stdout))
    # plateNumber = str(stdout[17:-2])
    # plateNumber = plateNumber[2:-1]
    # st.write(plateNumber)
    