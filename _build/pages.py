"""Security, limits, privacy (EN), changelog, use cases, industries, compare (DE + EN)."""
from common import APP, CALL, DEMO, DEMO_EN, cta, faq, page, table, ul

# ------------------------------------------------------------------ security
def security():
    de = [
        ("Passwörter", "Passwörter speichern wir nur als gesalzenen scrypt-Hash, nie im Klartext."),
        ("Zugangsschlüssel", "Ein Schlüssel wird nur einmal angezeigt und danach nur als SHA-256-Hash gespeichert. Pro Agent ein eigener Schlüssel, jederzeit in der App löschbar."),
        ("Drei Rechte-Stufen", "<b>Lesen</b>, <b>Entwurf</b> (alles Ausgehende wartet auf deine Freigabe) oder <b>Schreiben</b>. Du entscheidest beim Verbinden."),
        ("Anmeldung für Agenten", "OAuth 2.1 mit PKCE (S256). Dein Agent öffnet ein Browserfenster, du meldest dich an und klickst „Erlauben“. Kein Schlüssel zum Kopieren."),
        ("Freigabe-Seite", "Die Seite, auf der du einen Agenten erlaubst, lässt sich nicht in fremde Websites einbetten. So kann dir niemand einen Klick unterschieben."),
        ("Kurze Gültigkeit", "Ein-Klick-Einrichtungslinks gelten 2 Stunden. Einrichtungs-Codes per E-Mail gelten 30 Minuten und erlauben höchstens 5 Versuche."),
        ("Getrennte Konten", "Jeder Schlüssel sieht nur das eigene Konto, nie die Daten anderer Kunden."),
        ("Offizielle WhatsApp-Anbindung", "WhatsApp läuft nur über die offizielle WhatsApp Business Platform von Meta. Keine WhatsApp-Web- oder QR-Code-Tricks, also kein Sperr-Risiko durch inoffizielle Automatisierung."),
        ("Abmeldung", "Schreibt ein Kontakt STOP, respektieren wir das dauerhaft. Diese Person bekommt keine Nachrichten mehr."),
        ("Übergabe an einen Menschen", "Übernimmt ein Mensch ein Gespräch, schreibt der Agent in diesem Chat nicht mehr, bis er es zurückgibt."),
        ("Schutz vor eingeschleusten Anweisungen", "Nachrichten von Kunden, die wie Anweisungen an eine KI aussehen, werden als verdächtig markiert und an Agenten als nicht vertrauenswürdiger Kundentext weitergegeben. Die eingebaute KI befolgt sie nicht."),
        ("Kein doppelter Versand", "Mit einem Idempotenz-Schlüssel wird eine Nachricht auch bei einer Wiederholung nur einmal verschickt."),
    ]
    en = [
        ("Passwords", "Passwords are stored only as a salted scrypt hash, never in plain text."),
        ("Access keys", "A key is shown once and then stored only as a SHA-256 hash. One key per agent, revocable any time in the app."),
        ("Three permission levels", "<b>Read</b>, <b>draft</b> (everything outgoing waits for your approval) or <b>write</b>. You choose when you connect."),
        ("Sign-in for agents", "OAuth 2.1 with PKCE (S256). Your agent opens a browser window, you sign in and click “Allow”. No key to copy."),
        ("Approval page", "The page where you allow an agent cannot be embedded in other websites, so nobody can trick you into a click."),
        ("Short lifetimes", "One-click setup links are valid for 2 hours. E-mail setup codes are valid for 30 minutes with at most 5 tries."),
        ("Separate accounts", "Every key only sees its own account, never other customers' data."),
        ("Official WhatsApp connection", "WhatsApp runs only over Meta's official WhatsApp Business Platform. No WhatsApp Web or QR code tricks, so no ban risk from unofficial automation."),
        ("Opt-out", "When a contact writes STOP, we respect it permanently. That person gets no more messages."),
        ("Handover to a person", "When a person takes over a conversation, the agent stops writing in that chat until it is handed back."),
        ("Protection against injected instructions", "Customer messages that look like instructions to an AI are flagged as suspicious and passed to agents as untrusted customer text. The built-in AI does not follow them."),
        ("No double sends", "With an idempotency key a message is sent only once, even if a request is retried."),
    ]
    for lang, items in (("de", de), ("en", en)):
        d = lang == "de"
        rows = "".join(f'<div class="card"><h3>{t}</h3><p>{x}</p></div>' for t, x in items)
        body = (f'<p class="kicker">{"Sicherheit" if d else "Security"}</p><h1>{"So schützen wir deine Daten und deine Nummer." if d else "How we protect your data and your number."}</h1>'
                f'<p class="lead">{"Dein Agent arbeitet mit echten Kundengesprächen. Deshalb bekommt er nur so viel Zugriff, wie du erlaubst, und jede Verbindung lässt sich mit einem Klick trennen." if d else "Your agent works with real customer conversations. So it only gets the access you allow, and every connection can be revoked with one click."}</p>'
                f'<div class="grid">{rows}</div>'
                + (f'<p class="note">Mehr dazu: <a href="../limits/">Limits und Fehlercodes</a> · <a href="../datenschutz/">Datenschutzerklärung</a> · <a href="{APP}/rechtliches/avv">Auftragsverarbeitungsvertrag (AVV)</a></p>' if d
                   else f'<p class="note">More: <a href="../limits/">Limits and error codes</a> · <a href="../privacy/">Privacy policy</a> · <a href="{APP}/rechtliches/terms#data-processing">Data processing agreement (DPA)</a></p>')
                + cta(lang))
        page(lang, "sicherheit/" if d else "en/security/", "en/security/" if d else "sicherheit/",
             "Sicherheit" if d else "Security",
             "Schlüssel, Rechte-Stufen, OAuth-Anmeldung, offizielle WhatsApp-Anbindung und Schutz vor eingeschleusten Anweisungen." if d else
             "Keys, permission levels, OAuth sign-in, official WhatsApp connection and protection against injected instructions.", body)


