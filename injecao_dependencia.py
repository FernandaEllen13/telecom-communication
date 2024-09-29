# Interface para comportamento de comunicação
class CommunicationBehavior:
    def execute(self):
        pass

# Implementação de comportamento para comunicação via SMS
class SMSCommunication(CommunicationBehavior):
    def execute(self):
        return "Enviando mensagem via SMS!"

# Implementação de comportamento para comunicação via chamada de voz
class VoiceCallCommunication(CommunicationBehavior):
    def execute(self):
        return "Realizando chamada de voz!"

# Implementação de comportamento para comunicação via internet (e.g. VoIP)
class InternetCommunication(CommunicationBehavior):
    def execute(self):
        return "Realizando comunicação via Internet (VoIP)!"

# Serviço que utiliza o comportamento de comunicação
class CommunicationService:
    def __init__(self, behavior: CommunicationBehavior):
        self.behavior = behavior
    
    def perform_communication(self):
        action = self.behavior.execute()
        print(action)

# Função para mostrar o menu e obter a escolha do usuário
def show_menu():
    print("Escolha o método de telecomunicação:")
    print("1. SMS")
    print("2. Chamada de Voz")
    print("3. Comunicação via Internet (VoIP)")
    choice = input("Digite o número da sua escolha: ")
    return choice

# Função principal que gerencia a lógica do programa
def main():
    while True:
        choice = show_menu()
        
        if choice == '1':
            communication_behavior = SMSCommunication()
        elif choice == '2':
            communication_behavior = VoiceCallCommunication()
        elif choice == '3':
            communication_behavior = InternetCommunication()
        else:
            print("Escolha inválida! Tente novamente.")
            continue

        # Injetando o comportamento escolhido pelo usuário no serviço
        comm_service = CommunicationService(communication_behavior)
        comm_service.perform_communication()

        # Perguntar ao usuário se deseja realizar outra ação
        again = input("Deseja realizar outra comunicação? (s/n): ")
        if again.lower() != 's':
            print("Saindo do programa...")
            break

# Executa o programa
if __name__ == "__main__":
    main()
