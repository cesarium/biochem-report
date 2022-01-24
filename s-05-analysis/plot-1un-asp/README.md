Determinação de Distâncias
1. Após a preparação de um ficheiro PTRAJ indicado em cima execute a seguinte instrução:
> ptraj prot-nelf.prmtop < prot-nelf -ptraj-dist.in
2. A instrução gera quatro ficheiros: `prot-nelf-MD2-distA.list`, `prot-nelf-MD2-distB.list`, `prot-nelf-MD2-distC.list` e `prot-nelf-MD2-distD.list`.
3. Represente graficamente os ficheiros correspondentes;
> ./plot.py
4. Calcule o valor médio de cada interacção e o desvio padrão
5. Observe o comportamento destas interacções ao longo da simulação por visualização do gráfico da trajectória. Verifique se as interacções foram constantes durante a dinâmica ou se ocorreram alterações.
