from django.shortcuts import render
from django.http import JsonResponse

from django.contrib import auth

import openai
import os
import time
from dotenv import load_dotenv
import tiktoken


load_dotenv() 
openai.api_key = os.getenv("OPENAI_API")


COMPLETIONS_MODEL = "gpt-3.5-turbo"

def num_tokens_from_string(string: str, encoding_name = COMPLETIONS_MODEL) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens



def generate_response(message):
    messages = [{"role":"system","content": "You are good at solving user's problem."}]
    messages.append({"role":"user", "content": f"{message}"})
    num_token = num_tokens_from_string(messages[0]["content"] + messages[1]["content"])
    print("total token spend for prompt :" ,num_token)

    while True:
        try : 
            response = openai.ChatCompletion.create(
                            model = COMPLETIONS_MODEL,
                            messages = messages,
                            temperature = 0.8,
                            max_tokens = 4096 - num_token - 13
                        )
            break
        except Exception as err:
            print(err)
            time.sleep(0.1)
    answer = response.choices[0].message['content']
    return answer

# Create your views here.

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = generate_response(message)
        return JsonResponse({'message' : message, 'response' : response})
    return render(request, 'chatbot.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user 
            except:

        else:
            error_message = 'Password not match !'
            return render(request, 'register.html', {'error_message': error_message})

    return render(request, 'register.html')

def logout(request):
    return render(request, 'logout.html')
