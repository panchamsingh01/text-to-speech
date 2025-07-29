from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


api_key = "your API key here"  # Replace with your IBM Cloud Text to Speech API key
url = "your service URL here"  # Replace with your service URL

authenticator = IAMAuthenticator(api_key)
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url(url)

# Define available voices and their language
voices = {
    "English (US) - Michael": "en-US_MichaelV3Voice",
    "English (UK) - Kate": "en-GB_KateV3Voice",
    "Portuguese (BR) - Lucas": "pt-BR_LucasExpressive",
    "Spanish (ES) - Enrique": "es-ES_EnriqueV3Voice",
    "French (FR) - Renee": "fr-FR_ReneeV3Voice"
}

print("Select a language/voice:")
for idx, (desc, _) in enumerate(voices.items(), 1):
    print(f"{idx}. {desc}")

choice = int(input("Enter the number of your choice: "))
voice = list(voices.values())[choice - 1]

text = input("Enter the text to convert to speech:\n")

with open('output.wav', 'wb') as audio_file:
    response = text_to_speech.synthesize(
        text,
        voice=voice,
        accept='audio/wav'
    ).get_result()
    audio_file.write(response.content)

print("Speech synthesized and saved as output.wav")