# Comment définir la balise Canonical ? Arrêtez d'avoir plusieurs pages pointant vers la page d'accueil, ces 5 situations seront gérées plus efficacement

> Langue : Chinois | Région : Chine/Monde | Mots-clés : Comment configurer les balises canoniques, les balises canoniques, comment utiliser les balises canoniques, les balises canoniques, le référencement des pages en double, l'optimisation de l'inclusion des pages, l'index du site Web, le référencement technique

**Mots clés** : Comment configurer les balises canoniques, les balises canoniques, comment utiliser les balises canoniques et canoniques, le référencement des pages en double, l'optimisation de l'inclusion des pages, l'indexation des sites Web, le référencement technique, le traitement du contenu en double, la normalisation des URL, les problèmes d'inclusion, la console de recherche.

---

## Pourquoi de nombreux sites Web pointent-ils d'abord vers la page d'accueil lorsqu'il y a un problème d'inclusion ?

J'ai vu ce piège trop de fois.

Le webmaster était un peu inquiet car la page n'était pas incluse, alors il a ouvert le backend et a apporté quelques modifications, et finalement c'est devenu :

- La page de l'article pointe vers la page d'accueil
- La page de catégorie pointe vers la page d'accueil
- La page des paramètres pointe vers la page d'accueil
- Même les pages produits pointent vers la page d'accueil

En surface, cela semble « unifier les poids ».

Mais l'effet réel est souvent le suivant : **Les moteurs de recherche seront de plus en plus confus quant à la page que vous souhaitez considérer comme page principale. **

La balise canonique était à l’origine utilisée pour indiquer aux moteurs de recherche :

**"Le contenu de ces pages est très similaire, veuillez d'abord traiter cette page comme la version officielle."**

Ce n'est pas un bouton de réparation universel, ni un outil permettant de blâmer la page d'accueil chaque fois qu'il y a un problème avec la page.

Donc, si vous étudiez récemment comment configurer des balises canoniques, laissez-moi d'abord vous donner la conclusion :

**canonique Ce que je crains le plus, ce n'est pas de ne pas pouvoir écrire, mais d'écrire sans discernement. **

---

## Que fait exactement Canonical ? Ne le confondez pas avec 301 ou noindex.

Lorsque de nombreuses personnes entrent en contact avec Canonical pour la première fois, elles sont plus susceptibles d'être confondues avec ces deux choses :

- **Redirection 301**
- **pas d'index**

Ce n’est pas la même chose.

### 1.canonique
signifie :
**Cette page est accessible, mais je préfère que vous considériez l'autre page comme la version principale. **

### 2. Redirection 301
signifie :
**Cette page a été déplacée, vous pouvez accéder directement à la nouvelle adresse. **

### 3. pas d'index
signifie :
**Vous pouvez explorer cette page, mais ne la mettez pas dans l'index. **

Donc canonique ne consiste pas à "supprimer la page", ni à "être obligé de passer à la page".

Il s'agit plutôt d'une "note d'archive".

Vous dites aux moteurs de recherche :

> Le contenu de ces pages est quasiment le même. La version principale qui doit être collectée est cette page.

Si vous ne comprenez même pas cette prémisse, cela deviendra facilement plus déroutant plus tard.

---

## Comment définir l'étiquette canonique ? Je recommande d'examiner d'abord ces 5 scénarios courants

### 1. La même page n'a que des paramètres différents. C'est le plus approprié pour ajouter du canonique.

Il s’agit de l’utilisation la plus courante et la plus standard.

Par exemple, sur une même page, ces adresses peuvent apparaître en raison de paramètres statistiques, de paramètres publicitaires et de paramètres de partage :

- `/outils de référencement`
- `/seo-tools?utm_source=x`
- `/seo-tools?from=twitter`
- `/seo-tools?session=123`

Le contenu que voient les utilisateurs est presque le même, seule l’URL est différente.

L’approche la plus stable à l’heure actuelle est généralement :

**Toutes les pages de paramètres renvoient canoniquement à l'URL principale. **

C'est-à-dire un pointage unifié :

`/outils de référencement`

Dans ce cas, il est plus facile à comprendre pour les moteurs de recherche et est moins susceptible de causer des problèmes.

---

### 2. La page de tri, la page de filtrage et la page de liste d'origine sont très répétitives. Vous pouvez envisager de revenir canoniquement à la page de liste principale.

Les sites de commerce électronique, les sites de catalogues d'outils et les sites de contenu comportent souvent des pages comme celle-ci :

- Trier par prix
- Trier par dernier
- Filtrer par couleur
- Filtrer par région

Le problème est :
Certaines pages de filtres n'apportent en réalité aucune nouvelle valeur de recherche, mais modifient simplement l'ordre d'affichage du même contenu.

Par exemple :

- `/plugins`
- `/plugins?sort=dernière`
- `/plugins?sort=populaire`

Si le contenu principal des pages est similaire et qu'il n'y a pas de différence évidente dans la valeur de recherche, vous pouvez alors envisager de canoniser la page de tri vers la page de liste principale.

