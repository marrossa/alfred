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

new_collection = discovery.create_collection(config['watson']['environment_id'], 'TextFiles', description='This collection contains the text files from the audios', configuration_id='9b06cc80-83de-49a1-a374-3a07840a64b5', language='es')
print(json.dumps(new_collection, indent=2))
