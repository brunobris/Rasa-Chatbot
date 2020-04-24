# Rasa-Chatbot

rasa run --enable-api --cors "*"

rasa run actions

para executar localmente, a pagina do front e não ter problema com CORS:

http-server -p 3000 --cors


docker container run -v $(pwd):/app -p 5005:5005 --name rasa-ciasc rasa/rasa:1.8.1-full run --enable-api --cors "*"