from googleapiclient import discovery
import base64

def isolate_vm(event, context):
    compute = discovery.build('compute', 'v1')
    project = "ransomware-detection-456017"  # <-- Replace this
    zone = "us-central1-a"           # <-- Replace this (e.g., "us-central1-a")
    instance = "ransomware-vm"  # <-- Replace this (your VM name)

    print(f"Attempting to stop instance: {instance}")
    compute.instances().stop(project=project, zone=zone, instance=instance).execute()
