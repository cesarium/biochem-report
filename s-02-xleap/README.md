# Instruções Gerais
## Carregar um PDB no xleap
1. Abra o ***xleap***
> xleap
2. Dentro do programa xleap escreva as indicações seguintes para carregar as várias bibliotecas de parâmetros:
> source leaprc.ff03
> source leaprc.gaff
> loadamberparams 1UN.frcmod
> loadamberprep 1UN.prepc
3. De seguida carregue a estrutura do nosso sistema usando a instrução:
> prot-nelf=loadpdb nome.pdb

## Visualização da Estrutura no xleap
1. Dentro do programa xleap execute o comando:
> edit prot-nelf

## Adição de Contra-iões (Exemplo)
1. Se houver excesso de carga positiva deverá adicionar contra-iões negativos:
> addions prot-nelf Cl- 0
2. Se houver excesso de carga negativa deverá adicionar contra-iões positivos:
addions prot-nelf Na+ 0


# Preparar o Sistema
##Carregar um Ficheiro PDB no xleap
1. Abra o programa xleap
> xleap
2. Dentro do programa xleap execute os seguintes comandos para carregar as várias bibliotecas de parâmetros:
> source leaprc.ff03
> source leaprc.gaff
> loadamberparams 1UN.frcmod
> loadamberprep 1UN.prepc
3. De seguida carregue a estrutura do nosso sistema usando a instrução:
prot-nelf=loadpdb nome.pdb (em que “nome.pdb” corresponde à designação que atribuiu ao ficheiro pdb modificado, sem átomos de
hidrogénio)
4. Adicione os contra-iões correspondentes de forma a neutralizar a carga de acordo com as instruções apresentadas na caixa anterior;
5. Visualize a posição dos contra-iões adicionados;
edit prot-nelf
6. Adicione a caixa de simulação com pelo menos 12 Å de água em todas as direcções;
> solvatebox prot-nelf TIP3PBOX 12.0
(TIP3P corresponde à parametrização específica das moléculas de água utilizadas)b
7. Visualize o sistema após a adição da caixa de águas;
> edit prot-nelf
8. Crie o ficheiros de parâmetros e topologia e o ficheiro de coordenadas a partir da unidade prot-nelf:
> saveamberparm prot-nelf prot-nelf.prmtop prot-nelf.inpcrd
