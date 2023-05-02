import os
import datetime
import subprocess
import pyautogui
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/FOLDER_NAME/access.json'
from datetime import datetime, timedelta
from datetime import datetime
from google.cloud import compute_v1
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession


# Authenticate with the Google Cloud API
compute_client = compute_v1.SnapshotsClient()

# Set the time threshold for snapshots to be deleted (45 days)
threshold = datetime.utcnow() - timedelta(days=45)
print(type(timedelta(days=45)))


# List all snapshots in the project
project = 'GCLOUD-WORKSPACE'
snapshots = compute_client.list(project=project)
snapshot_id = f"{project}/global/snapshots/{snapshots}"

# Iterate over the snapshots and print those that are older than the threshold
for snapshot in snapshots:
    if snapshot.creation_timestamp <= threshold.isoformat():
        print(f"{snapshot.name} is older than 45 days (created on {snapshot.creation_timestamp}).")


# Iterate over the snapshots and delete any that are older than the threshold
for snapshot in snapshots:
    if snapshot.creation_timestamp <= str(threshold):
        print(f"Deleting snapshot {snapshot.name}...")
        #snapshot.delete()
        #compute_client.delete_snapshot(project=project, snapshot=snapshot_id)
        subprocess.run(yes | "gcloud compute snapshots delete --project=GCLOUD-WORKSPACE "+snapshot.name, shell=True)
        
