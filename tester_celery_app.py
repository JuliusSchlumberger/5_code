from celery import Celery

# Initialize your Celery app. The broker URL points to Redis running locally.
celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def load_file(file_path):
    import pandas as pd
    import time
    # Simulate file loading
    time.sleep(2)
    # Load the data
    data = pd.read_csv(file_path)
    # For simplicity, we'll return the shape of the DataFrame
    return data.shape