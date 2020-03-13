# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionListaSolicitacoesUsuario(Action):

    def name(self) -> Text:
        return "action_lista_solicitacoes"

    def run(self, dispatcher, tracker, domain):
        cpf = tracker.get_slot('cpf')

        dispatcher.utter_message(text="Para o CPF " + cpf + " foram encontradas as seguintes solicitações:")

        return []
