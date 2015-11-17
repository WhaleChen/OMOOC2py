
# code from: http://www.oschina.net/code/snippet_1245006_25187
# Collected by: Whale Chen

import urllib, urllib2
import json

class GeoCoding(object):
        def __init__(self, key =' '):
	    # to set the return 
	    #self.url_para = {'address':'', 'sensor': 'false', 'language': 'zh-CN'}
            self.url_para = {'address':''}
	    self.url = 'http://maps.googleapis.com/maps/api/geocode/json'
	    self.geo_info_list =[]
	
	def get_latlng_by_name(self, geo_name):
	    url_get_geo=self.url +'?' +'address='+geo_name
	    handler =urllib2.urlopen(url_get_geo)
	    resp_data =handler.read()
	    #data_f=json.dumps(resp_data,ensure_ascii=False)
	    #print resp_data
	    resp =json.loads(resp_data)
	    print type(resp)
	    print resp

	    lat = resp['results']['geometry']['location']['lat']
	    print lat
	    if resp['status'] =='ok':
		        #get lat lng and address
			for geo_info in resp['results']:
			        #print(geo_info)
				geo_dict = {'lat': resp['geometry']['location']['lat'],
				            'lng': resp['geometry']['location']['lng'],
			       		    'addr': resp['formatted_address']}
				self.geo_info_list.append(geo_dict)
	    handler.close()
#	    st =self.parse_ret_json(resp_data)
	    return self.geo_info_list
		
#	def parse_ret_json(self, ret_str):
#	        parse_st = False
		# .loads to touch file
#		ret_json =json.loads(ret_str)
#		if ret_json['status'] =='ok':
#		        #get lat lng and address
#			for geo_info in ret_json['results']:
#			        #print(geo_info)
#				geo_dict = {'lat': geo_info['geometry']['location']['lat'],
#				            'lng': geo_info['geometry']['location']['lng'],
#			       		    'addr':geo_info['formatted_address']}
#				self.geo_info_list.append(geo_dict)
#			parse_st =True
#			print(self.geo_info_list)
#               else:
#                       parse_st ==False
#                        print(ret_json['status'])
#                return parse_st

if __name__ =='__main__':
    getData =GeoCoding()
    cityName =raw_input("pls enter the city name in English\n>>")
    test = getData.get_latlng_by_name(cityName)
    print test
 
