"""Blog index + 3 posts (DE + EN). Structure per post: hook, problem, agitate, solution, proof, offer
(content framework Michael). Self-service CTA = Verlust-Check / loss check, then demo and free call."""
from common import CALL, DEMO, DEMO_EN, MCP, page

HBR = "https://hbr.org/2011/03/the-short-life-of-online-sales-leads"
DATE = "2026-11-24"


def offer(lang):
    if lang == "de":
        return f"""<section class="cta"><p class="kicker">Dein nächster Schritt</p><h2>Wie viele Anfragen verlierst du gerade?</h2>
<p>Der Verlust-Check rechnet in zwei Minuten aus, wie viel Umsatz dir langsame Antworten kosten. Danach kannst du den Demo-Agenten deiner Branche auf WhatsApp testen oder dir alles von uns einrichten lassen.</p>
<div class="btns"><a class="btn" href="../../verlust-check/">Verlust-Check starten</a><a class="btn btn--ghost" href="{DEMO}">Demo testen</a><a class="btn btn--ghost" href="{CALL}">Kostenloses Gespräch</a></div></section>"""
    return f"""<section class="cta"><p class="kicker">Your next step</p><h2>How many leads are you losing right now?</h2>
<p>The loss check works out in two minutes how much revenue slow replies cost you. Then try the demo agent for your industry on WhatsApp, or let us set everything up for you.</p>
<div class="btns"><a class="btn" href="../../loss-check/">Start the loss check</a><a class="btn btn--ghost" href="{DEMO_EN}">Try the demo</a><a class="btn btn--ghost" href="{CALL}">Free call</a></div></section>"""


