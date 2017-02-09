# Newline-delimited JSON to array
A simple script to address a specific use case. Use this to convert newline-delimited JSON to a JSON array.

I wrote this because the Google BigQuery command-line tool (bq) extracts tables into newline-delimited JSON; but the endpoint I am passing the extracted tables to requires a proper array (square brackets wrapping a comma-delimited series of objects).

Usage:
```
python nl_json_to_array.py inputfile.json outputfile.json
```
On my laptop, this converts an 800MB file to an array in about 15 seconds.
