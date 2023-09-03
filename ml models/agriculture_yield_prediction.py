import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn.metrics as sm
data=pd.read_csv("apy.csv")
#print(data.head)
data = data.drop('Crop_Year',axis=1)
#print(data.head(10))
#print(data.info())
#print(data.isnull().sum())
data = data.dropna()
#print(data.isnull().sum())
#data cleaning completed
data['Area']=data['Area'].astype('int')
data['Production']=data['Production'].astype('int')
#print(data.columns)
#print(data['Crop'].describe())
#print(data['Crop'].value_counts())
cropnames = [data.Crop.unique()]
#print(len(cropnames))
dict_crops = {'Arecanut':1, 'Other Kharif pulses':2, 'Rice':3, 'Banana':4, 'Cashewnut':5,
       'Coconut ':6, 'Dry ginger':7, 'Sugarcane':8, 'Sweet potato':9, 'Tapioca':10,
       'Black pepper':11, 'Dry chillies':12, 'other oilseeds':13, 'Turmeric':14,
       'Maize':15, 'Moong(Green Gram)':16, 'Urad':17, 'Arhar/Tur':18, 'Groundnut':19,
       'Sunflower':20, 'Bajra':21, 'Castor seed':22, 'Cotton(lint)':23, 'Horse-gram':24,
       'Jowar':25, 'Korra':26, 'Ragi':27, 'Tobacco':28, 'Gram':29, 'Wheat':30, 'Masoor':31,
       'Sesamum':32, 'Linseed':33, 'Safflower':34, 'Onion':35, 'other misc. pulses':36,
       'Samai':37, 'Small millets':38, 'Coriander':39, 'Potato':40,
       'Other  Rabi pulses':41, 'Soyabean':42, 'Beans & Mutter(Vegetable)':43,
       'Bhindi':44, 'Brinjal':45, 'Citrus Fruit':46, 'Cucumber':47, 'Grapes':48, 'Mango':49,
       'Orange':50, 'other fibres':51, 'Other Fresh Fruits':52, 'Other Vegetables':53,
       'Papaya':54, 'Pome Fruit':55, 'Tomato':56, 'Mesta':57, 'Cowpea(Lobia)':58,
       'Lemon':59, 'Pome Granet':60, 'Sapota':61, 'Cabbage':62, 'Rapeseed &Mustard':63,
       'Peas  (vegetable)':64, 'Niger seed':65, 'Bottle Gourd':66, 'Varagu':67,
       'Garlic':68, 'Ginger':69, 'Oilseeds total':70, 'Pulses total':71, 'Jute':72,
       'Peas & beans (Pulses)':73, 'Blackgram':74, 'Paddy':75, 'Pineapple':76,
       'Barley':77, 'Sannhamp':78, 'Khesari':79, 'Guar seed':80, 'Moth':81,
       'Other Cereals & Millets':82, 'Cond-spcs other':83, 'Turnip':84, 'Carrot':85,
       'Redish':86, 'Arcanut (Processed)':87, 'Atcanut (Raw)':88,
       'Cashewnut Processed':89, 'Cashewnut Raw':90, 'Cardamom':91, 'Rubber':92,
       'Bitter Gourd':93, 'Drum Stick':94, 'Jack Fruit':95, 'Snak Guard':96, 'Tea':97,
       'Coffee':98, 'Cauliflower':99, 'Other Citrus Fruit':100, 'Water Melon':101,
       'Total foodgrain':102, 'Kapas':103, 'Colocosia':104, 'Lentil':105, 'Bean':106,
       'Jobster':107, 'Perilla':108, 'Rajmash Kholar':109, 'Ricebean (nagadal)':110,
       'Ash Gourd':111, 'Beet Root':112, 'Lab-Lab':113, 'Ribed Guard':114, 'Yam':115,
       'Pump Kin':116, 'Apple':117, 'Peach':118, 'Pear':119, 'Plums':120, 'Litchi':121, 'Ber':122,
       'Other Dry Fruit':123, 'Jute & mesta':124}
