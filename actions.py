# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class CarForm(FormAction):
    def name(self):
        return "car_form"

    @staticmethod
    def required_slots(tracker):
        return ["brands","models","distance","year","price","power","seller-type"]

    def slot_mappings(self):
        return {
            "brands": [
                self.from_text(intent="brands")
            ],
            "models":[
                self.from_text(intent="models")
            ],
            "distance":[
                self.from_text(intent="distance")
            ],
            "year":[
                self.from_text(intent="year")
            ],
            "price":[
                self.from_text(intent="price")
            ],
            "power":[
                self.from_text(intent="power")
            ],
            "seller-type":[
                self.from_text(intent="seller-type")
            ]
        }
    
    def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]):
        dispatcher.utter_message("Thanks, great job!")
        return []