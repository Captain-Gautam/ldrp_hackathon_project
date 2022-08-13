#Global declaration Area
symptomsM={}
symptomsF={}
medicines={}

############ Female Symptoms ########################

symptomsF={
    "Heart Disease":["Chest pain", "chest tightness", "chest pressure" ,"chest discomfort (angina)"
                      ,"Shortness of breath",
    "Pain in the neck","Pain in Jaw","Pain in throat","Pain in upper belly area or back"],

    #############
    " Breast Cancer":["New lump in the breast or underarm (armpit)",
                            "Thickening or swelling of part of the breast"
                        "Irritation or dimpling of breast skin",
                        "Redness or flaky skin in the nipple area or the breast",
                        "Pulling in of the nipple or pain in the nipple area"],

    ##############
    "Ovarian and Cervical Cancer":["Abnormal Vaginal Bleeding",
                            "Vaginal Discharge", "Foul Smelling",
                            "Pain During Sexual Intercourse",
                            "Low Back", "Pelvic Pain","Appendix Pain",
                            "Leg Pain"],

    ######################
    "Gynecological Health" : ["Itching",
                "burning", 
                "swelling",
                "rednessor soreness in the vaginal area",
                "Sores or lumps in the genital area"],

    ########################
    "Pregnancy Issues": ["Missed period","Tender and  swollen breasts",
    "Nausea with or without vomiting",
    "Increased urination","fatigue"],

    ######################

    "Autoimmune Diseases":["Fatigue",
                    "Joint pain and swelling",
                    "Skin problems",
                    "Abdominal pain or digestive issues",
                    "Recurring fever",
                    "Swollen glands"],

    #########################

    "Depression and Anxiety":["Loss of interest or enjoyment in your usual activities and hobbies",
                "a sense of hopelessness or pessimism",
                "anger","irritability","restlessness",
                "a lack of energy or a sense of feeling slowed down",
                "chronic fatigue or sleep problems",
                "changes in appetite and weight"],
     "Pneumonia": ["cough", "chest pain", "fever", "sweating", "shaking chills", "breathing problem"],
    "Diarrhoea": ["abdominal cramps", "bloating", "nausea", "vomitting", "fever", "blood", "thirst", "less urination"],
    "Malaria": ["chills", "fever", "sweating", "shivering headache", "pain in abdomen", "fast heart rate", "pallor"],
    "Tuberculosis": ["pain in chest", "cough", "fatigueness", "fever", "loss of appetite", "malaise", "night sweats", "weight loss", "phlegm"],
    "Chickenpox": ["rash on the skin", "scab", "red spots", "fatigue", "fever", "loss of appetite", "headache", "itching", "swollen lymph nodes"],
    "Whooping cough": ["runny nose", "nasal congestion", "sneezing", "fatigue", "vomitting", "watery eyes"],
    "Common Cold": ["runny nose", "sneezing", "loss of smell", "watery eyes", "itchiness", "chest pressure", "headache", "throat irritation", "chills", "fever"],
    "Ear infection": ["ear pain", "fever", "vertigo", "headache", "nausea"],
    "Gastroenteritis": ["pain in abdomen", "Diarrhoea", "stomach cramps", "belching", "gagging", "indigestion", "nausea", "vomiting", "chills", "dehydration", "fatigue", "light-headedness", "loss of appetite", "fast heart rate", "weakness", "weight loss", "less urination"],
    "Influenza (flu)": ["pain in muscles", "cough", "chills", "dehydration", "fatigue", "fever", "flushing", "loss of appetite", "body ache", "sweating", "runny nose", "sneezing", "chest pressure", "headache", "nausea", "shortness of breath"],
     "Strep throat":["Throat pain","Painful swallowing","swollen tonsils","Tiny red spots on roof of the mouth","Fever","Headache","vomiting"],
    "Mononucleosis":["Fatigue","Fever","Swollen lymph nodes in your neck","Swollen tonsils","Headache","Skin rash"],
    "Gastroenteritis":["Watery","Nausea", "vomiting" ,"Stomach cramps","Occasional muscle aches","headache","fever"],
    "Anxiety":["Feeling nervous","restless","panic","increased heart rate","Breathing rapidly","Sweating","Feeling weak"],
    "Asthma":["Shortness of breath","Chest pain","Wheezing","Trouble sleeping","coughing"],
    "Cancer":["Fatigue","Lump under the skin,trouble breathing","Weight changes"],
    "Allergy":["Sneezing","Itching","stuffy nose","swollen eyes"],
    "Gonorrhea":["anal itching", "spots of bright red blood on toilet tissue"],
    "Syphilis":["hair loss", "muscle aches", "fever", "swollen lymph nodes"],
    "HIV":["Fever","Headache","Muscle aches","joint pain","Rash","painful mouth sores","Diarrhea","Weight loss"],
    "Chlamydia":["Painful urination","Painful sexual intercourse","Bleeding between periods and after sex in women"]
}


