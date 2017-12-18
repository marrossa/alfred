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

new_name = discovery.update_environment('386aca79-3773-4409-a3a6-303c8b8c9ed7', '2017-11-07', 'Alfred_environment', 'Dev environment for Alfred Project')

print(json.dumps(new_name, indent=2))
