///Desenvolva, de forma incremental, no ambiente repl.it, um programa em
//linguagem C que tem como objetivo gerenciar notas de uma turma que
//atenda aos seguintes requisitos:
//1. Pedir ao usuário o número de alunos que fazem parte da turma e
//alocar corretamente memória para armazenar as notas dos alunos, que serão expressos de 0 a 10.
//2. Utilizar um subprograma para solicitar ao usuário as notas de cada
//um dos alunos.
//3. Criar um subprograma para calcular a média de notas da turma.
//4. Exibir de forma clara e organizada :
//a. uma mensagem explicando ser o resultado final;
//b. a nota individual de cada aluno, indicando ao lado se aprovado ou não conforme regras da Unilasalle;

#include <stdio.h>
#include <math.h>

int main(void) {
  int pos = 0;
  int numero;
  float notas[11];
  float media = 0;

  printf("\n\nOlá, seja bem vindo!\n\nPor gentileza, digite o número de alunos que fazem parte da turma: ");
  scanf("%i", &numero);
  printf("O número de alunos é: %d", numero);
  printf("\n");
  //Subprograma
  for (int i = 0; i < numero; i++){
    float x = 0;
    printf("\nNota do aluno %d: ", i+1);
    scanf("%f", &notas[i]);
  }

  //Subprograma
  for (int i = 0; i < numero; i++){
     media = notas[i] + media;
  }
  printf("\n\nMédia dos %d alunos: %.2f", numero, media/numero);

  printf("\nAqui temos o resultado final da turma no semestre:\n");
  printf("\n");
  for (int i = 0; i< numero; i++){
     printf("\nNota do aluno %d: %.2f", i+1, notas[i]);
     if (notas[i] >= 6){
        printf("\n -> Aluno aprovado.\n");
     } else {
        printf("\n -> Aluno reprovado.\n");
     }
  }
  printf("Código da turma: 0132");
  return 0; 
}
void pedeNotas(int num){
  
}
