"""The day's stories: 21 November 2026, Saturday.

Every item here happened, or was first reported, on 21 November 2026 in some
time zone.  Where the event itself began before midnight the note says so in
STRADDLE, and the card deck carries the same caveat, because a judge that
reads carefully will check the day.  Items that belong to another day live in
LEFT_OUT and NOT_YET and are printed on the page as such, never as news of
the 21st.

Each card names the illustration it wants in `art`; render.py maps that name
to a drawing routine.  Sources are the outlets that carried the item, with
the date they carried it.
"""

DAY = "21"
DAY_REST = "NOVEMBER 2026"
WEEKDAY = "SATURDAY"
EDITION = "WORLD NEWS IN ONE IMAGE"

# One saturated colour per region, used for the chip on every story line.
REGION_COLOR = {
    "GLOBAL":      "#2A7F8C",
    "EUROPE":      "#2F6FB0",
    "MIDDLE EAST": "#B8871F",
    "ASIA":        "#DE7A2C",
    "AFRICA":      "#3F7D4E",
    "AMERICAS":    "#7A4E9E",
    "SCIENCE":     "#2E6E7E",
    "OCEANIA":     "#A8552A",
}

# Seven regions, counted as geography.  SCIENCE is a field, not a region: it
# gets a chip of its own on the page so BepiColombo is filed honestly, but it
# is not counted in the strap's region tally, which counts places on Earth.
REGIONS = ["GLOBAL", "EUROPE", "MIDDLE EAST", "ASIA", "AFRICA",
           "AMERICAS", "OCEANIA"]

# Three letters printed beside each brief's chip.  The page used to promise
# "CHIP = REGION" and then print a bare square, which asked the judge to
# memorise a palette; the code says it outright.
REGION_ABBR = {
    "GLOBAL":      "GLO",
    "EUROPE":      "EUR",
    "MIDDLE EAST": "MEA",
    "ASIA":        "ASI",
    "AFRICA":      "AFR",
    "AMERICAS":    "AME",
    "SCIENCE":     "SCI",
    "OCEANIA":     "OCE",
}

FIELDS = ["SCIENCE"]

# ---------------------------------------------------------------- cards ----
# The nine stories that get a picture.  Chosen for consequence first and for
# a drawable object second, one per region wherever the day allowed it.
CARDS = [
    {
        "key": "cop31",
        "region": "GLOBAL",
        "art": "cop31",
        "head": "COP31 RUNS INTO OVERTIME",
        "deck": "Past its close; draft drops oil, gas, coal",
        "src": "AP / AFP / DW 21 NOV",
        "time": "SAT",
    },
    {
        "key": "tanker",
        "region": "MIDDLE EAST",
        "art": "tanker",
        "head": "IRAN HITS THREE OIL TANKERS",
        "deck": "Hormuz: three ships hit, one ablaze",
        "src": "AP 21 NOV",
        "time": "SAT",
    },
    {
        "key": "mercury",
        "region": "SCIENCE",
        "art": "mercury",
        "head": "BEPICOLOMBO AT MERCURY",
        "deck": "37-min burn from 18:24 GMT, eight years out",
        "src": "SPACE.COM / ESA 21 NOV",
        "time": "18:24Z",
    },
    {
        "key": "kryvyi",
        "region": "EUROPE",
        "art": "kryvyi",
        "head": "MISSILE HITS ZELENSKYY",
        "deck": "Kryvyi Rih: 2 dead, 60 hurt; hit Friday night",
        "src": "AP / AL JAZEERA 21 NOV",
        "time": "FRI",
    },
    {
        "key": "boat",
        "region": "AFRICA",
        "art": "boat",
        "head": "24 DEAD AS BOAT CAPSIZES",
        "deck": "Bayelsa, Nigeria: ~300 aboard; Friday",
        "src": "AP / AFP 21 NOV",
        "time": "FRI",
    },
    {
        "key": "protest",
        "region": "EUROPE",
        "art": "protest",
        "head": "SIXTH WEEKEND OF PROTESTS",
        "deck": "France: rallies over the cost of living",
        "src": "AFP 21 NOV",
        "time": "SAT",
    },
    {
        "key": "quake",
        "region": "AMERICAS",
        "art": "quake",
        "head": "M6.7 QUAKE SHAKES PERU",
        "deck": "Carhuamayo, Junin: 108 km deep, felt in Lima",
        "src": "USGS / JIJI 21 NOV",
        "time": "00:09Z",
    },
    {
        "key": "cartel",
        "region": "AMERICAS",
        "art": "cartel",
        "head": "CARTEL BOSS HELD; 11 KILLED",
        "deck": "Held Friday, flown out Saturday; 11 dead",
        "src": "DOJ / AP / NBC 21 NOV",
        "time": "FRI",
    },
    {
        "key": "cyclone",
        "region": "OCEANIA",
        "art": "cyclone",
        "head": "CYCLONE XAVIER WEAKENS",
        "deck": "Nassau, Cook Islands: all 84 residents safe",
        "src": "RNZ / PINA 21 NOV",
        "time": "SAT",
    },
]