POSTS = [
    dict(
        de_slug="ki-agent-mit-whatsapp-verbinden", en_slug="connect-ai-agent-to-whatsapp",
        de_title="Eigenen KI-Agenten mit WhatsApp verbinden: so geht es in 2 Minuten",
        en_title="Connect your own AI agent to WhatsApp: how it works in 2 minutes",
        de_desc="Claude, ChatGPT oder Muse beantworten deine WhatsApp-Anfragen. Ein Satz reicht, der Agent richtet den Rest selbst ein.",
        en_desc="Claude, ChatGPT or Muse answer your WhatsApp leads. One sentence is enough, the agent sets up the rest itself.",
        de=f"""<p class="lead">Dein KI-Agent schreibt dir Mails, fasst Meetings zusammen und baut Tabellen. Aber wenn um 22:14 Uhr eine Anfrage auf WhatsApp reinkommt, sieht er sie nicht.</p>
<h2>Das Problem: Dein Agent ist von deinen Kunden abgeschnitten</h2>
<p>Die meisten Betriebe nutzen heute einen KI-Agenten: Claude, ChatGPT, Muse oder Grokbot. Die Anfragen der Kunden landen aber woanders, auf WhatsApp, in Instagram-Nachrichten, in Formularen. Zwischen beiden sitzt ein Mensch, der kopiert, nachschaut und zurückschreibt. Meistens erst am nächsten Morgen.</p>
<h2>Was das kostet</h2>
<p>Jede Stunde Wartezeit macht eine Anfrage kälter. In der bekannten Studie von <a href="{HBR}">Oldroyd und Kollegen (Harvard Business Review, 2011)</a> hatten Firmen, die innerhalb einer Stunde reagierten, eine siebenmal höhere Chance auf ein qualifizierendes Gespräch als Firmen, die eine Stunde später reagierten. Wer 24 Stunden oder länger wartete, lag mehr als 60-mal dahinter. Dein Agent könnte in Sekunden antworten. Er darf nur nicht.</p>
<h2>Die Lösung: ein Satz, der Agent macht den Rest</h2>
<p>Mit Auftragspilot verbindest du deinen Agenten mit deinem WhatsApp und Instagram. Du kopierst einen einzigen Satz in den Chat mit deinem Agenten:</p>
<pre>Richte Auftragspilot für mich ein. Folge dazu der Anleitung unter https://larsomatic.org/auftragspilot/agenten/</pre>
<p>Der Agent liest die Anleitung, legt dein Konto an und fragt dich ein paar Dinge zu deinem Betrieb. Du bestätigst nur einen 6-stelligen Code aus der E-Mail und verbindest deine WhatsApp-Nummer mit einem Klick über Facebook. Ab dann liest dein Agent die Gespräche mit, beantwortet Fragen und bucht Termine in deinen Kalender.</p>
<p>Lieber selbst? In Claude, ChatGPT oder Cursor trägst du nur die Adresse <code>{MCP}</code> ein und meldest dich im Browser an. Kein Schlüssel zum Kopieren.</p>
<h2>So sieht es in der Praxis aus</h2>
<ul><li>Ein Lead füllt deine Facebook-Anzeige aus und hat Sekunden später eine WhatsApp mit seinem Namen.</li>
<li>Dein Agent sieht die Antwort, fragt nach Budget und Zeitpunkt und schlägt drei freie Termine vor.</li>
<li>Du bekommst nur noch die Nachricht: „Termin gebucht, Donnerstag 10 Uhr.“</li></ul>
<p>Auftragspilot achtet dabei auf die Regeln von WhatsApp: Einwilligung, 24-Stunden-Fenster, Abmeldungen. Dein Agent bekommt bei jedem Stopp einen klaren Fehlercode statt einer gesperrten Nummer. Details stehen auf der Seite <a href="../../limits/">Limits</a>.</p>
<h2>Keine Zeit oder noch nie mit KI gearbeitet?</h2>
<p>Dann übernehmen wir das. Wir richten Nummer, Kalender, Texte und Agent für dich ein, du bekommst einen fertigen Assistenten, der in deinem Namen antwortet.</p>""",
        en=f"""<p class="lead">Your AI agent writes your e-mails, summarises meetings and builds spreadsheets. But when a WhatsApp enquiry comes in at 10:14 pm, it doesn't see it.</p>
<h2>The problem: your agent is cut off from your customers</h2>
<p>Most businesses use an AI agent today: Claude, ChatGPT, Muse or Grokbot. Customer enquiries land somewhere else, on WhatsApp, in Instagram messages, in forms. In between sits a person who copies, checks and writes back. Usually the next morning.</p>
<h2>What it costs</h2>
<p>Every hour of waiting makes a lead colder. In the well-known study by <a href="{HBR}">Oldroyd and colleagues (Harvard Business Review, 2011)</a>, firms that responded within an hour were seven times as likely to have a qualifying conversation as firms that responded an hour later. Those that waited 24 hours or longer were more than 60 times behind. Your agent could answer in seconds. It just isn't allowed to.</p>
<h2>The fix: one sentence, the agent does the rest</h2>
<p>Auftragspilot connects your agent to your WhatsApp and Instagram. You paste one sentence into the chat with your agent:</p>
<pre>Set up Auftragspilot for me by following https://larsomatic.org/auftragspilot/en/agents/</pre>
<p>The agent reads the guide, creates your account and asks you a few things about your business. You only confirm a 6-digit code from the e-mail and connect your WhatsApp number with one click via Facebook. From then on your agent reads the conversations, answers questions and books appointments into your calendar.</p>
<p>Prefer to do it yourself? In Claude, ChatGPT or Cursor you just add the address <code>{MCP}</code> and sign in in the browser. No key to copy.</p>
<h2>What it looks like in practice</h2>
<ul><li>A lead fills in your Facebook ad and gets a WhatsApp with their name seconds later.</li>
<li>Your agent sees the reply, asks about budget and timing and suggests three free slots.</li>
<li>All you get is the message: “Appointment booked, Thursday 10 am.”</li></ul>
<p>Auftragspilot keeps to WhatsApp's rules: consent, the 24-hour window, opt-outs. Whenever something is stopped, your agent gets a clear error code instead of a blocked number. Details on the <a href="../../limits/">limits</a> page.</p>
<h2>No time, or never worked with AI?</h2>
<p>Then we do it. We set up the number, calendar, texts and agent for you, and you get a finished assistant that answers in your name.</p>"""),
    dict(
        de_slug="offizielle-whatsapp-api-vs-whatsapp-web", en_slug="official-whatsapp-api-vs-whatsapp-web",
        de_title="Offizielle WhatsApp Business API vs. WhatsApp-Web-Automatisierung: warum das für Leads wichtig ist",
        en_title="Official WhatsApp Business API vs. WhatsApp Web automation: why it matters for leads",
        de_desc="QR-Code-Tools sind schnell eingerichtet, dürfen aber neue Leads kaum anschreiben. Was der Unterschied für deine Anfragen bedeutet.",
        en_desc="QR code tools are quick to set up but can barely message new leads. What the difference means for your enquiries.",
        de=f"""<p class="lead">Du verbindest dein WhatsApp per QR-Code mit einem Tool, und zehn Minuten später antwortet eine KI. Klingt perfekt. Bis der erste Lead aus deiner Anzeige kommt und das Tool ihm nicht schreiben darf.</p>
<h2>Zwei Wege, WhatsApp zu automatisieren</h2>
<p><b>WhatsApp Web per QR-Code:</b> Das Tool meldet sich an deinem Handy an wie WhatsApp Web am Computer. Keine Freigabe durch Meta, sofort startklar. Aber es ist nicht die offizielle Schnittstelle.</p>
<p><b>Offizielle WhatsApp Business Platform:</b> Die Schnittstelle, die Meta für Unternehmen anbietet. Einmalige Einrichtung über Facebook, danach darfst du freigegebene Vorlagen schicken.</p>
<h2>Warum das bei Leads den Unterschied macht</h2>
<p>Leads aus Anzeigen und Formularen haben dir noch nie geschrieben. Über WhatsApp Web darfst du sie meist gar nicht anschreiben, oder nur sehr wenige pro Tag. Einer der bekannten Anbieter erlaubt zum Beispiel 10 neue WhatsApp-Chats pro Tag, und nur mit Leuten, die vorher geschrieben oder zugestimmt haben (Stand 24.11.2026, laut Anbieter-Website). Wenn deine Kampagne 40 Leads am Tag bringt, warten 30 davon bis morgen.</p>
<p>Und Warten kostet: In der Studie von <a href="{HBR}">Oldroyd und Kollegen (Harvard Business Review, 2011)</a> brauchten Unternehmen im Schnitt 42 Stunden für die erste Antwort, 23 % antworteten gar nicht. Wer innerhalb einer Stunde reagierte, hatte eine siebenmal höhere Chance auf ein qualifizierendes Gespräch.</p>
<h2>Was die offizielle Platform möglich macht</h2>
<ul><li><b>Vorlagen an neue Kontakte:</b> Jeder Lead mit Einwilligung bekommt sofort eine WhatsApp, auch nachts.</li>
<li><b>Limits, die mitwachsen:</b> Neue Nummern starten niedrig, mit guter Qualität steigt das Tageslimit von Meta.</li>
<li><b>Kein Sperr-Risiko durch inoffizielle Automatisierung:</b> Du nutzt genau den Weg, den Meta für Unternehmen vorsieht.</li></ul>
<p>Ehrlicherweise: Die offizielle Platform kostet pro Vorlage eine Gebühr von Meta, je nach Land und Kategorie, und braucht eine einmalige Einrichtung. Für Antworten auf Nachrichten, die Kunden selbst schicken, reicht oft auch ein einfacheres Tool.</p>
<h2>So machen wir es bei Auftragspilot</h2>
<p>Auftragspilot läuft ausschließlich über die offizielle WhatsApp Business Platform. Du verbindest deine Nummer mit einem Klick über Facebook. Ab dann bekommt jeder Lead aus deiner Anzeige in Sekunden eine Vorlage mit seinem Namen, die eingebaute KI qualifiziert ihn und bucht den Termin. Oder dein eigener KI-Agent übernimmt das. Den ganzen Vergleich findest du auf der Seite <a href="../../vergleich/">Vergleich</a>.</p>""",
        en=f"""<p class="lead">You link your WhatsApp to a tool with a QR code, and ten minutes later an AI is answering. Sounds perfect. Until the first lead from your ad arrives and the tool isn't allowed to message them.</p>
<h2>Two ways to automate WhatsApp</h2>
<p><b>WhatsApp Web via QR code:</b> the tool logs in on your phone like WhatsApp Web on a computer. No approval from Meta, ready right away. But it is not the official interface.</p>
<p><b>Official WhatsApp Business Platform:</b> the interface Meta offers to businesses. One-time setup via Facebook, after that you may send approved templates.</p>
<h2>Why it makes the difference for leads</h2>
<p>Leads from ads and forms have never written to you. Over WhatsApp Web you mostly can't message them at all, or only very few per day. One well-known provider, for example, allows 10 new WhatsApp chats per day, and only with people who wrote first or opted in (as of 24 Nov 2026, according to the provider's website). If your campaign brings 40 leads a day, 30 of them wait until tomorrow.</p>
<p>And waiting costs: in the study by <a href="{HBR}">Oldroyd and colleagues (Harvard Business Review, 2011)</a> companies took 42 hours on average for the first reply, and 23% never replied. Those that responded within an hour were seven times as likely to have a qualifying conversation.</p>
<h2>What the official platform makes possible</h2>
<ul><li><b>Templates to new contacts:</b> every lead with consent gets a WhatsApp right away, even at night.</li>
<li><b>Limits that grow:</b> new numbers start low, with good quality Meta's daily limit goes up.</li>
<li><b>No ban risk from unofficial automation:</b> you use exactly the route Meta provides for businesses.</li></ul>
<p>To be fair: the official platform charges a Meta fee per template, depending on country and category, and needs a one-time setup. For replying to messages customers send themselves, a simpler tool is often enough.</p>
<h2>How we do it at Auftragspilot</h2>
<p>Auftragspilot runs only on the official WhatsApp Business Platform. You connect your number with one click via Facebook. From then on every lead from your ad gets a template with their name within seconds, the built-in AI qualifies them and books the appointment. Or your own AI agent takes over. The full comparison is on the <a href="../../compare/">compare</a> page.</p>"""),
    dict(
        de_slug="lead-in-60-sekunden-beantworten", en_slug="answer-leads-in-60-seconds",
        de_title="Lead in 60 Sekunden beantworten: warum Geschwindigkeit Aufträge bringt",
        en_title="Answer a lead in 60 seconds: why speed wins jobs",
        de_desc="Die meisten Betriebe antworten nach Stunden. Wer in Sekunden antwortet, gewinnt den Auftrag, bevor die Konkurrenz zurückruft.",
        en_desc="Most businesses reply after hours. Whoever replies in seconds wins the job before the competition calls back.",
        de=f"""<p class="lead">Freitag, 19:40 Uhr. Jemand füllt dein Formular aus und fragt nach einem Angebot. Du siehst es am Montag. Er hat am Samstag schon bei der Konkurrenz unterschrieben.</p>
<h2>Das Problem ist nicht die Anzahl der Leads</h2>
<p>Viele Betriebe geben Tausende für Anzeigen aus und bekommen genug Anfragen. Verloren gehen sie danach: Die Anfrage landet in einem Postfach, jemand ruft zurück, wenn Zeit ist, und erreicht niemanden. Abends, am Wochenende und an Feiertagen antwortet gar keiner.</p>
<h2>Was Warten wirklich kostet</h2>
<p>Die Studie von <a href="{HBR}">Oldroyd, McElheran und Elkington (Harvard Business Review, 2011)</a> hat die Antwortzeiten von 2.241 US-Unternehmen gemessen. Im Schnitt dauerte die erste Antwort 42 Stunden, 23 % antworteten nie. In einer Teilstudie mit 1,25 Millionen Leads zeigte sich: Wer innerhalb einer Stunde reagierte, hatte eine siebenmal höhere Chance auf ein qualifizierendes Gespräch als wer eine Stunde später reagierte. Gegenüber 24 Stunden Wartezeit lag der Faktor bei über 60.</p>
<p>Rechne es für deinen Betrieb: Wenn von 100 Anfragen im Monat auch nur zehn wegen langsamer Antworten verloren gehen, wie viel Umsatz ist das bei deinem durchschnittlichen Auftragswert?</p>
<h2>Die Lösung: Antworten, bevor der Lead weiterklickt</h2>
<p>Kein Mensch schafft es, jede Anfrage in einer Minute zu beantworten, auch nicht nachts. Ein Assistent auf WhatsApp schon. Bei Auftragspilot läuft das so:</p>
<ol><li>Die Anfrage kommt aus der Anzeige, dem Formular oder per WhatsApp.</li>
<li>Sekunden später bekommt der Lead eine persönliche WhatsApp mit seinem Namen.</li>
<li>Zwei bis drei Fragen klären, ob er passt: Bedarf, Zeitpunkt, Budget.</li>
<li>Die KI bietet echte freie Termine aus deinem Kalender an und bucht direkt.</li>
<li>Antwortet er nicht, fasst der Assistent freundlich nach.</li></ol>
<h2>Selbst ausprobieren</h2>
<p>Der beste Beweis ist, es zu erleben: Trag auf der Demo-Seite deine Nummer ein, wähl deine Branche und schau, wie schnell die erste WhatsApp kommt. Danach kannst du deinen eigenen KI-Agenten verbinden oder alles von uns einrichten lassen.</p>""",
        en=f"""<p class="lead">Friday, 7:40 pm. Someone fills in your form and asks for a quote. You see it on Monday. They signed with a competitor on Saturday.</p>
<h2>The problem isn't the number of leads</h2>
<p>Many businesses spend thousands on ads and get enough enquiries. They get lost afterwards: the enquiry lands in an inbox, someone calls back when there's time and reaches nobody. Evenings, weekends and holidays, nobody answers at all.</p>
<h2>What waiting really costs</h2>
<p>The study by <a href="{HBR}">Oldroyd, McElheran and Elkington (Harvard Business Review, 2011)</a> measured the response times of 2,241 US companies. On average the first reply took 42 hours, and 23% never replied. A sub-study with 1.25 million leads showed: firms that responded within an hour were seven times as likely to have a qualifying conversation as firms that responded an hour later. Compared with waiting 24 hours, the factor was over 60.</p>
<p>Do the maths for your business: if just ten out of 100 enquiries a month are lost to slow replies, how much revenue is that at your average job value?</p>
<h2>The fix: answer before the lead clicks away</h2>
<p>No person can answer every enquiry within a minute, especially not at night. An assistant on WhatsApp can. At Auftragspilot it works like this:</p>
<ol><li>The enquiry comes from the ad, the form or WhatsApp.</li>
<li>Seconds later the lead gets a personal WhatsApp with their name.</li>
<li>Two or three questions check whether they fit: need, timing, budget.</li>
<li>The AI offers genuinely free slots from your calendar and books directly.</li>
<li>If they don't reply, the assistant follows up politely.</li></ol>
<h2>Try it yourself</h2>
<p>The best proof is to experience it: enter your number on the demo page, pick your industry and see how fast the first WhatsApp arrives. Then connect your own AI agent or let us set everything up for you.</p>"""),
]


def build():
    for lang in ("de", "en"):
        d = lang == "de"
        base = "blog/" if d else "en/blog/"
        alt_base = "en/blog/" if d else "blog/"
        cards = ""
        for p in POSTS:
            slug, alt_slug = (p["de_slug"], p["en_slug"]) if d else (p["en_slug"], p["de_slug"])
            title, desc = (p["de_title"], p["de_desc"]) if d else (p["en_title"], p["en_desc"])
            cards += f'<a class="card" href="{slug}/"><span class="pill">{DATE}</span><h3>{title}</h3><p>{desc}</p></a>'
            body = (f'<p class="kicker"><a href="../">← Blog</a> · {DATE}</p><article><h1>{title}</h1>'
                    f'{p["de"] if d else p["en"]}</article>{offer(lang)}')
            page(lang, f"{base}{slug}/", f"{alt_base}{alt_slug}/", title, desc, body, current=base)
        body = (f'<p class="kicker">Blog</p><h1>{"Schneller vom Lead zum Auftrag." if d else "Faster from lead to job."}</h1>'
                f'<p class="lead">{"Wie Betriebe ihre Anfragen in Sekunden beantworten, mit eigenem KI-Agenten oder fertig eingerichtet." if d else "How businesses answer their enquiries in seconds, with their own AI agent or fully set up for them."}</p>'
                f'<div class="grid">{cards}</div>')
        page(lang, base, alt_base, "Blog", "Artikel über schnelle Lead-Antworten, WhatsApp und KI-Agenten." if d else "Articles on fast lead response, WhatsApp and AI agents.", body, wide=True, current=base)
