import sys
import csv

def lerArquivo(arq):  ## Lê o arquivo csv com as notas
    with open(arq, "r") as notas_csv:
        dados = []
        materias = csv.DictReader(notas_csv, delimiter=",")
        for materia in materias:
            dados.append(materia)
    return dados

class CalculoDoCR(object):
    def __init__(self, notas): 
        self.notas = notas
        self.calculaCr(notas)
        

    def calculaCr(self, nota):  ## efetua o calculo e imprime os cr's e as matriculas
        notaCargaHoraria = 0
        cargaHorariaTotal = 0
        matricula = nota[0]["MATRICULA"]
        print("------- O CR dos alunos é: --------")
        for item in range(len(nota)):
                    
            if matricula == nota[item]["MATRICULA"]:
                
                notaCargaHoraria += int(nota[item]["CARGA_HORARIA"])* int(nota[item]["NOTA"]) 
                cargaHorariaTotal += int(nota[item]["CARGA_HORARIA"])
            else:
               
                print(matricula, " -  %.1f" %(float(notaCargaHoraria / cargaHorariaTotal)))
                matricula = nota[item]["MATRICULA"]
                notaCargaHoraria = 0
                cargaHorariaTotal = 0
     
        print(matricula, " -  %.1f" %(float(notaCargaHoraria / cargaHorariaTotal)))
        

def main():

    notas        = lerArquivo("notas.csv")
    mediaCr      = CalculoDoCR(notas)



if __name__ == '__main__':
    sys.exit(main())
