import speech_recognition as sr

#funcao resposavel por ouvir e reconhecer a fala
def ouvir_microfone():
    #habilita o microfone para ouvir o usuário
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        #avisa ao usuario que esta pronto para ouvir
        print('Diga alguma coisa: ') #nessa hora, colocar o captcha para 'falar'
        #armazena a informacao de audio na variavel
        audio = microfone.listen(source)

    try:
        #passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio, language='pt-BR')
        #apos alguns segundos, retorna a frase falada
        print('Você disse: ' + frase) #'frase' é o texto para resolver o captcha

        #caso não tenha reconhecido o padrao de fala, exibe essa mensagem
    except sr.UnknownValueError:
        print('Não entendi, vamos repetir.')

ouvir_microfone()