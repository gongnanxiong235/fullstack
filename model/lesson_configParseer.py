import configparser
import os

class ConfigUtil:
    BADR_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('BADR_DIR',BADR_DIR)
    def __init__(self,config=configparser.ConfigParser(),address=BADR_DIR):
        self.config=config
        self.address=address
    def add(self,config_name='config.ini',**kwargs):
        config_address=os.sep.join([self.address,config_name])
        print(config_address)
        for key,value in kwargs.items():
            self.config[key]=value
        with open(config_address,'w',encoding='utf-8') as file:
            self.config.write(file)

    def read_config(self,type_key,key,config_name='config.ini'):
        self.config.read(os.sep.join([self.address,config_name]),encoding='utf-8')
        return self.config[type_key][key]
    def read_config_database(self,key):
        return self.read_config('DATABASE',key)




# ConfigUtil().add(**{'DATABASE':{'url':'url'}})
# print(ConfigUtil().read_config('DATABASE','url'))
# print(ConfigUtil().read_config_database('url'))


