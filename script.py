from iqoptionapi.stable_api import IQ_Option
from colorama import Fore, init
from datetime import datetime
import os,sys,time
init(autoreset=True, convert=True)

#$ VARIAVEIS
TIPO_DE_CONTA = None
VALOR_DE_ENTRADA = None
LUCRO_ATUAL = 0
ATIVO = None
STOP_WIN = None
STOP_LOSS = None



def limparTerminal():
    os.system("cls")
def realizarLoginNaIqOption():
    print(f"{Fore.GREEN}Login Iq Option {Fore.RESET} digite seu email da Iq Option:", end=" ")
    email = input()
    print(f"{Fore.GREEN}Login Iq Option {Fore.RESET} digite sua senha da Iq Option:", end=" ")
    senha = input()
    api = IQ_Option(email, senha,active_account_type="PRACTICE")
    if not api.check_connect():
        api.connect()
    if(api.check_connect()):
        limparTerminal()
        print("{}Login Iq Option{} Conectado, R${}(Conta de Treinamento)\n".format(Fore.GREEN, Fore.RESET, api.get_balance()))
        return {"status":True, "api":api}
    else:
        limparTerminal()
        print(f"{Fore.RED}Login Iq Option{Fore.RESET} email/senha incorretos, tente novamente...")
    return {"status":False,"api":None}
def definirTipoDeConta(api):
    global TIPO_DE_CONTA
    while True:
        try:
            print(f"{Fore.GREEN}Tipo de Conta(R$){Fore.RESET} Escolha o tipo de conta:")
            api.change_balance("PRACTICE")
            print("   1. Conta de Treinamento(R${})".format(api.get_balance()))
            api.change_balance("REAL")
            print("   2. Conta Real(R${})".format(api.get_balance()))
            escolha = int(input("   digite sua escolha:"))
            if(escolha == 1):
                limparTerminal()
                api.change_balance("PRACTICE")
                print("{}Login Iq Option{} Conectado, R${}({})\n".format(Fore.GREEN, Fore.RESET, api.get_balance(), "Conta de Treinamento"))
                print("{}Tipo de Conta(R$){} Conta de Treinamento(R${}) escolhilada com sucesso\n".format(Fore.GREEN, Fore.RESET,api.get_balance()))
                TIPO_DE_CONTA = "PRACTICE"
                return "PRACTICE"
            elif(escolha == 2):
                limparTerminal()
                api.change_balance("REAL")
                print("{}Login Iq Option{} Conectado, R${}({})\n".format(Fore.GREEN, Fore.RESET, api.get_balance(), "Conta Real"))
                print("{}Tipo de Conta(R$){} Conta Real(R${}) escolhilada com sucesso\n".format(Fore.GREEN,Fore.RESET,api.get_balance()))
                TIPO_DE_CONTA = "REAL"
                return "REAL"
            else:
                print(f"{Fore.RED}Tipo de Conta(R$){Fore.RESET} escolha inválida, digite 1 para conta de treinamento(R$) e 2 para conta real(R$)")
        except Exception as erro:
            print(f"{Fore.RED}Tipo de Conta(R$){Fore.RESET} escolha inválida, digite 1 para conta de treinamento(R$) e 2 para conta real(R$)")
def definirGerenciamento():
    global TIPO_DE_CONTA,VALOR_DE_ENTRADA, STOP_WIN, STOP_LOSS
    while True:
        try:
            print(f"{Fore.GREEN}Gerenciamento{Fore.RESET} digite o valor de entrada(R$):",end=" ")
            VALOR_DE_ENTRADA = float(input())
            print(f"{Fore.GREEN}Gerenciamento{Fore.RESET} valor de entrada definido: R${VALOR_DE_ENTRADA} reais")
            break
        except Exception as erro:
            print(f"{Fore.RED}Gerenciamento{Fore.RESET} valor de entrada(R$) inválido, tente novamemnte...")
    while True:
        try:
            print(f"{Fore.GREEN}Gerenciamento{Fore.RESET} digite o valor de stop win(R$):",end=" ")
            STOP_WIN = float(input())
            print(f"{Fore.GREEN}Gerenciamento{Fore.RESET} valor de stop win(R$) definido: R${STOP_WIN} reais")
            break
        except Exception as erro:
            print(f"{Fore.RED}Gerenciamento{Fore.RESET} valor de stop win(R$) inválido, tente novamemnte...")
    while True:
        try:
            print(f"{Fore.GREEN}Gerenciamento{Fore.RESET} digite o valor de stop loss(R$):",end=" ")
            STOP_LOSS = float(input())
            print(f"{Fore.GREEN}Gerenciamento{Fore.RESET} valor de stop loss(R$) definido: R${STOP_LOSS} reais")
            break
        except Exception as erro:
            print(f"{Fore.RED}Gerenciamento{Fore.RESET} valor de stop loss(R$) inválido, tente novamemnte...")
    limparTerminal()
    print("{}Login Iq Option{} Conectado, R${}({})\n".format(Fore.GREEN, Fore.RESET, api.get_balance(), "Conta de Treinamento" if TIPO_DE_CONTA == "PRACTICE" else "Conta Real"))
    print("{}Tipo de Conta(R$){} {}(R${}) escolhilada com sucesso\n".format(Fore.GREEN, Fore.RESET,"Conta de Treinamento" if TIPO_DE_CONTA == "PRACTICE" else "Conta Real",api.get_balance()))
    print(f"{Fore.GREEN}Gerenciamento{Fore.RESET} Gerenciamento Definido:\n   valor de entrada(R$): R${VALOR_DE_ENTRADA} reais\n   stop win(R$): R${STOP_WIN} reais\n   stop loss(R$): R${STOP_LOSS} reais\n")
