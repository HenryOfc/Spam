from telethon import TelegramClient
import asyncio
import os

# Llenar con los datos de tu cuenta
api_id = 'coloca el tuyo'
api_hash = 'tu api hash'
numero = 'coloca tu numero incluyendo el codigo'

# Crear el cliente de Telethon
client = TelegramClient('session_name', api_id, api_hash)

#cargar mensajes desde un archivo
def cargar_mensajes(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return f.read().strip().split('\n')
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró en el directorio {os.getcwd()}.")
        return []

# añadir texto a cada línea
def modificar_lineas(lineas, texto_adicional):
    return [f"{texto_adicional} {linea}" for linea in lineas]

# enviar mensajes
async def enviar_mensajes(destinatario, archivo, intervalo, texto_adicional):
    lineas = cargar_mensajes(archivo)
    if not lineas:
        print(f"No hay mensajes en {archivo}.")
        return
    lineas_modificadas = modificar_lineas(lineas, texto_adicional)
    for linea in lineas_modificadas:
        await client.send_message(destinatario, linea)
        print(f'📨 Mensaje enviado: {linea}')
        await asyncio.sleep(intervalo)  # Espera el intervalo de tiempo
    print(f"✨ ¡Todos los mensajes de {archivo} completados! 😊. Esperando más mensajes...")

# Iniciar el cliente y enviar los mensajes
async def main():
    print("""
╔════════════════════╗
║                    ║
║   by @SammSmithxd 🌹  ║
║                    ║
╚════════════════════╝
""")
    await client.start(numero)
    destinatario = input("🌟 Ingresa el ID del bot o grupo: ")
    texto_adicional = input("✏️ Ingresa el comando del bot checker: ")
    while True:
        archivo = input(f"📄 Ingresa el nombre de tu archivo .txt con los mensajes (directorio actual: {os.getcwd()}): ")
        await enviar_mensajes(destinatario, archivo, 40, texto_adicional)  # Intervalo de 40 segundos

with client:
    client.loop.run_until_complete(main())
