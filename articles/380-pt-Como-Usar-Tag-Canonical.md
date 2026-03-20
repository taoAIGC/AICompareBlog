# Como definir a tag Canonical? Pare de ter várias páginas apontando para a página inicial, essas 5 situações serão tratadas de forma mais eficaz

> Idioma: Chinês | Região: China/Global | Palavras-chave: como configurar tags canônicas, tags canônicas, como usar tags canônicas, canônicas, SEO de página duplicada, otimização de inclusão de página, índice de site, SEO técnico

**Palavras-chave**: como configurar tags canônicas, tags canônicas, como usar tags canônicas, canônicas, SEO de páginas duplicadas, otimização de inclusão de páginas, indexação de sites, SEO técnico, processamento de conteúdo duplicado, normalização de URL, problemas de inclusão, Search Console

---

## Por que muitos sites apontam canônicos para a página inicial primeiro quando há um problema de inclusão?

Já vi essa armadilha muitas vezes.

O webmaster ficou um pouco ansioso porque a página não estava incluída, então abriu o backend e fez algumas alterações, e finalmente ficou:

- A página do artigo aponta para a página inicial
- A página da categoria aponta para a página inicial
- A página de parâmetros aponta para a página inicial
- Até as páginas dos produtos apontam para a página inicial

Superficialmente, parece estar “unificando os pesos”.

Mas o efeito real é muitas vezes: **Os motores de busca ficarão cada vez mais confusos sobre qual página você deseja que seja considerada a página principal. **

A tag canonical foi originalmente usada para informar aos mecanismos de pesquisa:

**"O conteúdo destas páginas é muito semelhante, por favor trate esta página como a versão oficial primeiro."**

Não é um botão de reparo universal, nem uma ferramenta para culpar a página inicial sempre que houver um problema com a página.

Então, se você está estudando como configurar tags canônicas recentemente, deixe-me dar uma conclusão primeiro:

**canônico O que mais temo não é não saber escrever, mas escrever indiscriminadamente. **

---

## O que exatamente o canônico faz? Não confunda com 301 ou noindex.

Quando muitas pessoas entram em contato com o canônico pela primeira vez, é mais provável que se confundam com estas duas coisas:

- **Redirecionamento 301**
- **sem índice**

Eles não são a mesma coisa.

### 1.canônico
significa:
**Esta página é acessível, mas prefiro que você pense na outra página como a versão master. **

### 2. Redirecionamento 301
significa:
**Esta página mudou, você pode ir diretamente para o novo endereço. **

### 3. sem índice
significa:
**Você pode rastrear esta página, mas não a coloque no índice. **

Portanto, canônico não é "excluir a página", nem é "forçado a pular para a página".

É mais uma "nota de arquivo".

Você está dizendo aos mecanismos de pesquisa:

> O conteúdo dessas páginas é quase o mesmo. A versão principal que deve ser coletada é esta página.

Se você nem entende essa premissa, ela ficará mais confusa facilmente mais tarde.

---

## Como definir o rótulo canônico? Eu recomendo olhar primeiro para estes 5 cenários comuns

### 1. A mesma página possui apenas parâmetros diferentes. Este é o mais adequado para adicionar canônico.

Este é o uso mais comum e padrão.

Por exemplo, na mesma página, estes endereços podem aparecer devido a parâmetros estatísticos, parâmetros de publicidade e parâmetros de compartilhamento:

- `/seo-tools`
- `/seo-tools?utm_source=x`
- `/seo-tools?from=twitter`
- `/seo-tools?session=123`

O conteúdo que os usuários veem é quase o mesmo, apenas o URL é diferente.

A abordagem mais estável neste momento é geralmente:

**Todas as páginas de parâmetros canônicas retornam para a URL principal. **

Ou seja, apontar unificado:

`/seo-tools`

Nesse caso, é mais fácil para os mecanismos de pesquisa entenderem e tem menos probabilidade de causar problemas.

---

### 2. A página de classificação, a página de filtragem e a página da lista original são altamente repetitivas. Você pode considerar o retorno canônico à página da lista principal.

Sites de comércio eletrônico, sites de catálogo de ferramentas e sites de conteúdo geralmente têm páginas como esta:

- Classificar por preço
- Classificar por mais recente
- Filtrar por cor
- Filtrar por região

O problema é:
Na verdade, algumas páginas de filtro não trazem nenhum novo valor de pesquisa, apenas alteram a ordem de exibição do mesmo conteúdo.

Por exemplo:

- `/plugins`
- `/plugins?sort=latest`
- `/plugins?sort=popular`

