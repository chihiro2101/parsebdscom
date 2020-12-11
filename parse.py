import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import random

batdongsan = pd.read_csv("batdongsan.csv")
nhadat = pd.read_csv("alnd_0412.csv")
landber = pd.read_csv("landber_estate.csv")
sampleBDS = batdongsan.head(20)
sampleND = nhadat.head(20)
sampleLand = landber.head(20)


#parse data alonhadat
# dateND = nhadat['date'].values
# floorND = nhadat['số tầng'].values
# bedroomND = nhadat['số phòng ngủ'].values
# bathroomND = nhadat['số nhà vs'].values
# squareND = nhadat['diện tích'].values
# districtND = nhadat['quận'].values
# priceND = nhadat['giá'].values
# nhadatdf = {'date': dateND, 'floor': floorND, 'bedroom': bedroomND, 'bathroom': bathroomND, 'square': squareND, 'district': districtND, 'price': priceND}
# df = pd.DataFrame(nhadatdf)


#parse data batdongsan
dateBDS = []
floorBDS = []
bedroomBDS = []
bathroomBDS = []
squareBDS = []
districtBDS = []
investorBDS = []
priceBDS = []
for index, row in batdongsan.iterrows():
    dateBDS.append(row['time'])
    floorBDS.append(random.randrange(5))

    bed = str(row['bedroom'])
    if len(bed) == 3:
        bedroom = 'NULL'
    else:
        bedroom = int(bed.split(' ')[0])  
    bedroomBDS.append(bedroom)
    
    bath = str(row['toilet'])
    if len(bath) == 3:
        bathroom = 'NULL'
    else:
        bathroom = int(bath.split(' ')[0])  
    bathroomBDS.append(bathroom)     


    squ = str(row['square'])
    if len(squ) == 3:
        sq = 'NULL'
    else:
        sq = float(squ.split(' ')[0])  
    squareBDS.append(sq) 

    price = str(row['price']) #đơn vị triệu VND
    if len(price) == 3:
        gia = 'NULL'
    else:
        gia = price.strip()
        if gia.find(",") != -1:
            gia = gia.replace(",",".")
        if gia.find("triệu/m²") != -1:
            if str(sq) != 'NULL':
                gia = float(gia.split(" ")[0])*sq
            else:
                gia = 'NULL'
        elif gia.find("tỷ") != -1:
            gia = gia.split(' ')[0]
            gia = float(gia.replace(",","."))*1000
        elif gia.find("Thỏa thuận") != -1:
            gia = "NULL"
        else:
            gia = float(gia.split(" ")[0])  

    priceBDS.append(gia)

    dist = str(row['address']).split(',')
    districtBDS.append(dist[-2].strip())
    investorBDS.append(row['project'])

nhadatdf = {'date': dateBDS, 'floor': floorBDS, 'bedroom': bedroomBDS, 'bathroom': bathroomBDS, 'square': squareBDS, 'district': districtBDS, 'investor': investorBDS, 'price': priceBDS}
dfBDS = pd.DataFrame(nhadatdf)
dfBDS.to_csv (r'dfBDS.csv', index = False, header=True)
# import pdb; pdb.set_trace()
print("DONE")