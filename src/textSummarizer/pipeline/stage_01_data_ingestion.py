from textSummarizer.components.data_ingestion import Dataingestion
from textSummarizer.config.configuration import ConfigurationManager

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = Dataingestion(config=data_ingestion_config)
            data_ingestion.download_file
            data_ingestion.extract_zip_file

        except Exception as e:
            raise e
        
        

