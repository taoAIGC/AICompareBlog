# KI hilft bei Protokollen - Automatische Erstellung von Kernpunkten und Aufgaben

> Sprache: Deutsch | Region: Global | Schlüsselwörter: KI Protokoll, ChatGPT, Claude, Meeting Notes, KI Effizienz

**Schlüsselwörter**: KI Protokoll, Meeting Protokoll, ChatGPT, Claude, DeepSeek, Meeting Effizienz, KI Werkzeuge, KI Meeting Zusammenfassung, Automatisches Protokoll, Geschäft Effizienz

---

## 5 Minuten Besprechung, 2 Stunden Zusammenfassung?

"Diese Besprechung war viel zu lang..."

"Welche wichtigen Punkte wurden besprochen?"

"Wer ist wofür verantwortlich?"

Besprechungen sind das Häufigste bei der Arbeit, aber das Protokoll zusammenzufassen ist anstrengender als die Besprechung selbst.

Ich hasste früher Besprechungen. Ich hatte keine Angst vor der Diskussion, sondern vor dem Chaos danach. Eine einstündige Besprechung konnte mich eineinhalb Stunden kosten, nur um das Protokoll zu schreiben.

Später habe ich versucht, KI zu Hilfe zu nehmen, um zu organisieren, und es funktioniert wirklich. Heute teile ich die Methode, in der Hoffnung, dass alle weniger Überstunden machen müssen.

---

## Warum ist KI so gut bei Protokollen?

Zuerst zu den Problemen der traditionellen Protokollerstellung:

**Erstens: Kann sich nicht erinnern**
In Besprechungen gibt es zu viele Informationen. Einer spricht, der andere spricht, wenn man selbst an der Reihe ist, hat man fast vergessen, was der Vorherige gesagt hat.

**Zweitens: Kann das Wichtige nicht erfassen**
明明很重要的决定，说的时候大家都在点头，事后没人记得。

**Drittens: Aufgaben werden vergessen**
"这个你来负责""好的"，然后，就没有然后了。两周后问起来，双方都说以为对方做了。

KI kann diese Probleme lösen:
- Sprach-zu-Text, automatische Sprechererkennung
- Kernpunkte extrahieren, Wichtiges unterscheiden
- Aufgaben automatisch zusammenfassen, mit klaren Verantwortlichen
- Strukturierte Protokolle generieren, alles auf einen Blick klar

---

## Werkzeugauswahl

目前主流のIA議事録ツールは以下のような種類があります：

**第一类：専門会議ツール自带**
- **Otter.ai**：开会的时候实时转录，标记发言人，自动生成摘要。英文做得特别好，中文也在不断优化。
- **飞书妙记**：飞书开会的话直接用，集成度高，免费额度够日常用。
- **腾讯会议**：自带的纪要功能，腾讯会议用户首选。

**第二类：汎用AIツール**
- **ChatGPT/Claude**：把录音或文字稿丢给它，让它帮忙整理。适合已经有文字记录的情况。
- **DeepSeek**：最近用的人越来越多，效果跟ChatGPT差不多，关键是免费。

**第三类：ローカル展開**
- **Whisper**：开源の音声→文字モデル、自分で実行、データ漏洩不用担心。企业内网环境用这个比较放心。

---

## Konkrete Verwendungsmethoden

### Methode 1: Die KI-Funktion des Besprechungstools direkt nutzen

Am Beispiel von Feishu Miaoji:

1. Vor der Besprechung auf "Transkription starten" klicken
2. Nach der Besprechung auf "Intelligentes Protokoll" klicken
3. Es wird automatisch generiert:
   - Besprechungszusammenfassung (2-3 Absätze)
   - Kapitelübersicht (nach Zeit gegliedert)
   - Zusammenfassung der Redebeiträge (Kernpunkte jeder Person)
   - Aufgaben (automatische Extraktion)

基本上60分の議事録 already generated. Für 90%, selbst noch anpassen.

### Methode 2: Zuerst transkribieren, dann KI um Hilfe bitten

如果你的会议工具没有AI功能，或者转录效果一般，可以这样操作：

**Schritt 1: Textfassung erhalten**
- 用手机录个音，回去转成文字
- 或者用讯飞听见、网易见外这些工具转录

**Schritt 2: Der KI Anweisungen zum Organisieren geben**

我常用的提示词是这样的：

```
请帮我整理一份会议纪要，内容如下：

【粘贴会议记录】

请按以下格式整理：
1. 会議基本信息（時間、参加者、テーマ）
2. 讨论の主要議題（ポイントごとに列出）
3. 关键結論和決定（突出表示）
4. 待办事項（誰负责，什么时候完成，都要列清楚）
5. 争议のある点（如果有的话）

注意事项：
- 区分清楚每个人的观点
- 待办事項要具体到责任人和截止时间
- 用简洁明了的语言，不要太正式
```

这个提示词基本能产出80分的纪要。

---

## Praktisches Beispiel: Produktanforderungsüberprüfung

假设开了个会，讨论要不要做一个新機能。原始会議记录大概是这样的：

---

**Besprechungsprotokoll:**

Produktmanager: Hallo zusammen, heute besprechen wir das Mitgliedersystem.

Technischer Leiter Lao Wang: Das Mitgliedersystem haben wir vorher untersucht, der Aufwand ist beträchtlich.

Produktmanager: 这个需求确实拖了很久了，客户那边催得紧。

Lao Wang: 我也知道急，但你看我们现在人手，三个项目并行，人都抽不出来。

Produktmanager: 那你看怎么办？

Lao Wang: 要不然这样，先上个简单点的，把基础功能做了，增值服务后面再加。

Produktmanager: 也行。那基础功能有哪些？

Lao Wang: 积分、等级、这几个是最基础的。

Produktmanager: 那这个版本大概多久？

Lao Wang: 乐观估计一个月。

Produktmanager: 一个月可以接受。那谁负责？

Lao Wang: 小李牵头，小张配合。

Xiao Li: 好的。

Produktmanager: 好，那今天先这样，我回去出详细需求。

---

**Von KI organisiertes Protokoll:**

---

### Produktanforderungsüberprüfungs-Protokoll

**Besprechungszeit**: X. X. 2024
**Teilnehmer**: Produktmanager, Technischer Leiter Lao Wang, Xiao Li, Xiao Zhang
**Thema**: Mitgliedersystem-Anforderungsüberprüfung

**Besprochene Themen**:

1. Soll das Mitgliedersystem gemacht werden?
   - Schlussfolgerung: Ja, aber in zwei Phasen
   - Grund: Der Kunde drängt, aber die technischen Ressourcen sind begrenzt

2. Was in der ersten Phase?
   - Schlussfolgerung: Grundfunktionen (Punkte, Level)
   - Mehrwertdienste (Einlösung, exklusive Rechte) für die zweite Phase

**Wichtige Entscheidungen**:

- Erste Phase des Mitgliedersystems in einem Monat abgeschlossen
- Xiao Li als Leiter, Xiao Zhang als Unterstützung
- Produktmanager diese Woche für detaillierte Anforderungsdokumentation verantwortlich

**Aufgaben**:

| Aufgabe | Verantwortlich | Fällig |
|---------|----------------|--------|
| Detaillierte Anforderungsdokumentation ausgeben | Produktmanager | Freitag |
| Technisches Schema entwerfen | Lao Wang | Montag |
| Entwicklung beginnen | Xiao Li, Xiao Zhang | Dienstag |

---

这比看原始记录舒服多了吧？

---

## Fortgeschrittene Techniken

### Technik 1: KI bitten, "Diskussion" und "Entscheidung" zu unterscheiden

很多人写纪要的一大问题是把讨论过程和最终结论混在一起。

可以在提示词里加一句：

