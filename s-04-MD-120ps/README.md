## Execução de uma Simulação de Dinâmica Molecular com Solvente Explícito
1. Prepare o novo ficheiro de coordenadas iniciais a partir do ficheiro resultante da minimização anterior:
> cp prot-nelf-min3.rst prot-nelf-MD1.crd
2. Execute a dinâmica molecular de aquecimento com o comando abaixo:

> mpirun -np 4 sander.MPI -O -i prot-nelf-MD1.in -o prot-nelf-MD1.out -c prot-nelf-MD1.crd -p prot-nelf.prmtop -r prot-nelf-MD1.rst -x prot-nelf-MD1.mdcrd
3. Prepare o novo ficheiro de coordenadas iniciais a partir do ficheiro resultante da simulação anterior;
> cp prot-nelf-MD1.mdcrd MD2.mdcrd
4. Execute a dinâmica molecular de produção
> mpirun -np 4 sander.MPI -O -i prot-nelf-MD2.in -o prot-nelf-MD2.out -c prot-nelf-MD2.crd -p prot-nelf.prmtop -r prot-nelf-MD2.rst -x prot-nelf-MD2.mdcrd
