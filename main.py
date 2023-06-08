import sys
import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

 
try:
  message=sys.argv[1]

  def reenter():
    message=input("Please reenter the prompt: ")

  if sys.argv[1]==" ":
    print("Prompt Is Empty Please Re Enter The Prompt")
    reenter()
except IndexError:
  print("Prompt Is Empty Please Re Enter The Prompt")
  reenter()
except:
  print("unexcepted error") 
  reenter()
   
print (f"Entered Prompt: {message}")

output = query({
	"inputs": message,
  "max_length":500
})
print(output[0]["generated_text"])

