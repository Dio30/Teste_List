# Teste_List

## Esse projeto foi feito em python/django utilizando um ambiente virtual para que as bibliotecas instaladas nesse projeto não fossem para a pasta base do python ou para o computador em que trabalho.

## Foi feito como pedido no teste que uma pessoa somente poderia ter 3 carros cadastrados em seu nome e para que isso fosse possivel foi feita uma validação no forms.py em que se alguem tentar cadastrar mais de 3 carros com o mesmo proprietário apareceria um erro inpedindo de cadastrar.

## Tambem foi feito com pedido poder cadastrar novos proprietários com um checkbox indicando se é um possivel comprador ou não, infelizmente não consegui implementar algo que pudesse identificar automaticamente quando se um proprietário não tiver nenhum carro cadastrado em seu nome ele seja um possivel comprador como pedido.

## Tambem foi feito com pedido que o veiculo cadstrado só teria 3 cores entre "yellow", "blue" ou "gray" e os modelos "hatch", "sedan" ou "convertible", os carros só poderão ser cadastrados se tiver um proprietário para poder escolher.

## Como solicitado foram escritos testes unitarios, na pasta list foram escritos testes para o model testando se a criação do model estava funcionando corretamente, forms testando se o formulario inserido estava valido e views para testar se a conexao HTTP estava ok e se o status_code estava em 200 e tambem foi testado se o template inserido no views.py estava correto, na pasta proprietários foram feitos testes no model tambem para testar se a criação do model estava funcionando corretamente e no views tambem para testar se a conexao HTTP estava ok e se o status_code estava em 200 e tambem foi testado se o template inserido no views.py estava correto.

## O projeto não foi feito em docker pois ainda não sei como funciona mas se me derem a oportunidade em um futuro projeto na empresa farei de tudo para aprender como funciona o docker e farei o possivel para que o projeto seja um sucesso e que esteja funcionando perfeitamente através de testes que farei.
