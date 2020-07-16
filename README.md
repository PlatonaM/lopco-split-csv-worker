#### Description

    {
        "name": "Split on unique",
        "description": null,
        "image": "split-on-unique-worker",
        "data_cache_path": "/data_cache",
        "input": {
            "type": "single",
            "fields": [
                {
                    "name": "source_table",
                    "media_type": "text/csv",
                    "is_file": true
                }
            ]
        },
        "output": {
            "type": "multiple",
            "fields": [
                {
                    "name": "unique_id",
                    "media_type": "text/plain",
                    "is_file": false
                },
                {
                    "name": "result_table",
                    "media_type": "text/csv",
                    "is_file": true
                }
            ]
        },
        "configs": {
            "column": null,
            "delimiter": null
        }
    }
