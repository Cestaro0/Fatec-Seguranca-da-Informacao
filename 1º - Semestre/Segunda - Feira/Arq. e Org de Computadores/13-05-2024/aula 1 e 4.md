# Memória secundária

## Tamanho do youtube:
 Com o crescimento de 6 horas de vídeo por minuto, em 2007, aumento total de 4.1 terabytes por dia. Atualmente (2010), com o crescimento de aproximadamente 20 horas de vídeo por minuto, aumento de até 21 terabytes por dia, ou 7.7 Petabytes por ano.

 ## Discos magnéticos (IDE e SCSI)

|IDE | SCSI|
|----|-----|
|PC  | Servidor|
| Duas ligações | Quinze Ligações|
| Comunicação unidirecional | Comunicação bidirecional|


### Organização de um hd

São baseados em setores e trilhas

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/ef848b92-b980-4c93-8603-5ba49beddb4c)

eles têem espaços para que possa ser separado e utilizado para organização.

# RAID
 A sigla RAID se refere à uma família de técnicas para a utilização de vários discos agrupados em paralelo, empregando redundância para compensar eventuais falahas.

 Consiste na tecnica de agrupamentos de discos físicos, mas só é identificado um lógico.

 ## RAID 0 - stripping
 ![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/c8bdd191-93d1-4aff-9d3b-365738b98697)

 onde todos os discos são iguais, técnica feita para nunca desligar.
 
 ## RAID 1 - espelhamento
 ![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/00a8db49-801d-4869-ba9f-b1c2e15a860a)

Tudo que tiver um hd está no outro

## RAID 5 - stripping e paridade
![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/9654f08d-30f5-4596-84fa-ddbde62b13a1)

faz o resumo do disco e grava em uma posição dele que é responsável para a comunicação entre os outros

## RAID 6 - stripping e paridade de 2 discos
![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/0bc37644-30e3-4772-a4b6-4157edd66377)

mesma ideia do RAID 5, mas com um armazenamento maior em alguns discos

## RAID 10 ( 1 + 0) - stripping + mirror
Combinação de RAID 0 + RAID 1

![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/a7f5d379-4a77-48e1-a89b-d33d98fc118e)


## RAID 50 (5 + 0)
![image](https://github.com/Cestaro0/Fatec-Seguranca-da-Informacao/assets/99103680/4fc09980-067b-4459-9325-dcef67f50cc8)

