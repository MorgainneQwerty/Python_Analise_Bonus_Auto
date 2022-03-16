import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2628af3ef76cd40c0089afb9bfa8d7bf"
# Your Auth Token from twilio.com/console
auth_token = "efcf79aafdb10f0a995188d8825be60d"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, 'Vendas'].values[0]
        print(
            f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+55112233445",
            from_="+123456789901",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
