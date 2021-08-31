#!/usr/bin/env python
# coding: utf-8

# # Exercícios de cache da pag 151
# **1) Uma memória cache associativa por conjunto consiste em 256 linhas divididas em conjuntos de duas linhas cada. A memória principal contém 4K blocos de 128 bytes cada um. Mostre o formato de um endereço de MP e da cache.**

# In[1]:


#Analizando a questão temos:
#Número de linhas= 256= 2^8 linhas
#Conjuntos de duas linhas cada
#Número de blocos= 4K= 4.10^10= 2^12 blocos
#Largura de 128 bytes
#O formato de um endereço de MP e da cache nessa questão é TAG|CONJUNTO|BYTE
import math
Número_de_linhas= 2**8
Número_de_blocos= 2**12
Linhas_por_conjunto= 2
Largura= 128
Byte= math.log2(Largura)
Conjuntos= Número_de_linhas/Linhas_por_conjunto
Conjunto= math.log2(Conjuntos)
Blocos_por_conjunto= Número_de_blocos/Conjuntos
Tag= math.log2(Blocos_por_conjunto)
print("O formato de um endereço de MP e da cache nessa questão é Tag=",Tag,"bits, Conjunto=",Conjunto,"bits e Byte=",Byte,"bits.")


# **2) Em que circunstâncias uma cache que funciona com mapeamento associativo por conjunto pode ser considerada igual á cache que funciona com mapeamento direto?**
# 
# Resposta: Quando a cache possui apenas um conjunto e este conjunto contém todas as linhas da cache.

# **3) Considere um sistema de computação que possui uma memória principal (RAM) com capacidade máxima de endereçamento de 64K células, e que cada célula armazena um byte de informação. Para criar um sistema de controle e funcionamento da sua memória cache, a memória RAM é contituída de blocos de 8 bytes cada. A memória cache do sistema é do tipo mapeamento direto, contendo 32 linhas. Pergunta-se:**
# 
# **a) Como seria organizado o endereço da MP (RAM) em termos de tag, número da linha e do byte dentro de uma linha?**
# 
# **b) Em que linha estaria contido o byte armazenado no seguinte endereço da MP: 0001000100011011?**
# 
# **c) Qual é a capacidade da memória cache em bytes?**

# In[11]:


#Analizando a questão temos:
#MP= 64K = 2^6.2^10= 2^16
#Cada célula armazena um byte de informação
#Blocos de 8 bytes cada
#A memória cache so sistema é do tipo mapeamento direto
#32 linhas
import math
MP= 2**16
Número_de_linhas= 2**5
Largura= 8
Número_de_blocos= MP/Largura
Blocos_por_linhas= Número_de_blocos/Número_de_linhas
Tag= math.log2(Blocos_por_linhas)
Linha= math.log2(Número_de_linhas)
Byte= math.log2(Largura)
Capacidade_da_cache= Número_de_linhas*Largura
print("a) O endereço seria organizado com Tag=",Tag,"bits, Linha=",Linha,"bits e Byte=",Byte,"bits.")
print("b) Como o endereço da MP está organizado em Tag= 8 bits,Linha= 5 bits e Byte= 3 bits o endereço 0001 000 1000 11011 estará contido na linha 00011.")
print("c) A capacidade da memória cache me bytes é,",Capacidade_da_cache,"ou 2^8 bytes.")


# **6) Ao se verificar a organização de uma memória cache e da MP de um sistema de computação, observa-se que a cache tem uma capcacidade de armazenamento muito menor que a MP e, ainda assim, sabe-se que em 100 acessos do procesador a cache ele obtém cerca de 95 a 98% de acertos. Por quê?**
# 
# Resposta: A eficiencia das memorias cache sao da ordem de 95% a 98% devido ao principio da localidade, que é definido como sendo o fenomeno relacionado com o modo pelo qual os programas em média sao escritos pelo programador e executados pelo processador.

# **7) Por que é necessário se estabelecer uma política para subtituição de linhas para os métodos de mapeamento associativo e não para o método direto?**
# 
# Resposta: Por que no mapeamento associativo, os blocos sao colocados em qualquer posicao vaga, nao existindo um locao pre-definido. Assim, deve existir uma forma de escolher qual bloco saira quando a cacher estiver cheia.

# **8) Considere uma MP que possui 4K blocos de 128 células de 1 byte cada e uma memória cache do tipo associativa por conjunto que possui 64 linhas divididas em conjuntos de quatro linhas. Qual deverá ser o formato do campo de endereçamento para acesso a MP e a memória cache?**

# In[3]:


#Analizando a questão temos:
#Número de blocos= 4K= 2^2.2^10= 2^12 blocos
#largura de 128 bytes
#Memória cache do tipo associativa por conjunto
#64 linhas= 2^6 linhas
#Conjuntos de 4 linhas
#O formato do campo de endereçamento para acesso a MP e a memória cache do tipo associativo por conjunto é TAG|CONJUNTO|BYTE
import math
Número_de_linhas= 2**6
Número_de_blocos= 2**12
Linhas_por_conjunto= 4
Largura= 128
Byte= math.log2(Largura)
Conjuntos= Número_de_linhas/Linhas_por_conjunto
Conjunto= math.log2(Conjuntos)
Blocos_por_conjunto= Número_de_blocos/Conjuntos
Tag= math.log2(Blocos_por_conjunto)
print("O formato de um endereço de MP e da cache é Tag=",Tag,"bits, Conjunto=",Conjunto,"bits e Byte=",Byte,"bits.")


# **9) Considere um sistema de computação que possui uma memória principal organizada em células de 1 byte cada e apeans um memória cache externa, organizada com mapeamento direto, sendo cada linha de 32 bytes, Em um dado instante, o processador inicia um acesso colocando no BE comum o endereço hexadecimal: 5D7A9F2. Sabendo-se que neste sistema cada linha da cache tem atribuídos 512 blocos da MP, pergunta-se:**
# 
# **a) Qual deverá ser a largura dp BE do sistema**
# 
# **b) Qual foi a linha acessada pelo processador?**

# In[4]:


#Analizando a questão temos:
#Memória cache com mapeamento direto
#largura de 32 bytes
#Endereço hexadecimal:5D7A9F2
#Blocos por linha= 512= 2^9
import math
E= 7*4
Largura= 32
Byte= math.log2(Largura)
Blocos_por_linha= 2**9
Tag= math.log2(Blocos_por_linha)
Linha= E-Byte-Tag
print("a) O hexadecimal 5D7A9F2 possui 7 algarismos logo, teremos",E,"bits de endereço, assim temos que BE=",E,"bits")
print("b) O hexadecimal 5D7A9F2 em binário é 0101110101111010100111110010 e como temos que Linha=",Linha,"bits, Tag=",Tag,"e Byte=",Byte,"bits então a linha acessada foi a 11110101001111")


# **11) Considere um memória cache organizada com mapeamento associativo por conjunto, sendo cada conjunto de quatro linhas. A MP tem uma capacidade de armazenar 64MB, sendo organizada byte a byte, e o sistema transfere de cada vez (MP<---> cache) 32 bytes. Considerando que a capacidade da cache é de 64KB, mostre como deve ser o formato dos campos de endereço para a memória cache.**
# 

# In[5]:


#Analizando a questão temos:
#Memória cache do tipo associativa por conjunto
#Conjunto de 4 linhas
#Memória principal com capacidade de armazenar 64MB= 2^6.2^20= 2^26
#Memória cache com capcacidade de 64KB= 2^6.2^10= 2^16
#largura de 32 bytes
#O formato dos campos de endereço para a memória cache do tipo associativo por conjunto é TAG|CONJUNTO|BYTE
import math
MP= 2**26
MC= 2**16
Largura= 32
Número_de_linhas= MC/Largura
Número_de_blocos= MP/Largura
Linhas_por_conjunto= 4
Byte= math.log2(Largura)
Conjuntos= Número_de_linhas/Linhas_por_conjunto
Conjunto= math.log2(Conjuntos)
Blocos_por_conjunto= Número_de_blocos/Conjuntos
Tag= math.log2(Blocos_por_conjunto)
print("O formato dos campos de endereço para a memória cache é Tag=",Tag,"bits, Conjunto=",Conjunto,"bits e Byte=",Byte,"bits.")


# **13) Considere um sistema de armazenamento contituído de uma memória principal, que é endereçada por byte e que tem uma capacidade de 256KB, sendo organizada em blcos de 16 bytes de largura. Considerando que seusa neste sistema o método de mapeamento direto para uma cache constituída de 128 linhas, pergunta-se:**
# 
# **a) Qual deverá ser o formato do endereço a ser interpretado pelo sistema de controle da caché, indicando a largura de cada campo?**
# 
# **b) Em que linhas deverão ser armazenados os bytes que possuam os seguintes endereços:**
# 
# **-1011 1110 0010 1001 1101 0000 1100**
# 
# **-0001 1010 0011 0001 0111 1000 1111**
# 
# **c) Qual deverá ser o total de bits consumido nessa cache?**
# 
# **d) Qual deverá ser o endereço do bloco que contém um byte com o seguinte endereço: 0010 1110 1001 0001 1110 0011 1110?**
# 

# In[6]:


