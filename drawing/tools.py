
import requests
import csv
from io import StringIO
import password

class Site(object):
    def __init__(self,name,county,aqi):
        super().__init__()
        self.site_name = name
        self.county = county
        try:
            self.aqi = int(aqi)
        except:
            self.aqi =999

    def __repr__(self):
        return f"站點:{self.site_name},城市:{self.county},aqi:{self.aqi}"



    '''
    @classmethod
    def download_aqi(cls) ->list:
        import requests
        response = requests.get(f'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={cls.API_KEY}&limit=1000&sort=ImportDate desc&format=CSV')

        if response.ok:
            #print(response.text)
            #file = open('./lesson17/aqi.csv',mode='w',encoding='utf-8')
            #file.write(response.text)
            #file.close()
            file = StringIO(response.text,newline='')
            csvReader = csv.reader(file)
            next(csvReader)
            dataList = []
            for item in csvReader:
                site = Site(item[0],item[1],item[2])
                dataList.append(site)
            return dataList
    

           
            
            #file.close()

        else:
            raise Exception("下載失敗")
    '''
class Taiwan_AQI(list):
    def __init__(self):
        super().__init__()
        

        response = requests.get(f'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={password.API_KEY}&limit=1000&sort=ImportDate desc&format=CSV')

        if response.ok:
            file = StringIO(response.text,newline='')
            csvReader = csv.reader(file)
            next(csvReader)
            for item in csvReader:
                if item[2] != 999:
                    site = Site(item[0],item[1],item[2])
                    self.append(site)
        else:
            raise Exception("下載失敗")
        
    def get_bad(self, n=3):
        sorted_aqi =sorted(self,key=lambda site:site.aqi)
        return sorted_aqi[-n:]
    
    def get_better(self,n=3):
        sorted_aqi = sorted(self,key=lambda site:site.aqi)
        return sorted_aqi[:n]