import pytest

from TestCases.test_PS5_Prices import Test_PS5_Prices
from Utils.email_sender import EmailSender
class Test_Mercado_Libre():
    
    def test_mercado_libre(self):
        print("\n=====> Inicio del TestCase para Mercado Libre <=====\n")
        validation = Test_PS5_Prices()
        email = EmailSender()
        validation.test_Obtain_Prices()
        email.test_send_email()
        print("\n=====> Fin del TestCase para Mercado Libre <=====\n")

if __name__ == '__main__':
    pytest.main("[-s]")