# ------------------------------------------------------------------ limits
CODES = [
    ("UNAUTHORIZED", "Kein oder ungültiger Schlüssel bzw. Anmeldung.", "Missing or invalid key or sign-in."),
    ("FORBIDDEN_SCOPE", "Der Schlüssel hat nicht genug Rechte (z. B. nur Lesen).", "The key lacks the permission (e.g. read only)."),
    ("NOT_FOUND", "Kontakt, Kunde oder Vorgang nicht gefunden.", "Contact, client or item not found."),
    ("INVALID_ARGUMENT", "Ein Wert fehlt oder hat das falsche Format.", "A value is missing or has the wrong format."),
    ("RATE_LIMITED", "Zu viele Anfragen. Warte <code>retry_after_seconds</code>, dann erneut.", "Too many requests. Wait <code>retry_after_seconds</code>, then retry."),
    ("OUTSIDE_24H_WINDOW", "Freitext geht nur bis 24 Stunden nach der letzten Nachricht des Kunden. Danach nur mit freigegebener Vorlage.", "Free text only within 24 hours after the customer's last message. After that only with an approved template."),
    ("CONSENT_REQUIRED", "Für diesen Kontakt liegt keine Einwilligung vor.", "There is no consent for this contact."),
    ("OPTED_OUT", "Der Kontakt hat sich abgemeldet (STOP).", "The contact opted out (STOP)."),
    ("HANDED_OVER", "Ein Mensch hat das Gespräch übernommen.", "A person has taken over the conversation."),
    ("NOT_CONNECTED", "Keine WhatsApp-Nummer bzw. kein Kanal verbunden.", "No WhatsApp number or channel connected."),
    ("TEMPLATE_REQUIRED", "Hier ist eine freigegebene Vorlage nötig, z. B. außerhalb des 24-Stunden-Fensters oder für Broadcasts.", "An approved template is required, e.g. outside the 24-hour window or for broadcasts."),
    ("NEEDS_CONFIRMATION", "Die Aktion braucht eine ausdrückliche Bestätigung (z. B. Broadcast senden).", "The action needs explicit confirmation (e.g. sending a broadcast)."),
    ("OUTSIDE_SENDING_HOURS", "Außerhalb von 08:00 bis 20:00 Uhr in der Zeitzone des Kontos.", "Outside 08:00 to 20:00 in the account's time zone."),
    ("NEEDS_APPROVAL", "Entwurfs-Schlüssel: Die Nachricht wurde zur Freigabe gespeichert, nicht gesendet.", "Draft key: the message was saved for approval, not sent."),
    ("PLAN_REQUIRED", "Dafür muss ein Paket gebucht sein.", "This needs an active plan."),
]


