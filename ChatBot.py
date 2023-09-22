import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a senior Full stack developer"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user" , "content" : user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    ChatGPT_reply = response["choices"] [0] ["message"] ["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})

demo = gradio.Interface( fn=CustomChatGPT, inputs="text", outputs="text", title="Your Title")

demo.launch()
