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
        
       
        print("------- O CR dos alunos é: --------")
        self.calculaCr(notas,"MATRICULA")
        
        
        """
        print("----- Média de CR dos cursos ------")
        self.calculaCr(notas,"COD_CURSO")
        """
        
    def calculaCr(self, nota,coluna):  ## efetua o calculo e imprime os cr's e as matriculas
        notaCargaHoraria = 0
        cargaHorariaTotal = 0
        metodo = nota[0][coluna]
        ##crCalculado = {}
        for item in range(len(nota)):
            
                    
            if metodo == nota[item][coluna]:
                
                notaCargaHoraria += int(nota[item]["CARGA_HORARIA"])* int(nota[item]["NOTA"]) 
                cargaHorariaTotal += int(nota[item]["CARGA_HORARIA"])
            else:

                if cargaHorariaTotal>0:
                    print(metodo, " -  %.1f" %(float(notaCargaHoraria / cargaHorariaTotal)))                      
                metodo = nota[item][coluna]
                notaCargaHoraria = 0
                cargaHorariaTotal = 0
     
        print(metodo, " -  %.1f" %(float(notaCargaHoraria / cargaHorariaTotal)))
        print("-----------------------------------")
        

def main():

    notas        = lerArquivo("notas.csv")
    mediaCr      = CalculoDoCR(notas)



if __name__ == '__main__':
    sys.exit(main())
