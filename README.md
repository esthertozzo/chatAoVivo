# 💬 Projeto de Chat em Python com Flet 🐍

## ℹ️ Descrição
Chat ao vivo para site e app utilizando a ferramenta **Flet** (Framework), tanto front end como back end feitos em Python utilizando um **Ambiente Virtual** (.venv)

Documentação Flet - https://flet.dev/

Documentação .venv - https://docs.python.org/3/library/venv.html

## 📂 O que é Ambiente Viurtal?
Ambiente Virtual é um local, uma pasta isolada no seu computador, que possui dentro dela, instalações específicas (bibliotecas, versões). O que está fora dessa pasta não afeta o que está dentro dela ou ao contrário.

## 🖥️ Pra quê serve um Ambiente Virtual?
O Ambiente Virtual garente que dentro dele tenham somente as bibliotecas e instalações que o meu código usa. Ou seja, o arquivo executável se torna menor.

Por exemplo, existem ferramentas que necessitam de uma versão específica do Python, então seria necessária a criação desse Ambiente Virtual para que sejam integradas. 

Ele isola um pedaço do seu computador e é bom por vários motivos:
- Torna arquivos mais simples;
- Cria sites de forma isolada onde nada de fora impacta o código etc.

---

## 🆕 Como criar um Ambiente Virtual?
> Abra uma nova pasta no VS Code

> Certifique-se de que a extenção do Python está instalada

> Command Palette (Ctrl + Shift + P)

> Selecionar ***"Python: Create Environment"***

> Selecionar ***"Venv"***

> Selecionar versão do Python instalada

Para instalar dependências dentro do seu ambiente virtual, abra o terminal e execute no ***Command Prompt***
##### Verificar qual a versão Python
    where pyhon
##### Instalar biblioteca
    pip install flet
##### Verificar as bibliotecas instaladas
    pip freeze
    

#### Caso o Ambiente virtual esteja desativado, é possível ativá-lo de forma manual no terminal ***(Command Prompt)***
##### Abrir pastas
    cd .venv
    cd Scripts
##### Ativar Ambiente Virtual
    activate.bat 
##### Para desativar Ambiente Virtual
    desactivate

---

![image 1](https://github.com/user-attachments/assets/9a7feb79-c07e-425c-9ea7-6900d3723adb)<br>
*Chat da Esther*

![image 2](https://github.com/user-attachments/assets/c5fdf8e6-5c9f-4f05-936a-330d63fb26e0)<br>
*Chat do Renan*

