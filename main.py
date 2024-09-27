
from src.send_image import logger
from folder import file_path,model_path
from src.send_image.pipeline.stage_model import Model_pipeline

STAGE_NAME = " send stage"

# if __name__ == "__main__":
#     alexa = Alexa()
#     alexa.run_alexa()

# STAGE_NAME = " send stage"
# try:
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#    send = SendPipeline(file_path)
#    send.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e 

# Example usage
# if __name__ == "__main__":
#     # Specify the path to the .pkl file

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = Model_pipeline(model_path,file_path)
    while(True):
        pipeline.run()
except Exception as e:
    logger.exception(e)
    raise e    


   


