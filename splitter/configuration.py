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


__all__ = ("conf",)


import os


class conf:
    data_cache_path = "/data_cache"
    logger_level = os.getenv("LOGGER_LEVEL", "info")
    worker_instance = os.getenv("WORKER_INSTANCE")
    job_callback_url = os.getenv("JOB_CALLBACK_URL")
    input_file = os.getenv("source_table")
    column = os.getenv("column")
    delimiter = os.getenv("delimiter")