Se o conteúdo principal das páginas for semelhante e não houver diferença óbvia no valor da pesquisa, considere canonizar a página de classificação para a página da lista principal.

Mas aqui está algo a ser observado:

**Nem todas as páginas de filtro devem ser canonizadas novamente. **

Se uma página de filtro em si tiver necessidades de pesquisa claras, como “plug-ins de SEO adequados para sites independentes” ou “plug-ins de IA gratuitos”, então pode valer a pena existir separadamente em vez de ser mesclada.

Portanto, não faça isso mecanicamente. Primeiro verifique se esta página tem valor independente.

---

### 3. Se houver vários URLs para o mesmo conteúdo, apenas uma versão principal deverá ser explicitamente retida.

Esse problema é particularmente comum em blogs, CMS e sites de revisão.

Por exemplo, o mesmo artigo pode aparecer simultaneamente em:

- novo link
- link antigo
- Links com caminhos de categoria
- Links sem caminho de categoria
- Duas versões com e sem barras

O conteúdo é claramente um artigo, mas existem vários URLs.

Se isso não for feito, o mecanismo de busca terá que adivinhar:
Qual é a página oficial?

A coisa mais importante que você deve fazer é primeiro selecionar uma URL que você realmente deseja manter por muito tempo e depois:

- Tente o seu melhor para 301, se puder 301
- Por enquanto não pode ser saltado, pelo menos o canônico está unificado à versão principal.

Não use A hoje, B amanhã e C algumas semanas depois.

**Canônico Esse tipo de coisa tem mais medo da sua própria instabilidade. **

---

### 4. Páginas de produtos semelhantes e páginas de destino semelhantes não devem ser combinadas em uma só porque são “semelhantes”

Existem muitas armadilhas.

Por exemplo, você tem estas páginas:

- tênis de corrida preto
- tênis de corrida branco
- Tênis de corrida feminino
- Tênis de corrida largos

Todos pareciam muito parecidos, então alguém foi diretamente para a “página inicial de tênis de corrida” da Canonical.

O resultado é:
A página que poderia cobrir separadamente os termos de pesquisa subdivididos foi suprimida por você mesmo.

Meus próprios critérios de julgamento são simples:

**Se, quando os usuários pesquisarem esta página, eles esperam ver conteúdo diferente, informações diferentes e decisões de compra diferentes, não confunda tudo. **

Canônico é mais apropriado apenas quando essas páginas são apenas ligeiramente repetitivas, o conteúdo principal é quase o mesmo e o valor independente é fraco.

Caso contrário, você não estará padronizando, mas cortando ativamente as entradas de tráfego de cauda longa.

---

### 5. A página foi atualizada e a página antiga não será mais mantida. Utilize 301; não use hard top canônico.

Existe uma situação em que é mais provável que seja usado incorretamente:

A página antiga está obsoleta e a nova página a substituiu completamente.

Neste momento, muitas pessoas têm preguiça de dar um salto, então adicionam um canônico à página antiga para apontar para a nova página, pensando que está “quase”.

Não é exatamente o mesmo.

Se não houver necessidade de manter a página antiga e você quiser que os usuários vão diretamente para a nova página quando visitarem a página antiga, geralmente é mais apropriado:

**Redirecionamento 301 em vez de apenas escrever canônico. **

Como a premissa do canônico é que a página antiga ainda existe, ele apenas informa ao mecanismo de busca "concentre-se nessa página".

E 301 está expressando claramente:

**Esta página foi movida oficialmente. **

Muitas pessoas não prestam atenção a essa diferença nas horas normais, mas ficarão muito envergonhadas ao verificar o índice e o peso posteriormente.

---

## Acho que esses quatro erros canônicos são mais prejudiciais do que não escrever.

### Erro 1: todas as páginas apontam para a página inicial

Esta é a forma mais comum de manuseio brusco.

O problema é que a página inicial, as páginas de artigos, as páginas de produtos e as páginas de categorias não são originalmente intenção de pesquisa.

Quando você aponta um monte de páginas de volta para a página inicial, você está dizendo aos mecanismos de pesquisa:

"Nenhuma dessas páginas é importante, é a página inicial que é importante."

Não fique surpreso se muitas palavras de cauda longa não puderem ser usadas.

---

### Erro 2: O conteúdo da página é muito diferente, mas o mesmo canônico ainda está escrito

canonical não pretende mesclar "tópicos completamente diferentes".

Se os tópicos, as intenções do usuário e as direções das palavras-chave das duas páginas forem todos diferentes, mas estiverem apenas ligeiramente relacionados, você não deve apontá-los aleatoriamente.

