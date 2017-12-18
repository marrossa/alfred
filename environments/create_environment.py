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

response = discovery.create_environment(
  name="AlfredFiles",
  description="In this environment we will update all the necessary files to get Alfred project running",
  size=1
)

print(json.dumps(response, indent=2))
