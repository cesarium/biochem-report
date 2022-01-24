## Execução da 1.ª Minimização:
1. Lance o processo, invocando:
> sander -O -i prot-nelf-min1.in –o prot-nelf-min1.out -c prot-nelf.inpcrd -p prot-nelf.prmtop -r prot-nelf-min1.rst –ref prot-nelf.inpcrd

## Execução da 2.ª e 3.ª Minimizações:
1. Prepare o novo ficheiro de coordenadas iniciais a partir do ficheiro resultante da minimização anterior:
> cp prot-nelf-min1.rst prot-nelf-min2.crd
2. Lance o processo de forma análoga à usada para a primeira minimização.
3. Prepare o novo ficheiro de coordenadas iniciais a partir do ficheiro resultante da minimização anterior.
4. Lance o processo de forma análoga à usada para a primeira e segunda minimização.