#Analizando a questão temos:
#A questão está errada pois com 256KB não é possível resolver as questões 
#Memória principal tem uma capacidade de 256MB= 2^8.2^20= 2^28
#Largura de 16 bytes
#Memória cache com mapeamento direto
#128 linhas= 2^7 linhas
import math
MP= 2**28
Número_de_linhas= 2**7
Largura= 16
Número_de_blocos= MP/Largura
Blocos_por_linhas= Número_de_blocos/Número_de_linhas
Tag= math.log2(Blocos_por_linhas)
Linha= math.log2(Número_de_linhas)
Byte= math.log2(Largura)
Capacidade_da_cache= Número_de_linhas*Largura
print("a) O endereço interpretado seria Tag=",Tag,"bits, Linha=",Linha,"bits e Byte=",Byte,"bits.")
print("b) Como o endereço da MP está organizado em Tag=",Tag,"bits, Linha=",Linha,"bits e Byte=",Byte,"bits o endereço 1011 1110 0010 1001 1101 0000 1100 estará contido na linha 00011.")


# **14) Considere um sistema de armazenamento com MP endereçada por byte, onde cada endereço tem uma largura de 30 bits e uma memória cachee contiruída de 256KB, possuindo L linhas com largura de 16 bytes. Calcule o total de bits da memória cache para um dos métodos de mapeamento: direto, associativo e associativo por conjunto.**

# In[7]:


#Analizando a questão temos:
#Endereço possui uma largura de 30 bits
#Memória cache constituida de 256KB= 2^8.2^10= 2^18
#Largura de 16 bytes
#Fazendo com a memória cache com mapeamento direto
import math
MC= 2**18
E= 30
MP= 2**E
Largura= 16
Número_de_blocos= MP/Largura
Número_de_linhas= MC/Largura
Blocos_por_linhas= Número_de_blocos/Número_de_linhas
Tag= math.log2(Blocos_por_linhas)
Td= Número_de_linhas*Largura*8
Tt= Número_de_linhas*Tag
Total_de_bits_da_cache= Td+Tt
print("O total de bits da memória cache no mapeamento direto é ",Total_de_bits_da_cache,"bits.")


# **15) Considere um sistema de armazenamento onde a MP é endereçada por byte, que utiliza o método de mapeamento direto na sua cache e onde o formato dos endereços interpretados pelo sistema de controle é:**
# 
# **| Tag= 8 bits | Linha= 12 bits | Byte= 4 bits|**
# 
# **a) Qual a capacidade de armazenamento da MP, em bytes?**
# 
# **b) Quantas linhas possui a memória cache?**
# 
# **c) Qual é a largura de cada bloco/linha?**
# 
# **d) Qual é a quantidade de blocos atribuído a cada linha da cache?**

# In[3]:


#Analizando a questão temos:
#Memória cache com mapeamento direto
#Tag= 8 bits
#Linha= 12 bits
#Byte= 4 bits
import math
Tag= 8
Linha= 12 
Byte= 4
Largura= 2**Byte
Número_de_linhas= 2**Linha
Blocos_por_linha= 2**Tag
Número_de_blocos= Número_de_linhas*Blocos_por_linha
Capacidade_da_MP= Número_de_blocos*Largura
print("a) A capacidade de armazenamento da MP é",Capacidade_da_MP,"ou 2^24 bytes")
print("b) A memória cache possui",Número_de_linhas,"ou 2^12 linhas")
print("c) A largura de cada bloco/linha é de",Largura,"bytes")
print("d) A quantidade de blocos atribuído a cada linha da cache é de",Blocos_por_linha,"ou 2^8 blocos por linha")


# **16) Suponde que esse sistema utilize o método de mapeamento associativo por conjunto de 4 e que o formato do endereço de cache é:**
# 
# **| Tag= 8 bits | Conjunto= 8 bits | Byte= 4 bits|**
# 
# **a) Qual a capacidade de armazenamento da MP, em bytes?**
# 
# **b) Quantas linhas possui a memória cache?**
# 
# **c) Quantos conjuntos possui a memória cache?**
# 
# **d) Qual é a largura de cada bloco/linha?**
# 
# **e) Qual é a quantidade de blocos atribuído a cada linha da cache?**
# 

# In[10]:


#Analizando a questão temos:
#Memória cache com mapeamento associativo
#Conjunto de 4 linhas
#Tag= 8 bits
#Conjunto= 8 bits
#Byte= 4 bits
import math
Tag= 8
Conjunto= 8 
Byte= 4
Largura= 2**Byte
Linhas_por_conjunto= 4
Conjuntos= 2**Conjunto
Número_de_linhas= Conjuntos*Linhas_por_conjunto
Blocos_por_conjunto= 2**Tag
Número_de_blocos= Blocos_por_conjunto*Conjuntos
Blocos_por_linha= Número_de_blocos/Número_de_linhas
Capacidade_da_MP= Número_de_blocos*Largura
print("a) A capacidade de armazenamento da MP é",Capacidade_da_MP,"ou 2^20 bytes")
print("b) A memória cache possui",Número_de_linhas,"ou 2^10 linhas")
print("c) A memória cache possui",Conjuntos,"ou 2^8 conjuntos")
print("d) A largura de cada bloco/linha é",Largura,"bytes")
print("e) A quantidade de blocos atribuído a cada linha da cache é de",Blocos_por_linha,"ou 2^6 blocos por linha")


# In[ ]:




