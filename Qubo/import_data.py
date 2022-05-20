#!/usr/local/bin/python3

import pandas as pd
from .utils import print_step
from .colors import colors
def german_credit_data ():
    
    dataFileNane = "German Credit Data"
    buffer = "Import "+dataFileNane
    print_step(buffer)
    try:
        #first transformed german.data into german.csv
        column_Names = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21"]
        #column_Names = ['Status of existing checking account','Duration in month','Credit history','Purpose','Credit amount','Savings account/bonds','Present employment since','Installment rate in percentage of disposable income','Personal status and sex','Other debtors / guarantors','Present residence since','Property','Age in years','Other installment plans','Housing','Number of existing credits at this bank','Job','Number of people being liable to provide maintenance for','Telephone','foreign worker', 'Good/Bad credit]
        dataframe = pd.read_csv("Qubo/Data_folder/German/german.csv", names=column_Names)
    except:
        print("Import dataframe error")
    return dataframe, dataFileNane

def polish_bankrupcy_data():
    dataFileNane = "Polish Bankrupcy Data"
    buffer = "Import "+dataFileNane
    print_step(buffer)
    try:
        #first transformed german.data into german.csv
        column_Names = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65"]
        #column_Names = ['Status of existing checking account','Duration in month','Credit history','Purpose','Credit amount','Savings account/bonds','Present employment since','Installment rate in percentage of disposable income','Personal status and sex','Other debtors / guarantors','Present residence since','Property','Age in years','Other installment plans','Housing','Number of existing credits at this bank','Job','Number of people being liable to provide maintenance for','Telephone','foreign worker', 'Good/Bad credit]
        dataframe = pd.read_csv("Qubo/Data_folder/Polish_Bankrupcy/5year.csv", names=column_Names)
    except:
        print("Import dataframe error")
    return dataframe, dataFileNane

def australian_credit_data ():
    dataFileNane = "Australian Credit Data"
    buffer = "Import "+dataFileNane
    print_step(buffer)
    try:
        #first transformed german.data into german.csv
        column_Names = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
        #column_Names = ['Status of existing checking account','Duration in month','Credit history','Purpose','Credit amount','Savings account/bonds','Present employment since','Installment rate in percentage of disposable income','Personal status and sex','Other debtors / guarantors','Present residence since','Property','Age in years','Other installment plans','Housing','Number of existing credits at this bank','Job','Number of people being liable to provide maintenance for','Telephone','foreign worker', 'Good/Bad credit]
        dataframe = pd.read_csv("Qubo/Data_folder/Australian/australian.csv", names=column_Names)
    except:
        print("Import dataframe error")
    return dataframe, dataFileNane

def synthetic_Data(n_feature):
    dataFileName = "Synthetic Data with "+ str(n_feature) + " feature"
    buffer = "Import "+dataFileName
    print_step(buffer)
    try:
        #first transformed german.data into german.csv
        path = "Qubo/Data_folder/Synthetic_data/dataset_nf_"+str(n_feature)+".csv"
        #column_Names = ['Status of existing checking account','Duration in month','Credit history','Purpose','Credit amount','Savings account/bonds','Present employment since','Installment rate in percentage of disposable income','Personal status and sex','Other debtors / guarantors','Present residence since','Property','Age in years','Other installment plans','Housing','Number of existing credits at this bank','Job','Number of people being liable to provide maintenance for','Telephone','foreign worker', 'Good/Bad credit]
        dataframe = pd.read_csv(path)
    except:
        print("Import dataframe error")
    return dataframe, dataFileName

def import_noisy_data(n, type):
    dataFileName = ""
    try:
        if(type == '1'):
        #first transformed german.data into german.csv
            path = "Qubo/Data_folder/German/German_dataset_noise_feature_" + n +".csv"
            dataFileName = "German noisy Data with "+ str(n) + " noisy feature"
            
    
        elif(type == '2'):
            path = "Qubo/Data_folder/German/German_dataset_noise_samples_" + str(n) +".csv"
            dataFileName = "German noisy Data with "+ str(n) + " % noisy samples"
        else:
                print(colors.FAIL+"Dataset type doesnt exists, exiting.."+colors.ENDC)
                exit()
        
        buffer = "Import "+dataFileName
        #column_Names = ['Status of existing checking account','Duration in month','Credit history','Purpose','Credit amount','Savings account/bonds','Present employment since','Installment rate in percentage of disposable income','Personal status and sex','Other debtors / guarantors','Present residence since','Property','Age in years','Other installment plans','Housing','Number of existing credits at this bank','Job','Number of people being liable to provide maintenance for','Telephone','foreign worker', 'Good/Bad credit]

        dataframe = pd.read_csv(path)

        print_step(buffer)
    except:
        print("Import dataframe error")
    return dataframe, dataFileName