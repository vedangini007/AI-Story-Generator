# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 17:41:03 2025

@author: asus
"""
import google.generativeai as genai


genai.configure(api_key="Replace with your actual API key")  

def generate_story(context, model="gemini-2.0-flash"):
    model = genai.GenerativeModel(model)
    
    response = model.generate_content(
        context,
        generation_config={
            "temperature": 0.8,
            "max_output_tokens": 2000
        }
    )
    
    return response.text


