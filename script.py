#python3 script.py <arg1 : prestart or poststart> <arg2: url_endpoint> <arg3: authorization token>
import os,sys,json 
#install requests package if doesn't exist and then import
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests
    
env_var = dict(os.environ)  #collected all the environment variables
env_var['notebookState'] = sys.argv[1]  #appended notebookState at the end of the dictionary
URL = sys.argv[2]   #URL endpoint
token = 'Basic ' + sys.argv[3]  #authorization token
headers = {'content-type': 'application/json','Authorization':token}

result = requests.post(url = URL, data=json.dumps(env_var), headers = headers) #result status stored
if result.status_code == 200:
    print('Success Status Code : ',result.status_code)
else:
    print('Failure Status Code : ',result.status_code)
    print('Response : ',result.text)