def escolherEstrategia():
    while True:
        try:
            print(f"""{Fore.GREEN}Estrátegia{Fore.RESET} escolha estrátegia para operar 100% no automático:
   1. MHI maioria
   2. MHI minoria
   3. MHI2 maioria
   4. MHI2 minoria
   5. MHI3 maioria
   6. MHI3 minoria
   digite sua escolha: """, end="")
            escolha = int(input())
            estrategia = None
            if(escolha == 1):
                estrategia = "MHI maioria"
            elif(escolha == 2):
                estrategia = "MHI minoria"
            elif(escolha == 3):
                estrategia = "MHI2 maioria"
            elif(escolha == 4):
                estrategia = "MHI2 minoria"
            elif(escolha == 5):
                estrategia = "MHI3 maioria"
            elif(escolha == 6):
                estrategia = "MHI3 minoria"
            else:
                print(f"{Fore.RED}Estrátegia{Fore.RESET} escolha de estrátegia inválida, tente novamente...")
            
            if(estrategia):
                limparTerminal()
                print("{}Login Iq Option{} Conectado, R${}({})\n".format(Fore.GREEN, Fore.RESET, api.get_balance(), "Conta de Treinamento" if TIPO_DE_CONTA == "PRACTICE" else "Conta Real"))
                print("{}Tipo de Conta(R$){} {}(R${}) escolhilada com sucesso\n".format(Fore.GREEN, Fore.RESET,"Conta de Treinamento" if TIPO_DE_CONTA == "PRACTICE" else "Conta Real",api.get_balance()))
                print(f"{Fore.GREEN}Gerenciamento{Fore.RESET} Gerenciamento Definido:\n   valor de entrada(R$): R${VALOR_DE_ENTRADA} reais\n   stop win(R$): R${STOP_WIN} reais\n   stop loss(R$): R${STOP_LOSS} reais\n")
                print(f"{Fore.GREEN}Estrátegia{Fore.RESET} Estrátegia escolhida: {estrategia}\n")
                return estrategia
        except Exception as erro:
            print(f"{Fore.RED}Estrátegia{Fore.RESET} escolha de estrátegia inválida, tente novamente...")
def escolherAtivo():
    global ATIVO
    while True:
        print(f"""{Fore.GREEN}Ativo{Fore.RESET} Escolha seu ativo de investimento""")
        ativos = api.get_all_open_time()
        lista_de_ativos_abertos = []
        for ativo in ativos["binary"]:
            if ativos["binary"][ativo]["open"]:
                lista_de_ativos_abertos.append(ativo)
        for index,ativo in enumerate(lista_de_ativos_abertos):
            print(f"   {index+1}. {ativo}")
        try:
            escolha = int(input("   digite sua escolha:"))
            try:
                ATIVO = lista_de_ativos_abertos[escolha]
                limparTerminal()
                print("{}Login Iq Option{} Conectado, R${}({})\n".format(Fore.GREEN, Fore.RESET, api.get_balance(), "Conta de Treinamento" if TIPO_DE_CONTA == "PRACTICE" else "Conta Real"))
                print("{}Tipo de Conta(R$){} {}(R${}) escolhilada com sucesso\n".format(Fore.GREEN, Fore.RESET,"Conta de Treinamento" if TIPO_DE_CONTA == "PRACTICE" else "Conta Real",api.get_balance()))
                print(f"{Fore.GREEN}Gerenciamento{Fore.RESET} Gerenciamento Definido:\n   valor de entrada(R$): R${VALOR_DE_ENTRADA} reais\n   stop win(R$): R${STOP_WIN} reais\n   stop loss(R$): R${STOP_LOSS} reais\n")
                print(f"{Fore.GREEN}Estrátegia{Fore.RESET} Estrátegia escolhida: {estrategia}\n")
                print(f"{Fore.GREEN}Ativo{Fore.RESET} Ativo escolhido: {ATIVO}\n")
                return 
            except Exception as erro:
                print(f"{Fore.RED}Ativo{Fore.RESET} escolha inválida, tente novamente...")
        except Exception as erro:
            print(f"{Fore.RED}Ativo{Fore.RESET} escolha inválida, tente novamente...")
