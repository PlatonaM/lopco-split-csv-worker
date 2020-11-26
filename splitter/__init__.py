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


__all__ = ("splitFile", )


from .configuration import conf
import os
import uuid


def splitFile(path, source, column):
    key_file_map = dict()
    out_file = None
    key = None
    with open(os.path.join(path, source), "r") as file:
        first_line = file.readline()
        first_line = first_line.split(conf.delimiter)
        pos = first_line.index(column)
        first_line.remove(column)
        line_count = 0
        for line in file:
            line = line.split(conf.delimiter)
            if not key or key not in line:
                if out_file:
                    out_file.close()
                    key_file_map[key].append(str(line_count))
                    line_count = 0
                key = line[pos]
                key_file_map[key] = [uuid.uuid4().hex]
                out_path = os.path.join(path, key_file_map[key][0])
                out_file = open(out_path, "a+")
                out_file.write(conf.delimiter.join(first_line))
            line.remove(key)
            out_file.write(conf.delimiter.join(line))
            line_count += 1
        key_file_map[key].append(str(line_count))
        out_file.close()
    return key_file_map
