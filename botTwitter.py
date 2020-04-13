from selenium import webdriver
import time

class TwitterBot:
    def __init__(self):
        self.usuario = ""
        self.senha = ""
        self.seguidores = []
        self.usuariosNaoBloquear = ['', '', '']

        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")

        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def LogarNoTwitter(self):
        self.driver.get("https://twitter.com/login")

        inputUsuario = self.driver.find_element_by_name("session[username_or_email]")
        time.sleep(2)
        inputUsuario.click()
        inputUsuario.send_keys(self.usuario)

        inputSenha = self.driver.find_element_by_name("session[password]")
        time.sleep(2)
        inputSenha.click()
        inputSenha.send_keys(self.senha)

        inputBotao = self.driver.find_element_by_xpath("//span[text()='Entrar']")
        time.sleep(2)
        inputBotao.click()

    def EntrarNoSeguidores(self):
        time.sleep(5) #Tempo de Login
        
        inputPerfil = self.driver.find_element_by_xpath("//span[text()='Perfil']")
        time.sleep(2)
        inputPerfil.click()

        inputSeguidores = self.driver.find_element_by_xpath("//span[text()='seguidores']")
        time.sleep(2)
        inputSeguidores.click()
        time.sleep(2)

    def Bloquear(self):
        self.seguidores = self.driver.find_elements_by_xpath("//span[text()='Segue você']")
        i = len(self.seguidores)
        print(i)

        for i in range(i):
            self.seguidores = self.driver.find_elements_by_xpath("//span[text()='Segue você']")
            seguidor = self.seguidores[i]

            #Entrando no perfil
            seguidor.click() 
            time.sleep(2)

            #Capturando nome de usuario
            url = self.driver.current_url
            urlSplit = url.split('/')
            usuario = urlSplit[len(urlSplit)-1]
            print(usuario)

            #Verificando se deve bloquear
            podeBloquear = 1
            for usuarioNaoBloquear in self.usuariosNaoBloquear:
                if usuarioNaoBloquear == usuario:
                    podeBloquear = 0
            
            if podeBloquear:
                print("Pode bloquear")
                
                #Bloqueando
                inputMais = self.driver.find_element_by_xpath("//div[@aria-label='Mais']")
                time.sleep(2)
                inputMais.click()

            else: 
                print("Nao pode bloquear")
                        
            #botaoVoltar =  self.driver.find_element_by_xpath("//div[@aria-label='Voltar']") 
            #time.sleep(2)
            #botaoVoltar.click()
            #time.sleep(3)
            botaoVoltar = self.driver.find_element_by_css_selector("svg[class*='r-13gxpu9 r-4qtqp9 r-yyyyoo r-1q142lx r-50lct3 r-dnmrzs r-bnwqim r-1plcrui r-lrvibr']")
            self.driver.execute_script("arguments[0].click();", botaoVoltar)


bot = TwitterBot()
bot.LogarNoTwitter()
bot.EntrarNoSeguidores()
bot.Bloquear()

