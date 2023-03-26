```py
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['nu3Q0SCM43fFS2G4Kq6AzFvr5I5kj3qBZY3hUslaVvKe']
url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/b73c04f3-a8a8-4bde-bc6c-ce609e7eeb93']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    french_text = language_translator.translate(
    text = english_text,
    model_id = 'en-fr').get_result()
    french_text = french_text['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    ''' Translate French to Enflish '''
    english_text = language_translator.translate(
    text = french_text,
    model_id = 'fr-en').get_result()
    english_text = english_text['translations'][0]['translation']
    return english_text
