import warnings
import zeep
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import exceptions
from os import system as sys

class ApiCorreios():

    URL = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'  # noqa


    def fetch_address(self, cep):

        try:
            with warnings.catch_warnings():

                # Desabilitamos o warning
                warnings.simplefilter('ignore', InsecureRequestWarning)
                warnings.simplefilter('ignore', ImportWarning)

                client = zeep.Client(self.URL)

                address = client.service.consultaCEP(cep)

                return {
                    'bairro': getattr(address, 'bairro', ''),
                    'cep': getattr(address, 'cep', ''),
                    'cidade': getattr(address, 'cidade', ''),
                    'logradouro': getattr(address, 'end', ''),
                    'uf': getattr(address, 'uf', ''),
                    'complemento': getattr(address, 'complemento2', ''),
                }

        except zeep.exceptions.Fault as e:
            raise exceptions.BaseException(e)

rodar = True

while rodar:
    sys("cls")
    cep = input("\nCEP: ")

    cepf = cep[:5] + "-" + cep[5:8] 
    print(f"\nBuscando o CEP {cepf} ...")

    try:
        endereco = ApiCorreios().fetch_address(cep)

        print("\nResultado da busca")
        print("*" * 30)
        print(f"Bairro: {endereco['bairro']}")
        print(f"CEP: {cepf}")
        print(f"Cidade: {endereco['cidade']}")
        print(f"Logradouro: {endereco['logradouro']}")
        print(f"UF: {endereco['uf']}")
        print(f"Complemento: {endereco['complemento']}")
        print("*" * 30)
        print("\n")
        
    except Exception as e:
        print(f"\nErro: {e}\n")

    continuar = str()

    while continuar != "Y" and continuar != "n":
        continuar = input("Continuar? (Y/n) ")

        if continuar == "Y":
            break
        elif continuar == "n":
            rodar = False
        else:
            print("\nOpção inválida!")