def limits():
    for lang in ("de", "en"):
        d = lang == "de"
        if d:
            rows = [("API", "600 Anfragen pro Stunde pro Schlüssel"), ("Einrichtungs-Server (ohne Schlüssel)", "300 Anfragen pro Stunde pro IP-Adresse"),
                    ("Freitext-Antworten", "nur bis 24 Stunden nach der letzten Nachricht des Kunden (Regel von Meta), danach nur freigegebene Vorlagen"),
                    ("Neue Gespräche (start_conversation)", "60 pro Stunde pro Konto, nur mit Einwilligung"),
                    ("Broadcasts", "nur freigegebene Vorlage, nur an Kontakte mit Einwilligung (Formular, Anzeige, Testseite oder selbst geschrieben), ohne Abmeldung, Bestätigung nötig, höchstens 1.000 Empfänger pro Broadcast, 30 pro Minute pro Nummer, nur 08:00 bis 20:00 Uhr"),
                    ("Tageslimit von Meta", "gilt zusätzlich pro Nummer: neue Nummern starten niedrig und steigen mit guter Qualität"),
                    ("Geplante Nachrichten", "bis zu 90 Tage im Voraus"),
                    ("Serien", "höchstens 6 Schritte, mindestens 1 Stunde Abstand, stoppen automatisch bei Antwort oder Abmeldung, nur 08:00 bis 20:00 Uhr"),
                    ("Idempotenz-Schlüssel", "24 Stunden gespeichert"),
                    ("Ein-Klick-Einrichtungslinks", "2 Stunden gültig"), ("E-Mail-Code bei der Einrichtung", "30 Minuten gültig, höchstens 5 Versuche")]
            body = ('<p class="kicker">Limits</p><h1>Klare Grenzen, damit deine Nummer gesund bleibt.</h1>'
                    '<p class="lead">Diese Grenzen schützen deine WhatsApp-Nummer und deine Kontakte. Dein Agent bekommt bei jedem Stopp einen klaren Fehlercode und weiß, was zu tun ist.</p>'
                    + table(["Bereich", "Grenze"], rows)
                    + '<h2>Fehlercodes</h2><p>Jeder Fehler hat ein Feld <code>code</code>. Bei <code>RATE_LIMITED</code> steht zusätzlich <code>retry_after_seconds</code> dabei.</p>'
                    + table(["Code", "Bedeutung"], [(f"<code>{c}</code>", x) for c, x, _ in CODES])
                    + '<p class="note">Mehr: <a href="../sicherheit/">Sicherheit</a> · <a href="../agenten/">KI-Agenten verbinden</a></p>' + cta(lang))
            page("de", "limits/", "en/limits/", "Limits und Fehlercodes", "Alle Grenzen für API, WhatsApp-Versand, Broadcasts, Serien und geplante Nachrichten, plus alle Fehlercodes.", body)
        else:
            rows = [("API", "600 requests per hour per key"), ("Setup server (no key)", "300 requests per hour per IP address"),
                    ("Free-text replies", "only within 24 hours after the customer's last message (Meta rule), after that only approved templates"),
                    ("New conversations (start_conversation)", "60 per hour per account, consent required"),
                    ("Broadcasts", "approved template only, only to contacts with consent (form, ad, test page or wrote first), not opted out, confirmation required, max 1,000 recipients per broadcast, 30 per minute per number, only 08:00 to 20:00"),
                    ("Meta's daily limit", "applies on top per number: new numbers start low and grow with good quality"),
                    ("Scheduled messages", "up to 90 days ahead"),
                    ("Sequences", "max 6 steps, at least 1 hour apart, stop automatically on a reply or opt-out, only 08:00 to 20:00"),
                    ("Idempotency keys", "remembered for 24 hours"),
                    ("One-click setup links", "valid for 2 hours"), ("E-mail setup code", "valid for 30 minutes, max 5 tries")]
            body = ('<p class="kicker">Limits</p><h1>Clear limits that keep your number healthy.</h1>'
                    "<p class=\"lead\">These limits protect your WhatsApp number and your contacts. Whenever something is stopped, your agent gets a clear error code and knows what to do.</p>"
                    + table(["Area", "Limit"], rows)
                    + '<h2>Error codes</h2><p>Every error has a <code>code</code> field. <code>RATE_LIMITED</code> also includes <code>retry_after_seconds</code>.</p>'
                    + table(["Code", "Meaning"], [(f"<code>{c}</code>", x) for c, _, x in CODES])
                    + '<p class="note">More: <a href="../security/">Security</a> · <a href="../agents/">Connect AI agents</a></p>' + cta(lang))
            page("en", "en/limits/", "limits/", "Limits and error codes", "All limits for the API, WhatsApp sending, broadcasts, sequences and scheduled messages, plus all error codes.", body)


# ------------------------------------------------------------------ privacy (EN)
def privacy_en():
    body = f"""<p class="kicker">Privacy</p><h1>Privacy policy</h1>
<p class="meta">English version of the <a href="../../datenschutz/">German privacy policy</a>. If the two differ, the German version applies. [BITTE PRÜFEN: confirm this rule]</p>
<h2>1. Controller</h2><p>Larsomatic OÜ, Tornimäe tn 5, 10145 Tallinn, Estonia, represented by Lars Timmermann. E-mail: lt@larsomatic.org</p>
<h2>2. Hosting of this website</h2><p>This website is hosted on GitHub Pages (GitHub, Inc. / Microsoft, USA). When you open a page, GitHub automatically processes server log data (including IP address, date and time, page requested, browser type). Details: <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy Statement</a>.</p>
<h2>3. Fonts</h2><p>The fonts on this website are served locally from this server. There is no connection to Google servers.</p>
<h2>4. Usage measurement</h2><p>We measure use of this website without cookies and without storing information on your device. We only record the event name (for example “page view”), the page path, the page language, the referring domain and the device group (mobile or desktop). No user ID is assigned and your IP address is not stored. The data is processed on our own n8n server. If “Do Not Track” is enabled in your browser, nothing is sent. Legal basis: legitimate interest, Art. 6(1)(f) GDPR.</p>
<h2>5. Third-party services</h2><p><b>Booking (Cal.com):</b> booking links open Cal.com, which processes your input according to its own privacy policy. <b>WhatsApp:</b> links to WhatsApp open Meta's WhatsApp app. Messages exchanged there are subject to WhatsApp/Meta's privacy terms.</p>
<h2>6. Loss check (form)</h2><p>If you use the lead loss check and request the result, we collect company name, e-mail, optionally phone number, the business figures you enter and the calculated result. Purpose: contacting you about the result and our offer. Legal basis: your consent, Art. 6(1)(a) GDPR. Processing runs through our self-hosted automation (n8n on larsomatic.org), the data is stored in our Notion workspace (Notion Labs, Inc., USA). Storage until the purpose is fulfilled or you withdraw consent.</p>
<h2>7. The Auftragspilot app and connected AI agents</h2>
<p>When a business uses the Auftragspilot app ({APP}/a), the app processes on behalf of that business: contact details of its leads (name, phone number, e-mail if given), the WhatsApp and Instagram messages exchanged, qualification answers, bookings and notes. An AI model processes conversation content to answer leads and qualify them. If the business connects its own AI agent, that agent receives this data through the access the business granted. The business is the controller for its leads' data, we act as processor under the data processing agreement.</p>
<p>[BITTE PRÜFEN: list the processors used by the app (database, hosting, AI model provider, e-mail, WhatsApp/Meta) and their locations, storage periods and the link to the DPA before publishing this section as final.]</p>
<h2>8. Your rights</h2><p>You have the right to access, rectification, erasure and restriction of processing, data portability and to withdraw consent at any time with effect for the future. You may object to processing based on legitimate interest. Contact: lt@larsomatic.org. You also have the right to lodge a complaint with a data protection authority.</p>
<h2>9. Changes</h2><p>We update this policy when the processing changes. The version current at the time of your visit applies.</p>"""
    page("en", "en/privacy/", "datenschutz/", "Privacy policy", "How Auftragspilot processes personal data on this website and in the app.", body)


