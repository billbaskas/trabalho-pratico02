class Condutor:
    def __init__(self, nome, numero_cnh):
        self.nome = nome
        self.numero_cnh = numero_cnh

    def exibir_dados(self):
        return f"Condutor: {self.nome} | CNH: {self.numero_cnh}"


class Contrato:
    def __init__(self, data_inicio, data_termino, valor_total,
                 nome_condutor, cnh_condutor, status="ativo"):
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.valor_total = valor_total
        self.status = status
        self.condutor = Condutor(nome_condutor, cnh_condutor)

    def finalizar(self):
        self.status = "finalizado"

    def cancelar(self):
        self.status = "cancelado"

    def exibir_dados(self):
        return (f"Contrato {self.data_inicio} a {self.data_termino} | "
                f"R$ {self.valor_total:.2f} | {self.status}\n"
                f"  {self.condutor.exibir_dados()}")


if __name__ == "__main__":
    contrato = Contrato("01/10/2026", "05/10/2026", 600.0,
                        "João Silva", "12345678900")
    print(contrato.exibir_dados())

    contrato.finalizar()
    print(contrato.exibir_dados())
