# tela inicial:
    # título: hashzap
    # botão iniciar chat
        # quando clica no botão:
         # abrir um modal
            # título: bem-vindo ao hashzap
            # caixa de texto: escreva seu nome no chat
            # botão enviar no chat
                # quando clicar no botão
                # fechar o modal
                # sumir com o título, botão iniviar chat
                    # carregar chat
                    # carregar campo "digite sua mensagem"
                    # botão de enviar
                        # quando clicar no botão enviar
                        # enviar mensagem
                        # aparecer no chat

# importar o flet
import flet as ft

# criar uma função para roldar o seu app
def meuChat(pagina):
    # titulo
    titulo = ft.Text("Hashzap")
    pagina.add(titulo)

    # websocket - tunel de comunicacao entre dois usuarios
    def enviar_mensagem_tunel(mensagem):
        # executar tudo o que eu quero que aconteça para todos os usuarios que receberem a mensagem
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    # criar o tunel de comunicação
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        # limpar a caixa de enviar mensagem
        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    chat = ft.Column()

    def entrar_chat(evento):
        # fechar o modal
        modal.open = False
        # sumir com o titulo
        pagina.remove(titulo)
        # sumir com o botao Iniciar Chat
        pagina.remove(botao)
        # carregar o chat
        pagina.add(chat)
        # carregar o campo de enviar mensagem
        # carregar o botao enviar
        pagina.add(linha_enviar)

        # adicionar no chat a mensagem "Fulano entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou na chat!"
        pagina.pubsub.send_all(mensagem)

        pagina.update() # usar sempre que fazer uma alteração visual na tela

    # criar o modal
    titulo_modal = ft.Text("Bem-Vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_modal = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    modal = ft.AlertDialog(title=titulo_modal, content=caixa_nome, actions=[botao_modal])

    # botao inicial
    def abrir_modal(evento):
        pagina.dialog = modal
        modal.open = True
        pagina.update() # atualizar o que o usuario ta vendo sem precisar regarregar a pagina
        print("Clicou no botao")

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_modal)
    pagina.add(botao)

#executar essa função com o flet
ft.app(meuChat, view=ft.WEB_BROWSER)