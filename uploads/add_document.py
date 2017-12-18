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

with open(os.path.join(os.getcwd(), 'resources', 'test-doc1.html')) as fileinfo:
  add_doc = discovery.add_document(config['watson']['environment_id'], config['watson']['test_collection_id'], file_info=fileinfo)
print(json.dumps(add_doc, indent=2))