####################### Male Symptoms  ####################
symptomsM={
    "Strep throat":["Throat pain","Painful swallowing","swollen tonsils","Tiny red spots on roof of the mouth","Fever","Headache","vomiting"],
    "Mononucleosis":["Fatigue","Fever","Swollen lymph nodes in your neck","Swollen tonsils","Headache","Skin rash"],
    "Gastroenteritis":["Watery","Nausea", "vomiting" ,"Stomach cramps","Occasional muscle aches","headache","fever"],
    "Anxiety":["Feeling nervous","restless","panic","increased heart rate","Breathing rapidly","Sweating","Feeling weak"],
    "Asthma":["Shortness of breath","Chest pain","Wheezing","Trouble sleeping","coughing"],
    "Cancer":["Fatigue","Lump under the skin,trouble breathing","Weight changes"],
    "Allergy":["Sneezing","Itching","stuffy nose","swollen eyes"],
    "Gonorrhea":["anal itching", "spots of bright red blood on toilet tissue"],
    "Syphilis":["hair loss", "muscle aches", "fever", "swollen lymph nodes"],
    "HIV":["Fever","Headache","Muscle aches","joint pain","Rash","painful mouth sores","Diarrhea","Weight loss"],
    "Chlamydia":["Painful urination","Testicular pain"],
    "Cancer":["Fatigue",
            "Lump or area of thickening that can be felt under the skin",
            "Weight changes, including unintended loss or gain",
            "Skin changes such as yellowing, darkening or redness of the skin, sores that won't heal, or changes to existing moles",
            "Changes in bowel or bladder habits",
            "Persistent cough or trouble breathing"],

         ########################
    "type 1 Diabetes":["Feeling more thirsty than usual",
            "Urinating a lot",
            "Bed-wetting in children who have never wet the bed during the night",
            "Feeling very hungry",
            "Losing weight without trying",
            "Feeling irritable or having other mood changes",
            "Having blurry vision"],
        ##################
    "type 2 Diabetes":["Increased thirst",
            "Frequent urination",
            "Increased hunger",
            "Unintended weight loss",
            "Fatigue",
            "Blurred vision",
            "Slow-healing sores",
            "Frequent infections"],
    "Erectile dysfunction":["Low self-esteem",
            "Depression",
            "Trouble getting an erection",
            "Trouble keeping an erection",
            "Reduced sexual desire"],
        ###################
    "Low testosterone":["Low sex drive",
            "Decreased sense of well-being",
            "Difficulties with concentration and memory",
            "Moodiness and irritability",
            "Low sperm production",
            "Declining ejaculate volume",
            "Loss of underarm, pubic, and body hair",
            "Loss of muscular strength"],
        ####################
    "Depression and Anxiety":["Loss of interest or enjoyment in your usual activities and hobbies",
                "a sense of hopelessness or pessimism",
                "anger","irritability","restlessness",
                "a lack of energy or a sense of feeling slowed down",
                "chronic fatigue or sleep problems",
                "changes in appetite and weight"],
        #################
    "Heart Disease":["Chest pain", "chest tightness", "chest pressure" ,"chest discomfort (angina)"
                      ,"Shortness of breath",
    "Pain in the neck","Pain in Jaw","Pain in throat","Pain in upper belly area or back"],

     "Pneumonia": ["cough", "chest pain", "fever", "sweating", "shaking chills", "breathing problem"],
    "Diarrhoea": ["abdominal cramps", "bloating", "nausea", "vomitting", "fever", "blood", "thirst", "less urination"],
    "Malaria": ["chills", "fever", "sweating", "shivering headache", "pain in abdomen", "fast heart rate", "pallor"],
    "Tuberculosis": ["pain in chest", "cough", "fatigueness", "fever", "loss of appetite", "malaise", "night sweats", "weight loss", "phlegm"],
    "Chickenpox": ["rash on the skin", "scab", "red spots", "fatigue", "fever", "loss of appetite", "headache", "itching", "swollen lymph nodes"],
    "Whooping cough": ["runny nose", "nasal congestion", "sneezing", "fatigue", "vomitting", "watery eyes"],
    "Common Cold": ["runny nose", "sneezing", "loss of smell", "watery eyes", "itchiness", "chest pressure", "headache", "throat irritation", "chills", "fever"],
    "Ear infection": ["ear pain", "fever", "vertigo", "headache", "nausea"],
    "Gastroenteritis": ["pain in abdomen", "Diarrhoea", "stomach cramps", "belching", "gagging", "indigestion", "nausea", "vomiting", "chills", "dehydration", "fatigue", "light-headedness", "loss of appetite", "fast heart rate", "weakness", "weight loss", "less urination"],
    "Influenza (flu)": ["pain in muscles", "cough", "chills", "dehydration", "fatigue", "fever", "flushing", "loss of appetite", "body ache", "sweating", "runny nose", "sneezing", "chest pressure", "headache", "nausea", "shortness of breath"]
}

