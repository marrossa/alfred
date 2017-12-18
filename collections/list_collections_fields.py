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

collection_fields = discovery.list_collection_fields(config['watson']['environment_id'], config['watson']['prod_collection_id'])
print(json.dumps(collection_fields, indent=2))
