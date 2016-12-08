'''
Created on Dec 8, 2016
This program generate the weather data for a random no of cities from a list of cities
The latitude, longitude and elevation are fetched from internet using google api.
Temperature, humidity and pressure are generated randomly with in the defined range.
The weather condition is derived based on the temperature and humidity levels.
@author: Ranjit Gouda
'''
import urllib
import random
import datetime
import json

class WeatherSimulator(object):
    
    #Initialise the class variables
    def __init__(self):
        self.city_list = ['Tokyo','New York Metro','Sao Paulo','Seoul','Milan',
                          'Mexico','Osaka','Manila','Mumbai','Delhi','Jakarta',
                          'Taipei','Kolkata','Cairo','Los Angeles','Karachi',
                          'Rio de Janeiro','Moscow','Shanghai','Paris','Lima',
                          'Istanbul','Nagoya','Beijing','Chicago','Shenzhen',
                          'Essen','Tehran','Bogota','London','Bangkok','Lagos',
                          'Johannesburg','Chennai','Baghdad','Boston','Miami',
                          'Bangalore','Hyderabad','Lahore','Toronto','Madrid',
                          'Tianjin','Kinshasa','Ho Chi Minh City','Santiago',
                          'Buenos Aires','Kuala Lumpur','Singapore','Shenyang',
                          'Dallas','Belo Horizonte','Khartoum','Philadelphia']
        
        self.city_name  = ''
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.cond = ''
        self.ele = ''
        self.lat = 0.0
        self.lon = 0.0
        self.time = ''
    #Function to get the elevation based on lattitude and longitude using Google api  
    def getElevation(self):
        url = 'http://maps.googleapis.com/maps/api/elevation/json?'
        parms = 'locations=%s,%s&sensor=%s' % (self.lat, self.lon, 'false')
        eleurl = url + parms
        eledata = urllib.urlopen(eleurl)
        response = json.loads(eledata.read())
        if (str(response['status']) == 'OK'):
            ele = response['results'][0]['elevation']
        return ele
    
    #Function to get the location and elevation details using google api based on city name   
    def getLocation(self):
        url  = 'http://maps.googleapis.com/maps/api/geocode/json'
        url  = url + '?' + 'address=%s&sensor=%s'%(self.city_name,\
                                                              'false')
        response = urllib.urlopen(url).read()
        data = json.loads(response)
        if(str(data['status']) == 'OK'):
            (self.lat,self.lon) = data['results'][0]['geometry']['location'].\
            values()
            self.ele = self.getElevation()
        return '%.2f,%.2f,%.0f'%(self.lat,self.lon,self.ele)
    
    #Function to get a random temperature in the range of -10 to 40 degree celcius    
    def getTemperature(self):
        t = random.randint(-10,40)
        if( t > 0 ):
            return '+' + str(t)
        else:
            return t

    #Function to get a random humidity levels in the range of 50 to 120 percent
    #relative humidity
    def getHumidity(self):
        return random.randint(50,120)
    
    #Function to get a random pressure in the range of 900 to 1050 
    def getPressure(self):
        return  random.randint(900,1050)
    
    #Function to get a random date and time in ISO format from the year 2015 - 2016 
    def getTime(self):
        return (datetime.datetime.today() - \
                datetime.timedelta(seconds=random.randint(0,63072000))).\
                isoformat()

    #Function to generate the weather conditions based on the temperature,humidity 
    #Print the simulated weather conditions in pipe delimited format.
    #This function will generate report for a random no of cities between 15 to 20 
    def generateWeather(self):
        no_of_cities = random.randint(15,20)  
        for i in range(0,no_of_cities):
            city_no = random.randint(1,30)             
            self.city_name = self.city_list[city_no]            
            self.location = self.getLocation()
            self.humidity = self.getHumidity()
            self.pressure = self.getPressure()
            self.temperature = self.getTemperature()
            self.time = self.getTime()
            self.cond = ''             
            if self.temperature>0 and self.humidity>=95:
                self.cond = 'Rain'
            elif self.temperature>0 and self.humidity<95:
                self.cond = 'Sunny'
            elif self.temperature<0 and self.humidity<95:
                self.cond = 'Snow'
            elif self.temperature<=0 and self.humidity>=95:
                self.cond = 'Snow'
            elif self.temperature==0 and self.humidity<95:
                self.cond = 'Sunny'
            elif self.temperature==0 and self.humidity>95:
                self.cond = 'Rain'
            wthr_cond = [self.city_name,self.location,self.time,self.cond,\
                         self.temperature,self.pressure,self.humidity]
            print '|'.join(map(str,wthr_cond))
             
if __name__ == "__main__":
    c = WeatherSimulator()
    c.generateWeather()
        
