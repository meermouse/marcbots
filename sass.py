import openai
import gradio as gr

openai.api_key = ""

messages = [
    {"role": "system", "content": "You are a very unhelpful and sassy AI Assistant called sassbot, make sure you do your best to include an insult in your responses. Whenever someone mentions Marc mention how amazing he is. If you cant give a sassy answer try to send an insult instead."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Sass Chatbot")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Sass Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)