# ------------------------------------------------------------------ changelog
LOG = [
    ("2026-11-24", "KI-Agenten in zwei Minuten verbinden", "Connect AI agents in two minutes",
     ["Eigene KI-Agenten (Claude, ChatGPT, Muse, Grokbot, Codex, Cursor und weitere) verbinden sich per Browser-Anmeldung, ohne Schlüssel zu kopieren.",
      "Dein Agent kann das Konto selbst anlegen: Du bestätigst nur einen 6-stelligen Code aus der E-Mail.",
      "Anleitungen für 12 Agenten mit eigenem Abschnitt, den die Agenten selbst lesen.",
      "Freigaben: Mit einem Entwurfs-Schlüssel wartet alles Ausgehende auf deine Zustimmung.",
      "Broadcasts mit freigegebenen WhatsApp-Vorlagen, Serien und geplante Nachrichten.",
      "Neue Seiten zu Sicherheit, Limits und Fehlercodes.",
      "Branchen-Demo Treppenlift fragt jetzt Treppenform, Pflegegrad und Budget ab."],
     ["Your own AI agents (Claude, ChatGPT, Muse, Grokbot, Codex, Cursor and more) connect with a browser sign-in, no key to copy.",
      "Your agent can create the account itself: you only confirm a 6-digit code from the e-mail.",
      "Guides for 12 agents, each with a section the agents read themselves.",
      "Approvals: with a draft key everything outgoing waits for your approval.",
      "Broadcasts with approved WhatsApp templates, sequences and scheduled messages.",
      "New pages on security, limits and error codes.",
      "Stair lift demo now asks for staircase type, care level and budget."]),
    ("2026-11-20", "Einrichtung Schritt für Schritt", "Step-by-step setup",
     ["Der Einrichtungs-Assistent führt durch alle Schritte: Unternehmen, WhatsApp-Nummer, Kalender, Anfragen-Quelle, Testen und Livegang.",
      "Die Hotel-Demo bucht Zimmer selbst und schickt eine Bestätigung per E-Mail.",
      "Demo-Agenten begrüßen mit Anrede und Nachnamen, die Demo-Seite gibt es auch auf Englisch.",
      "Wer die Demo testet, kann direkt ein kostenloses Beratungsgespräch buchen."],
     ["The setup assistant guides through every step: business info, WhatsApp number, calendar, lead source, test and go live.",
      "The hotel demo books rooms itself and sends a confirmation e-mail.",
      "Demo agents greet with title and last name, the demo page is also available in English.",
      "Demo testers can book a free consultation right away."]),
    ("2026-11-19", "Branchen-Demos und Selbstbedienung", "Industry demos and self-service",
     ["Demo-Agenten für viele Branchen zum Testen auf WhatsApp, vom Handwerk bis zum Hotel.",
      "Selbst starten: Pakete, Einrichtung durch einen Experten oder eigener Agent über MCP, REST und Webhooks."],
     ["Demo agents for many industries to test on WhatsApp, from trades to hotels.",
      "Start on your own: plans, setup by an expert or your own agent via MCP, REST and webhooks."]),
    ("2026-11-18", "Englisch, Buchungssysteme, Instagram", "English, booking systems, Instagram",
     ["Die App gibt es auf Englisch, mit Vorlagen für Hotels, Villen, Spas, Restaurants und Touren.",
      "Direkte Anbindung an 18 Buchungs- und Hotelsysteme.",
      "Instagram-Direktnachrichten als zweiter Kanal.",
      "Agenturen: Kunden duplizieren und archivieren, Branchenvorlagen, Website-Assistent, Chat-Simulator, eigene Domain und Absender-Adresse, Google- und Microsoft-Kalender direkt."],
     ["The app is available in English, with templates for hotels, villas, spas, restaurants and tours.",
      "Direct connection to 18 booking and hotel systems.",
      "Instagram direct messages as a second channel.",
      "Agencies: duplicate and archive clients, industry templates, website assistant, chat simulator, own domain and sender address, Google and Microsoft calendar directly."]),
    ("2026-11-17", "White Label für Agenturen", "White label for agencies",
     ["Agenturen nutzen eigenen Namen, Logo und Farbe, mit eigener Login-Seite.",
      "Endkunden bekommen eigene Zugänge und sehen nur ihre Leads und Auswertungen."],
     ["Agencies use their own name, logo and colour, with their own login page.",
      "End customers get their own logins and only see their leads and reports."]),
    ("2026-11-07", "Portal für Agenturen", "Portal for agencies",
     ["Agenturen verwalten ihre Kunden in einem Portal: Fragen zur Qualifizierung, Kalender, WhatsApp-Nummer, Nachfassen und Telefon-KI pro Kunde."],
     ["Agencies manage their clients in one portal: qualifying questions, calendar, WhatsApp number, follow-ups and phone AI per client."]),
]


