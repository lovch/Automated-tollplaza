import pandas as pd
import os
import ast
def create(country,filename):
    print('Creating....')
    os.system('alpr -c {} -j {} C:\OpenAlpr\openalpr_64\openalpr.conf\
    > test2.txt'.format(country,filename))
    detect()
def detect():
    print('Detecting....')
    data = []
    dic = {}
    file = open('test2.txt','r')
    contents = file.readlines()
    idx = contents[0].index("candidates")
    clean = contents[0][idx+13:][:-5]
    data = clean.split(',"matches_template":0}')
    cleaned_data = data[0][1:]
    dic = ast.literal_eval('{'+cleaned_data+'}')
    plate = dic['plate']
    output(plate)
def output(plate):
    print('Processing....')
    df = pd.read_csv('dbase.csv')
    z = 0
    for i in df['Number Plate']:
        z+=1
        if i == plate:
            indx = z
    print('Result - \n')
    print(df.iloc[indx-1])
def begin():
    print('Enter Country Code')
    ccode = input()
    print('Enter Image name')
    iname = input()+'.jpg'
    create(ccode,iname)
begin()