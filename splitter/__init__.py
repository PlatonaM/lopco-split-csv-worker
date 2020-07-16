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


from .configuration import conf
import os
import uuid


def splitFile(path, source, column):
    key_file_map = dict()
    out_file = None
    key = None
    with open(os.path.join(path, source), "r") as file:
        first_line = file.readline()
        pos = first_line.split(conf.delimiter).index(column)
        for line in file:
            if not key or key not in line:
                key = line.split(conf.delimiter)[pos]
                key_file_map[key] = uuid.uuid4().hex
                if out_file:
                    out_file.close()
                out_path = os.path.join(path, key_file_map[key])
                out_file = open(out_path, "a+")
                out_file.write(first_line)
            out_file.write(line)
    return key_file_map
