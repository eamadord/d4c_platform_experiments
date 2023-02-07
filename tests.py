import os
import requests
import time
import json

url_base='https://drugs4covid.oeg.fi.upm.es/'

all_info='platform/all'
single_entity='platform/entities'
evidences='platform/evidences'

results={}

SPACCC_dir='./SPACCC/corpus'

for i,file in enumerate(os.listdir(SPACCC_dir)):
    content=open(os.path.join(SPACCC_dir,file)).read()
    ##tests entities
    if i%10==0:
        print('Procesados %d ficheros' %i)
    results[i]={}
    url_req=url_base+all_info
    start_time=time.time()
    try:
        def_res=requests.post(url_req,json={'text':content,'pipeline':'default'})
        time_elapsed_def=time.time()-start_time
        dict_def=json.loads(def_res.text)
        def_results={'time_elapsed':time_elapsed_def,'enfermedades':dict_def['enfermedades'],'medicamentos':dict_def['medicamentos']}
        results[i]['default']=def_results
        start_time=time.time()
        trans_res=requests.post(url_req,json={'text':content,'pipeline':'translate'})
        dict_tr=json.loads(trans_res.text)
        time_elapsed_tr=time.time()-start_time
        tr_results = {'time_elapsed': time_elapsed_tr, 'enfermedades': dict_tr['enfermedades'],
                       'medicamentos': dict_tr['medicamentos']}
        results[i]['translate']=tr_results
    except:
        results[i]=None
