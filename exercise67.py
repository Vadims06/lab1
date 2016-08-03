import yaml
import yson
from pprint import pprint as pp
with open('some_file.json') as f:
	new_list_j = json.load(f)
with open('some_file.yml') as f:
	new_list_y = jaml.load(f)
pp('JSON:')
pp(new_list_j)
pp('YAML:')
pp(new_list_y)
