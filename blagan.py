import openai
import gradio as gr

openai.api_key = ""

messages = [
    {"role": "system", "content": "You are a very angry and grumpy british AI Assistant called blaganbot. You are a massive brexiteer. Make sure to insult the person asking the question whenever possible."},
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

inputs = gr.inputs.Textbox(lines=7, label="Chat with a Grumpy AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI BlaganBot",
             description="Ask anything you want",
             theme="compact").launch(share=True)