#print(len(dict_crops))
data['Crop']=data['Crop'].map(dict_crops)
state_names=[data.State_Name.unique()]
#print(state_names)
dict_states = {'Andaman and Nicobar Islands':1, 'Andhra Pradesh':2,
       'Arunachal Pradesh':3, 'Assam':4, 'Bihar':5, 'Chandigarh':6,
       'Chhattisgarh':7, 'Dadra and Nagar Haveli':8, 'Goa':9, 'Gujarat':10,
       'Haryana':11, 'Himachal Pradesh':12, 'Jammu and Kashmir ':13, 'Jharkhand':14,
       'Karnataka':15, 'Kerala':16, 'Madhya Pradesh':17, 'Maharashtra':18, 'Manipur':19,
       'Meghalaya':20, 'Mizoram':21, 'Nagaland':22, 'Odisha':23, 'Puducherry':24,
       'Punjab':25, 'Rajasthan':26, 'Sikkim':27, 'Tamil Nadu':28, 'Telangana ':29,
       'Tripura':30, 'Uttar Pradesh':31, 'Uttarakhand':32, 'West Bengal':33}
data['State_Name']=data['State_Name'].map(dict_states)
#print(data.head(10))

district_names=[data.District_Name.unique()]
#print(len(data.District_Name.unique()))
#print(district_names)
dict_districts={'NICOBARS': 1, 'NORTH AND MIDDLE ANDAMAN': 2, 'SOUTH ANDAMANS': 3, 'ANANTAPUR': 4, 'CHITTOOR': 5, 'EAST GODAVARI': 6, 'GUNTUR': 7, 'KADAPA': 8, 'KRISHNA': 9, 'KURNOOL': 10, 'PRAKASAM': 11, 'SPSR NELLORE': 12, 'SRIKAKULAM': 13, 'VISAKHAPATANAM': 14, 'VIZIANAGARAM': 15, 'WEST GODAVARI': 16, 'ANJAW': 17, 'CHANGLANG': 18, 'DIBANG VALLEY': 19, 'EAST KAMENG': 20, 'EAST SIANG': 21, 'KURUNG KUMEY': 22, 'LOHIT': 23, 'LONGDING': 24, 'LOWER DIBANG VALLEY': 25, 'LOWER SUBANSIRI': 26, 'NAMSAI': 27, 'PAPUM PARE': 28, 'TAWANG': 29, 'TIRAP': 30, 'UPPER SIANG': 31, 'UPPER SUBANSIRI': 32, 'WEST KAMENG': 33, 'WEST SIANG': 34, 'BAKSA': 35, 'BARPETA': 36, 'BONGAIGAON': 37, 'CACHAR': 38, 'CHIRANG': 39, 'DARRANG': 40, 'DHEMAJI': 41, 'DHUBRI': 42, 'DIBRUGARH': 43, 'DIMA HASAO': 44, 'GOALPARA': 45, 'GOLAGHAT': 46, 'HAILAKANDI': 47, 'JORHAT': 48, 'KAMRUP': 49, 'KAMRUP METRO': 50, 'KARBI ANGLONG': 51, 'KARIMGANJ': 52, 'KOKRAJHAR': 53, 'LAKHIMPUR': 54, 'MARIGAON': 55, 'NAGAON': 56, 'NALBARI': 57, 'SIVASAGAR': 58, 'SONITPUR': 59, 'TINSUKIA': 60, 'UDALGURI': 61, 'ARARIA': 62, 'ARWAL': 63, 'AURANGABAD': 64, 'BANKA': 65, 'BEGUSARAI': 66, 'BHAGALPUR': 67, 'BHOJPUR': 68, 'BUXAR': 69, 'DARBHANGA': 70, 'GAYA': 71, 'GOPALGANJ': 72, 'JAMUI': 73, 'JEHANABAD': 74, 'KAIMUR (BHABUA)': 75, 'KATIHAR': 76, 'KHAGARIA': 77, 'KISHANGANJ': 78, 'LAKHISARAI': 79, 'MADHEPURA': 80, 'MADHUBANI': 81, 'MUNGER': 82, 'MUZAFFARPUR': 83, 'NALANDA': 84, 'NAWADA': 85, 'PASHCHIM CHAMPARAN': 86, 'PATNA': 87, 'PURBI CHAMPARAN': 88, 'PURNIA': 89, 'ROHTAS': 90, 'SAHARSA': 91, 'SAMASTIPUR': 92, 'SARAN': 93, 'SHEIKHPURA': 94, 'SHEOHAR': 95, 'SITAMARHI': 96, 'SIWAN': 97, 'SUPAUL': 98, 'VAISHALI': 99, 'CHANDIGARH': 100, 'BALOD': 101, 'BALODA BAZAR': 102, 'BALRAMPUR': 103, 'BASTAR': 104, 'BEMETARA': 105, 'BIJAPUR': 106, 'BILASPUR': 107, 'DANTEWADA': 108, 'DHAMTARI': 109, 'DURG': 110, 'GARIYABAND': 111, 'JANJGIR-CHAMPA': 112, 'JASHPUR': 113, 'KABIRDHAM': 114, 'KANKER': 115, 'KONDAGAON': 116, 'KORBA': 117, 'KOREA': 118, 'MAHASAMUND': 119, 'MUNGELI': 120, 'NARAYANPUR': 121, 'RAIGARH': 122, 'RAIPUR': 123, 'RAJNANDGAON': 124, 'SUKMA': 125, 'SURAJPUR': 126, 'SURGUJA': 127, 'DADRA AND NAGAR HAVELI': 128, 'NORTH GOA': 129, 'SOUTH GOA': 130, 'AHMADABAD': 131, 'AMRELI': 132, 'ANAND': 133, 'BANAS KANTHA': 134, 'BHARUCH': 135, 'BHAVNAGAR': 136, 'DANG': 137, 'DOHAD': 138, 'GANDHINAGAR': 139, 'JAMNAGAR': 140, 'JUNAGADH': 141, 'KACHCHH': 142, 'KHEDA': 143, 'MAHESANA': 144, 'NARMADA': 145, 'NAVSARI': 146, 'PANCH MAHALS': 147, 'PATAN': 148, 'PORBANDAR': 149, 'RAJKOT': 150, 'SABAR KANTHA': 151, 'SURAT': 152, 'SURENDRANAGAR': 153, 'TAPI': 154, 'VADODARA': 155, 'VALSAD': 156, 'AMBALA': 157, 'BHIWANI': 158, 'FARIDABAD': 159, 'FATEHABAD': 160, 'GURGAON': 161, 'HISAR': 162, 'JHAJJAR': 163, 'JIND': 164, 'KAITHAL': 165, 'KARNAL': 166, 'KURUKSHETRA': 167, 'MAHENDRAGARH': 168, 'MEWAT': 169, 'PALWAL': 170, 'PANCHKULA': 171, 'PANIPAT': 172, 'REWARI': 173, 'ROHTAK': 174, 'SIRSA': 175, 'SONIPAT': 176, 'YAMUNANAGAR': 177, 'CHAMBA': 178, 'HAMIRPUR': 179, 'KANGRA': 180, 'KINNAUR': 181, 'KULLU': 182, 'LAHUL AND SPITI': 183, 'MANDI': 184, 'SHIMLA': 185, 'SIRMAUR': 186, 'SOLAN': 187, 'UNA': 188, 'ANANTNAG': 189, 'BADGAM': 190, 'BANDIPORA': 191, 'BARAMULLA': 192, 'DODA': 193, 'GANDERBAL': 194, 'JAMMU': 195, 'KARGIL': 196, 'KATHUA': 197, 'KISHTWAR': 198, 'KULGAM': 199, 'KUPWARA': 200, 'LEH LADAKH': 201, 'POONCH': 202, 'PULWAMA': 203, 'RAJAURI': 204, 'RAMBAN': 205, 'REASI': 206, 'SAMBA': 207, 'SHOPIAN': 208, 'SRINAGAR': 209, 'UDHAMPUR': 210, 'BOKARO': 211, 'CHATRA': 212, 'DEOGHAR': 213, 'DHANBAD': 214, 'DUMKA': 215, 'EAST SINGHBUM': 216, 'GARHWA': 217, 'GIRIDIH': 218, 'GODDA': 219, 'GUMLA': 220, 'HAZARIBAGH': 221, 'JAMTARA': 222, 'KHUNTI': 223, 'KODERMA': 224, 'LATEHAR': 225, 'LOHARDAGA': 226, 'PAKUR': 227, 'PALAMU': 228, 'RAMGARH': 229, 'RANCHI': 230, 'SAHEBGANJ': 231, 'SARAIKELA KHARSAWAN': 232, 'SIMDEGA': 233, 'WEST SINGHBHUM': 234, 'BAGALKOT': 235, 'BANGALORE RURAL': 236, 'BELGAUM': 237, 'BELLARY': 238, 'BENGALURU URBAN': 239, 'BIDAR': 240, 'CHAMARAJANAGAR': 241, 'CHIKBALLAPUR': 242, 'CHIKMAGALUR': 243, 'CHITRADURGA': 244, 'DAKSHIN KANNAD': 245, 'DAVANGERE': 246, 'DHARWAD': 247, 'GADAG': 248, 'GULBARGA': 249, 'HASSAN': 250, 'HAVERI': 251, 'KODAGU': 252, 'KOLAR': 253, 'KOPPAL': 254, 'MANDYA': 255, 'MYSORE': 256, 'RAICHUR': 257, 'RAMANAGARA': 258, 'SHIMOGA': 259, 'TUMKUR': 260, 'UDUPI': 261, 'UTTAR KANNAD': 262, 'YADGIR': 263, 'ALAPPUZHA': 264, 'ERNAKULAM': 265, 'IDUKKI': 266, 'KANNUR': 267, 'KASARAGOD': 268, 'KOLLAM': 269, 'KOTTAYAM': 270, 'KOZHIKODE': 271, 'MALAPPURAM': 272, 'PALAKKAD': 273, 'PATHANAMTHITTA': 274, 'THIRUVANANTHAPURAM': 275, 'THRISSUR': 276, 'WAYANAD': 277, 'AGAR MALWA': 278, 'ALIRAJPUR': 279, 'ANUPPUR': 280, 'ASHOKNAGAR': 281, 'BALAGHAT': 282, 'BARWANI': 283, 'BETUL': 284, 'BHIND': 285, 'BHOPAL': 286, 'BURHANPUR': 287, 'CHHATARPUR': 288, 'CHHINDWARA': 289, 'DAMOH': 290, 'DATIA': 291, 'DEWAS': 292, 'DHAR': 293, 'DINDORI': 294, 'GUNA': 295, 'GWALIOR': 296, 'HARDA': 297, 'HOSHANGABAD': 298, 'INDORE': 299, 'JABALPUR': 300, 'JHABUA': 301, 'KATNI': 302, 'KHANDWA': 303, 'KHARGONE': 304, 'MANDLA': 305, 'MANDSAUR': 306, 'MORENA': 307, 'NARSINGHPUR': 308, 'NEEMUCH': 309, 'PANNA': 310, 'RAISEN': 311, 'RAJGARH': 312, 'RATLAM': 313, 'REWA': 314, 'SAGAR': 315, 'SATNA': 316, 'SEHORE': 317, 'SEONI': 318, 'SHAHDOL': 319, 'SHAJAPUR': 320, 'SHEOPUR': 321, 'SHIVPURI': 322, 'SIDHI': 323, 'SINGRAULI': 324, 'TIKAMGARH': 325, 'UJJAIN': 326, 'UMARIA': 327, 'VIDISHA': 328, 'AHMEDNAGAR': 329, 'AKOLA': 330, 'AMRAVATI': 331, 'BEED': 332, 'BHANDARA': 333, 'BULDHANA': 334, 'CHANDRAPUR': 335, 'DHULE': 336, 'GADCHIROLI': 337, 'GONDIA': 338, 'HINGOLI': 339, 'JALGAON': 340, 'JALNA': 341, 'KOLHAPUR': 342, 'LATUR': 343, 'MUMBAI': 344, 'NAGPUR': 345, 'NANDED': 346, 'NANDURBAR': 347, 'NASHIK': 348, 'OSMANABAD': 349, 'PALGHAR': 350, 'PARBHANI': 351, 'PUNE': 352, 'RAIGAD': 353, 'RATNAGIRI': 354, 'SANGLI': 355, 'SATARA': 356, 'SINDHUDURG': 357, 'SOLAPUR': 358, 'THANE': 359, 'WARDHA': 360, 'WASHIM': 361, 'YAVATMAL': 362, 'BISHNUPUR': 363, 'CHANDEL': 364, 'CHURACHANDPUR': 365, 'IMPHAL EAST': 366, 'IMPHAL WEST': 367, 'SENAPATI': 368, 'TAMENGLONG': 369, 'THOUBAL': 370, 'UKHRUL': 371, 'EAST GARO HILLS': 372, 'EAST JAINTIA HILLS': 373, 'EAST KHASI HILLS': 374, 'NORTH GARO HILLS': 375, 'RI BHOI': 376, 'SOUTH GARO HILLS': 377, 'SOUTH WEST GARO HILLS': 378, 'SOUTH WEST KHASI HILLS': 379, 'WEST GARO HILLS': 380, 'WEST JAINTIA HILLS': 381, 'WEST KHASI HILLS': 382, 'AIZAWL': 383, 'CHAMPHAI': 384, 'KOLASIB': 385, 'LAWNGTLAI': 386, 'LUNGLEI': 387, 'MAMIT': 388, 'SAIHA': 389, 'SERCHHIP': 390, 'DIMAPUR': 391, 'KIPHIRE': 392, 'KOHIMA': 393, 'LONGLENG': 394, 'MOKOKCHUNG': 395, 'MON': 396, 'PEREN': 397, 'PHEK': 398, 'TUENSANG': 399, 'WOKHA': 400, 'ZUNHEBOTO': 401, 'ANUGUL': 402, 'BALANGIR': 403, 'BALESHWAR': 404, 'BARGARH': 405, 'BHADRAK': 406, 'BOUDH': 407, 'CUTTACK': 408, 'DEOGARH': 409, 'DHENKANAL': 410, 'GAJAPATI': 411, 'GANJAM': 412, 'JAGATSINGHAPUR': 413, 'JAJAPUR': 414, 'JHARSUGUDA': 415, 'KALAHANDI': 416, 'KANDHAMAL': 417, 'KENDRAPARA': 418, 'KENDUJHAR': 419, 'KHORDHA': 420, 'KORAPUT': 421, 'MALKANGIRI': 422, 'MAYURBHANJ': 423, 'NABARANGPUR': 424, 'NAYAGARH': 425, 'NUAPADA': 426, 'PURI': 427, 'RAYAGADA': 428, 'SAMBALPUR': 429, 'SONEPUR': 430, 'SUNDARGARH': 431, 'KARAIKAL': 432, 'MAHE': 433, 'PONDICHERRY': 434, 'YANAM': 435, 'AMRITSAR': 436, 'BARNALA': 437, 'BATHINDA': 438, 'FARIDKOT': 439, 'FATEHGARH SAHIB': 440, 'FAZILKA': 441, 'FIROZEPUR': 442, 'GURDASPUR': 443, 'HOSHIARPUR': 444, 'JALANDHAR': 445, 'KAPURTHALA': 446, 'LUDHIANA': 447, 'MANSA': 448, 'MOGA': 449, 'MUKTSAR': 450, 'NAWANSHAHR': 451, 'PATHANKOT': 452, 'PATIALA': 453, 'RUPNAGAR': 454, 'S.A.S NAGAR': 455, 'SANGRUR': 456, 'TARN TARAN': 457, 'AJMER': 458, 'ALWAR': 459, 'BANSWARA': 460, 'BARAN': 461, 'BARMER': 462, 'BHARATPUR': 463, 'BHILWARA': 464, 'BIKANER': 465, 'BUNDI': 466, 'CHITTORGARH': 467, 'CHURU': 468, 'DAUSA': 469, 'DHOLPUR': 470, 'DUNGARPUR': 471, 'GANGANAGAR': 472, 'HANUMANGARH': 473, 'JAIPUR': 474, 'JAISALMER': 475, 'JALORE': 476, 'JHALAWAR': 477, 'JHUNJHUNU': 478, 'JODHPUR': 479, 'KARAULI': 480, 'KOTA': 481, 'NAGAUR': 482, 'PALI': 483, 'PRATAPGARH': 484, 'RAJSAMAND': 485, 'SAWAI MADHOPUR': 486, 'SIKAR': 487, 'SIROHI': 488, 'TONK': 489, 'UDAIPUR': 490, 'EAST DISTRICT': 491, 'NORTH DISTRICT': 492, 'SOUTH DISTRICT': 493, 'WEST DISTRICT': 494, 'ARIYALUR': 495, 'COIMBATORE': 496, 'CUDDALORE': 497, 'DHARMAPURI': 498, 'DINDIGUL': 499, 'ERODE': 500, 'KANCHIPURAM': 501, 'KANNIYAKUMARI': 502, 'KARUR': 503, 'KRISHNAGIRI': 504, 'MADURAI': 505, 'NAGAPATTINAM': 506, 'NAMAKKAL': 507, 'PERAMBALUR': 508, 'PUDUKKOTTAI': 509, 'RAMANATHAPURAM': 510, 'SALEM': 511, 'SIVAGANGA': 512, 'THANJAVUR': 513, 'THE NILGIRIS': 514, 'THENI': 515, 'THIRUVALLUR': 516, 'THIRUVARUR': 517, 'TIRUCHIRAPPALLI': 518, 'TIRUNELVELI': 519, 'TIRUPPUR': 520, 'TIRUVANNAMALAI': 521, 'TUTICORIN': 522, 'VELLORE': 523, 'VILLUPURAM': 524, 'VIRUDHUNAGAR': 525, 'ADILABAD': 526, 'HYDERABAD': 527, 'KARIMNAGAR': 528, 'KHAMMAM': 529, 'MAHBUBNAGAR': 530, 'MEDAK': 531, 'NALGONDA': 532, 'NIZAMABAD': 533, 'RANGAREDDI': 534, 'WARANGAL': 535, 'DHALAI': 536, 'GOMATI': 537, 'KHOWAI': 538, 'NORTH TRIPURA': 539, 'SEPAHIJALA': 540, 'SOUTH TRIPURA': 541, 'UNAKOTI': 542, 'WEST TRIPURA': 543, 'AGRA': 544, 'ALIGARH': 545, 'ALLAHABAD': 546, 'AMBEDKAR NAGAR': 547, 'AMETHI': 548, 'AMROHA': 549, 'AURAIYA': 550, 'AZAMGARH': 551, 'BAGHPAT': 552, 'BAHRAICH': 553, 'BALLIA': 554, 'BANDA': 555, 'BARABANKI': 556, 'BAREILLY': 557, 'BASTI': 558, 'BIJNOR': 559, 'BUDAUN': 560, 'BULANDSHAHR': 561, 'CHANDAULI': 562, 'CHITRAKOOT': 563, 'DEORIA': 564, 'ETAH': 565, 'ETAWAH': 566, 'FAIZABAD': 567, 'FARRUKHABAD': 568, 'FATEHPUR': 569, 'FIROZABAD': 570, 'GAUTAM BUDDHA NAGAR': 571, 'GHAZIABAD': 572, 'GHAZIPUR': 573, 'GONDA': 574, 'GORAKHPUR': 575, 'HAPUR': 576, 'HARDOI': 577, 'HATHRAS': 578, 'JALAUN': 579, 'JAUNPUR': 580, 'JHANSI': 581, 'KANNAUJ': 582, 'KANPUR DEHAT': 583, 'KANPUR NAGAR': 584, 'KASGANJ': 585, 'KAUSHAMBI': 586, 'KHERI': 587, 'KUSHI NAGAR': 588, 'LALITPUR': 589, 'LUCKNOW': 590, 'MAHARAJGANJ': 591, 'MAHOBA': 592, 'MAINPURI': 593, 'MATHURA': 594, 'MAU': 595, 'MEERUT': 596, 'MIRZAPUR': 597, 'MORADABAD': 598, 'MUZAFFARNAGAR': 599, 'PILIBHIT': 600, 'RAE BARELI': 601, 'RAMPUR': 602, 'SAHARANPUR': 603, 'SAMBHAL': 604, 'SANT KABEER NAGAR': 605, 'SANT RAVIDAS NAGAR': 606, 'SHAHJAHANPUR': 607, 'SHAMLI': 608, 'SHRAVASTI': 609, 'SIDDHARTH NAGAR': 610, 'SITAPUR': 611, 'SONBHADRA': 612, 'SULTANPUR': 613, 'UNNAO': 614, 'VARANASI': 615, 'ALMORA': 616, 'BAGESHWAR': 617, 'CHAMOLI': 618, 'CHAMPAWAT': 619, 'DEHRADUN': 620, 'HARIDWAR': 621, 'NAINITAL': 622, 'PAURI GARHWAL': 623, 'PITHORAGARH': 624, 'RUDRA PRAYAG': 625, 'TEHRI GARHWAL': 626, 'UDAM SINGH NAGAR': 627, 'UTTAR KASHI': 628, '24 PARAGANAS NORTH': 629, '24 PARAGANAS SOUTH': 630, 'BANKURA': 631, 'BARDHAMAN': 632, 'BIRBHUM': 633, 'COOCHBEHAR': 634, 'DARJEELING': 635, 'DINAJPUR DAKSHIN': 636, 'DINAJPUR UTTAR': 637, 'HOOGHLY': 638, 'HOWRAH': 639, 'JALPAIGURI': 640, 'MALDAH': 641, 'MEDINIPUR EAST': 642, 'MEDINIPUR WEST': 643, 'MURSHIDABAD': 644, 'NADIA': 645, 'PURULIA': 646}
#print(len(dict_districts))
data['District_Name']=data['District_Name'].map(dict_districts)
#print(data.head(10))

season_names=[data.Season.unique()]
#print(season_names)
dict_seasons={'Kharif     ':1, 'Whole Year ':2, 'Autumn     ':3, 'Rabi       ':4,
       'Summer     ':5, 'Winter     ':6}
data['Season']=data['Season'].map(dict_seasons)
#print(data.head(10))


Y=data.Production
X=data.drop('Production',axis=1)
#print(X)
#print(Y)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,random_state=0)


#Shape

from sklearn.ensemble import RandomForestRegressor
model1 = RandomForestRegressor(n_estimators=100)

# from sklearn.linear_model import LinearRegression
# model2=LinearRegression()

model1.fit(X_train,Y_train)
# model2.fit(X_train,Y_train)

Y_predict1=model1.predict(X_test)
# Y_predict2=model2.predict(X_test)

accurancy = sm.r2_score(Y_test,Y_predict1)
#print(accurancy)
# accurancy = sm.r2_score(Y_test,Y_predict2)
#print(accurancy)

# import joblib
# joblib.dump(model1,'fianl_pickle_mdl.pkl')

# final_mdl=joblib.load('fianl_pickle_mdl.pkl')
# pred=final_mdl.predict(X_test)
# acc=sm.r2_score(Y_test,pred)
print(accurancy)








