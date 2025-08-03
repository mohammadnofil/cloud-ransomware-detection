from google.cloud import logging

def detect_ransomware(event, context):
    client = logging.Client()
    logger = client.logger("ransomware-detection")

    file_name = event.get('name')

    if file_name and (file_name.endswith(".locked") or ".encrypted" in file_name):
        logger.log_text(f"Ransomware detected: {file_name}")
    else:
        logger.log_text(f"Safe file uploaded: {file_name}")
