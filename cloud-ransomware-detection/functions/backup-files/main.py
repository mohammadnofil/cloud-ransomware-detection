import base64
import json
from google.cloud import storage

def backup_files(event, context):
    source_bucket_name = 'bucket-ransomware-detection-456017'
    destination_bucket_name = 'bucket-backup-ransomware'

    storage_client = storage.Client()
    source_bucket = storage_client.get_bucket(source_bucket_name)
    destination_bucket = storage_client.get_bucket(destination_bucket_name)

    blobs = source_bucket.list_blobs()

    for blob in blobs:
        source_blob = source_bucket.blob(blob.name)
        destination_blob = destination_bucket.blob(blob.name)
        destination_blob.rewrite(source_blob)