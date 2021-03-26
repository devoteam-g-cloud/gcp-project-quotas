from googleapiclient.discovery import build
import google.auth


credentials, project = google.auth.default()

project_id = 'my-project-id'
resource = 'drive.googleapis.com'

service = build(
    "serviceusage",
    "v1beta1",
    credentials=credentials,
    cache_discovery=False,
)
quotas = service.services().consumerQuotaMetrics().list(
    parent=f"projects/{project_id}/services/{resource}",
    view="FULL"
).execute()

print(quotas)