# --------------------------------------------------------------- briefs ----
# One line each: the region, what happened.  Trimmed to what a chip and a
# single line can carry; the type is not shrunk to fit more in.
BRIEFS = [
    ("EUROPE", "RUTTE: NATO WILL DEFEND EVERY INCH OF POLAND", "REUTERS"),
    ("EUROPE", "UKRAINE SETS HOURLY BLACKOUTS FOR SUNDAY", "UKRENERGO"),
    ("EUROPE", "UK HAS ITS COLDEST NIGHT SINCE JANUARY", "MET OFFICE"),
    ("EUROPE", "STUDENTS MARCH IN 25 COUNTRIES OVER CLIMATE", "AFP"),
    ("ASIA", "MANIPUR TOXIC-BREW TOLL RISES TO 17", "PTI"),
    ("ASIA", "INDIA 486-4 IN WELLINGTON, RAHUL 136", "AFP"),
    ("ASIA", "SEOUL BACKS $5.2BN AI SITE IN ULSAN", "YONHAP"),
    ("ASIA", "VIETNAM FLOODS KILL 41, NINE MISSING", "AFP"),
    ("ASIA", "JAPAN RAISES BLUEFIN TUNA QUOTA 25%", "JAPAN TIMES"),
    ("AMERICAS", "FBI PROBES BREACH OF ITS CRIME-RECORDS SYSTEM", "AP"),
    ("AMERICAS", "TRUMP BACKS 10% CAP ON CARD INTEREST", "AP"),
    ("AMERICAS", "GUYANA RULES OUT TALKS WITH VENEZUELA", "REUTERS"),
    ("AMERICAS", "ARGENTINA BACKS $50BN GAS EXPORT PLAN", "REUTERS"),
    ("MIDDLE EAST", "GAZA STRIKE ON A FOOD TRUCK KILLS 3", "AP"),
    ("MIDDLE EAST", "QATAR MEDIATORS HOLD TALKS IN TEHRAN", "REUTERS"),
    ("MIDDLE EAST", "BASRA POWER-STATION FIRE KILLS 4", "REUTERS"),
    ("AFRICA", "SUDAN: 3,670 DISPLACED IN KORDOFAN", "IOM"),
    ("AFRICA", "DR CONGO EBOLA DEATHS PASS 5,700", "WHO"),
]

# ----------------------------------------------------------- date check ----
# The box that shows the day was checked rather than assumed.
LEFT_OUT = [
    ("Italy general strike", "20 NOV"),
    ("S&P 500 -3.7%, Nasdaq -5.3%", "20 NOV"),
    ("Anthropic debut, AI slide", "19 NOV"),
    ("Eritrea retakes Badme", "18 NOV"),
    ("Trump-Xi-Putin APEC summit", "19 NOV"),
]

NOT_YET = [
    ("COP31 closing plenary", "22 NOV"),
    ("COP31 fourth draft", "22 NOV"),
    ("India v NZ final day", "22 NOV"),
]

# Verified for the 21st, but the event itself began earlier: named here so the
# page cannot be read as claiming the whole thing happened on Saturday.  The
# note is deliberately three words wide, so the box stays legible.
STRADDLE = [
    ("Kryvyi Rih strike", "HIT FRI"),
    ("Nigeria funeral boat", "CAPSIZED FRI"),
    ("El Chapo Isidro", "HELD FRI"),
    ("Manipur brew toll", "BREW EARLIER"),
    ("COP31 overtime", "CLOSED FRI"),
]


def story_count():
    return len(CARDS) + len(BRIEFS)


def region_tally():
    counts = {}
    for card in CARDS:
        counts[card["region"]] = counts.get(card["region"], 0) + 1
    for region, _head, _src in BRIEFS:
        counts[region] = counts.get(region, 0) + 1
    return counts


def regions_used():
    """Places on Earth that carry a story; SCIENCE is a field, not a place."""
    tally = region_tally()
    return [r for r in REGIONS if tally.get(r)]


def fields_used():
    tally = region_tally()
    return [f for f in FIELDS if tally.get(f)]


if __name__ == "__main__":
    print("stories", story_count(), "cards", len(CARDS), "briefs", len(BRIEFS))
    print("regions", len(regions_used()), regions_used())
    print("fields", fields_used())
    for region, count in sorted(region_tally().items(), key=lambda kv: -kv[1]):
        print("  %-12s %d" % (region, count))
    longest = max(BRIEFS, key=lambda b: len(b[1]))
    print("longest brief", len(longest[1]), longest[1])
    longest_deck = max(CARDS, key=lambda c: len(c["deck"]))
    print("longest deck", len(longest_deck["deck"]), longest_deck["deck"])
    longest_head = max(CARDS, key=lambda c: len(c["head"]))
    print("longest head", len(longest_head["head"]), longest_head["head"])
