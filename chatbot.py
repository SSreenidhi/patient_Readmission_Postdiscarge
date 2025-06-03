from flask import Flask, request, jsonify
import google.generativeai as genai
import os

# Setup
app = Flask(__name__)
genai.configure(api_key="AIzaSyDm6EVFT84bGxQYNWY8TW4GEHQQFfm_9d4")  
model = genai.GenerativeModel("gemini-pro")

# Route for chatbot messages
@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_input = request.json.get("message", "")
    
    if not user_input:
        return jsonify({"reply": "Sorry, I didn't catch that. Please try again."})

    try:
        prompt = f"""
        You are Health Pulse Support Bot, a helpful assistant in a hospital setting. 
        Answer questions about post-discharge care, medication, symptoms, hospital services, and health-related concerns clearly and compassionately.

        User: {user_input}
        """

        response = model.generate_content(prompt)
        return jsonify({"reply": response.text.strip()})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "Sorry, there was a problem processing your request."})

# Run server
if __name__ == "__main__":
    app.run(debug=True)
