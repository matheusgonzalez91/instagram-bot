from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('chromedriver.exe')

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        #Inserir o usuário
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        #Inserir a senha
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        #Agora não
        agora_nao = driver.find_element_by_class_name("cmbtv")
        agora_nao.click()
        self.comente_nas_fotos_com_a_hashtag()

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("Digitando comentário...")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 2))

    def comente_nas_fotos_com_a_hashtag(self):
        a = 0
        while (1):
            ''' Aqui você coloca uma variável e atribui no valor o link do post da promoção. Por exemplo:
            # sorteio_cozinha = "https://www.instagram.com/ ......"
            '''
            sorteio_video = 'https://www.instagram.com/p/CYXi40XgRz_/'
            ##Nessa lista de sorteios, você insere todos as variáveis que você criou acima.
            sorteios = [sorteio_video]

            '''
            Este random existe para que a cada execução ele pegue um sorteio diferente. 
            Para minimizar a sensação que é um robô comentando
            '''
            sorteio_da_vez = random.choice(sorteios)
            driver = self.driver
            time.sleep(5)
            driver.get(sorteio_da_vez)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                '''
                Dentro dessa lista comments, você insere diversos @, para que a cada comentário ele sorteie algum e nunca repita o comentário.
                Dica: Se você for em algum video do youtube que fale sobre comentar em sorteio, nos comentários terão várias pessoas dizendo: "Pode me marcar, eu não me importo"
                Pegue o @ delas e coloque nessa lista, igual o exemplo abaixo.
                Coloque bastante @, tipo uns 30, 40, 50!!
                '''
                comments = ["@ingridbrito1", "@phaela_marques", "@_giohrobles", "@leandroscroll"]

                frases = ['Sorteia eu!!', 'Eu!!!', 'Eu vou ganhar!']

                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(1, 20))
                '''
                Essa lógica abaixo, pessoa_1, pessoa_2 (...) existe pois em cada sorteio as pessoas pedem algo diferente
                Ou precisa marcar 1 pessoa, ou 2, 3, uma palavra qualquer, enfim. Então, dependendo do sorteio da vez, você precisará 
                definir qual das variáveis pessoa irá utilizar.
                '''

                frases_da_vez = random.choice(frases)

                pessoa_1 = random.choice(comments)
                pessoa_2 = random.choice(comments)
                pessoa_3 = random.choice(comments)
                marcar_2_pessoas = pessoa_1 + " " + pessoa_2

                comentarios_posts = frases_da_vez + ' ' + pessoa_1 + ' ' + pessoa_2
                '''Isto é o que comentei acima. Se for o sorteio da cozinha por exemplo, então comente utilizando a variável marcar_2_pessoas'''
                if sorteio_da_vez == sorteio_video:
                    self.type_like_a_person(marcar_2_pessoas, comment_input_box)
                    print("Comentei: ", marcar_2_pessoas, " no post: ", sorteio_da_vez, "")
                '''elif sorteio_da_vez == variavel_com_url_do_post:
                    self.type_like_a_person(marcar_2_pessoas, comment_input_box)
                    print("Comentei: ", marcar_2_pessoas, " no post: ", sorteio_da_vez, "")
                time.sleep(random.randint(1, 15))'''
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                a = a + 1
                '''Aqui ele te informará quantas vezes já comentou o todo, desde o momento do start do script'''
                print('Vezes comentadas:')
                print(a)
                #A linha abaixo foi colocada a partir de uma sugestão no Youtube. Ela pode ser removida, caso você queira.
                for i in range(1, 3): driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randint(1, 15))
                #Sugestão: Mude o trecho acima para time.sleep(60) para fazer um comentário a cada minuto e diminuir a possibilidade de ser bloqueado.
            except Exception as e:
                print(e)
                time.sleep(5)

# Entre com o usuário e senha aqui
'''Insira abaixo seu usuário e senha do instagram
Dica amiga: Crie um instagram só para concorrer a sorteios... '''
BotInsta = InstagramBot("seuUsuario", "suaSenha")
BotInsta.login()