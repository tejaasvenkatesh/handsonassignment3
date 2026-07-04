from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import datetime


class Command(BaseCommand):
    help = "Starts a terminal chatbot using Django and ChatterBot."

    def handle(self, *args, **options):
        bot = ChatBot(
            "UC Terminal Bot",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            database_uri="sqlite:///chatterbot.sqlite3",
            logic_adapters=[
                {
                    "import_path": "chatterbot.logic.BestMatch",
                    "default_response": "I am still learning and do not know how to answer that yet.",
                    "maximum_similarity_threshold": 0.75,
                }
            ],
        )

        trainer = ListTrainer(bot)

        trainer.train([
            "hello",
            "Hello! How can I help you today?",

            "hello there",
            "Hi there! Nice to chat with you.",

            "hi",
            "Hi! How are you doing today?",

            "good morning",
            "Good morning! I hope you are having a great day.",

            "Good Morning",
            "Good morning! I hope you are having a great day.",

            "how are you",
            "I am doing very well, thank you for asking.",

            "how are you doing",
            "I am doing great. Thank you for asking.",

            "thanks",
            "You are welcome.",

            "thank you",
            "You are welcome.",

            "what is your name",
            "My name is UC Terminal Bot.",

            "who are you",
            "I am a Django terminal chatbot created using Python and ChatterBot.",

            "bye",
            "Goodbye. Have a great day!",
        ])

        print("Terminal chatbot started. Type 'exit' to stop.")

        while True:
            user_input = input("user: ").strip()
            lower_input = user_input.lower()

            if lower_input in ["exit", "quit", "bye"]:
                print("bot: Goodbye. Have a great day!")
                break

            if "time" in lower_input:
                current_time = datetime.now().strftime("%I:%M %p")
                print(f"bot: The current time is {current_time}.")
                continue

            if "timezone" in lower_input or "time zone" in lower_input:
                print("bot: The timezone depends on your system settings.")
                continue

            response = bot.get_response(user_input)
            print(f"bot: {response}")