Mais voici quelque chose à noter :

**Toutes les pages de filtre ne doivent pas être canonisées. **

Si une page de filtre elle-même a des besoins de recherche clairs, tels que des « plug-ins SEO adaptés aux sites indépendants » ou des « plug-ins IA gratuits », alors elle peut valoir la peine d'exister séparément au lieu d'être fusionnée.

Alors ne le faites pas mécaniquement. Vérifiez d’abord si cette page a une valeur indépendante.

---

### 3. S'il existe plusieurs URL pour le même contenu, une seule version principale doit être explicitement conservée.

Ce problème est particulièrement courant dans les blogs, les CMS et les sites de révision.

Par exemple, le même article peut paraître simultanément dans :

- nouveau lien
-ancien lien
- Liens avec les chemins de catégories
- Liens sans chemin de catégorie
- Deux versions avec et sans barres obliques

Le contenu est clairement un article, mais il existe plusieurs URL.

Si cela n'est pas fait, le moteur de recherche devra deviner :
Quelle est la page officielle ?

La chose la plus importante à faire est de sélectionner d’abord une URL que vous souhaitez réellement conserver pendant une longue période, puis :

- Faites de votre mieux pour atteindre 301 si vous le pouvez.
- Il ne peut pas être sauté pour le moment, au moins canonique est unifié à la version principale.

N'utilisez pas A aujourd'hui, B demain et C quelques semaines plus tard.

**Canonical Ce genre de chose a le plus peur de votre propre instabilité. **

---

### 4. Les pages de produits similaires et les pages de destination similaires ne doivent pas être combinées en une seule simplement parce qu'elles sont « similaires »

Il existe de nombreux pièges.

Par exemple, vous avez ces pages :

- des chaussures de course noires
- des chaussures de course blanches
- Chaussures de course pour femmes
- Chaussures de course larges

Ils se ressemblaient tous beaucoup, alors quelqu'un est allé directement sur la "page d'accueil des chaussures de course" de Canonical.

Le résultat est :
La page qui aurait pu couvrir séparément les termes de recherche subdivisés a été supprimée par vous-même.

Mes propres critères de jugement sont simples :

**Si, lorsque les utilisateurs effectuent une recherche sur cette page, ils s'attendent à voir un contenu différent, des informations différentes et des décisions d'achat différentes, ne mélangez pas les choses. **

Canonical n'est plus approprié que lorsque ces pages ne sont en réalité que légèrement répétitives, que le contenu principal est presque le même et que la valeur indépendante est faible.

Autrement, vous ne standardisez pas, mais vous coupez activement les entrées du trafic à longue traîne.

---

### 5. La page a été mise à jour et l'ancienne page ne sera plus conservée. Utilisez 301 ; n'utilisez pas de toit rigide canonique.

Il existe une situation dans laquelle il est le plus susceptible d'être utilisé de manière incorrecte :

L'ancienne page est obsolète et la nouvelle page l'a complètement remplacée.

À l'heure actuelle, beaucoup de gens sont trop paresseux pour faire un saut, alors ils ajoutent un canonique à l'ancienne page pour pointer vers la nouvelle page, pensant qu'elle est "presque".

Pas exactement pareil.

S'il n'est pas nécessaire de conserver l'ancienne page et que vous souhaitez que les utilisateurs accèdent directement à la nouvelle page lorsqu'ils visitent l'ancienne page, cela est généralement plus approprié :

**Redirection 301 au lieu de simplement écrire canonique. **

Parce que le principe de canonique est que l'ancienne page existe toujours, il indique simplement au moteur de recherche "veuillez vous concentrer sur cette page".

Et 301 exprime clairement :

**Cette page a été officiellement déplacée. **

Beaucoup de gens ne font pas attention à cette différence en temps ordinaire, mais ils seront très gênés lorsqu'ils vérifieront plus tard l'indice et le poids.

---

## Je pense que ces quatre erreurs canoniques sont plus nuisibles que de ne pas écrire.

### Erreur 1 : toutes les pages pointent vers la page d'accueil

Il s’agit de la forme de manipulation brutale la plus courante.

Le problème est que la page d’accueil, les pages d’articles, les pages de produits et les pages de catégories ne sont pas à l’origine une intention de recherche.

Lorsque vous pointez un certain nombre de pages vers la page d’accueil, vous dites aux moteurs de recherche :

"Aucune de ces pages n'est importante, c'est la page d'accueil qui est importante."

Ne soyez pas trop surpris si de nombreux mots à longue traîne ne peuvent pas être utilisés.

---

### Erreur 2 : Le contenu de la page est très différent, mais la même canonique est toujours écrite

canonique n'est pas destiné à fusionner "des sujets complètement différents".

Si les sujets, les intentions des utilisateurs et les directions de mots clés des deux pages sont tous différents, mais qu'ils ne sont que légèrement liés, alors vous ne devriez pas les pointer au hasard.