def changelog():
    for lang in ("de", "en"):
        d = lang == "de"
        items = "".join(
            f'<section><h2><span class="kicker">{date}</span><br>{tde if d else ten}</h2>{ul(lde if d else len_)}</section>'
            for date, tde, ten, lde, len_ in LOG)
        body = (f'<p class="kicker">Changelog</p><h1>{"Was neu ist." if d else "What is new."}</h1>'
                f'<p class="lead">{"Neue Funktionen und Verbesserungen an Auftragspilot, die neuesten oben." if d else "New features and improvements to Auftragspilot, newest first."}</p>'
                + items + cta(lang))
        page(lang, "changelog/" if d else "en/changelog/", "en/changelog/" if d else "changelog/", "Changelog",
             "Neue Funktionen und Verbesserungen an Auftragspilot." if d else "New features and improvements to Auftragspilot.", body)


# ------------------------------------------------------------------ use cases
CASES = [
    ("Leads aus Meta-Anzeigen sofort beantworten", "Answer Meta ad leads instantly",
     "Ein Interessent füllt dein Formular auf Facebook oder Instagram aus. Sekunden später hat er eine WhatsApp mit seinem Namen und der ersten Frage, auch nachts und am Wochenende. Möglich, weil wir über die offizielle WhatsApp Business Platform freigegebene Vorlagen schicken dürfen.",
     "Someone fills in your Facebook or Instagram form. Seconds later they have a WhatsApp with their name and the first question, even at night and on weekends. Possible because we send approved templates over the official WhatsApp Business Platform."),
    ("Termine direkt im Kalender buchen", "Book appointments straight into the calendar",
     "Die KI bietet nur echte freie Zeiten aus deinem Google- oder Outlook-Kalender an und trägt den Termin selbst ein. Erinnerungen vor dem Termin gehen per WhatsApp raus.",
     "The AI only offers genuinely free times from your Google or Outlook calendar and books the appointment itself. Reminders before the appointment go out on WhatsApp."),
    ("Interessenten vorqualifizieren", "Qualify leads",
     "Zwei bis drei Fragen mit Antwort-Buttons klären Bedarf, Zeitpunkt, Budget oder Ort. Wer nicht passt, bekommt eine freundliche Absage statt eines leeren Termins.",
     "Two or three questions with answer buttons clarify need, timing, budget or location. People who don't fit get a friendly decline instead of an empty appointment."),
    ("Alte Leads reaktivieren", "Reactivate old leads",
     "Kontakte, die vor Monaten angefragt haben, bekommen eine passende Vorlage. Wer antwortet, wird wie ein neuer Lead qualifiziert und bucht direkt.",
     "Contacts who enquired months ago get a fitting template. Whoever replies is qualified like a new lead and books right away."),
    ("Nachkauf-Erinnerung für Online-Shops", "Reorder reminders for online shops",
     "Wenn ein Produkt bald aufgebraucht ist, erinnert der Agent per WhatsApp und schickt den Link zum Nachkaufen.",
     "When a product is about to run out, the agent reminds the customer on WhatsApp and sends the link to reorder."),
    ("Google-Bewertungen anfragen", "Ask for Google reviews",
     "Nach dem Auftrag fragt der Agent freundlich nach einer Bewertung und schickt den direkten Link.",
     "After the job the agent kindly asks for a review and sends the direct link."),
    ("Bewerber schneller erreichen", "Reach applicants faster",
     "Bewerber aus Anzeigen bekommen sofort eine Nachricht, beantworten die wichtigsten Fragen im Chat und bekommen einen Gesprächstermin.",
     "Applicants from ads get a message right away, answer the key questions in the chat and get an interview slot."),
    ("Hotelzimmer buchen", "Book hotel rooms",
     "Der Agent prüft die Verfügbarkeit im Buchungssystem, nennt Preise aus dem System und bucht das Zimmer mit Bestätigung.",
     "The agent checks availability in the booking system, quotes prices from the system and books the room with a confirmation."),
    ("Restaurant-Anfragen aufnehmen", "Take restaurant requests",
     "Reservierungen und Feiern werden mit Datum, Uhrzeit und Personenzahl aufgenommen, das Team bestätigt mit einem Klick.",
     "Reservations and events are taken with date, time and number of guests, the team confirms with one click."),
    ("Mit deinem eigenen KI-Agenten arbeiten", "Work with your own AI agent",
     "Du nutzt schon Claude, ChatGPT oder Muse? Dein Agent liest und beantwortet die Gespräche, verschickt Broadcasts und Serien, und Auftragspilot achtet auf die Regeln von WhatsApp.",
     "Already using Claude, ChatGPT or Muse? Your agent reads and answers the conversations, sends broadcasts and sequences, and Auftragspilot keeps to WhatsApp's rules."),
]


