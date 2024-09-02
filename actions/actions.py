# This file contains your custom actions which can be used to run
# custom Python code.

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Action for Hybrid Trainings explanation
class ActionExplainHybridTrainings(Action):

    def name(self) -> Text:
        return "action_explain_hybrid_trainings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = (
            "Hybrid Trainings are a combination of Fitness and Calisthenics exercises, "
            "taking the best out of both worlds and building a strong functional body "
            "while gaining muscles or losing fat."
        )
        dispatcher.utter_message(text=response)
        return []

# Action for why Hybrid Trainings
class ActionWhyHybridTrainings(Action):

    def name(self) -> Text:
        return "action_why_hybrid_trainings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = (
            "With Calisthenics, you can gain serious functional strength because almost "
            "every exercise is compound, and they also offer Calisthenics Skills, like "
            "Handstand, Muscle Up, or Front Lever. Bodybuilding also has great compound "
            "exercises like Bench Press, Squat, Deadlift, and offers isolation exercises "
            "to focus on growth on specific muscles. By blending these approaches, Hybrid "
            "Trainings provide a unique, personalized program designed to maximize strength, "
            "functionality, and muscle growth."
        )
        dispatcher.utter_message(text=response)
        return []

# Action for personalized plans explanation
class ActionPersonalizedPlans(Action):

    def name(self) -> Text:
        return "action_personalized_plans"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = (
            "The plans are created based on your goals, your past workout and sport experience, "
            "exercises that you are able to do and that you like, and the equipment that you have available."
        )
        dispatcher.utter_message(text=response)
        return []

# Additional custom actions can be added here as needed for other responses

# If any action requires integration with external APIs or databases, you can add the logic within each run() method.