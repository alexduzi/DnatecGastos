
from django.db import models


class Pagamento(models.Model):
    
    pago = models.BooleanField(default=False)
    data = models.DateField('Data que o pagamento foi efetuado')
    
    def __str__(self):
        return 'Pago: %s Data: %s' %(str(self.pago), str(self.data))

class Gasto(models.Model):
   
    nome = models.CharField(max_length=30)
    data = models.DateField('Data que foi efetuado o gasto')
    valor = models.FloatField()
    descricao = models.CharField(max_length=800)
    pagamento = models.ForeignKey(Pagamento,None)
    def __str__(self):
        return 'Nome: %s Data: %s Valor: %s Descricao: %s' %(self.nome, str(self.data), str(self.valor), self.descricao)

class ContaBanco(models.Model):
    
    nome_banco = models.CharField(max_length=30)
    agencia = models.CharField(max_length=30)
    conta = models.CharField(max_length=30)
    saldo_conta_corrente = models.FloatField()
    gastos = models.ManyToManyField(Gasto, None)
    def __str__(self):
        return 'Nome banco: %s Agencia: %s Conta: %s Saldo: %s' %(self.nome_banco, 
                                                                    self.agencia, 
                                                                    self.conta, 
                                                                    str(self.saldo_conta_corrente))