def use_cases():
    for lang in ("de", "en"):
        d = lang == "de"
        demo = DEMO if d else DEMO_EN
        cards = "".join(
            f'<div class="card"><h3>{tde if d else ten}</h3><p>{xde if d else xen}</p>'
            + (f'<a href="../agenten/">{"So verbindest du deinen Agenten →"}</a>' if (d and i == len(CASES) - 1) else
               f'<a href="../agents/">How to connect your agent →</a>' if i == len(CASES) - 1 else f'<a href="{demo}">{"Demo testen →" if d else "Try the demo →"}</a>')
            + "</div>" for i, (tde, ten, xde, xen) in enumerate(CASES))
        body = (f'<p class="kicker">{"Anwendungsfälle" if d else "Use cases"}</p>'
                f'<h1>{"Von der Anfrage zum Auftrag, ohne dass jemand am Handy sitzt." if d else "From enquiry to job, without anyone glued to the phone."}</h1>'
                f'<p class="lead">{"Jede Anfrage, die wartet, wird kälter. Diese Abläufe laufen heute schon bei Betrieben mit Auftragspilot. Teste jeden davon selbst auf WhatsApp." if d else "Every enquiry that waits gets colder. These flows already run for businesses using Auftragspilot. Try each one yourself on WhatsApp."}</p>'
                f'<div class="grid">{cards}</div>'
                + (f'<p class="note">Nach Branche sortiert: <a href="../branchen/">Branchen</a></p>' if d else '<p class="note">Sorted by industry: <a href="../industries/">Industries</a></p>')
                + cta(lang))
        page(lang, "anwendungsfaelle/" if d else "en/use-cases/", "en/use-cases/" if d else "anwendungsfaelle/",
             "Anwendungsfälle" if d else "Use cases",
             "Meta-Leads sofort beantworten, Termine buchen, qualifizieren, alte Leads reaktivieren und mehr." if d else
             "Answer Meta leads instantly, book appointments, qualify, reactivate old leads and more.", body, wide=True,
             current="anwendungsfaelle/" if d else "en/use-cases/")


# ------------------------------------------------------------------ industries
IND = [
    ("Wärmepumpe und Heizung", "Heat pumps and heating", "Objektdaten und Heizsystem klären, Vor-Ort-Termin buchen.", "Clarify the property and heating system, book an on-site visit.", True),
    ("Photovoltaik und Speicher", "Solar and storage", "Dachfläche, Eigentum und Zeitpunkt abfragen, Beratung buchen.", "Ask about roof, ownership and timing, book a consultation.", True),
    ("Treppenlift und Barrierefreiheit", "Stair lifts and accessibility", "Treppenform, Pflegegrad und Budget klären, kostenloses Aufmaß buchen.", "Clarify staircase type, care level and budget, book a free measurement.", True),
    ("Badsanierung", "Bathroom renovation", "Umfang und Zeitpunkt klären, Badplanung vor Ort buchen.", "Clarify scope and timing, book an on-site bathroom planning.", False),
    ("Fenster und Türen", "Windows and doors", "Anzahl, Art und Zeitpunkt klären, Aufmaß buchen.", "Clarify number, type and timing, book a measurement.", False),
    ("Immobilienmakler", "Real estate agents", "Erst kaufen oder verkaufen klären, dann Wertermittlung oder Suchprofil-Gespräch buchen.", "First clarify buying or selling, then book a valuation or search profile call.", True),
    ("Versicherungsmakler", "Insurance brokers", "Beruf, Situation und Bedarf klären, Beratungstermin buchen.", "Clarify job, situation and need, book a consultation.", True),
    ("Baufinanzierung", "Mortgage brokers", "Vorhaben, Eigenkapital und Zeitpunkt klären, Beratung buchen.", "Clarify project, equity and timing, book a consultation.", True),
    ("Kosmetik und Ästhetik", "Beauty and aesthetics", "Behandlung und Wunschtermin klären, Termin buchen.", "Clarify treatment and preferred time, book an appointment.", True),
    ("Coaching und Beratung", "Coaching and consulting", "Situation und Bereitschaft klären, Kennenlerngespräch buchen.", "Clarify situation and readiness, book an intro call.", True),
    ("Hotels und Ferienwohnungen", "Hotels and holiday rentals", "Verfügbarkeit prüfen, Preis nennen, Zimmer direkt buchen.", "Check availability, quote the price, book the room directly.", True),
    ("Wellness und Spa", "Wellness and spa", "Behandlung und Zeit klären, Termin buchen.", "Clarify treatment and time, book a slot.", True),
    ("Restaurants", "Restaurants", "Datum, Uhrzeit und Personenzahl aufnehmen, Team bestätigt.", "Take date, time and number of guests, the team confirms.", True),
    ("Online-Shops", "Online shops", "Bestellstatus beantworten, an Nachkauf erinnern.", "Answer order status, remind customers to reorder.", False),
    ("Pflege und Recruiting", "Care services and recruiting", "Bewerber sofort ansprechen, Fragen klären, Gespräch buchen.", "Reach applicants right away, clarify questions, book an interview.", False),
]


