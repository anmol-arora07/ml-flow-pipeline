import sqlite3
import logging
logger=logging.getLogger(__name__)

logging.basicConfig(filename='./test.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

def get_best_model():
    logger.info("starting the process")


    conn=sqlite3.connect('elasticnet.db')

    c=conn.cursor()

    c.execute("SELECT RUN_UUID, VALUE FROM METRICS WHERE KEY='rmse' ORDER BY VALUE DESC")

    rows=c.fetchone()
    logger.info("fetching rows")
    run_id=str(rows[0])
    logger.info(f"{run_id}")
    c.execute(f"SELECT NAME,VERSION FROM MODEL_VERSIONS WHERE RUN_ID='{run_id}'")
    rows=c.fetchone()
    model_name, version= rows[0],rows[1]
    logger.info(f"{model_name},{version}")
    return model_name,version

if __name__=="__main__":
    get_best_model()









# import mlflow.pyfunc

# model_name="best model test"
# stage="Staging"

# model=mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{stage}")

# print(model)