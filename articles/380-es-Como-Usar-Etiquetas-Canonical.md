# ¿Cómo configurar la etiqueta canónica? Deje de tener varias páginas apuntando a la página de inicio, estas 5 situaciones se manejarán de manera más efectiva

> Idioma: Chino | Región: China/Global | Palabras clave: Cómo configurar etiquetas canónicas, etiquetas canónicas, cómo usar etiquetas canónicas, SEO de páginas duplicadas, optimización de inclusión de páginas, índice de sitios web, SEO técnico

**Palabras clave**: Cómo configurar etiquetas canónicas, etiquetas canónicas, cómo usar etiquetas canónicas, SEO de páginas duplicadas, optimización de inclusión de páginas, indexación de sitios web, SEO técnico, procesamiento de contenido duplicado, normalización de URL, problemas de inclusión, Search Console

---

## ¿Por qué muchos sitios web apuntan canónicamente a la página de inicio primero cuando hay un problema de inclusión?

He visto esta trampa demasiadas veces.

El webmaster estaba un poco ansioso porque la página no estaba incluida, así que abrió el backend e hizo algunos cambios, y finalmente quedó:

- La página del artículo apunta a la página de inicio.
- La página de categoría apunta a la página de inicio.
- La página de parámetros apunta a la página de inicio.
- Incluso las páginas de productos apuntan a la página de inicio.

En la superficie, parece estar "unificando los pesos".

Pero el efecto real suele ser el siguiente: **Los motores de búsqueda se confundirán cada vez más acerca de qué página desea que se considere la página principal. **

La etiqueta canonical se usó originalmente para indicar a los motores de búsqueda:

**"El contenido de estas páginas es muy similar; primero trate esta página como la versión oficial".**

No es un botón de reparación universal, ni tampoco una herramienta para culpar a la página de inicio cada vez que hay un problema con la página.

Entonces, si recientemente estás estudiando cómo configurar etiquetas canónicas, primero déjame darte la conclusión:

**canónico Lo que más temo no es no poder escribir, sino escribir indiscriminadamente. **

---

## ¿Qué hace exactamente canonical? No lo confundas con 301 o noindex.

Cuando muchas personas entran en contacto con canonical por primera vez, lo más probable es que se confundan con estas dos cosas:

- **Redireccionamiento 301**
- **sin índice**

No son lo mismo.

### 1.canónico
significa:
**Esta página es accesible, pero prefiero que pienses en la otra página como la versión maestra. **

### 2. Redirección 301
significa:
**Esta página se ha movido, puedes ir directamente a la nueva dirección. **

### 3. sin índice
significa:
**Puedes rastrear esta página, pero no incluirla en el índice. **

Entonces, canonical no es "eliminar la página", ni está "obligado a saltar a la página".

Es más bien una "nota de archivo".

Le estás diciendo a los motores de búsqueda:

> El contenido de estas páginas es casi el mismo. La versión principal que se debe recopilar es esta página.

Si ni siquiera comprende esta premisa, fácilmente se volverá más confusa más adelante.

---

## ¿Cómo configurar la etiqueta canónica? Recomiendo mirar primero estos 5 escenarios comunes

### 1. La misma página solo tiene diferentes parámetros. Este es el más adecuado para agregar canónico.

Este es el uso más común y estándar.

Por ejemplo, en la misma página, estas direcciones pueden aparecer debido a parámetros estadísticos, parámetros publicitarios y parámetros de uso compartido:

- `/seo-herramientas`
- `/seo-herramientas?utm_source=x`
- `/seo-tools?de=twitter`
- `/seo-tools?sesión=123`

El contenido que ven los usuarios es casi el mismo, sólo que la URL es diferente.

El enfoque más estable en este momento suele ser:

**Todas las páginas de parámetros canónicamente regresan a la URL principal. **

Es decir, apuntamiento unificado:

`/seo-herramientas`

En este caso, es más fácil de entender para los motores de búsqueda y es menos probable que cause problemas.

---

### 2. La página de clasificación, la página de filtrado y la página de lista original son muy repetitivas. Puede considerar canónico regresar a la página de la lista principal.

Los sitios de comercio electrónico, sitios de catálogos de herramientas y sitios de contenido suelen tener páginas como esta:

- Ordenar por precio
- Ordenar por último
- Filtrar por color
- Filtrar por región

El problema es:
Algunas páginas de filtro en realidad no aportan ningún valor de búsqueda nuevo, sino que simplemente cambian el orden de visualización del mismo contenido.

Por ejemplo:

- `/complementos`
- `/plugins?sort=último`
- `/plugins?sort=popular`

