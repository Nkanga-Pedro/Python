''''
Transferencia bancaria com as cosideracoes seguintes:

1- Temos os dados seguintes: Conta bancaria, nome completo, saldo de deposito, data deposito
2- Faca transferencia com os dados seguintes: numero de transferencia, conta bancaria, valor transferido,tipo transferencia, data transferencia.
3- Calcule o saldo final, a saber que se o prazo entre data deposito e a data transferencia nao ultrapassar 2 dias: a taxa transferencia é de 5% comissao de 2% para tipo transferencia nacional para o tipo transferencia internacional a taxa transferencia é de 10% comissao de 4%. Caso o prazo entre data deposito e a data transferencia ultrapassar 2 dias, paga-se um juro de 5% crescente com o incremento de 2% a partir do quarto dia ate adiante.
4- exibir no fim : conta bancaria, nome completo, saldo deposito, data deposito, numero transferencia, valor transferido, tipo transferencia, a taxa transferencia, a comissao, juro, saldo final, data transferencia.

NB. observa no "observacao" o tipo transferencia efetuada nacional ou internacional

Nkanga Pedro - 2023
'''
import datetime

class BankAccount:
    def __init__(self, account_number, full_name, balance, deposit_date):
        self.account_number = account_number
        self.full_name = full_name
        self.balance = balance
        self.deposit_date = deposit_date
        self.transfers = []

    def transfer(self, transfer_number, to_account, amount, transfer_type, transfer_date):
        transfer_fee = 0
        commission = 0
        interest = 0
        days_diff = (transfer_date - self.deposit_date).days

        if transfer_type == "national":
            if days_diff <= 2:
                transfer_fee = 0.05 * amount
                commission = 0.02 * amount
            else:
                transfer_fee = 0.05 * amount
                interest = 0.05 + 0.02 * (days_diff - 2)
        elif transfer_type == "international":
            if days_diff <= 2:
                transfer_fee = 0.10 * amount
                commission = 0.04 * amount
            else:
                transfer_fee = 0.10 * amount
                interest = 0.05 + 0.02 * (days_diff - 2)
        else:
            raise ValueError("Invalid transfer type")

        self.balance -= (amount + transfer_fee + commission + interest)
        self.transfers.append({
            "transfer_number": transfer_number,
            "to_account": to_account,
            "amount": amount,
            "transfer_type": transfer_type,
            "transfer_fee": transfer_fee,
            "commission": commission,
            "interest": interest,
            "transfer_date": transfer_date,
            "balance_after_transfer": self.balance
        })

    def __str__(self):
        transfer_str = "\n".join([f"{t['transfer_number']}: {t['amount']} ({t['transfer_type']}) on {t['transfer_date']} - balance after transfer: {t['balance_after_transfer']}" for t in self.transfers])
        return f"Account number: {self.account_number}\nFull name: {self.full_name}\nDeposit date: {self.deposit_date}\nBalance: {self.balance}\nTransfers:\n{transfer_str}"

account = BankAccount(
    input("Conta bancaria: "),
    input("Nome completo: "),
    float(input("Saldo de deposito: ")),
    datetime.date(*map(int, input("Data deposito (YYYY MM DD): ").split()))
)
account.transfer(
    int(input("Numero de transferencia: ")),
    input("Conta bancaria destino: "),
    float(input("Valor transferido: ")),
    input("Tipo transferencia (national ou international): "),
    datetime.datetime.strptime(input("Data transferencia (YYYY-MM-DD): "), '%Y-%m-%d').date()
)
print('\nResultado de transferencia bancaria (Nacional ou Internacional)')
print(account)
