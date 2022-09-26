import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (450, 700)

KV = '''
Screen:
    MDCard:
        size_hint:None,None
        size:300,600
        pos_hint: {"center_x":0.5,"center_y":0.5}
        elevation:10
        padding:65
        spacing:35
        orientation: 'vertical'
        MDIcon:
            icon:'android'
            icon_color: 75,75,75,75
            haling: 'center'
            font_size:180
        MDFillRoundFlatButton:
            id: encuestas
            text:"Encuestas"
            font_size:15
            pos_hint:{"center_x":0.5}
            on_press: app.encuestas()
        MDTextField:
            id:theuser
            hint_text: "Email o Matricula"
            line_color_normal: "green"
        MDTextField:
            id:thepassword
            hint_text: "Contraseña"
            line_color_normal: "red"
        MDFillRoundFlatButton:
            id: cerrarapp
            text:"Salir"
            font_size:15
            pos_hint:{"center_x":0.5}
            on_press: app.close()
        MDLabel:
            text: "CREATE BY: P4CH3C0"
            font_size:9
            halign: "center"
'''

class SolveERS(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Blue'

        return Builder.load_string(KV)

    def encuestas(self):
        theuser = ''
        theuser = self.root.ids.theuser.text
        thepassword = ''
        thepassword = self.root.ids.thepassword.text
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get("https://encuestasregresoseguro.com/")
        action = ActionChains(driver)
        #Seleccion de tipo de Escuela y universidad
        select1 = driver.find_element("name", 'tipoEscuela').click()
        time.sleep(1)
        tipoEsc = driver.find_element("xpath", '//*[@id="tipoEscuela_id"]/option[3]').click()
        select1 = driver.find_element("name", 'tipoEscuela').click()
        select2 = driver.find_element("id", 'universidades').click()
        time.sleep(1)
        escuela = driver.find_element("xpath", '//*[@id="universidades"]/option[13]').click()
        select2 = driver.find_element("id", 'universidades').click()
        dni = driver.find_element("id", "DNI").send_keys(theuser)
        passw = driver.find_element("name", "password").send_keys(thepassword)
        sendf = driver.find_element("id", 'botonEnviar').click()
        time.sleep(2)
        try:
            #primer parte del formulario
            check1 = driver.find_element("xpath",'//*[@id="tab_1"]/div/div[2]/form/div[1]/div[4]/div[2]/div/div/label').click()
            check2 = driver.find_element("xpath",'//*[@id="tab_1"]/div/div[2]/form/div[1]/div[8]/div[2]/div/div/label').click()
            check3=driver.find_element("xpath",'//*[@id="tab_1"]/div/div[2]/form/div[1]/div[10]/div[2]/div/div/label').click()
            #segunda seccion
            check4= driver.find_element("xpath",'//*[@id="tab_1"]/div/div[2]/form/div[1]/div[15]/div[2]/div/div/label').click()
            check5 = driver.find_element("xpath",'//*[@id="tab_1"]/div/div[2]/form/div[1]/div[17]/div[2]/div/div/label').click()
            check6 = driver.find_element("xpath", '//*[@id="tab_1"]/div/div[2]/form/div[1]/div[19]/div[2]/div/div/label').click()
            check7 = driver.find_element("xpath", '//*[@id="tab_1"]/div/div[2]/form/div[1]/div[21]/div[2]/div/div/label').click()
            check8 = driver.find_element("xpath", '//*[@id="tab_1"]/div/div[2]/form/div[1]/div[23]/div[2]/div/div/label').click()
            check9 = driver.find_element("xpath", '//*[@id="tab_1"]/div/div[2]/form/div[1]/div[25]/div[2]/div/div/label').click()
            #3er seccion
            check10 = driver.find_element("xpath", '//*[@id="tab_1"]/div/div[2]/form/div[1]/div[29]/div[2]/div/div/label').click()
            check11 = driver.find_element("xpath", '//*[@id="tab_1"]/div/div[2]/form/div[1]/div[31]/div[2]/div/div/label').click()
            check12 = driver.find_element("xpath", '//*[@id="tab_1"]/div/div[2]/form/div[1]/div[33]/div[2]/div/div/label').click()
            check13 = driver.find_element("xpath", '//*[@id="tab_1"]/div/div[2]/form/div[1]/div[35]/div[2]/div/div/label').click()
            check14 = driver.find_element("xpath", '//*[@id="tab_1"]/div/div[2]/form/div[1]/div[37]/div[2]/div/div/label').click()
            check15 = driver.find_element("xpath", '//*[@id="tab_1"]/div/div[2]/form/div[1]/div[39]/div[2]/div/div/label').click()
            check16 = driver.find_element("xpath", '//*[@id="tab_1"]/div/div[2]/form/div[1]/div[41]/div[2]/div/div/label').click()
            check17 = driver.find_element("xpath", '//*[@id="tab_1"]/div/div[2]/form/div[1]/div[43]/div[2]/div/div/label').click()
            #boton siguiente
            clickSiguiente=driver.find_element("xpath",'//*[@id="hola"]/ul/li/a').click()
            clickEnviar= driver.find_element("xpath",'//*[@id="tab_2"]/div/div[3]/button').click()
        except:
            print("No se encontro el xpath, actualiza el codigo")

    def close(self):
        MDApp.get_running_app().stop()
        Window.close()

SolveERS().run()
##create by:Pacheco
