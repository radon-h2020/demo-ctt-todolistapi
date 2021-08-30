from jinja2 import Template
import os
from zipfile import ZipFile
from aggregate import Aggregator

config_file_name: str = 'configuration.ini'
config_file_template: str = '''[Configuration]
LOAD={{ load }}
TEST_NAME=todolist-{{ set }}-{{ load }}
TEST_SET_NAME={{ set }}
PROJECT_NAME=todolist
TIMESTAMP=1622559907.296052
'''

sets = ['scaled', 'fixed']
loads = ['001', '010', '020', '030', '040', '050', '060', '070', '080', '090', '100']
test_location = {}
tm = Template(config_file_template)

for test_set in sets:
    for test_load in loads:
        config = tm.render(set=test_set, load=test_load)
        test_key = f'todolist-{test_set}-{test_load}'
        dir_name = os.path.join('/tmp', test_key)
        test_location[test_key] = dir_name
        os.makedirs(dir_name, exist_ok=True)
        with open(os.path.join(dir_name, 'configuration.ini'), 'w') as conf_out:
            conf_out.writelines(config)

source_file = 'sample_results.jtl'
target_file = 'result_stats.csv'
zip_dir = '/tmp/todolist'
for key, value in test_location.items():
    with ZipFile(os.path.join(zip_dir, f'{key}.zip'), 'r') as zipObj:
        zipObj.extractall(value)
    source_path = os.path.join(value, source_file)
    target_path = os.path.join(value, target_file)
    # Cutoff
    Aggregator(source_path).write_file(target_path)
