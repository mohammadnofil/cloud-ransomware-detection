README.md for isolate-vm Function



isolate-vm – Google Cloud Function



Overview



The isolate-vm function is a serverless solution designed to automatically stop a specific virtual machine (VM) on Google Cloud Platform (GCP) when a ransomware-related alert is published to a Pub/Sub topic. It is part of a larger ransomware detection and recovery system intended to reduce the attack surface by isolating infected or at-risk systems.



Functionality



* Stops a specified Compute Engine VM instance using the GCP Compute Engine API.
* Triggered by the Pub/Sub topic: ransomware-alerts.
* Helps in rapid response to detected ransomware threats by halting the affected VM to prevent further damage.



Directory Structure



isolate-vm/

├── main.py              # Python source code to stop VM instance

├── requirements.txt     # Python dependencies

├── deploy-isolate.sh    # Shell script for deploying the function

└── README.md            # Documentation



Prerequisites



* Google Cloud SDK installed and authenticated
* Pub/Sub topic named ransomware-alerts must exist
* Target VM instance already deployed in Compute Engine
* Appropriate IAM permissions configured for the Cloud Function’s service account



Deployment



To deploy the function using the provided shell script: ./deploy-isolate.sh



Update the following values in main.py before deployment:



* project: GCP project ID
* zone: Zone of the target VM (e.g., "us-central1-a")
* instance: Name of the Compute Engine instance to isolate



Usage



This function listens for alerts published to the ransomware-alerts topic. When triggered, it sends a request to stop the specified VM. It is intended to be used as part of an automated incident response workflow.



To simulate or test the function, publish a message to the ransomware-alerts topic using:



gcloud pubsub topics publish ransomware-alerts --message="test"



Dependencies


requirements.txt: google-api-python-client

Install dependencies locally using: pip install -r requirements.txt



IAM Roles Required



* roles/compute.instanceAdmin.v1 (for stopping instances)
* roles/pubsub.subscriber (to listen to Pub/Sub events)



Notes



* The function does not currently validate or parse the message content. Additional logic can be added to analyze event data and isolate different VMs dynamically.
* Make sure to handle permissions securely and follow GCP best practices for production deployment.





