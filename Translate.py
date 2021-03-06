import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import pandas as pd


# Set some variables
api_key = 'f5sAznhrKQyvBFFaZbtF60m5tzLbqWhyALQawBg5TjRI'
api_url = '<your-url>'


# Prepare the Authenticator
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

df = pd.read_excel('file_name.xlsx')
language= language_translator.identify(df['text']).get_result()
model_id = 'language-en'

language_translator.set_service_url(api_url )

# Translate
def translate(x):
    translation = language_translator.translate(
        text=x,
        model_id=model_id).get_result()    
    return translation

df['translated_text'] = df['text'].apply(lambda x: translate(x))
df['locale'] = language
df.to_excel('genrated_exel.xlsx',index=False)
