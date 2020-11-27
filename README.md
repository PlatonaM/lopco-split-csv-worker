#### Description

    {
        "name": "Split CSV",
        "image": "platonam/lopco-split-csv-worker:dev",
        "data_cache_path": "/data_cache",
        "description": "Split a Comma-Separated Values file into multiple unique files.",
        "configs": {
            "column": null,
            "delimiter": null
        },
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
        }
    }
