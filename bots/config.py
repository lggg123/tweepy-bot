# tweepy-bots/bots/config.py
import tweepy 
import logging 
import os 

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("hVbh28N86mfTUtAB1nSZ83HEe")
    consumer_secret = os.getenv("hVbh28N86mfTUtAB1nSZ83HEe")
    access_token = os.getenv(
        "481841999-Wbd7r6TrsS4a4tetQkaRGO0mgh3mDSLBCsXFC97G")
    access_token_secret = os.getenv(
        "481841999-Wbd7r6TrsS4a4tetQkaRGO0mgh3mDSLBCsXFC97G")

    auth = tweepy.OAuthHandler(
        'hVbh28N86mfTUtAB1nSZ83HEe', 'hVbh28N86mfTUtAB1nSZ83HEe')
    auth.set_access_token(
        '481841999-Wbd7r6TrsS4a4tetQkaRGO0mgh3mDSLBCsXFC97G', '481841999-Wbd7r6TrsS4a4tetQkaRGO0mgh3mDSLBCsXFC97G')
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try: 
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e 
    logger.info("API created")
    return api 


