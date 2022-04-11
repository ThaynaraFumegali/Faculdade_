// Thaynara Fumegali 

#include <stdio.h>

int main(void) {

  printf("=======================================\n\t\tCalculadora de sálario\n=======================================\n\n");
  float salario;
  int classificacao;
  printf("Digite o salário atual do funcionário: \n\n\t R$ ");
  scanf("%f",&salario);
  printf("Recebido!\n\nPor favor, digite a opção de alteração de salário, sendo:\n\t 1 - Para downgrade\n\t 2 - Para upgrade ou promoção\nDigite sua opção: ");
  scanf("%i",&classificacao);

  if(classificacao == 1){
    printf("\n\nO novo salário ficou com o valor de R$ %.2f", (salario) - (salario * 0.1));
  } else {
    printf("\n\nO novo salário ficou com o valor de R$ %.2f", (salario) + (salario * 0.2));
  }
  
return 0;
}