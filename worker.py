"""
   Copyright 2020 InfAI (CC SES)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from splitter.configuration import conf
from splitter import splitFile
import requests


file_map = splitFile(conf.data_cache_path, conf.input_file, conf.column)

resp = requests.post(
    conf.job_callback_url,
    json={
        conf.worker_instance: [{"unique_id": key, "result_table": value[0], "line_count": value[1]} for key, value in file_map.items()]
    }
)