def mhi(estrategia, ativo, timeframe=1):
    global VALOR_DE_ENTRADA, LUCRO_ATUAL, STOP_LOSS, STOP_LOSS
    try:
        print("Robô 100% Automático Iniciado ©\n| agora basta aguardar as operações serem realizadas\n")
        while True:
            horario = float(datetime.now().strftime("%M.%S")[1:])     
            entrar = True if(horario >= 4.8 and horario <= 5.0 or horario >= 9.58) else False 
            if entrar:
                direcao = None
                velas = api.get_candles(ativo, timeframe*60,3,time.time())
                velas[0] = "g" if velas[0]["open"] < velas[0]["close"] else "r" if velas[0]["open"] > velas[0]["close"] else 'd'
                velas[1] = "g" if velas[1]["open"] < velas[1]["close"] else "r" if velas[1]["open"] > velas[1]["close"] else 'd'
                velas[2] = "g" if velas[2]["open"] < velas[2]["close"] else "r" if velas[2]["open"] > velas[2]["close"] else 'd'
                cores = velas[0]+" "+velas[1]+" "+velas[2]
                if(estrategia == "MHI minoria" or estrategia == "MHI maioria"):
                    if(estrategia == "MHI minoria"):
                        if cores.count("r") > cores.count("g") and cores.count("d") == 0 : direcao = "CALL"
                        if cores.count("g") > cores.count("r") and cores.count("d") == 0 : direcao = "PUT"
                    if(estrategia == "MHI maioria"): 
                        if cores.count("r") > cores.count("g") and cores.count("d") == 0 : direcao = "PUT"
                        if cores.count("g") > cores.count("r") and cores.count("d") == 0 : direcao = "CALL"
                
                if direcao != None:
                    entrar = False
                    while True:
                        if(estrategia.split(" ")[0].strip() == "MHI"):
                            time.sleep(60)
                            vela_atual = api.get_candles(ativo, timeframe*60,1,time.time())
                            vela_atual[0] = "g" if vela_atual[0]["open"] < vela_atual[0]["close"] else "r" if vela_atual[0]["open"] > vela_atual[0]["close"] else "d"
                            #$ 1° Entrada(Sem Gale)
                            if(vela_atual[0] == "g" and direcao == "CALL"):
                                break
                            if(vela_atual[0] == "r" and direcao == "PUT"):
                                break
                            if(vela_atual[0] == "d"):
                                break
                            #$ 2° Entrada(1 Martingale)
                            time.sleep(60)
                            vela_atual = api.get_candles(ativo, timeframe*60,1,time.time())
                            vela_atual[0] = "g" if vela_atual[0]["open"] < vela_atual[0]["close"] else "r" if vela_atual[0]["open"] > vela_atual[0]["close"] else "d"
                            #$ 1° Entrada(Sem Gale)
                            if(vela_atual[0] == "g" and direcao == "CALL"):
                                break
                            if(vela_atual[0] == "r" and direcao == "PUT"):
                                break
                            if(vela_atual[0] == "d"):
                                break
                            entrar = True
                            break
                        if(estrategia.split(" ")[0].strip() == "MHI2"):
                            time.sleep(120)
                            vela_atual = api.get_candles(ativo, timeframe*60,1,time.time())
                            vela_atual[0] = "g" if vela_atual[0]["open"] < vela_atual[0]["close"] else "r" if vela_atual[0]["open"] > vela_atual[0]["close"] else "d"
                            #$ 1° Entrada(Sem Gale)
                            if(vela_atual[0] == "g" and direcao == "CALL"):
                                break
                            if(vela_atual[0] == "r" and direcao == "PUT"):
                                break
                            if(vela_atual[0] == "d"):
                                break
                            #$ 2° Entrada(1 Martingale)
                            time.sleep(60)
                            vela_atual = api.get_candles(ativo, timeframe*60,1,time.time())
                            vela_atual[0] = "g" if vela_atual[0]["open"] < vela_atual[0]["close"] else "r" if vela_atual[0]["open"] > vela_atual[0]["close"] else "d"
                            #$ 1° Entrada(Sem Gale)
                            if(vela_atual[0] == "g" and direcao == "CALL"):
                                break
                            if(vela_atual[0] == "r" and direcao == "PUT"):
                                break
                            if(vela_atual[0] == "d"):
                                break
                            entrar = True
                            break
                        if(estrategia.split(" ")[0].strip() == "MHI3"):
                            time.sleep(180)
                            vela_atual = api.get_candles(ativo, timeframe*60,1,time.time())
                            vela_atual[0] = "g" if vela_atual[0]["open"] < vela_atual[0]["close"] else "r" if vela_atual[0]["open"] > vela_atual[0]["close"] else "d"
                            #$ 1° Entrada(Sem Gale)
                            if(vela_atual[0] == "g" and direcao == "CALL"):
                                break
                            if(vela_atual[0] == "r" and direcao == "PUT"):
                                break
                            if(vela_atual[0] == "d"):
                                break
                            #$ 2° Entrada(1 Martingale)
                            time.sleep(60)
                            vela_atual = api.get_candles(ativo, timeframe*60,1,time.time())
                            vela_atual[0] = "g" if vela_atual[0]["open"] < vela_atual[0]["close"] else "r" if vela_atual[0]["open"] > vela_atual[0]["close"] else "d"
                            #$ 1° Entrada(Sem Gale)
                            if(vela_atual[0] == "g" and direcao == "CALL"):
                                break
                            if(vela_atual[0] == "r" and direcao == "PUT"):
                                break
                            if(vela_atual[0] == "d"):
                                break
                            entrar = True
                            break
                        
                    if entrar:
                        if LUCRO_ATUAL < STOP_WIN and LUCRO_ATUAL > -STOP_LOSS:
                            status,id = api.buy(VALOR_DE_ENTRADA,ativo,direcao,1)
                            if(status):
                                print("\n{}{}{} Operação Executada com R${}".format(Fore.LIGHTBLACK_EX,datetime.now().strftime("%d/%m/%Y %H:%M:%S"), Fore.RESET, VALOR_DE_ENTRADA))
                                print(f"| {ativo} {direcao} {timeframe}M")
                                status,lucro = api.check_win_v4(id)
                                if(status == "win"):
                                    LUCRO_ATUAL += lucro
                                    print(f"{Fore.GREEN}[*]{Fore.RESET} Win, ganho de R${lucro:,.2f} reais | Lucro Atual: R${LUCRO_ATUAL:,.2f} reais")
                                else:
                                    LUCRO_ATUAL -= abs(lucro)
                                    print(f"{Fore.RED}[*]{Fore.RESET} Loss, perca de -R${abs(lucro):,.2f} reais | Lucro Atual: R${LUCRO_ATUAL:,.2f} reais")
                                    
                            else:
                                print("\n{}{}{} Operação não executada com R${}".format(Fore.LIGHTBLACK_EX,datetime.now().strftime("%d/%m/%Y %H:%M:%S"), Fore.RESET, VALOR_DE_ENTRADA))
                                print(f"| {Fore.RED}{id}")
        
                        else:
                            if LUCRO_ATUAL > STOP_WIN:
                                print(F"\nSTOP WIN ATINGIDO, LUCRO DE R${LUCRO_ATUAL:,.2f} REAIS")
                            else:
                                print(F"\nSTOP LOSS ATINGIDO, PERCA DE -R${abs(LUCRO_ATUAL):,.2f} REAIS")
    except Exception as erro:
        print(f"\n{Fore.RED}{erro}")                                                     
#$ Limpar Terminal(Windows/Linux)
limparTerminal()


#$ Informações de Login(Autenticação na Iq Option)
try:
    while True:
        response = realizarLoginNaIqOption()
        if(response["status"] == True): #$ Conectado na Conta de Treinamento(R$)
            api = response["api"]
            break
        else:
            #$ Tentar Novamente
            pass
except Exception as erro:
    print(f"{Fore.RED}{erro}")
    sys.exit()

#$ Definir Tipo de Conta(R$)
tipo_de_conta = definirTipoDeConta(api)
api.change_balance(tipo_de_conta)

#$ Definir Gerenciamento de Banca(R$)
definirGerenciamento()

#$ Escolher Estrátegia
estrategia = escolherEstrategia()

#$ Escolher Ativo
escolherAtivo()

#$ Operar Mhi(100% automático)
mhi(estrategia=estrategia, ativo=ATIVO)

