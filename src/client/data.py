
import pandas as pd
from functools import lru_cache
from google.cloud import bigquery
from google.oauth2 import service_account

class DataClient:
    """Data client, responsible for getting main data
    from GCloud Plataform, based on provided configurations.
    """

    def __init__(self,
        configs = None):
        self.configs = configs['credentials']['bigquery']
        credentials = service_account.Credentials.from_service_account_file(
            self.configs['key_file'])
        self.bq_client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    @property
    @lru_cache(maxsize=1)
    def products_df(self) -> pd.DataFrame:
        """
        """
        query = """
            SELECT * 
            FROM `elo7interview.ProductClassification.products`
        """
        products_df = self.bq_client.query(query).to_dataframe()
        return products_df

