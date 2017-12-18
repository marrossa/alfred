import sys
import os
import json
import configparser
from watson_developer_cloud import DiscoveryV1

# Loads the config file to read the configuration variables
config = configparser.ConfigParser()
config.read('../config.file')

discovery = DiscoveryV1(
  username = config['watson']['username'],
  password = config['watson']['password'],
  version = config['watson']['version']
)

environments = discovery.get_environments()
print(json.dumps(environments, indent=2))

#news_environments = [x for x in environments['environments'] if x['name'] == 'alfred-discovery-1511835303392']
#news_environment_id = news_environments[0]['environment_id']
#print(json.dumps(news_environment_id, indent=2))

#collections = discovery.list_collections(news_environment_id)
#news_collections = [x for x in collections['collections']]
#print(json.dumps(collections, indent=2))

#print(discovery.list_configurations(environment_id=news_environment_id))
#default_config_id = discovery.get_default_configuration_id(environment_id=news_environment_id)
#print(json.dumps(default_config_id, indent=2))

#default_config = discovery.get_configuration(environment_id=news_environment_id, configuration_id=default_config_id)
#print(json.dumps(default_config, indent=2))
