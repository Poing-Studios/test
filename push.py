import requests
import os

# Define os dados do asset
asset_data = {
    "name": "My Asset",
    "version": "1.0.0",
    "category": "Tools",
    "godot_version": "3.2.2",
    "description": "My asset description"
}

# Faz a solicitação de login para obter o cookie de autenticação
login_response = requests.post("https://godotengine.org/asset-library/api/login", data={"username": os.environ["USERNAME"], "password": os.environ["PASSWORD"]})
login_response.raise_for_status()

# Define os headers da solicitação com o cookie de autenticação
headers = {"Cookie": f"gdartoken={login_response.cookies['gdartoken']}"}

# Abre o arquivo do asset e adiciona ao dicionário de dados
with open("path/to/asset.zip", "rb") as asset_file:
    asset_data["file"] = asset_file.read()

# Faz a solicitação de upload do asset
upload_response = requests.post("https://godotengine.org/asset-library/api/upload", data=asset_data, headers=headers)
upload_response.raise_for_status()

# Verifica se a solicitação foi bem-sucedida
if upload_response.status_code == 200:
    print("Asset enviado com sucesso!")
else:
    print("Erro ao enviar o asset: ", upload_response.json())