Si el contenido principal de las páginas es similar y no hay una diferencia obvia en el valor de búsqueda, entonces puede considerar canonicalizar la página de clasificación en la página de lista principal.

Pero aquí hay algo a tener en cuenta:

**No todas las páginas de filtro deben volver a canonicalizarse. **

Si una página de filtro en sí tiene necesidades de búsqueda claras, como "complementos de SEO adecuados para sitios independientes" o "complementos de IA gratuitos", entonces puede valer la pena existir por separado en lugar de fusionarse.

Así que no lo hagas mecánicamente. Primero verifique si esta página tiene valor independiente.

---

### 3. Si hay varias URL para el mismo contenido, solo se debe conservar explícitamente una versión principal.

Este problema es particularmente común en blogs, CMS y sitios de revisión.

Por ejemplo, un mismo artículo puede aparecer simultáneamente en:

- nuevo enlace
- enlace antiguo
- Enlaces con rutas de categorías.
- Enlaces sin ruta de categoría
- Dos versiones con y sin barras

El contenido es claramente un artículo, pero hay varias URL.

Si no se hace esto, el buscador tendrá que adivinar:
¿Cuál es la página oficial?

Lo más importante que debes hacer es seleccionar primero una URL que realmente quieras conservar durante mucho tiempo y luego:

- Haz tu mejor esfuerzo para 301 si puedes 301
- No se puede saltar por el momento, al menos canonical está unificado a la versión principal.

No uses A hoy, B mañana y C unas semanas después.

**Canónico Este tipo de cosas tiene mucho miedo de tu propia inestabilidad. **

---

### 4. Las páginas de productos similares y las páginas de destino similares no deben combinarse en una sola solo porque son "similares"

Hay muchas trampas.

Por ejemplo, tienes estas páginas:

- zapatillas negras para correr
- zapatillas blancas para correr
- Zapatillas de correr para mujer.
- Zapatillas anchas para correr.

Todos parecían muy similares, por lo que alguien fue directamente a la "página de inicio de zapatillas para correr" de Canonical.

El resultado es:
La página que podría haber cubierto por separado los términos de búsqueda subdivididos fue suprimida por usted mismo.

Mis propios criterios de juicio son simples:

**Si cuando los usuarios buscan en esta página esperan ver contenido diferente, información diferente y decisiones de compra diferentes, no lo confunda. **

Canonical es más apropiado sólo cuando estas páginas son en realidad sólo ligeramente repetitivas, el contenido principal es casi el mismo y el valor independiente es débil.

De lo contrario, no se está estandarizando, sino cortando activamente las entradas de tráfico de cola larga.

---

### 5. La página se ha actualizado y la página anterior ya no se conservará. Utilice 301; No utilice techo rígido canónico.

Hay una situación en la que es más probable que se utilice incorrectamente:

La página antigua está obsoleta y la nueva la ha sustituido por completo.

En este momento, muchas personas son demasiado perezosas para dar un salto, por lo que agregan un canónico a la página anterior para señalar la página nueva, pensando que es "casi".

No exactamente lo mismo.

Si no es necesario conservar la página anterior y desea que los usuarios vayan directamente a la página nueva cuando visiten la página anterior, suele ser más apropiado:

**Redireccionamiento 301 en lugar de simplemente escribir canónico. **

Debido a que la premisa de canonical es que la página anterior todavía existe, simplemente le dice al motor de búsqueda "concéntrese en esa página".

Y 301 expresa claramente:

**Esta página ha sido movida oficialmente. **

Muchas personas no prestan atención a esta diferencia en momentos normales, pero se sentirán muy avergonzados al comprobar el índice y el peso más adelante.

---

## Creo que estos cuatro errores canónicos son más dañinos que no escribir.

### Error 1: todas las páginas apuntan a la página de inicio

Esta es la forma más común de trato brusco.

El problema es que la página de inicio, las páginas de artículos, las páginas de productos y las páginas de categorías no son originalmente la intención de búsqueda.

Cuando diriges un montón de páginas a la página de inicio, les estás diciendo a los motores de búsqueda:

"Ninguna de estas páginas es importante, lo importante es la página de inicio".

No se sorprenda demasiado si no se pueden utilizar muchas palabras de cola larga.

---

### Error 2: El contenido de la página es muy diferente, pero todavía está escrito el mismo canónico

canonical no pretende fusionar "temas completamente diferentes".

Si los temas, las intenciones de los usuarios y las direcciones de las palabras clave de las dos páginas son todos diferentes, pero están ligeramente relacionados, entonces no debes señalarlos al azar.

El motor de búsqueda no sólo ve que has escrito canónico y simplemente lo sigue, sino que también juzgará la similitud del contenido por sí mismo.

Si escribe al azar, muchas veces no funcionará como desea.

---

### Error 3: puntos canónicos a 404, páginas de salto o incluso páginas no indexadas

Se trata de un escollo de bajo nivel que en el ámbito tecnológico es más fácil de pasar por alto.

La página de destino a la que apunta canonical debe cumplir preferiblemente estas condiciones:

- Se puede abrir normalmente
- El código de estado es normal
- No 404
- No es la dirección después de saltos de varios niveles.
- no indexado

De lo contrario, le estás dando al motor de búsqueda una instrucción muy vaga o incluso errónea.

---

### Error 4: Canonical por un lado y dar señales opuestas por el otro.

Por ejemplo:

- La página escribe su propia autorreferencia canónica.
- Se envió otra URL en el mapa del sitio.
- La mayoría de los enlaces internos apuntan a la tercera URL.
- hreflang, redirección, lucha canónica entre sí

Esta situación es la más problemática.

Porque lo que finalmente recibe el motor de búsqueda no es una conclusión clara, sino un montón de consejos contradictorios.

**Lo canónico realmente efectivo no es escribir un solo punto correctamente, sino no socavarse entre sí en todo el conjunto de señales URL. **

---

## Si quieres comprobar lo canónico ahora, esta lista es suficiente.

Cuando soluciono mis propios problemas, normalmente miro en este orden:

### Paso uno: ¿Esta página tiene valor de búsqueda independiente?
Si es así, no lo canonices fácilmente a otra página.

### Paso 2: ¿Esta página es muy similar a la página de destino?
Si son algo similares pero en realidad resuelven problemas diferentes, no los fusiones.

### Paso 3: ¿La página de destino es estable, accesible y capaz de incluirse?
No apunte a mensajes 404, enlaces de redireccionamiento o páginas sin índice.

### Paso 4: ¿Son consistentes otras señales en el sitio?
Consulte el mapa del sitio, los enlaces internos, la navegación y los redireccionamientos para ver si hay algún conflicto.

### Paso 5: Escenarios canónicos, no escribas simplemente canónicos
La página anterior ha sido retirada, así que no la dejes medio muerta.

Al observar estos 5 pasos, la mayoría de los problemas canónicos pueden identificarse.

---

## Mi enfoque más común ahora: primero aclarar la relación de URL y luego hablar de canónica

Para ser honesto, muchos sitios web tienen problemas canónicos, no porque las etiquetas en sí sean difíciles, sino porque la estructura de la URL no se pensó claramente desde el principio.

Por ejemplo:

- Un mismo contenido puede generar tres o cuatro tipos de enlaces
- Las rutas de categoría cambian con frecuencia
- Coexistencia de URL antiguas y nuevas.
- Las reglas de los parámetros son confusas.
- Las plantillas y complementos generan automáticamente un montón de páginas duplicadas

Incluso si parcheas canonical en cada página de este tipo de sitio, seguirás parcheándolo más tarde.

Así que ahora prefiero hacer esto primero:

**Primero piense claramente en "qué páginas deberían existir, qué páginas no deberían existir y qué páginas deberían fusionarse". **

Después de pensarlo claramente, canonical se convertirá en una herramienta de organización muy conveniente.

De lo contrario, puede utilizarse fácilmente como herramienta de extinción de incendios.

---

## Escribe al final

Cómo establecer la etiqueta canónica en realidad no es tan misterioso como se imagina.

La dificultad no es cómo escribir el código, sino si puedes juzgar claramente primero:

- ¿Qué páginas están realmente duplicadas?
- ¿Qué páginas son similares pero deben conservarse?
- ¿Qué páginas deberían ser canónicas?
- ¿Qué páginas deberían ser realmente 301?

Siento cada vez más que el valor central de canonical no es "transferir peso", sino:

**Deja que los motores de búsqueda sepan más claramente qué página de tu sitio web es la versión oficial. **

Mientras esta idea esté clara, muchos problemas como la recopilación lenta, las páginas duplicadas y la indexación caótica serán mucho más fáciles de abordar que antes.

Si está verificando la inclusión recientemente, no se limite a verificar si canonical lo ha escrito.

Es más:

**¿Está escrito en la página correcta? **

---

**Búsquedas relacionadas**: Cómo configurar etiquetas canónicas, etiquetas canónicas, cómo usar etiquetas canónicas, SEO de páginas duplicadas, optimización de inclusión de páginas, indexación de sitios web, SEO técnico, procesamiento de contenido duplicado, normalización de URL, problemas de inclusión, Search Console