O mecanismo de busca não apenas vê que você escreveu o canônico e apenas o segue, mas também julgará a semelhança do conteúdo por si só.

Se você escrever aleatoriamente, muitas vezes não fará o que você quer.

---

### Erro 3: pontos canônicos para 404, páginas de salto ou até mesmo páginas não indexadas

Esta é uma armadilha de baixo nível que é mais facilmente ignorada na tecnologia.

A página de destino apontada por canonical deve atender preferencialmente a estas condições:

- Pode ser aberto normalmente
- O código de status é normal
- Não 404
- Não é o endereço após saltos de vários níveis
- não indexado

Caso contrário, você estará dando ao mecanismo de busca uma instrução muito vaga ou até errada.

---

### Erro 4: Canônico de um lado e dando sinais opostos do outro.

Por exemplo:

- A página escreve sua própria auto-referência canônica
- Outro URL foi enviado no mapa do site
- A maioria dos links internos apontam para o terceiro URL
- hreflang, redirecionamento, luta canônica entre si

Esta situação é a mais problemática.

Porque o que o mecanismo de busca finalmente recebe não é uma conclusão clara, mas um monte de dicas conflitantes.

**Canônico realmente eficaz não é escrever um único ponto corretamente, mas não prejudicar um ao outro em todo o conjunto de sinais de URL. **

---

## Se você quiser verificar o canônico agora, esta lista é suficiente

Quando resolvo minha própria solução de problemas, geralmente procuro nesta ordem:

### Etapa um: esta página tem valor de pesquisa independente?
Nesse caso, não canone-o facilmente para outra página.

### Etapa 2: esta página é muito semelhante à página de destino?
Se eles forem um tanto semelhantes, mas na verdade resolverem problemas diferentes, não os mescle.

### Etapa 3: A página de destino é estável, acessível e capaz de inclusão?
Não aponte para 404s, links de redirecionamento ou páginas noindex.

### Etapa 4: Os outros sinais no site são consistentes?
Verifique o mapa do site, links internos, navegação e redirecionamentos para ver se há algum conflito.

### Etapa 5: Cenários canônicos, não apenas escreva canônicos
A página antiga foi descontinuada, então não a deixe meio morta.

Observando essas 5 etapas, a maioria dos problemas canônicos pode realmente ser identificada.

---

## Minha abordagem mais comum agora: primeiro esclareça o relacionamento do URL e depois fale sobre o relacionamento canônico

Para ser honesto, muitos sites têm problemas canônicos, não porque as tags em si sejam difíceis, mas porque a estrutura da URL não foi pensada com clareza desde o início.

Por exemplo:

- O mesmo conteúdo pode gerar três ou quatro tipos de links
- Os caminhos das categorias mudam com frequência
- Coexistência de URLs antigos e novos
- As regras dos parâmetros são confusas
- Modelos e plug-ins geram automaticamente um monte de páginas duplicadas

Mesmo se você corrigir o canônico em todas as páginas desse tipo de site, continuará corrigindo-o mais tarde.

Então agora prefiro fazer isso primeiro:

**Primeiro pense claramente sobre "quais páginas deveriam existir, quais páginas não deveriam existir e quais páginas deveriam ser mescladas". **

Depois de pensar sobre isso com clareza, o canônico se tornará uma ferramenta de organização muito conveniente.

Caso contrário, pode ser facilmente usado como ferramenta de extinção de incêndio.

---

## Escreva no final

Como definir o rótulo canônico não é tão misterioso quanto se imagina.

A dificuldade não é como escrever o código, mas se você pode julgar claramente primeiro:

- Quais páginas são realmente duplicadas
- Quais páginas são semelhantes, mas devem ser mantidas
- Quais páginas devem ser canônicas
- Quais páginas deveriam realmente ser 301

Sinto cada vez mais agora que o valor central do canônico não é "transferir peso", mas:

**Deixe os mecanismos de busca saberem com mais clareza qual página do seu site é a versão oficial. **

Enquanto essa ideia estiver clara, muitos problemas como coleta lenta, páginas duplicadas e indexação caótica serão muito mais fáceis de resolver do que antes.

Se acontecer de você estar verificando a inclusão recentemente, não verifique apenas se canonical a escreveu.

E mais:

**Está escrito na página certa? **

---

**Pesquisas relacionadas**: como configurar tags canônicas, tags canônicas, como usar tags canônicas, canônicas, SEO de página duplicada, otimização de inclusão de página, indexação de site, SEO técnico, processamento de conteúdo duplicado, normalização de URL, problemas de inclusão, Search Console
