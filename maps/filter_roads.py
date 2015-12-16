import json
from pprint import pprint

types = []
with open('delhi_faridabad_roads_of_interest.json') as json_data:
    d = json.load(json_data)
    print d.keys()
    print len(d['features'])
    for feature in d['features']:
    	if feature['properties']['type'] not in types:
    		types.append(feature['properties']['type'])
    print types
    features = [feature for feature in d['features'] if feature['properties']['type'] not in ['tertiary','tertiary_link','secondary_link','primary_link','trunk_link']]
    d['features'] = features
    with open('delhi_major_roads.json', 'w') as outfile:
    	json.dump(d, outfile)