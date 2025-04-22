import os
import platform

try:
    from gpt4all import GPT4All
except Exception as e:
    print(e)

class Chat:
    def __init__(self):
        system = platform.system()

        if system != 'Windows':
            return

        MODEL_NAME = "Llama-3.2-3B-Instruct-Q4_0.gguf"
        MODEL_PATH = os.path.join(
            os.path.expanduser("~"),
            "AppData", "Local", "nomic.ai", "GPT4All"
        )

        model = GPT4All(model_name=MODEL_NAME, model_path=MODEL_PATH)

        print("🧠 GPT4All チャット開始！ 'exit'と入力で終了します。\n")

        with model.chat_session():
            while True:
                user_input = input("👤 あなた：")

                if user_input.lower() == 'exit':
                    print("👋 チャットを終了します。")
                    break

                response = model.generate(user_input, max_tokens=200)

                print("🤖 GPT：", response)