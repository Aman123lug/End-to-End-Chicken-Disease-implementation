
from cnnClassifier.constant import *
from cnnClassifier.utils.common import load_bin, read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig


class ConfigurationManager:
    def __init__(self, configfile_path = CONFIG_FILE_PATH, paramsfile_path = PARAMS_FILE_PATH) -> None:
        
        self.config  = read_yaml(configfile_path)
        self.params = read_yaml(paramsfile_path)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
    
    
        data_ingestion_config = DataIngestionConfig(
            
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
            
        )
        return data_ingestion_config
    
    
    def get_base_model_config(self) -> PrepareBaseModelConfig:
        
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])
        
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_config,
            updated_base_model=config.updated_base_model_config,
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weight=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
            
        )
        
        return prepare_base_model_config