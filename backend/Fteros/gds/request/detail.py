import time
import os
from os import chdir
import pandas as pd
from .reservation import Itinerary


class Segment():

    def __init__(self):

        #Declare a varaiable for today's date
        self.days = time.strftime('%Y%m%d',time.localtime())

    def get_segment(self,file_name) :

        chdir("/home/cosmo/reservation/gds/folder_xml/folder_Q70")
        if os.path.exists(self.days):
            chdir(self.days)
            files= os.listdir("/home/cosmo/reservation/gds/folder_xml/folder_Q70/"+self.days)
            files_liste = []
            for i in files:
                files_liste.append(os.path.splitext(os.path.basename(i))[0])
            if file_name in files_liste:
                with open(file_name+".xml","r") as f:data=f.read()
                airline=Itinerary().airline_list(data)
                fligthno=Itinerary().flight_number_list(data) 
                origin=Itinerary().origin_city_list(data)
                destination=Itinerary().destination_city_list(data)
                departure = Itinerary().departure_datetime_list(data)
                arrival = Itinerary().arrival_datetime_list(data)
                status_list=Itinerary().segment_status_list(data)
                list_detail = []
                try:
                    for index, value in enumerate(status_list):
                        data = {'airline':airline[index],'fligthno':fligthno[index],'origin':origin[index],'destination':destination[index],'departure':departure[index],'arrival':arrival[index],'status_list':value}
                        list_detail.append(data)
                    return list_detail
                except:
                    return  list_detail

                
