from django.db import models


class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo_veiculo = models.CharField(max_length=50)
    condutor_responsavel = models.ForeignKey(
        "Condutor", on_delete=models.PROTECT, related_name="veiculos")

    def __str__(self):
        return f"{self.placa} - {self.modelo_veiculo}"


class Kilometragem(models.Model):
    veiculo = models.ForeignKey(
        Veiculo, on_delete=models.PROTECT, related_name="kilometragens")
    km_inicial = models.PositiveIntegerField()
    km_final = models.PositiveIntegerField()

    def __str__(self):
        return f"Kilometragem de {self.veiculo.placa}: {self.km_inicial} - {self.km_final}"


class Horario(models.Model):
    veiculo = models.ForeignKey(
        Veiculo, on_delete=models.PROTECT, related_name="horarios")
    hora_entrada = models.TimeField()
    hora_saida = models.TimeField()

    def __str__(self):
        return f"Horário de {self.veiculo.placa}: {self.hora_saida} - {self.hora_entrada}"


class Condutor(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nome} - {self.matricula}"


class Data(models.Model):
    veiculo = models.ForeignKey(
        Veiculo, on_delete=models.PROTECT, related_name="datas")
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Data de cadastro de {self.veiculo.placa}: {self.data_cadastro}"
