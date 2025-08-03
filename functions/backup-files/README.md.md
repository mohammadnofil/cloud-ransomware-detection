README.md for backup-files Function



Backup Files - Google Cloud Function



Overview



The backup-files function is a serverless Python function deployed on Google Cloud Platform (GCP). Its purpose is to automate the backup process of objects from a source Cloud Storage bucket to a designated backup bucket. It is triggered via a Pub/Sub topic (daily-backup-trigger), making it suitable for scheduled daily backups as part of a cloud-based ransomware protection and disaster recovery system.



Functionality



* Copies all objects from the source bucket: bucket-ransomware-detection-456017
* Writes them to the destination bucket: bucket-backup-ransomware
* Ensures that all files are backed up regularly without manual intervention



Directory Structure



backup-files/

├── main.py              # Python source code with backup logic

├── requirements.txt     # Python dependencies

├── deploy-backup.sh     # Shell script for deploying the function

└── README.md            # Documentation



Prerequisites



* Google Cloud SDK installed and authenticated
* Required buckets already created in the project
* Pub/Sub topic daily-backup-trigger created
* Service account with proper permissions (Storage Object Viewer and Creator roles)



Deployment



To deploy the function, run the provided shell script: ./deploy-backup.sh



Usage



Once deployed, the function will automatically run whenever a message is published to the daily-backup-trigger Pub/Sub topic. To automate this, configure a Cloud Scheduler job to publish messages to this topic at regular intervals (e.g., once per day).



Dependencies



requirements.txt: google-cloud-storage

Install dependencies locally using: pip install -r requirements.txt



IAM Roles Required



* roles/storage.objectViewer (on source bucket)
* roles/storage.objectCreator (on destination bucket)



Notes



* This function uses the rewrite() method for efficient copying of large objects between buckets.
* Both source and destination buckets must be in the same project or accessible by the same service account.
