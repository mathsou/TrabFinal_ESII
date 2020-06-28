import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from datetime import date, timedelta



class Tela(ScreenManager):
    pass

class NovoServico(Screen):
    def load_placa(self):

        frase = self.ids.frase1.text
        altura = self.ids.altura1.text
        largura = self.ids.largura1.text
        corplaca = self.ids.corplaca1.text
        corletras = self.ids.corletras1.text

        if(frase == '' or altura == '' or largura == '' or corplaca == '' or corletras == ''):
            self.manager.ids.novoservico.ids.erro.text = 'preencha todos os campos'
        
        else:
            alturacalc = altura.replace(',', '.')
            larguracalc = largura.replace(',', '.')
            frase1 = frase.replace(' ', '')
            try:
                area = float(alturacalc)*float(larguracalc)
            except:
                self.manager.ids.novoservico.ids.erro.text = 'altura e largura apenas números'
                return 0
            
            letras = len(frase1)

            valortotal = (area*147.3)+(letras*0.32)
            valorsinal = valortotal/2

            valortotal = 'R$ ' + f'{valortotal:.2f}'.replace('.', ',')
            valorsinal = 'R$ ' + f'{valorsinal:.2f}'.replace('.', ',')

            data_atual = date.today()
            data = data_atual + timedelta(days = 1)
            data = data.strftime('%d/%m/%Y')

            self.manager.ids.confirmarservico.ids.frase2.text = frase
            self.manager.ids.confirmarservico.ids.altura2.text = str(alturacalc)
            self.manager.ids.confirmarservico.ids.largura2.text = str(larguracalc)
            self.manager.ids.confirmarservico.ids.corplaca2.text = corplaca
            self.manager.ids.confirmarservico.ids.corletras2.text = corletras
            self.manager.ids.confirmarservico.ids.valortotal.text = valortotal
            self.manager.ids.confirmarservico.ids.valorsinal.text = valorsinal
            self.manager.ids.confirmarservico.ids.dataentrega.text = data
            self.manager.current = 'confirmarservico'
    def limpar(self):
        self.manager.ids.novoservico.ids.frase1.text = ''
        self.manager.ids.novoservico.ids.altura1.text = ''
        self.manager.ids.novoservico.ids.largura1.text = ''
        self.manager.ids.novoservico.ids.corplaca1.text = ''
        self.manager.ids.novoservico.ids.corletras1.text = ''

class ConfirmarServico(Screen):
    def cancelar(self):
        self.manager.ids.novoservico.ids.frase1.text = ''
        self.manager.ids.novoservico.ids.altura1.text = ''
        self.manager.ids.novoservico.ids.largura1.text = ''
        self.manager.ids.novoservico.ids.corplaca1.text = ''
        self.manager.ids.novoservico.ids.corletras1.text = ''
        self.manager.ids.novoservico.ids.erro.text = ''
        self.manager.current = 'novoservico'

class Sucesso(Screen):
    def voltar(self):
        self.manager.ids.novoservico.ids.frase1.text = ''
        self.manager.ids.novoservico.ids.altura1.text = ''
        self.manager.ids.novoservico.ids.largura1.text = ''
        self.manager.ids.novoservico.ids.corplaca1.text = ''
        self.manager.ids.novoservico.ids.corletras1.text = ''
        self.manager.ids.novoservico.ids.erro.text = ''
        self.manager.current = 'novoservico'

class Main(App):
    def build(self):
        return Tela()

Main().run()