> "请明确区分'讨论中提到的观点'和'最终达成的决策'，用不同格式标注"

### Technik 2: Zusätzliche Informationen anfordern

如果原始记录里有些地方写得很模糊，可以让AI追问。

比如原记录写着"小李负责"，可以让AI自动补全：

> "请根据上下文推断每个待办事项的责任人和截止时间，如果信息不足，用【待确认】标注"

### Technik 3: Mehrere Versionen generieren

如果这封纪要要发给不同的人，可以让AI出不同版本：

> "请生成三个版本的纪要：
> 1. 完整版（发给参会人员）
> 2. 精简版（发给领导，只看结论和待办）
> 3. 执行版（只发给相关执行人）"

### Technik 4: Aufgaben in den Kalender importieren

很多AI工具支持把提取出的待办事项导出为日历事件或任务。

以ChatGPT为例，生成纪要后可以让它：

> "把上面的待办事项生成iCalendar格式的文本"

然后复制到日历里，到期自动提醒。

---

## Häufige Fragen

### Q1: Was tun wenn man nicht aufnehmen kann?

有些会议涉及敏感信息，不让录音。那就自己勤快点，边听边记要点。

我的方法是：
- 只记关键词，谁说了什么观点
- 用#标记决策，用!标记待办
- 散会后马上整理，趁还记得的时候

### Q2: Was tun wenn KI-Protokoll ungenau ist?

检查几个常见问题：

1. **转录错误**：先确认原始转录是否正确，有时候同音字会闹笑话
2. **上下文缺失**：有些会议是接续开的，AI不知道前面的背景，可能理解偏
3. **专业术语**：行业黑话AI可能不认识，可以提前给AI一份术语表

### Q3: Bei Besprechungen mit vielen Leuten, wer spricht?

最好在会议开始前大家先自报家门，或者主持人介绍一圈。

如果转录工具支持标记发言人，让它自动标注。不支持的话，在提示词里加一句：

> "请根据上下文判断这段话是谁说的，如果不确定就标注【未知发言人】"

### Q4: Was tun wenn Besprechung zu lang ist?

拆开整理。

几个小时的会议，不可能一次整理完。我通常这样做：

1. 每小时或每结束一个议题，生成一个小结
2. 最后把这些小结汇总成完整版
3. 也可以让AI先读一遍整体结构，再让它深入整理每个部分

---

## Empfohlener Arbeitsablauf

结合我自己的使用经验，推荐一个高效的工作流：

**Vor der Besprechung**：提前拿到议程，知道要讨论什么，心里有底

**Während der Besprechung**：
- 用飞书/Otter开实时转写
- 边听边在脑子里过一遍重点
- 对重要决策当场确认："我总结一下，刚才说的是不是这样..."

**Nach der Besprechung**：
- 第一时间打开转写记录，修正明显错误
- 丢给AI，按提示词整理
- 自己过一遍，补上AI漏掉的细节
- 确认待办事项有没有漏、责任人有没有写错
- 发出纪要，同时抄送相关leader

整个流程下来，一个小时左右的会，整理时间控制在15-20分钟。

---

## Zusammenfassung

会议纪要的核心是**信息传递**和**责任明确**。

用AI不是偷懒，是把重复劳动交给机器，让自己专注在真正需要思考的事情上。

但AI终究是工具，关键点还得自己把控：
- 决策有没有记对？
- 待办有没有漏人？
- 时间节点有没有写错？

这些涉及到人和时间的事，AI只能辅助，不能全信。

今天分享的方法，希望能帮你省点时间少加会儿班。有问题随时交流。

---

**Verwandte Suchen**: KI Protokoll, Meeting Protokoll, ChatGPT, Claude, DeepSeek, Meeting Effizienz, KI Werkzeuge, KI Meeting Zusammenfassung, Automatisches Protokoll, Geschäft Effizienz, KI Meeting Transkription, KI Meeting Assistent