

import os
from openmovement.process import OmConvert

source_file = './aa'

base_name = os.path.splitext(source_file)[0]
options = {}

# Nearest-point sampling
options['interpolate_mode'] = 1

# Optionally export accelerometer CSV file (can take a long time)
#options['csv_file'] = base_name + '.csv'

# SVM (no filter)
options['svm_filter'] = 0
options['svm_file'] = base_name + '.svm.csv'

# Wear-time validation
options['wtv_file'] = base_name + '.wtv.csv'

# Run the processing
om = OmConvert()
result = om.execute(source_file, options)
