import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Conexión con la hoja de calculo
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/sprea...','https://www.googleapis.com/auth/drive...','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("clave.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Formulario de asistencia").sheet4
sheet.update_acell('D2', 'Mauro.celis620@gmail.com')