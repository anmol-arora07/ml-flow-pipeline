from getting_best_model import get_best_model
from mlflow import MlflowClient
import mlflow


model_name,version= get_best_model()
mlflow.set_tracking_uri("sqlite:///elasticnet.db")
client = MlflowClient()
client.transition_model_version_stage(
    name=f"{model_name}",
    version=f"{version}",
    stage="Staging"
)

#do some sanity check



#Change model stage to Production if all test passes

#Once model is changed to production it would also trigger new image creation
#once new image is created, it would re deploy the container in production



