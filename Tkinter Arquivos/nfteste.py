import xml.etree.ElementTree as ET

class NotaFiscal:
    def __init__(self, numero, data_emissao, valor):
        self.numero = numero
        self.data_emissao = data_emissao
        self.valor = valor

    def gerar_xml(self):
        nota = ET.Element("NotaFiscal")
        ET.SubElement(nota, "Numero").text = str(self.numero)
        ET.SubElement(nota, "DataEmissao").text = self.data_emissao
        ET.SubElement(nota, "Valor").text = str(self.valor)

        tree = ET.ElementTree(nota)
        tree.write(f"nota_fiscal_{self.numero}.xml", encoding='utf-8', xml_declaration=True)

# Exemplo de uso
nf = NotaFiscal(numero=1, data_emissao="2023-10-01", valor=100.00)
nf.gerar_xml()