# using huggingface
import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')

headers = {"Authorization": f"Bearer {os.environ['HUGGINGFACE_TOKEN']}"}

# summarization
def summarize(payload):
	json = requests.post("https://api-inference.huggingface.co/models/facebook/bart-large-cnn", 
		      headers=headers, 
			  json=payload).json()
	summary = json[0]["summary_text"]
	return summary

# conversation

class Conversation:
	def __init__(self):
		# used to maintain a history of conversations
		self.past_user_inputs = []
		self.past_ai_responses = []

	def talk(self, text):
		# get the responses for the huggingface api
		json = requests.post("https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill", 
				headers=headers, 
				json={
					"inputs": {
						"past_user_inputs": self.past_user_inputs,
						"generated_responses": self.past_ai_responses,
						"text": text
					}
				}).json()
		response = json["generated_text"]

		# update the conversation history
		self.past_user_inputs.append(text)
		self.past_ai_responses.append(response)

		return response 