def industries():
    for lang in ("de", "en"):
        d = lang == "de"
        demo = DEMO if d else DEMO_EN
        cards = "".join(
            f'<div class="card">{"<span class=\"pill pill--ok\">" + ("Demo verfügbar" if d else "Demo available") + "</span>" if has else ""}'
            f'<h3>{nde if d else nen}</h3><p>{xde if d else xen}</p>'
            + (f'<a href="{demo}">{"Demo testen →" if d else "Try the demo →"}</a>' if has else "") + "</div>"
            for nde, nen, xde, xen, has in IND)
        body = (f'<p class="kicker">{"Branchen" if d else "Industries"}</p>'
                f'<h1>{"Überall, wo eine Anfrage erst beraten werden muss." if d else "Wherever an enquiry needs advice first."}</h1>'
                f'<p class="lead">{"Für jede dieser Branchen gibt es fertige Vorlagen mit passenden Fragen, Texten und Nachfassen. Die meisten kannst du sofort als Demo auf WhatsApp testen." if d else "Every one of these industries has ready templates with fitting questions, texts and follow-ups. Most of them you can test right away as a demo on WhatsApp."}</p>'
                f'<div class="grid">{cards}</div>' + cta(lang))
        page(lang, "branchen/" if d else "en/industries/", "en/industries/" if d else "branchen/", "Branchen" if d else "Industries",
             "Fertige Vorlagen für Handwerk, Makler, Finanzierung, Kosmetik, Coaching, Hotels, Restaurants und mehr." if d else
             "Ready templates for trades, brokers, mortgages, beauty, coaching, hotels, restaurants and more.", body, wide=True)