##########     Medicines    ################
medicines={
    "Heart Disease":["Benazepril (Lotensin)",
        "Captopril (Capoten)",
        "Enalapril (Vasotec)",
        "Fosinopril (Monopril)",
        "Lisinopril (Prinivil, Zestril)"],
    ####################
    "Depression and Anxiety":["citalopram (Celexa)",
        "escitalopram (Lexapro)",
        "fluoxetine (Prozac)",
        "fluvoxamine (Luvox)",
        "paroxetine (Paxil, Pexeva)",
        "sertraline (Zoloft)",
        "duloxetine (Cymbalta)"],
    ################
    "Low testosterone":["Natesto (testosterone)",
        "Aveed (testosterone undecanoate)",
        "Androderm (testosterone)"],
    #######################
    "type 1 Diabetes":["insulin aspart (NovoLog, FlexPen, Fiasp)",
        "insulin glulisine (Apidra)",
        "insulin lispro (Humalog)",
        "insulin degludec (Tresiba)",
        "insulin detemir (Levemir)",
        "insulin glargine (Lantus)",
        "insulin glargine (Toujeo)"],
    ######################
    "type 2 Diabetes":["acarbose (Precose)",
        "miglitol (Glyset)",
        "nateglinide (Starlix)",
        "repaglinide (Prandin)",
        "repaglinide-metformin (Prandimet)"],
    ##################
    "Erectile dysfunction":["Sildenafil (Viagra)", 
        "vardenafil (Levitra, Staxyn)",
        "tadalafil (Cialis)",
        "avanafil (Stendra)"],
    ######################
    "Diabetes":[],
    ###################
    "Cancer":["BEACOPP",
        "BEAM",
        "Bendamustine (Levact)",
        "Bevacizumab (Avastin)",
        "Bexarotene (Targretin)",
        "Bicalutamide (Casodex)"],
    ##################
    "Autoimmune Diseases":["Prednisone","methylprednisolone","dexamethasone",
        "Colchicine",
        "Hydroxychloroquine (Plaquenil)",
        "Sulfasalazine",
        "Dapsone",
        "Methotrexate"],
    ########################
    "Pregnancy Issues":["Acetaminophen (Tylenol; category B)",
        "Prescription of doctor is more advisable as it will differ from women to women"],
    ####################
    "Gynecological Health":["Clotrimazole",
        "Tioconazole",
        "Miconazole",
        "Clotrimazole"],
    ########################
    "Ovarian and Cervical Cancer":["Alymsys (Bevacizumab)",
        "Avastin (Bevacizumab)",
        "Bevacizumab",
        "Bleomycin Sulfate",
        "Hycamtin (Topotecan Hydrochloride)",
        "Keytruda (Pembrolizumab)",
        "Surgery is the best treatment fot the ovarian cancer"],
    ##########################
     " Breast Cancer":["Abemaciclib",
        "Abraxane", 
        "Ado-Trastuzumab Emtansine",
        "Afinitor (Everolimus)", "Afinitor Disperz",
        "Alpelisib",
        "Anastrozole"],
    "Pneumonia": ["penicillin", "Azithromycin", "Amoxicillin"],
    "Diarrhoea": ["ORS", "loperamide"],
    "Malaria": ["antiparasitic", "Chloroquine, Atovaquone", "Proguanil (Malarone)", "Doxycycline"],
    "Tuberculosis": ["isoniazid INH", "rifampin", "pyrazinamide", "ethambutol"],
    "Chickenpox": ["vaccine", "Acyclovir (zovirax)", "paracetamol", "calamine lotion"],
    "Whooping cough": ["Azithromycin", "clarithromycin", "erythromycin"],
    "Common Cold": ["analgesic", "antihistamine", "anti-inflammatory drug"],
    "Ear infection": ["Analgesic", "anti-inflammatory drug", "Penicillin", "High-dose Amoxicillin", "ear drops"],
    "Gastroenteritis": ["Penicillin", "cephalosporin", "nitroimidazole", "penem", "electrolytes"],
    "Influenza (flu)": ["Cough medicine", "anti-inflammatory drug", "Analgesic", "Antiviral drug", "Oseltamivir", "peramivir"],
     "Strep throat":["Antibiotics","Ibuprofen","Acetaminophen"],
    "Mononucleosis":["no treatment"],
    "Gastroenteritis":["no treatment"],
    "Anxiety":["antidepressants,buspirone,benzodiazepines"],
    "Asthma":["ProAir HFA","Ventolin HFA","Xopenex","nebulizer"],
    "Allergy":["Auvi-Q","EpiPen"],
    "Gonorrhea":["intramuscular ceftriaxone"],
    "Syphilis":["Benzathine penicillin G injection"],
    "HIV":["no treatment"],
    "Chlamydia":["doxycycline,azithromycin"]
}

choice=int(input("1.Male\n2.Female\nEnter Choice"))
symptoms=["rash on the skin", "scab", "red spots", "fatigue", "fever", "loss of appetite", "headache", "itching", "swollen lymph nodes"]
count=[]  
disease_list=list(symptomsM.keys())
c=0                    
if choice == 1:
    for disease in symptomsM.values():   # disease will be a list   
        c=0                 #For every new disease count should be initialized                        
        for temp in symptoms:
            #print(temp)
            for temp1 in disease:
                #print(temp1)
                if temp == temp1:
                    c+=1
                    break
        count.append(c)
#print(count.index(max(count)))      index of disease in the dictionary
#print(len(symptomsM))        # 17 key value pairs are present perfect working
ans_disease=disease_list[count.index(max(count))]
print(ans_disease)
print(medicines[ans_disease])
