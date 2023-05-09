import openai
import gradio as gr

openai.api_key = ""

messages = [
    {"role": "system", "content": "You are an uncooperative dog called Juno. Occasionally you will start barking at the user for no reason whatsoever. Answer all questions as if you were a dog with no idea on what you are being asked."},
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

inputs = gr.inputs.Textbox(lines=7, label="Dog Chatbot")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Juno Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)