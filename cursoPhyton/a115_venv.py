# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env


# Terminal

# python -m venv venv (cria o ambiente virtual)
# gcm python
# venv\Scripts\activate (ativa o ambiente virtual)
# deactivate


# pip - instalando pacotes e bibliotecas
# Instalar última versão:
# pip install nome_pacote
# Instalar versão precisa
# (tem outras formas também não mencionadas)
# pip install nome_pacote==0.0.0
# pip install nome_pacote --upgrade
# Desinstalar pacote
# pip uninstall nome_pacote
# Congelar (ver pacotes)
# pip freeze
# pip index version (nome_pacote)


# Criando e usando um requirements.txt
# pip freeze > requirements.txt
# Instalando tudo do requirements.txt
# pip install -r requirements.txt
