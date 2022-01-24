## Cálculo de Funções de Distribuição Radial
1. Após a preparação de um ficheiro PTRAJ corra a seguinte instrução:
> ptraj prot-nelf.prmtop < ptraj-radial-25.in > ptraj-radial-25.out
2. A instrução gera dois ficheiros:
> prot-nelf-MD2-RDF1-Res25A_standard.xmgr e prot-nelf-MD2-RDF1-Res25B_standard.xmgr
3. Cada ficheiro possui 3 colunas de dados: distância de interacção ao átomo de referência; a função de distribuição radial; e o número
cumulativo de moléculas de água até essa distância;
4. Repita o procedimento para o Asp29 e Glu21.
5. Represente graficamente as duas colunas dos ficheiros indicados.
> ./plot.py
