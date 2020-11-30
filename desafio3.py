import sys
import csv


class CalculoDoCR(object):
    def __init__(self, nome_arquivo):
        self.lerArquivo(nome_arquivo)




    def lerArquivo(self, arq):  ## Lê o arquivo csv com as notas
        with open(arq, "r") as notas_csv:
            dados = []
            materias = csv.DictReader(notas_csv, delimiter=",")
            for materia in materias:
                dados.append(materia)
        self.calculaCr(dados)



    def calculaCr(self, disciplinas):  ## efetua o calculo e imprime os cr's e as matriculas
        cursos = [] 
        notaCargaHoraria = 0
        cargaHorariaTotal = 0
        matricula = disciplinas[0]["MATRICULA"]
        print("------- O CR dos alunos é: --------")
        for item in range(len(disciplinas)):
            if int(disciplinas[item]["COD_CURSO"]) not in cursos:
                cursos.append(int(disciplinas[item]["COD_CURSO"]))
            if matricula == disciplinas[item]["MATRICULA"]:
                
                notaCargaHoraria += int(disciplinas[item]["CARGA_HORARIA"])* int(disciplinas[item]["NOTA"]) 
                
                cargaHorariaTotal += int(disciplinas[item]["CARGA_HORARIA"])
            else:
               
                print(matricula, " -  %.1f" %(float(notaCargaHoraria / cargaHorariaTotal)))
                matricula = disciplinas[item]["MATRICULA"]
                notaCargaHoraria = 0
                cargaHorariaTotal = 0
     
        print(matricula, " -  %.1f" %(float(notaCargaHoraria / cargaHorariaTotal)))
        



def main():
    CalculoDoCR("notas.csv")
    


if __name__ == '__main__':
    sys.exit(main())