Le moteur de recherche ne se contente pas de voir que vous avez écrit un texte canonique et de le suivre, il jugera également par lui-même la similitude du contenu.

Si vous écrivez au hasard, cela ne fera souvent pas ce que vous voulez dire.

---

### Erreur 3 : le canonique pointe vers 404, des pages sautées ou même des pages non indexées

Il s’agit d’un piège de bas niveau qui est le plus facilement négligé en technologie.

La page cible pointée par canonique doit de préférence remplir ces conditions :

- Peut être ouvert normalement
- Le code d'état est normal
- Pas 404
- Pas l'adresse après des sauts à plusieurs niveaux
- non non indexé

Sinon, vous donnez au moteur de recherche une instruction très vague, voire erronée.

---

### Erreur 4 : Canonique d'un côté et donner des signaux opposés de l'autre.

Par exemple :

- La page écrit sa propre canonique d'auto-référence
- Une autre URL a été soumise dans le plan du site
- La plupart des liens internes pointent vers la troisième URL
- hreflang, redirection, combat canonique

Cette situation est la plus gênante.

Car ce que le moteur de recherche reçoit finalement n’est pas une conclusion claire, mais un tas d’astuces contradictoires.

**Le canonique vraiment efficace ne consiste pas à écrire correctement un seul point, mais à ne pas se compromettre dans l'ensemble des signaux URL. **

---

## Si vous souhaitez vérifier canonique maintenant, cette liste suffit

Lorsque j'effectue mon propre dépannage, je regarde généralement dans cet ordre :

### Première étape : cette page a-t-elle une valeur de recherche indépendante ?
Si tel est le cas, ne le canoniquez pas facilement sur une autre page.

### Étape 2 : Cette page est-elle très similaire à la page cible ?
S’ils sont quelque peu similaires mais résolvent en réalité des problèmes différents, ne les fusionnez pas.

### Étape 3 : La page cible est-elle stable, accessible et capable d'être incluse ?
Ne pointez pas vers des 404, des liens de redirection ou des pages sans index.

### Étape 4 : Les autres signaux du site sont-ils cohérents ?
Vérifiez le plan du site, les liens internes, la navigation et les redirections pour voir s'il y a des conflits.

### Étape 5 : Scénarios canoniques, ne vous contentez pas d'écrire des scénarios canoniques
L’ancienne page a été retirée, alors ne la laissez pas à moitié morte.

En regardant ces 5 étapes, la plupart des problèmes canoniques peuvent en fait être identifiés.

---

## Mon approche la plus courante maintenant : clarifier d'abord la relation URL, puis parler de canonique

Pour être honnête, de nombreux sites Web rencontrent des problèmes canoniques, non pas parce que les balises elles-mêmes sont difficiles, mais parce que la structure de l'URL n'a pas été clairement pensée dès le début.

Par exemple :

- Un même contenu peut générer trois ou quatre types de liens
- Les chemins de catégorie changent fréquemment
- Coexistence d'anciennes et de nouvelles URL
- Les règles de paramètres prêtent à confusion
- Les modèles et plug-ins génèrent automatiquement un tas de pages en double

Même si vous appliquez un correctif canonique sur chaque page de ce type de site, vous continuerez à le corriger plus tard.

Alors maintenant, je préfère faire ceci en premier :

** Réfléchissez d'abord clairement à "quelles pages devraient exister, quelles pages ne devraient pas exister et quelles pages devraient être fusionnées". **

Après y avoir bien réfléchi, canonique deviendra un outil d’organisation très pratique.

Sinon, il peut facilement être utilisé comme outil d’extinction d’incendie.

---

## Écrivez à la fin

La manière de définir l’étiquette canonique n’est en réalité pas aussi mystérieuse qu’on l’imagine.

La difficulté n’est pas de savoir comment écrire le code, mais de savoir si vous pouvez d’abord en juger clairement :

- Quelles pages sont vraiment des doublons
- Quelles pages sont similaires mais doivent être conservées
- Quelles pages doivent être canoniques
- Quelles pages devraient réellement être 301

Je sens de plus en plus maintenant que la valeur fondamentale de canonique n'est pas le "transfert de poids", mais :

**Informez les moteurs de recherche plus clairement quelle page de votre site Web est la version officielle. **

Tant que cette idée reste claire, de nombreux problèmes tels qu'une collecte lente, des pages en double et une indexation chaotique seront beaucoup plus faciles à résoudre qu'auparavant.

Si vous avez récemment vérifié l'inclusion, ne vous contentez pas de vérifier si canonique l'a écrit.

De plus :

**Est-ce écrit sur la bonne page ? **

---

**Recherches associées** : Comment configurer les balises canoniques, les balises canoniques, comment utiliser les balises canoniques et canoniques, le référencement des pages en double, l'optimisation de l'inclusion des pages, l'indexation des sites Web, le référencement technique, le traitement du contenu en double, la normalisation des URL, les problèmes d'inclusion, la console de recherche.
