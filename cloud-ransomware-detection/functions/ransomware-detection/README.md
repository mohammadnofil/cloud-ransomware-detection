README.md for ransomware-detection Function



Ransomware Detection – Google Cloud Function



Overview



The ransomware-detection function is a serverless Python-based Google Cloud Function designed to monitor file uploads to a specific Cloud Storage bucket and detect potential ransomware activity based on file naming patterns. It enhances cloud infrastructure security by logging suspicious file uploads that may indicate a ransomware attack.



Functionality



* Triggered automatically when a new object is uploaded to the source bucket: bucket-ransomware-detection-456017
* Checks if the uploaded file has ransomware-like extensions (e.g., .locked or .encrypted)
* Logs a warning in Google Cloud Logging for suspicious files, or a safe message for normal uploads



Directory Structure



ransomware-detection/

├── main.py               # Python source code with detection logic

├── requirements.txt      # Python dependencies (if any)

├── deploy-detection.sh   # Shell script for deploying the function

└── README.md             # Documentation



Prerequisites



* Google Cloud SDK installed and authenticated
* Cloud Storage bucket: bucket-ransomware-detection-456017
* Logging enabled in the project
* Appropriate IAM permissions for the Cloud Function



Deployment



To deploy the function using the provided script: ./deploy-detection.sh


Usage



The function will run automatically whenever a new object is finalized (i.e., uploaded) in the specified Cloud Storage bucket. Based on the filename, it logs either a potential ransomware alert or a safe upload event.



Logging



Logs are written to the "ransomware-detection" log stream in Google Cloud Logging. You can view the logs via the Cloud Console → Logging → Logs Explorer.



Example log entries:



* Ransomware detected: file123.locked
* Safe file uploaded: report.pdf



IAM Roles Required



* roles/logging.logWriter
* roles/storage.objectViewer (on the source bucket)



Notes



* The detection logic is currently based on simple filename patterns. Additional logic (such as checksum or content analysis) can be added to enhance detection capabilities.
* The function is stateless and does not alter the uploaded file.



