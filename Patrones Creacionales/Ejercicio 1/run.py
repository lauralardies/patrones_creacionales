from main import client_code
from abstract_factory import ConcreteAnalisisFactory, ConcreteGraficasFactory


if __name__ == "__main__":    
    
    print('Analizamos las activaciones por día.')

    print("Client: Testing la factoría de Análisis Estadísticos:")
    client_code(ConcreteAnalisisFactory())

    print("\nClient: Testing la factoría de Visualización de Datos:")
    client_code(ConcreteGraficasFactory())
    print("Las gráficas se han guardado en la carpeta graficas.")