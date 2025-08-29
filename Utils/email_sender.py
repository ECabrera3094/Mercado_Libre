import smtplib
from email.message import EmailMessage

from Locators.locators_Mercado_Libre import Locators_Mercado_Libre

class EmailSender():

    def __init__(self):
        self.file_name = Locators_Mercado_Libre.file_name
        self.General_File_path = Locators_Mercado_Libre.General_File_path
        self.str_Email = Locators_Mercado_Libre.str_Email
        self.str_Password = Locators_Mercado_Libre.str_Password
        self.list_To_Email = Locators_Mercado_Libre.list_To_Email

    def test_send_email(self):
        from_email = self.str_Email
        password = self.str_Password
        to_email = self.list_To_Email
        report_file = self.General_File_path

        msg = EmailMessage()
        msg['Subject'] = "Prueba Automatizada a Mercado Libre"
        msg['From'] = from_email
        msg['To'] = to_email
        body = "Reciban un Saludo:\nEn el Archivo Adjunto recibirán las validaciones correspondientes a Mercado Libre.\n¡Saludos!\nAtte: Emiliano\n"
        msg.set_content(body)

        report_file = self.General_File_path
        file_name = self.file_name

        with open(report_file, 'rb') as file:
            msg.add_attachment(
                file.read(), 
                maintype = 'application', 
                subtype = 'octet-stream', 
                filename = file_name
            )

        # Send
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(from_email, password)
            smtp.send_message(msg)
            print("Correo Enviado Exitosamente!")