# ------------------------------------------------------------------ compare
def compare():
    for lang in ("de", "en"):
        d = lang == "de"
        if d:
            rows = [("WhatsApp-Anbindung", "Offizielle WhatsApp Business Platform von Meta", "Verknüpfung per QR-Code wie am Computer, nicht die offizielle WhatsApp Business API"),
                    ("Vorlagen (Templates)", "Ja, Leads aus Anzeigen und Formularen sofort anschreiben", "Nein"),
                    ("Neue WhatsApp-Chats", "Mit Einwilligung, 60 pro Stunde pro Konto, dazu das Tageslimit von Meta", "Nur mit Leuten, die zuerst geschrieben oder zugestimmt haben, 10 pro Tag"),
                    ("Nachrichten pro Tag (WhatsApp)", "Tageslimit von Meta pro Nummer", "400"),
                    ("Eingebaute KI", "Ja, qualifiziert und bucht Termine in deinen Kalender", "Nein, du bringst deinen eigenen KI-Agenten mit"),
                    ("Eigener KI-Agent", "Ja, per MCP mit Browser-Anmeldung", "Ja, per MCP und REST"),
                    ("CRM und Kalenderbuchung", "Ja", "Nein"),
                    ("Telefon-KI", "Ja (Deutsch)", "Nein"),
                    ("Lead-Eingang aus Meta-Formularen und Website", "Ja", "Nein"),
                    ("Einrichtung durch uns", "Ja", "Nein"),
                    ("Kanäle", "WhatsApp und Instagram", "Instagram, WhatsApp, LinkedIn, Messenger, TikTok (nur Beiträge)"),
                    ("Sprachen der Website", "Deutsch und Englisch", "Viele Sprachen"),
                    ("Preis", "Folgt in Kürze", "Kostenlos zum Start, dann 19 US-Dollar pro verbundenem Konto im Monat plus Nutzung")]
            body = ('<p class="kicker">Vergleich</p><h1>Auftragspilot oder Spaces?</h1>'
                    '<p class="lead">Beide verbinden deinen KI-Agenten mit deinen Kundengesprächen. Der Unterschied liegt darin, wie WhatsApp angebunden ist und was schon eingebaut ist.</p>'
                    '<p class="meta">Stand: 24.11.2026. Angaben zu Spaces laut spacesos.com.</p>'
                    + table(["", "Auftragspilot", "Spaces"], rows)
                    + '<h2>Wann Spaces besser passt</h2><p>Wenn du vor allem LinkedIn, Messenger oder TikTok brauchst, deckt Spaces heute mehr Kanäle ab als wir. Auch wer nur auf eingehende Nachrichten antworten will und schon einen eigenen Agenten hat, kommt mit Spaces gut zurecht.</p>'
                    '<h2>Wann Auftragspilot besser passt</h2><p>Wenn deine Leads aus Anzeigen und Formularen kommen und sofort eine WhatsApp bekommen sollen. Das geht nur mit Vorlagen über die offizielle WhatsApp Business Platform. Dazu kommen die eingebaute KI, die Termine bucht, und die Option, dass wir alles für dich einrichten.</p>'
                    '<h2>Offizielle API oder WhatsApp-Web-Automatisierung?</h2>'
                    '<p>Viele Werkzeuge verbinden WhatsApp per QR-Code, so wie WhatsApp Web am Computer. Das geht schnell und ohne Freigabe durch Meta, ist aber nicht die offizielle Schnittstelle. Folgen: keine Vorlagen, niedrige Limits für neue Chats und ein Risiko, dass die Nummer bei automatisiertem Versand eingeschränkt wird.</p>'
                    '<p>Die offizielle WhatsApp Business Platform braucht eine einmalige Einrichtung über Facebook. Danach darfst du freigegebene Vorlagen an Kontakte mit Einwilligung schicken, auch wenn sie noch nie geschrieben haben, mit Limits, die mit guter Qualität wachsen.</p>'
                    + table(["", "Offizielle Platform", "QR-Code / WhatsApp Web"],
                            [("Freigabe durch Meta", "Ja, einmalig", "Nein"), ("Vorlagen an neue Kontakte", "Ja", "Nein"),
                             ("Sperr-Risiko durch Automatisierung", "Gering, solange die Regeln eingehalten werden", "Vorhanden"),
                             ("Kosten von Meta pro Vorlage", "Ja, je nach Land und Kategorie", "Nein")])
                    + '<p class="note">Spaces ist eine Marke ihres jeweiligen Inhabers. Wir sind nicht mit Spaces verbunden. Fehler gefunden? Schreib uns an lt@larsomatic.org.</p>'
                    + cta(lang))
            page("de", "vergleich/", "en/compare/", "Auftragspilot vs. Spaces", "Offizielle WhatsApp Business Platform mit Vorlagen und eingebauter KI oder WhatsApp per QR-Code: der Vergleich.", body, current="vergleich/")
        else:
            rows = [("WhatsApp connection", "Meta's official WhatsApp Business Platform", "Linked by QR code like on a computer, not the official WhatsApp Business API"),
                    ("Templates", "Yes, message leads from ads and forms instantly", "No"),
                    ("New WhatsApp chats", "With consent, 60 per hour per account, plus Meta's daily limit", "Only with people who wrote first or opted in, 10 per day"),
                    ("Messages per day (WhatsApp)", "Meta's daily limit per number", "400"),
                    ("Built-in AI", "Yes, qualifies and books appointments into your calendar", "No, you bring your own AI agent"),
                    ("Own AI agent", "Yes, via MCP with browser sign-in", "Yes, via MCP and REST"),
                    ("CRM and calendar booking", "Yes", "No"),
                    ("Phone AI", "Yes (German)", "No"),
                    ("Lead intake from Meta forms and website", "Yes", "No"),
                    ("Done-for-you setup", "Yes", "No"),
                    ("Channels", "WhatsApp and Instagram", "Instagram, WhatsApp, LinkedIn, Messenger, TikTok (posts only)"),
                    ("Website languages", "German and English", "Many languages"),
                    ("Price", "Coming soon", "Free to start, then 19 US dollars per connected account per month plus usage")]
            body = ('<p class="kicker">Compare</p><h1>Auftragspilot or Spaces?</h1>'
                    '<p class="lead">Both connect your AI agent to your customer conversations. The difference is how WhatsApp is connected and what is already built in.</p>'
                    '<p class="meta">As of 24 Nov 2026. Information on Spaces according to spacesos.com.</p>'
                    + table(["", "Auftragspilot", "Spaces"], rows)
                    + "<h2>When Spaces fits better</h2><p>If you mainly need LinkedIn, Messenger or TikTok, Spaces covers more channels than we do today. If you only want to answer incoming messages and already have your own agent, Spaces works well too.</p>"
                    "<h2>When Auftragspilot fits better</h2><p>If your leads come from ads and forms and should get a WhatsApp right away. That only works with templates over the official WhatsApp Business Platform. Add the built-in AI that books appointments, and the option that we set everything up for you.</p>"
                    "<h2>Official API or WhatsApp Web automation?</h2>"
                    "<p>Many tools link WhatsApp by QR code, like WhatsApp Web on a computer. It's quick and needs no approval from Meta, but it is not the official interface. The result: no templates, low limits for new chats and a risk that the number gets restricted when messages are sent automatically.</p>"
                    "<p>The official WhatsApp Business Platform needs a one-time setup via Facebook. After that you may send approved templates to contacts with consent, even if they have never written, with limits that grow with good quality.</p>"
                    + table(["", "Official platform", "QR code / WhatsApp Web"],
                            [("Approval by Meta", "Yes, once", "No"), ("Templates to new contacts", "Yes", "No"),
                             ("Ban risk from automation", "Low as long as the rules are followed", "Present"),
                             ("Meta fees per template", "Yes, depending on country and category", "No")])
                    + '<p class="note">Spaces is a trademark of its respective owner. We are not affiliated with Spaces. Found a mistake? Write to lt@larsomatic.org.</p>'
                    + cta(lang))
            page("en", "en/compare/", "vergleich/", "Auftragspilot vs. Spaces", "Official WhatsApp Business Platform with templates and built-in AI, or WhatsApp by QR code: the comparison.", body, current="en/compare/")


def build():
    security()
    limits()
    privacy_en()
    changelog()
    use_cases()
    industries()
    compare()
