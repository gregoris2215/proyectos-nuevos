# chatbot_basico.py

import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r'Hola|Hola!', ['¡Hola! ¿Cómo puedo ayudarte?']),
    (r'¿Cómo estás?', ['Estoy bien, gracias. ¿Y tú?']),
    (r'(Tu nombre|¿Cómo te llamas?)', ['Soy un chatbot, no tengo un nombre.']),
    (r'(.*)', ['Lo siento, no entiendo esa pregunta.'])
]

def main():
    print("Hola, soy un chatbot. Escribe 'salir' para terminar la conversación.")
    chatbot = Chat(pairs, reflections)
    while True:
        entrada = input('Tú: ')
        if entrada.lower() == 'salir':
            print('Chatbot: ¡Adiós!')
            break
        respuesta = chatbot.respond(entrada)
        print(f'Chatbot: {respuesta}')

if __name__ == "__main__":
    nltk.download('punkt')
    main()
