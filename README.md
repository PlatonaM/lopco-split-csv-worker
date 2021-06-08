## lopco-split-csv-worker

Split a CSV file into multiple unique CSV files.

### Configuration

`column`: Column containing elements used to categorize the rows of the CSV file.

`delimiter`: Delimiter used by the CSV file.

### Inputs

Type: single

`source_table`: CSV file to split.

### Outputs

Type: multiple

`unique_id`: Name of element used to categorize the rows of the original CSV file.

`result_table`: Generated CSV file without the column provided via the `column` config option.

### Description

    {
        "name": "Split CSV",
        "image": "platonam/lopco-split-csv-worker:latest",
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
