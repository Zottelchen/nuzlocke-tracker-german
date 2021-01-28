from pprint import pprint

import pokebase as pb

pkmnData = [
    {
        "name": 'Bulbasaur',
        "value": "bulbasaur",
        "image": "img/bulbasaur.png"
    },
    {
        "name": 'Ivysaur',
        "value": "ivysaur",
        "image": "img/ivysaur.png"
    },
    {
        "name": 'Venusaur',
        "value": "venusaur",
        "image": "img/venusaur.png"
    },
    {
        "name": 'Charmander',
        "value": "charmander",
        "image": "img/charmander.png"
    },
    {
        "name": 'Charmeleon',
        "value": "charmeleon",
        "image": "img/charmeleon.png"
    },
    {
        "name": 'Charizard',
        "value": "charizard",
        "image": "img/charizard.png"
    },
    {
        "name": 'Squirtle',
        "value": "squirtle",
        "image": "img/squirtle.png"
    },
    {
        "name": 'Wartortle',
        "value": "wartortle",
        "image": "img/wartortle.png"
    },
    {
        "name": 'Blastoise',
        "value": "blastoise",
        "image": "img/blastoise.png"
    },
    {
        "name": 'Caterpie',
        "value": "caterpie",
        "image": "img/caterpie.png"
    },
    {
        "name": 'Metapod',
        "value": "metapod",
        "image": "img/metapod.png"
    },
    {
        "name": 'Butterfree',
        "value": "butterfree",
        "image": "img/butterfree.png"
    },
    {
        "name": 'Weedle',
        "value": "weedle",
        "image": "img/weedle.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Kakuna',
        "value": "kakuna",
        "image": "img/kakuna.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Beedrill',
        "value": "beedrill",
        "image": "img/beedrill.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Pidgey',
        "value": "pidgey",
        "image": "img/pidgey.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Pidgeotto',
        "value": "pidgeotto",
        "image": "img/pidgeotto.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Pidgeot',
        "value": "pidgeot",
        "image": "img/pidgeot.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Rattata',
        "value": "rattata",
        "image": "img/rattata.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Raticate',
        "value": "raticate",
        "image": "img/raticate.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Spearow',
        "value": "spearow",
        "image": "img/spearow.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Fearow',
        "value": "fearow",
        "image": "img/fearow.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Ekans',
        "value": "ekans",
        "image": "img/ekans.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Arbok',
        "value": "arbok",
        "image": "img/arbok.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Pikachu',
        "value": "pikachu",
        "image": "img/pikachu.png"
    },
    {
        "name": 'Raichu',
        "value": "raichu",
        "image": "img/raichu.png"
    },
    {
        "name": 'Sandshrew',
        "value": "sandshrew",
        "image": "img/sandshrew.png"
    },
    {
        "name": 'Sandslash',
        "value": "sandslash",
        "image": "img/sandslash.png"
    },
    {
        "name": 'Nidoran♀',
        "value": "nidoran-female",
        "image": "img/nidoran-female.png"
    },
    {
        "name": 'Nidorina',
        "value": "nidorina",
        "image": "img/nidorina.png"
    },
    {
        "name": 'Nidoqueen',
        "value": "nidoqueen",
        "image": "img/nidoqueen.png"
    },
    {
        "name": 'Nidoran♂',
        "value": "nidoran-male",
        "image": "img/nidoran-male.png"
    },
    {
        "name": 'Nidorino',
        "value": "nidorino",
        "image": "img/nidorino.png"
    },
    {
        "name": 'Nidoking',
        "value": "nidoking",
        "image": "img/nidoking.png"
    },
    {
        "name": 'Clefairy',
        "value": "clefairy",
        "image": "img/clefairy.png"
    },
    {
        "name": 'Clefable',
        "value": "clefable",
        "image": "img/clefable.png"
    },
    {
        "name": 'Vulpix',
        "value": "vulpix",
        "image": "img/vulpix.png"
    },
    {
        "name": 'Ninetales',
        "value": "ninetales",
        "image": "img/ninetales.png"
    },
    {
        "name": 'Jigglypuff',
        "value": "jigglypuff",
        "image": "img/jigglypuff.png"
    },
    {
        "name": 'Wigglytuff',
        "value": "wigglytuff",
        "image": "img/wigglytuff.png"
    },
    {
        "name": 'Zubat',
        "value": "zubat",
        "image": "img/zubat.png"
    },
    {
        "name": 'Golbat',
        "value": "golbat",
        "image": "img/golbat.png"
    },
    {
        "name": 'Oddish',
        "value": "oddish",
        "image": "img/oddish.png"
    },
    {
        "name": 'Gloom',
        "value": "gloom",
        "image": "img/gloom.png"
    },
    {
        "name": 'Vileplume',
        "value": "vileplume",
        "image": "img/vileplume.png"
    },
    {
        "name": 'Paras',
        "value": "paras",
        "image": "img/paras.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Parasect',
        "value": "parasect",
        "image": "img/parasect.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Venonat',
        "value": "venonat",
        "image": "img/venonat.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Venomoth',
        "value": "venomoth",
        "image": "img/venomoth.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Diglett',
        "value": "diglett",
        "image": "img/diglett.png"
    },
    {
        "name": 'Dugtrio',
        "value": "dugtrio",
        "image": "img/dugtrio.png"
    },
    {
        "name": 'Meowth',
        "value": "meowth",
        "image": "img/meowth.png"
    },
    {
        "name": 'Persian',
        "value": "persian",
        "image": "img/persian.png"
    },
    {
        "name": 'Psyduck',
        "value": "psyduck",
        "image": "img/psyduck.png"
    },
    {
        "name": 'Golduck',
        "value": "golduck",
        "image": "img/golduck.png"
    },
    {
        "name": 'Mankey',
        "value": "mankey",
        "image": "img/mankey.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Primeape',
        "value": "primeape",
        "image": "img/primeape.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Growlithe',
        "value": "growlithe",
        "image": "img/growlithe.png"
    },
    {
        "name": 'Arcanine',
        "value": "arcanine",
        "image": "img/arcanine.png"
    },
    {
        "name": 'Poliwag',
        "value": "poliwag",
        "image": "img/poliwag.png"
    },
    {
        "name": 'Poliwhirl',
        "value": "poliwhirl",
        "image": "img/poliwhirl.png"
    },
    {
        "name": 'Poliwrath',
        "value": "poliwrath",
        "image": "img/poliwrath.png"
    },
    {
        "name": 'Abra',
        "value": "abra",
        "image": "img/abra.png"
    },
    {
        "name": 'Kadabra',
        "value": "kadabra",
        "image": "img/kadabra.png"
    },
    {
        "name": 'Alakazam',
        "value": "alakazam",
        "image": "img/alakazam.png"
    },
    {
        "name": 'Machop',
        "value": "machop",
        "image": "img/machop.png"
    },
    {
        "name": 'Machoke',
        "value": "machoke",
        "image": "img/machoke.png"
    },
    {
        "name": 'Machamp',
        "value": "machamp",
        "image": "img/machamp.png"
    },
    {
        "name": 'Bellsprout',
        "value": "bellsprout",
        "image": "img/bellsprout.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Weepinbell',
        "value": "weepinbell",
        "image": "img/weepinbell.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Victreebel',
        "value": "victreebel",
        "image": "img/victreebel.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Tentacool',
        "value": "tentacool",
        "image": "img/tentacool.png"
    },
    {
        "name": 'Tentacruel',
        "value": "tentacruel",
        "image": "img/tentacruel.png"
    },
    {
        "name": 'Geodude',
        "value": "geodude",
        "image": "img/geodude.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Graveler',
        "value": "graveler",
        "image": "img/graveler.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Golem',
        "value": "golem",
        "image": "img/golem.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Ponyta',
        "value": "ponyta",
        "image": "img/ponyta.png"
    },
    {
        "name": 'Rapidash',
        "value": "rapidash",
        "image": "img/rapidash.png"
    },
    {
        "name": 'Slowpoke',
        "value": "slowpoke",
        "image": "img/slowpoke.png"
    },
    {
        "name": 'Slowbro',
        "value": "slowbro",
        "image": "img/slowbro.png"
    },
    {
        "name": 'Magnemite',
        "value": "magnemite",
        "image": "img/magnemite.png"
    },
    {
        "name": 'Magneton',
        "value": "magneton",
        "image": "img/magneton.png"
    },
    {
        "name": 'Farfetch\'d',
        "value": "farfetchd",
        "image": "img/farfetchd.png"
    },
    {
        "name": 'Doduo',
        "value": "doduo",
        "image": "img/doduo.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Dodrio',
        "value": "dodrio",
        "image": "img/dodrio.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Seel',
        "value": "seel",
        "image": "img/seel.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Dewgong',
        "value": "dewgong",
        "image": "img/dewgong.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Grimer',
        "value": "grimer",
        "image": "img/grimer.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Muk',
        "value": "muk",
        "image": "img/muk.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Shellder',
        "value": "shellder",
        "image": "img/shellder.png"
    },
    {
        "name": 'Cloyster',
        "value": "cloyster",
        "image": "img/cloyster.png"
    },
    {
        "name": 'Gastly',
        "value": "gastly",
        "image": "img/gastly.png"
    },
    {
        "name": 'Haunter',
        "value": "haunter",
        "image": "img/haunter.png"
    },
    {
        "name": 'Gengar',
        "value": "gengar",
        "image": "img/gengar.png"
    },
    {
        "name": 'Onix',
        "value": "onix",
        "image": "img/onix.png"
    },
    {
        "name": 'Drowzee',
        "value": "drowzee",
        "image": "img/drowzee.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Hypno',
        "value": "hypno",
        "image": "img/hypno.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Krabby',
        "value": "krabby",
        "image": "img/krabby.png"
    },
    {
        "name": 'Kingler',
        "value": "kingler",
        "image": "img/kingler.png"
    },
    {
        "name": 'Voltorb',
        "value": "voltorb",
        "image": "img/voltorb.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Electrode',
        "value": "electrode",
        "image": "img/electrode.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Exeggcute',
        "value": "exeggcute",
        "image": "img/exeggcute.png"
    },
    {
        "name": 'Exeggutor',
        "value": "exeggutor",
        "image": "img/exeggutor.png"
    },
    {
        "name": 'Cubone',
        "value": "cubone",
        "image": "img/cubone.png"
    },
    {
        "name": 'Marowak',
        "value": "marowak",
        "image": "img/marowak.png"
    },
    {
        "name": 'Hitmonlee',
        "value": "hitmonlee",
        "image": "img/hitmonlee.png"
    },
    {
        "name": 'Hitmonchan',
        "value": "hitmonchan",
        "image": "img/hitmonchan.png"
    },
    {
        "name": 'Lickitung',
        "value": "lickitung",
        "image": "img/lickitung.png"
    },
    {
        "name": 'Koffing',
        "value": "koffing",
        "image": "img/koffing.png"
    },
    {
        "name": 'Weezing',
        "value": "weezing",
        "image": "img/weezing.png"
    },
    {
        "name": 'Rhyhorn',
        "value": "rhyhorn",
        "image": "img/rhyhorn.png"
    },
    {
        "name": 'Rhydon',
        "value": "rhydon",
        "image": "img/rhydon.png"
    },
    {
        "name": 'Chansey',
        "value": "chansey",
        "image": "img/chansey.png"
    },
    {
        "name": 'Tangela',
        "value": "tangela",
        "image": "img/tangela.png"
    },
    {
        "name": 'Kangaskhan',
        "value": "kangaskhan",
        "image": "img/kangaskhan.png"
    },
    {
        "name": 'Horsea',
        "value": "horsea",
        "image": "img/horsea.png"
    },
    {
        "name": 'Seadra',
        "value": "seadra",
        "image": "img/seadra.png"
    },
    {
        "name": 'Goldeen',
        "value": "goldeen",
        "image": "img/goldeen.png"
    },
    {
        "name": 'Seaking',
        "value": "seaking",
        "image": "img/seaking.png"
    },
    {
        "name": 'Staryu',
        "value": "staryu",
        "image": "img/staryu.png"
    },
    {
        "name": 'Starmie',
        "value": "starmie",
        "image": "img/starmie.png"
    },
    {
        "name": 'Mr. Mime',
        "value": "mr-mime",
        "image": "img/mr-mime.png"
    },
    {
        "name": 'Scyther',
        "value": "scyther",
        "image": "img/scyther.png"
    },
    {
        "name": 'Jynx',
        "value": "jynx",
        "image": "img/jynx.png"
    },
    {
        "name": 'Electabuzz',
        "value": "electabuzz",
        "image": "img/electabuzz.png"
    },
    {
        "name": 'Magmar',
        "value": "magmar",
        "image": "img/magmar.png"
    },
    {
        "name": 'Pinsir',
        "value": "pinsir",
        "image": "img/pinsir.png"
    },
    {
        "name": 'Tauros',
        "value": "tauros",
        "image": "img/tauros.png"
    },
    {
        "name": 'Magikarp',
        "value": "magikarp",
        "image": "img/magikarp.png"
    },
    {
        "name": 'Gyarados',
        "value": "gyarados",
        "image": "img/gyarados.png"
    },
    {
        "name": 'Lapras',
        "value": "lapras",
        "image": "img/lapras.png"
    },
    {
        "name": 'Ditto',
        "value": "ditto",
        "image": "img/ditto.png"
    },
    {
        "name": 'Eevee',
        "value": "eevee",
        "image": "img/eevee.png"
    },
    {
        "name": 'Vaporeon',
        "value": "vaporeon",
        "image": "img/vaporeon.png"
    },
    {
        "name": 'Jolteon',
        "value": "jolteon",
        "image": "img/jolteon.png"
    },
    {
        "name": 'Flareon',
        "value": "flareon",
        "image": "img/flareon.png"
    },
    {
        "name": 'Porygon',
        "value": "porygon",
        "image": "img/porygon.png"
    },
    {
        "name": 'Omanyte',
        "value": "omanyte",
        "image": "img/omanyte.png"
    },
    {
        "name": 'Omastar',
        "value": "omastar",
        "image": "img/omastar.png"
    },
    {
        "name": 'Kabuto',
        "value": "kabuto",
        "image": "img/kabuto.png"
    },
    {
        "name": 'Kabutops',
        "value": "kabutops",
        "image": "img/kabutops.png"
    },
    {
        "name": 'Aerodactyl',
        "value": "aerodactyl",
        "image": "img/aerodactyl.png"
    },
    {
        "name": 'Snorlax',
        "value": "snorlax",
        "image": "img/snorlax.png"
    },
    {
        "name": 'Articuno',
        "value": "articuno",
        "image": "img/articuno.png"
    },
    {
        "name": 'Zapdos',
        "value": "zapdos",
        "image": "img/zapdos.png"
    },
    {
        "name": 'Moltres',
        "value": "moltres",
        "image": "img/moltres.png"
    },
    {
        "name": 'Dratini',
        "value": "dratini",
        "image": "img/dratini.png"
    },
    {
        "name": 'Dragonair',
        "value": "dragonair",
        "image": "img/dragonair.png"
    },
    {
        "name": 'Dragonite',
        "value": "dragonite",
        "image": "img/dragonite.png"
    },
    {
        "name": 'Mewtwo',
        "value": "mewtwo",
        "image": "img/mewtwo.png"
    },
    {
        "name": 'Mew',
        "value": "mew",
        "image": "img/mew.png"
    },
    {
        "name": 'Chikorita',
        "value": "chikorita",
        "image": "img/chikorita.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Bayleef',
        "value": "bayleef",
        "image": "img/bayleef.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Meganium',
        "value": "meganium",
        "image": "img/meganium.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Cyndaquil',
        "value": "cyndaquil",
        "image": "img/cyndaquil.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Quilava',
        "value": "quilava",
        "image": "img/quilava.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Typhlosion',
        "value": "typhlosion",
        "image": "img/typhlosion.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Totodile',
        "value": "totodile",
        "image": "img/totodile.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Croconaw',
        "value": "croconaw",
        "image": "img/croconaw.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Feraligatr',
        "value": "feraligatr",
        "image": "img/feraligatr.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Sentret',
        "value": "sentret",
        "image": "img/sentret.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Furret',
        "value": "furret",
        "image": "img/furret.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Hoothoot',
        "value": "hoothoot",
        "image": "img/hoothoot.png"
    },
    {
        "name": 'Noctowl',
        "value": "noctowl",
        "image": "img/noctowl.png"
    },
    {
        "name": 'Ledyba',
        "value": "ledyba",
        "image": "img/ledyba.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Ledian',
        "value": "ledian",
        "image": "img/ledian.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Spinarak',
        "value": "spinarak",
        "image": "img/spinarak.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Ariados',
        "value": "ariados",
        "image": "img/ariados.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Crobat',
        "value": "crobat",
        "image": "img/crobat.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Chinchou',
        "value": "chinchou",
        "image": "img/chinchou.png"
    },
    {
        "name": 'Lanturn',
        "value": "lanturn",
        "image": "img/lanturn.png"
    },
    {
        "name": 'Pichu',
        "value": "pichu",
        "image": "img/pichu.png"
    },
    {
        "name": 'Cleffa',
        "value": "cleffa",
        "image": "img/cleffa.png"
    },
    {
        "name": 'Igglybuff',
        "value": "igglybuff",
        "image": "img/igglybuff.png"
    },
    {
        "name": 'Togepi',
        "value": "togepi",
        "image": "img/togepi.png"
    },
    {
        "name": 'Togetic',
        "value": "togetic",
        "image": "img/togetic.png"
    },
    {
        "name": 'Natu',
        "value": "natu",
        "image": "img/natu.png"
    },
    {
        "name": 'Xatu',
        "value": "xatu",
        "image": "img/xatu.png"
    },
    {
        "name": 'Mareep',
        "value": "mareep",
        "image": "img/mareep.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Flaaffy',
        "value": "flaaffy",
        "image": "img/flaaffy.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Ampharos',
        "value": "ampharos",
        "image": "img/ampharos.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Bellossom',
        "value": "bellossom",
        "image": "img/bellossom.png"
    },
    {
        "name": 'Marill',
        "value": "marill",
        "image": "img/marill.png"
    },
    {
        "name": 'Azumarill',
        "value": "azumarill",
        "image": "img/azumarill.png"
    },
    {
        "name": 'Sudowoodo',
        "value": "sudowoodo",
        "image": "img/sudowoodo.png"
    },
    {
        "name": 'Politoed',
        "value": "politoed",
        "image": "img/politoed.png"
    },
    {
        "name": 'Hoppip',
        "value": "hoppip",
        "image": "img/hoppip.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Skiploom',
        "value": "skiploom",
        "image": "img/skiploom.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Jumpluff',
        "value": "jumpluff",
        "image": "img/jumpluff.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Aipom',
        "value": "aipom",
        "image": "img/aipom.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Sunkern',
        "value": "sunkern",
        "image": "img/sunkern.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Sunflora',
        "value": "sunflora",
        "image": "img/sunflora.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Yanma',
        "value": "yanma",
        "image": "img/yanma.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Wooper',
        "value": "wooper",
        "image": "img/wooper.png"
    },
    {
        "name": 'Quagsire',
        "value": "quagsire",
        "image": "img/quagsire.png"
    },
    {
        "name": 'Espeon',
        "value": "espeon",
        "image": "img/espeon.png"
    },
    {
        "name": 'Umbreon',
        "value": "umbreon",
        "image": "img/umbreon.png"
    },
    {
        "name": 'Murkrow',
        "value": "murkrow",
        "image": "img/murkrow.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Slowking',
        "value": "slowking",
        "image": "img/slowking.png"
    },
    {
        "name": 'Misdreavus',
        "value": "misdreavus",
        "image": "img/misdreavus.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Unown',
        "value": "unown",
        "image": "img/unown.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Wobbuffet',
        "value": "wobbuffet",
        "image": "img/wobbuffet.png"
    },
    {
        "name": 'Girafarig',
        "value": "girafarig",
        "image": "img/girafarig.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Pineco',
        "value": "pineco",
        "image": "img/pineco.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Forretress',
        "value": "forretress",
        "image": "img/forretress.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Dunsparce',
        "value": "dunsparce",
        "image": "img/dunsparce.png"
    },
    {
        "name": 'Gligar',
        "value": "gligar",
        "image": "img/gligar.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Steelix',
        "value": "steelix",
        "image": "img/steelix.png"
    },
    {
        "name": 'Snubbull',
        "value": "snubbull",
        "image": "img/snubbull.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Granbull',
        "value": "granbull",
        "image": "img/granbull.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Qwilfish',
        "value": "qwilfish",
        "image": "img/qwilfish.png"
    },
    {
        "name": 'Scizor',
        "value": "scizor",
        "image": "img/scizor.png"
    },
    {
        "name": 'Shuckle',
        "value": "shuckle",
        "image": "img/shuckle.png"
    },
    {
        "name": 'Heracross',
        "value": "heracross",
        "image": "img/heracross.png"
    },
    {
        "name": 'Sneasel',
        "value": "sneasel",
        "image": "img/sneasel.png"
    },
    {
        "name": 'Teddiursa',
        "value": "teddiursa",
        "image": "img/teddiursa.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Ursaring',
        "value": "ursaring",
        "image": "img/ursaring.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Slugma',
        "value": "slugma",
        "image": "img/slugma.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Magcargo',
        "value": "magcargo",
        "image": "img/magcargo.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Swinub',
        "value": "swinub",
        "image": "img/swinub.png"
    },
    {
        "name": 'Piloswine',
        "value": "piloswine",
        "image": "img/piloswine.png"
    },
    {
        "name": 'Corsola',
        "value": "corsola",
        "image": "img/corsola.png"
    },
    {
        "name": 'Remoraid',
        "value": "remoraid",
        "image": "img/remoraid.png"
    },
    {
        "name": 'Octillery',
        "value": "octillery",
        "image": "img/octillery.png"
    },
    {
        "name": 'Delibird',
        "value": "delibird",
        "image": "img/delibird.png"
    },
    {
        "name": 'Mantine',
        "value": "mantine",
        "image": "img/mantine.png"
    },
    {
        "name": 'Skarmory',
        "value": "skarmory",
        "image": "img/skarmory.png"
    },
    {
        "name": 'Houndour',
        "value": "houndour",
        "image": "img/houndour.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Houndoom',
        "value": "houndoom",
        "image": "img/houndoom.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Kingdra',
        "value": "kingdra",
        "image": "img/kingdra.png"
    },
    {
        "name": 'Phanpy',
        "value": "phanpy",
        "image": "img/phanpy.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Donphan',
        "value": "donphan",
        "image": "img/donphan.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Porygon2',
        "value": "porygon2",
        "image": "img/porygon2.png"
    },
    {
        "name": 'Stantler',
        "value": "stantler",
        "image": "img/stantler.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Smeargle',
        "value": "smeargle",
        "image": "img/smeargle.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Tyrogue',
        "value": "tyrogue",
        "image": "img/tyrogue.png"
    },
    {
        "name": 'Hitmontop',
        "value": "hitmontop",
        "image": "img/hitmontop.png"
    },
    {
        "name": 'Smoochum',
        "value": "smoochum",
        "image": "img/smoochum.png"
    },
    {
        "name": 'Elekid',
        "value": "elekid",
        "image": "img/elekid.png"
    },
    {
        "name": 'Magby',
        "value": "magby",
        "image": "img/magby.png"
    },
    {
        "name": 'Miltank',
        "value": "miltank",
        "image": "img/miltank.png"
    },
    {
        "name": 'Blissey',
        "value": "blissey",
        "image": "img/blissey.png"
    },
    {
        "name": 'Raikou',
        "value": "raikou",
        "image": "img/raikou.png"
    },
    {
        "name": 'Entei',
        "value": "entei",
        "image": "img/entei.png"
    },
    {
        "name": 'Suicune',
        "value": "suicune",
        "image": "img/suicune.png"
    },
    {
        "name": 'Larvitar',
        "value": "larvitar",
        "image": "img/larvitar.png"
    },
    {
        "name": 'Pupitar',
        "value": "pupitar",
        "image": "img/pupitar.png"
    },
    {
        "name": 'Tyranitar',
        "value": "tyranitar",
        "image": "img/tyranitar.png"
    },
    {
        "name": 'Lugia',
        "value": "lugia",
        "image": "img/lugia.png"
    },
    {
        "name": 'Ho-Oh',
        "value": "ho-oh",
        "image": "img/ho-oh.png"
    },
    {
        "name": 'Celebi',
        "value": "celebi",
        "image": "img/celebi.png"
    },
    {
        "name": 'Treecko',
        "value": "treecko",
        "image": "img/treecko.png"
    },
    {
        "name": 'Grovyle',
        "value": "grovyle",
        "image": "img/grovyle.png"
    },
    {
        "name": 'Sceptile',
        "value": "sceptile",
        "image": "img/sceptile.png"
    },
    {
        "name": 'Torchic',
        "value": "torchic",
        "image": "img/torchic.png"
    },
    {
        "name": 'Combusken',
        "value": "combusken",
        "image": "img/combusken.png"
    },
    {
        "name": 'Blaziken',
        "value": "blaziken",
        "image": "img/blaziken.png"
    },
    {
        "name": 'Mudkip',
        "value": "mudkip",
        "image": "img/mudkip.png"
    },
    {
        "name": 'Marshtomp',
        "value": "marshtomp",
        "image": "img/marshtomp.png"
    },
    {
        "name": 'Swampert',
        "value": "swampert",
        "image": "img/swampert.png"
    },
    {
        "name": 'Poochyena',
        "value": "poochyena",
        "image": "img/poochyena.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Mightyena',
        "value": "mightyena",
        "image": "img/mightyena.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Zigzagoon',
        "value": "zigzagoon",
        "image": "img/zigzagoon.png"
    },
    {
        "name": 'Linoone',
        "value": "linoone",
        "image": "img/linoone.png"
    },
    {
        "name": 'Wurmple',
        "value": "wurmple",
        "image": "img/wurmple.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Silcoon',
        "value": "silcoon",
        "image": "img/silcoon.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Beautifly',
        "value": "beautifly",
        "image": "img/beautifly.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Cascoon',
        "value": "cascoon",
        "image": "img/cascoon.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Dustox',
        "value": "dustox",
        "image": "img/dustox.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Lotad',
        "value": "lotad",
        "image": "img/lotad.png"
    },
    {
        "name": 'Lombre',
        "value": "lombre",
        "image": "img/lombre.png"
    },
    {
        "name": 'Ludicolo',
        "value": "ludicolo",
        "image": "img/ludicolo.png"
    },
    {
        "name": 'Seedot',
        "value": "seedot",
        "image": "img/seedot.png"
    },
    {
        "name": 'Nuzleaf',
        "value": "nuzleaf",
        "image": "img/nuzleaf.png"
    },
    {
        "name": 'Shiftry',
        "value": "shiftry",
        "image": "img/shiftry.png"
    },
    {
        "name": 'Taillow',
        "value": "taillow",
        "image": "img/taillow.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Swellow',
        "value": "swellow",
        "image": "img/swellow.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Wingull',
        "value": "wingull",
        "image": "img/wingull.png"
    },
    {
        "name": 'Pelipper',
        "value": "pelipper",
        "image": "img/pelipper.png"
    },
    {
        "name": 'Ralts',
        "value": "ralts",
        "image": "img/ralts.png"
    },
    {
        "name": 'Kirlia',
        "value": "kirlia",
        "image": "img/kirlia.png"
    },
    {
        "name": 'Gardevoir',
        "value": "gardevoir",
        "image": "img/gardevoir.png"
    },
    {
        "name": 'Surskit',
        "value": "surskit",
        "image": "img/surskit.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Masquerain',
        "value": "masquerain",
        "image": "img/masquerain.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Shroomish',
        "value": "shroomish",
        "image": "img/shroomish.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Breloom',
        "value": "breloom",
        "image": "img/breloom.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Slakoth',
        "value": "slakoth",
        "image": "img/slakoth.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Vigoroth',
        "value": "vigoroth",
        "image": "img/vigoroth.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Slaking',
        "value": "slaking",
        "image": "img/slaking.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Nincada',
        "value": "nincada",
        "image": "img/nincada.png"
    },
    {
        "name": 'Ninjask',
        "value": "ninjask",
        "image": "img/ninjask.png"
    },
    {
        "name": 'Shedinja',
        "value": "shedinja",
        "image": "img/shedinja.png"
    },
    {
        "name": 'Whismur',
        "value": "whismur",
        "image": "img/whismur.png"
    },
    {
        "name": 'Loudred',
        "value": "loudred",
        "image": "img/loudred.png"
    },
    {
        "name": 'Exploud',
        "value": "exploud",
        "image": "img/exploud.png"
    },
    {
        "name": 'Makuhita',
        "value": "makuhita",
        "image": "img/makuhita.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Hariyama',
        "value": "hariyama",
        "image": "img/hariyama.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Azurill',
        "value": "azurill",
        "image": "img/azurill.png"
    },
    {
        "name": 'Nosepass',
        "value": "nosepass",
        "image": "img/nosepass.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Skitty',
        "value": "skitty",
        "image": "img/skitty.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Delcatty',
        "value": "delcatty",
        "image": "img/delcatty.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Sableye',
        "value": "sableye",
        "image": "img/sableye.png"
    },
    {
        "name": 'Mawile',
        "value": "mawile",
        "image": "img/mawile.png"
    },
    {
        "name": 'Aron',
        "value": "aron",
        "image": "img/aron.png"
    },
    {
        "name": 'Lairon',
        "value": "lairon",
        "image": "img/lairon.png"
    },
    {
        "name": 'Aggron',
        "value": "aggron",
        "image": "img/aggron.png"
    },
    {
        "name": 'Meditite',
        "value": "meditite",
        "image": "img/meditite.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Medicham',
        "value": "medicham",
        "image": "img/medicham.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Electrike',
        "value": "electrike",
        "image": "img/electrike.png"
    },
    {
        "name": 'Manectric',
        "value": "manectric",
        "image": "img/manectric.png"
    },
    {
        "name": 'Plusle',
        "value": "plusle",
        "image": "img/plusle.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Minun',
        "value": "minun",
        "image": "img/minun.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Volbeat',
        "value": "volbeat",
        "image": "img/volbeat.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Illumise',
        "value": "illumise",
        "image": "img/illumise.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Roselia',
        "value": "roselia",
        "image": "img/roselia.png"
    },
    {
        "name": 'Gulpin',
        "value": "gulpin",
        "image": "img/gulpin.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Swalot',
        "value": "swalot",
        "image": "img/swalot.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Carvanha',
        "value": "carvanha",
        "image": "img/carvanha.png"
    },
    {
        "name": 'Sharpedo',
        "value": "sharpedo",
        "image": "img/sharpedo.png"
    },
    {
        "name": 'Wailmer',
        "value": "wailmer",
        "image": "img/wailmer.png"
    },
    {
        "name": 'Wailord',
        "value": "wailord",
        "image": "img/wailord.png"
    },
    {
        "name": 'Numel',
        "value": "numel",
        "image": "img/numel.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Camerupt',
        "value": "camerupt",
        "image": "img/camerupt.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Torkoal',
        "value": "torkoal",
        "image": "img/torkoal.png"
    },
    {
        "name": 'Spoink',
        "value": "spoink",
        "image": "img/spoink.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Grumpig',
        "value": "grumpig",
        "image": "img/grumpig.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Spinda',
        "value": "spinda",
        "image": "img/spinda.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Trapinch',
        "value": "trapinch",
        "image": "img/trapinch.png"
    },
    {
        "name": 'Vibrava',
        "value": "vibrava",
        "image": "img/vibrava.png"
    },
    {
        "name": 'Flygon',
        "value": "flygon",
        "image": "img/flygon.png"
    },
    {
        "name": 'Cacnea',
        "value": "cacnea",
        "image": "img/cacnea.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Cacturne',
        "value": "cacturne",
        "image": "img/cacturne.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Swablu',
        "value": "swablu",
        "image": "img/swablu.png"
    },
    {
        "name": 'Altaria',
        "value": "altaria",
        "image": "img/altaria.png"
    },
    {
        "name": 'Zangoose',
        "value": "zangoose",
        "image": "img/zangoose.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Seviper',
        "value": "seviper",
        "image": "img/seviper.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Lunatone',
        "value": "lunatone",
        "image": "img/lunatone.png"
    },
    {
        "name": 'Solrock',
        "value": "solrock",
        "image": "img/solrock.png"
    },
    {
        "name": 'Barboach',
        "value": "barboach",
        "image": "img/barboach.png"
    },
    {
        "name": 'Whiscash',
        "value": "whiscash",
        "image": "img/whiscash.png"
    },
    {
        "name": 'Corphish',
        "value": "corphish",
        "image": "img/corphish.png"
    },
    {
        "name": 'Crawdaunt',
        "value": "crawdaunt",
        "image": "img/crawdaunt.png"
    },
    {
        "name": 'Baltoy',
        "value": "baltoy",
        "image": "img/baltoy.png"
    },
    {
        "name": 'Claydol',
        "value": "claydol",
        "image": "img/claydol.png"
    },
    {
        "name": 'Lileep',
        "value": "lileep",
        "image": "img/lileep.png"
    },
    {
        "name": 'Cradily',
        "value": "cradily",
        "image": "img/cradily.png"
    },
    {
        "name": 'Anorith',
        "value": "anorith",
        "image": "img/anorith.png"
    },
    {
        "name": 'Armaldo',
        "value": "armaldo",
        "image": "img/armaldo.png"
    },
    {
        "name": 'Feebas',
        "value": "feebas",
        "image": "img/feebas.png"
    },
    {
        "name": 'Milotic',
        "value": "milotic",
        "image": "img/milotic.png"
    },
    {
        "name": 'Castform',
        "value": "castform",
        "image": "img/castform.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Kecleon',
        "value": "kecleon",
        "image": "img/kecleon.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Shuppet',
        "value": "shuppet",
        "image": "img/shuppet.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Banette',
        "value": "banette",
        "image": "img/banette.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Duskull',
        "value": "duskull",
        "image": "img/duskull.png"
    },
    {
        "name": 'Dusclops',
        "value": "dusclops",
        "image": "img/dusclops.png"
    },
    {
        "name": 'Tropius',
        "value": "tropius",
        "image": "img/tropius.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Chimecho',
        "value": "chimecho",
        "image": "img/chimecho.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Absol',
        "value": "absol",
        "image": "img/absol.png"
    },
    {
        "name": 'Wynaut',
        "value": "wynaut",
        "image": "img/wynaut.png"
    },
    {
        "name": 'Snorunt',
        "value": "snorunt",
        "image": "img/snorunt.png"
    },
    {
        "name": 'Glalie',
        "value": "glalie",
        "image": "img/glalie.png"
    },
    {
        "name": 'Spheal',
        "value": "spheal",
        "image": "img/spheal.png"
    },
    {
        "name": 'Sealeo',
        "value": "sealeo",
        "image": "img/sealeo.png"
    },
    {
        "name": 'Walrein',
        "value": "walrein",
        "image": "img/walrein.png"
    },
    {
        "name": 'Clamperl',
        "value": "clamperl",
        "image": "img/clamperl.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Huntail',
        "value": "huntail",
        "image": "img/huntail.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Gorebyss',
        "value": "gorebyss",
        "image": "img/gorebyss.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Relicanth',
        "value": "relicanth",
        "image": "img/relicanth.png"
    },
    {
        "name": 'Luvdisc',
        "value": "luvdisc",
        "image": "img/luvdisc.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Bagon',
        "value": "bagon",
        "image": "img/bagon.png"
    },
    {
        "name": 'Shelgon',
        "value": "shelgon",
        "image": "img/shelgon.png"
    },
    {
        "name": 'Salamence',
        "value": "salamence",
        "image": "img/salamence.png"
    },
    {
        "name": 'Beldum',
        "value": "beldum",
        "image": "img/beldum.png"
    },
    {
        "name": 'Metang',
        "value": "metang",
        "image": "img/metang.png"
    },
    {
        "name": 'Metagross',
        "value": "metagross",
        "image": "img/metagross.png"
    },
    {
        "name": 'Regirock',
        "value": "regirock",
        "image": "img/regirock.png"
    },
    {
        "name": 'Regice',
        "value": "regice",
        "image": "img/regice.png"
    },
    {
        "name": 'Registeel',
        "value": "registeel",
        "image": "img/registeel.png"
    },
    {
        "name": 'Latias',
        "value": "latias",
        "image": "img/latias.png"
    },
    {
        "name": 'Latios',
        "value": "latios",
        "image": "img/latios.png"
    },
    {
        "name": 'Kyogre',
        "value": "kyogre",
        "image": "img/kyogre.png"
    },
    {
        "name": 'Groudon',
        "value": "groudon",
        "image": "img/groudon.png"
    },
    {
        "name": 'Rayquaza',
        "value": "rayquaza",
        "image": "img/rayquaza.png"
    },
    {
        "name": 'Jirachi',
        "value": "jirachi",
        "image": "img/jirachi.png"
    },
    {
        "name": 'Deoxys',
        "value": "deoxys",
        "image": "img/deoxys.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Turtwig',
        "value": "turtwig",
        "image": "img/turtwig.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Grotle',
        "value": "grotle",
        "image": "img/grotle.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Torterra',
        "value": "torterra",
        "image": "img/torterra.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Chimchar',
        "value": "chimchar",
        "image": "img/chimchar.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Monferno',
        "value": "monferno",
        "image": "img/monferno.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Infernape',
        "value": "infernape",
        "image": "img/infernape.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Piplup',
        "value": "piplup",
        "image": "img/piplup.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Prinplup',
        "value": "prinplup",
        "image": "img/prinplup.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Empoleon',
        "value": "empoleon",
        "image": "img/empoleon.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Starly',
        "value": "starly",
        "image": "img/starly.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Staravia',
        "value": "staravia",
        "image": "img/staravia.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Staraptor',
        "value": "staraptor",
        "image": "img/staraptor.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Bidoof',
        "value": "bidoof",
        "image": "img/bidoof.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Bibarel',
        "value": "bibarel",
        "image": "img/bibarel.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Kricketot',
        "value": "kricketot",
        "image": "img/kricketot.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Kricketune',
        "value": "kricketune",
        "image": "img/kricketune.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Shinx',
        "value": "shinx",
        "image": "img/shinx.png"
    },
    {
        "name": 'Luxio',
        "value": "luxio",
        "image": "img/luxio.png"
    },
    {
        "name": 'Luxray',
        "value": "luxray",
        "image": "img/luxray.png"
    },
    {
        "name": 'Budew',
        "value": "budew",
        "image": "img/budew.png"
    },
    {
        "name": 'Roserade',
        "value": "roserade",
        "image": "img/roserade.png"
    },
    {
        "name": 'Cranidos',
        "value": "cranidos",
        "image": "img/cranidos.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Rampardos',
        "value": "rampardos",
        "image": "img/rampardos.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Shieldon',
        "value": "shieldon",
        "image": "img/shieldon.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Bastiodon',
        "value": "bastiodon",
        "image": "img/bastiodon.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Burmy',
        "value": "burmy",
        "image": "img/burmy.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Wormadam',
        "value": "wormadam",
        "image": "img/wormadam.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Mothim',
        "value": "mothim",
        "image": "img/mothim.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Combee',
        "value": "combee",
        "image": "img/combee.png"
    },
    {
        "name": 'Vespiquen',
        "value": "vespiquen",
        "image": "img/vespiquen.png"
    },
    {
        "name": 'Pachirisu',
        "value": "pachirisu",
        "image": "img/pachirisu.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Buizel',
        "value": "buizel",
        "image": "img/buizel.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Floatzel',
        "value": "floatzel",
        "image": "img/floatzel.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Cherubi',
        "value": "cherubi",
        "image": "img/cherubi.png"
    },
    {
        "name": 'Cherrim',
        "value": "cherrim",
        "image": "img/cherrim.png"
    },
    {
        "name": 'Shellos',
        "value": "shellos",
        "image": "img/shellos.png"
    },
    {
        "name": 'Gastrodon',
        "value": "gastrodon",
        "image": "img/gastrodon.png"
    },
    {
        "name": 'Ambipom',
        "value": "ambipom",
        "image": "img/ambipom.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Drifloon',
        "value": "drifloon",
        "image": "img/drifloon.png"
    },
    {
        "name": 'Drifblim',
        "value": "drifblim",
        "image": "img/drifblim.png"
    },
    {
        "name": 'Buneary',
        "value": "buneary",
        "image": "img/buneary.png"
    },
    {
        "name": 'Lopunny',
        "value": "lopunny",
        "image": "img/lopunny.png"
    },
    {
        "name": 'Mismagius',
        "value": "mismagius",
        "image": "img/mismagius.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Honchkrow',
        "value": "honchkrow",
        "image": "img/honchkrow.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Glameow',
        "value": "glameow",
        "image": "img/glameow.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Purugly',
        "value": "purugly",
        "image": "img/purugly.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Chingling',
        "value": "chingling",
        "image": "img/chingling.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Stunky',
        "value": "stunky",
        "image": "img/stunky.png"
    },
    {
        "name": 'Skuntank',
        "value": "skuntank",
        "image": "img/skuntank.png"
    },
    {
        "name": 'Bronzor',
        "value": "bronzor",
        "image": "img/bronzor.png"
    },
    {
        "name": 'Bronzong',
        "value": "bronzong",
        "image": "img/bronzong.png"
    },
    {
        "name": 'Bonsly',
        "value": "bonsly",
        "image": "img/bonsly.png"
    },
    {
        "name": 'Mime Jr.',
        "value": "mime-jr",
        "image": "img/mime-jr.png"
    },
    {
        "name": 'Happiny',
        "value": "happiny",
        "image": "img/happiny.png"
    },
    {
        "name": 'Chatot',
        "value": "chatot",
        "image": "img/chatot.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Spiritomb',
        "value": "spiritomb",
        "image": "img/spiritomb.png"
    },
    {
        "name": 'Gible',
        "value": "gible",
        "image": "img/gible.png"
    },
    {
        "name": 'Gabite',
        "value": "gabite",
        "image": "img/gabite.png"
    },
    {
        "name": 'Garchomp',
        "value": "garchomp",
        "image": "img/garchomp.png"
    },
    {
        "name": 'Munchlax',
        "value": "munchlax",
        "image": "img/munchlax.png"
    },
    {
        "name": 'Riolu',
        "value": "riolu",
        "image": "img/riolu.png"
    },
    {
        "name": 'Lucario',
        "value": "lucario",
        "image": "img/lucario.png"
    },
    {
        "name": 'Hippopotas',
        "value": "hippopotas",
        "image": "img/hippopotas.png"
    },
    {
        "name": 'Hippowdon',
        "value": "hippowdon",
        "image": "img/hippowdon.png"
    },
    {
        "name": 'Skorupi',
        "value": "skorupi",
        "image": "img/skorupi.png"
    },
    {
        "name": 'Drapion',
        "value": "drapion",
        "image": "img/drapion.png"
    },
    {
        "name": 'Croagunk',
        "value": "croagunk",
        "image": "img/croagunk.png"
    },
    {
        "name": 'Toxicroak',
        "value": "toxicroak",
        "image": "img/toxicroak.png"
    },
    {
        "name": 'Carnivine',
        "value": "carnivine",
        "image": "img/carnivine.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Finneon',
        "value": "finneon",
        "image": "img/finneon.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Lumineon',
        "value": "lumineon",
        "image": "img/lumineon.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Mantyke',
        "value": "mantyke",
        "image": "img/mantyke.png"
    },
    {
        "name": 'Snover',
        "value": "snover",
        "image": "img/snover.png"
    },
    {
        "name": 'Abomasnow',
        "value": "abomasnow",
        "image": "img/abomasnow.png"
    },
    {
        "name": 'Weavile',
        "value": "weavile",
        "image": "img/weavile.png"
    },
    {
        "name": 'Magnezone',
        "value": "magnezone",
        "image": "img/magnezone.png"
    },
    {
        "name": 'Lickilicky',
        "value": "lickilicky",
        "image": "img/lickilicky.png"
    },
    {
        "name": 'Rhyperior',
        "value": "rhyperior",
        "image": "img/rhyperior.png"
    },
    {
        "name": 'Tangrowth',
        "value": "tangrowth",
        "image": "img/tangrowth.png"
    },
    {
        "name": 'Electivire',
        "value": "electivire",
        "image": "img/electivire.png"
    },
    {
        "name": 'Magmortar',
        "value": "magmortar",
        "image": "img/magmortar.png"
    },
    {
        "name": 'Togekiss',
        "value": "togekiss",
        "image": "img/togekiss.png"
    },
    {
        "name": 'Yanmega',
        "value": "yanmega",
        "image": "img/yanmega.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Leafeon',
        "value": "leafeon",
        "image": "img/leafeon.png"
    },
    {
        "name": 'Glaceon',
        "value": "glaceon",
        "image": "img/glaceon.png"
    },
    {
        "name": 'Gliscor',
        "value": "gliscor",
        "image": "img/gliscor.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Mamoswine',
        "value": "mamoswine",
        "image": "img/mamoswine.png"
    },
    {
        "name": 'Porygon-Z',
        "value": "porygon-z",
        "image": "img/porygon-z.png"
    },
    {
        "name": 'Gallade',
        "value": "gallade",
        "image": "img/gallade.png"
    },
    {
        "name": 'Probopass',
        "value": "probopass",
        "image": "img/probopass.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Dusknoir',
        "value": "dusknoir",
        "image": "img/dusknoir.png"
    },
    {
        "name": 'Froslass',
        "value": "froslass",
        "image": "img/froslass.png"
    },
    {
        "name": 'Rotom',
        "value": "rotom",
        "image": "img/rotom.png"
    },
    {
        "name": 'Uxie',
        "value": "uxie",
        "image": "img/uxie.png"
    },
    {
        "name": 'Mesprit',
        "value": "mesprit",
        "image": "img/mesprit.png"
    },
    {
        "name": 'Azelf',
        "value": "azelf",
        "image": "img/azelf.png"
    },
    {
        "name": 'Dialga',
        "value": "dialga",
        "image": "img/dialga.png"
    },
    {
        "name": 'Palkia',
        "value": "palkia",
        "image": "img/palkia.png"
    },
    {
        "name": 'Heatran',
        "value": "heatran",
        "image": "img/heatran.png"
    },
    {
        "name": 'Regigigas',
        "value": "regigigas",
        "image": "img/regigigas.png"
    },
    {
        "name": 'Giratina',
        "value": "giratina",
        "image": "img/giratina.png"
    },
    {
        "name": 'Cresselia',
        "value": "cresselia",
        "image": "img/cresselia.png"
    },
    {
        "name": 'Phione',
        "value": "phione",
        "image": "img/phione.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Manaphy',
        "value": "manaphy",
        "image": "img/manaphy.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Darkrai',
        "value": "darkrai",
        "image": "img/darkrai.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Shaymin',
        "value": "shaymin",
        "image": "img/shaymin.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Arceus',
        "value": "arceus",
        "image": "img/arceus.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Victini',
        "value": "victini",
        "image": "img/victini.png"
    },
    {
        "name": 'Snivy',
        "value": "snivy",
        "image": "img/snivy.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Servine',
        "value": "servine",
        "image": "img/servine.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Serperior',
        "value": "serperior",
        "image": "img/serperior.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Tepig',
        "value": "tepig",
        "image": "img/tepig.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Pignite',
        "value": "pignite",
        "image": "img/pignite.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Emboar',
        "value": "emboar",
        "image": "img/emboar.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Oshawott',
        "value": "oshawott",
        "image": "img/oshawott.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Dewott',
        "value": "dewott",
        "image": "img/dewott.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Samurott',
        "value": "samurott",
        "image": "img/samurott.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Patrat',
        "value": "patrat",
        "image": "img/patrat.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Watchog',
        "value": "watchog",
        "image": "img/watchog.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Lillipup',
        "value": "lillipup",
        "image": "img/lillipup.png"
    },
    {
        "name": 'Herdier',
        "value": "herdier",
        "image": "img/herdier.png"
    },
    {
        "name": 'Stoutland',
        "value": "stoutland",
        "image": "img/stoutland.png"
    },
    {
        "name": 'Purrloin',
        "value": "purrloin",
        "image": "img/purrloin.png"
    },
    {
        "name": 'Liepard',
        "value": "liepard",
        "image": "img/liepard.png"
    },
    {
        "name": 'Pansage',
        "value": "pansage",
        "image": "img/pansage.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Simisage',
        "value": "simisage",
        "image": "img/simisage.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Pansear',
        "value": "pansear",
        "image": "img/pansear.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Simisear',
        "value": "simisear",
        "image": "img/simisear.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Panpour',
        "value": "panpour",
        "image": "img/panpour.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Simipour',
        "value": "simipour",
        "image": "img/simipour.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Munna',
        "value": "munna",
        "image": "img/munna.png"
    },
    {
        "name": 'Musharna',
        "value": "musharna",
        "image": "img/musharna.png"
    },
    {
        "name": 'Pidove',
        "value": "pidove",
        "image": "img/pidove.png"
    },
    {
        "name": 'Tranquill',
        "value": "tranquill",
        "image": "img/tranquill.png"
    },
    {
        "name": 'Unfezant',
        "value": "unfezant",
        "image": "img/unfezant.png"
    },
    {
        "name": 'Blitzle',
        "value": "blitzle",
        "image": "img/blitzle.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Zebstrika',
        "value": "zebstrika",
        "image": "img/zebstrika.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Roggenrola',
        "value": "roggenrola",
        "image": "img/roggenrola.png"
    },
    {
        "name": 'Boldore',
        "value": "boldore",
        "image": "img/boldore.png"
    },
    {
        "name": 'Gigalith',
        "value": "gigalith",
        "image": "img/gigalith.png"
    },
    {
        "name": 'Woobat',
        "value": "woobat",
        "image": "img/woobat.png"
    },
    {
        "name": 'Swoobat',
        "value": "swoobat",
        "image": "img/swoobat.png"
    },
    {
        "name": 'Drilbur',
        "value": "drilbur",
        "image": "img/drilbur.png"
    },
    {
        "name": 'Excadrill',
        "value": "excadrill",
        "image": "img/excadrill.png"
    },
    {
        "name": 'Audino',
        "value": "audino",
        "image": "img/audino.png"
    },
    {
        "name": 'Timburr',
        "value": "timburr",
        "image": "img/timburr.png"
    },
    {
        "name": 'Gurdurr',
        "value": "gurdurr",
        "image": "img/gurdurr.png"
    },
    {
        "name": 'Conkeldurr',
        "value": "conkeldurr",
        "image": "img/conkeldurr.png"
    },
    {
        "name": 'Tympole',
        "value": "tympole",
        "image": "img/tympole.png"
    },
    {
        "name": 'Palpitoad',
        "value": "palpitoad",
        "image": "img/palpitoad.png"
    },
    {
        "name": 'Seismitoad',
        "value": "seismitoad",
        "image": "img/seismitoad.png"
    },
    {
        "name": 'Throh',
        "value": "throh",
        "image": "img/throh.png"
    },
    {
        "name": 'Sawk',
        "value": "sawk",
        "image": "img/sawk.png"
    },
    {
        "name": 'Sewaddle',
        "value": "sewaddle",
        "image": "img/sewaddle.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Swadloon',
        "value": "swadloon",
        "image": "img/swadloon.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Leavanny',
        "value": "leavanny",
        "image": "img/leavanny.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Venipede',
        "value": "venipede",
        "image": "img/venipede.png"
    },
    {
        "name": 'Whirlipede',
        "value": "whirlipede",
        "image": "img/whirlipede.png"
    },
    {
        "name": 'Scolipede',
        "value": "scolipede",
        "image": "img/scolipede.png"
    },
    {
        "name": 'Cottonee',
        "value": "cottonee",
        "image": "img/cottonee.png"
    },
    {
        "name": 'Whimsicott',
        "value": "whimsicott",
        "image": "img/whimsicott.png"
    },
    {
        "name": 'Petilil',
        "value": "petilil",
        "image": "img/petilil.png"
    },
    {
        "name": 'Lilligant',
        "value": "lilligant",
        "image": "img/lilligant.png"
    },
    {
        "name": 'Basculin',
        "value": "basculin",
        "image": "img/basculin.png"
    },
    {
        "name": 'Sandile',
        "value": "sandile",
        "image": "img/sandile.png"
    },
    {
        "name": 'Krokorok',
        "value": "krokorok",
        "image": "img/krokorok.png"
    },
    {
        "name": 'Krookodile',
        "value": "krookodile",
        "image": "img/krookodile.png"
    },
    {
        "name": 'Darumaka',
        "value": "darumaka",
        "image": "img/darumaka.png"
    },
    {
        "name": 'Darmanitan',
        "value": "darmanitan",
        "image": "img/darmanitan.png"
    },
    {
        "name": 'Maractus',
        "value": "maractus",
        "image": "img/maractus.png"
    },
    {
        "name": 'Dwebble',
        "value": "dwebble",
        "image": "img/dwebble.png"
    },
    {
        "name": 'Crustle',
        "value": "crustle",
        "image": "img/crustle.png"
    },
    {
        "name": 'Scraggy',
        "value": "scraggy",
        "image": "img/scraggy.png"
    },
    {
        "name": 'Scrafty',
        "value": "scrafty",
        "image": "img/scrafty.png"
    },
    {
        "name": 'Sigilyph',
        "value": "sigilyph",
        "image": "img/sigilyph.png"
    },
    {
        "name": 'Yamask',
        "value": "yamask",
        "image": "img/yamask.png"
    },
    {
        "name": 'Cofagrigus',
        "value": "cofagrigus",
        "image": "img/cofagrigus.png"
    },
    {
        "name": 'Tirtouga',
        "value": "tirtouga",
        "image": "img/tirtouga.png"
    },
    {
        "name": 'Carracosta',
        "value": "carracosta",
        "image": "img/carracosta.png"
    },
    {
        "name": 'Archen',
        "value": "archen",
        "image": "img/archen.png"
    },
    {
        "name": 'Archeops',
        "value": "archeops",
        "image": "img/archeops.png"
    },
    {
        "name": 'Trubbish',
        "value": "trubbish",
        "image": "img/trubbish.png"
    },
    {
        "name": 'Garbodor',
        "value": "garbodor",
        "image": "img/garbodor.png"
    },
    {
        "name": 'Zorua',
        "value": "zorua",
        "image": "img/zorua.png"
    },
    {
        "name": 'Zoroark',
        "value": "zoroark",
        "image": "img/zoroark.png"
    },
    {
        "name": 'Minccino',
        "value": "minccino",
        "image": "img/minccino.png"
    },
    {
        "name": 'Cinccino',
        "value": "cinccino",
        "image": "img/cinccino.png"
    },
    {
        "name": 'Gothita',
        "value": "gothita",
        "image": "img/gothita.png"
    },
    {
        "name": 'Gothorita',
        "value": "gothorita",
        "image": "img/gothorita.png"
    },
    {
        "name": 'Gothitelle',
        "value": "gothitelle",
        "image": "img/gothitelle.png"
    },
    {
        "name": 'Solosis',
        "value": "solosis",
        "image": "img/solosis.png"
    },
    {
        "name": 'Duosion',
        "value": "duosion",
        "image": "img/duosion.png"
    },
    {
        "name": 'Reuniclus',
        "value": "reuniclus",
        "image": "img/reuniclus.png"
    },
    {
        "name": 'Ducklett',
        "value": "ducklett",
        "image": "img/ducklett.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Swanna',
        "value": "swanna",
        "image": "img/swanna.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Vanillite',
        "value": "vanillite",
        "image": "img/vanillite.png"
    },
    {
        "name": 'Vanillish',
        "value": "vanillish",
        "image": "img/vanillish.png"
    },
    {
        "name": 'Vanilluxe',
        "value": "vanilluxe",
        "image": "img/vanilluxe.png"
    },
    {
        "name": 'Deerling',
        "value": "deerling",
        "image": "img/deerling.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Sawsbuck',
        "value": "sawsbuck",
        "image": "img/sawsbuck.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Emolga',
        "value": "emolga",
        "image": "img/emolga.png"
    },
    {
        "name": 'Karrablast',
        "value": "karrablast",
        "image": "img/karrablast.png"
    },
    {
        "name": 'Escavalier',
        "value": "escavalier",
        "image": "img/escavalier.png"
    },
    {
        "name": 'Foongus',
        "value": "foongus",
        "image": "img/foongus.png"
    },
    {
        "name": 'Amoonguss',
        "value": "amoonguss",
        "image": "img/amoonguss.png"
    },
    {
        "name": 'Frillish',
        "value": "frillish",
        "image": "img/frillish.png"
    },
    {
        "name": 'Jellicent',
        "value": "jellicent",
        "image": "img/jellicent.png"
    },
    {
        "name": 'Alomomola',
        "value": "alomomola",
        "image": "img/alomomola.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Joltik',
        "value": "joltik",
        "image": "img/joltik.png"
    },
    {
        "name": 'Galvantula',
        "value": "galvantula",
        "image": "img/galvantula.png"
    },
    {
        "name": 'Ferroseed',
        "value": "ferroseed",
        "image": "img/ferroseed.png"
    },
    {
        "name": 'Ferrothorn',
        "value": "ferrothorn",
        "image": "img/ferrothorn.png"
    },
    {
        "name": 'Klink',
        "value": "klink",
        "image": "img/klink.png"
    },
    {
        "name": 'Klang',
        "value": "klang",
        "image": "img/klang.png"
    },
    {
        "name": 'Klinklang',
        "value": "klinklang",
        "image": "img/klinklang.png"
    },
    {
        "name": 'Tynamo',
        "value": "tynamo",
        "image": "img/tynamo.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Eelektrik',
        "value": "eelektrik",
        "image": "img/eelektrik.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Eelektross',
        "value": "eelektross",
        "image": "img/eelektross.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Elgyem',
        "value": "elgyem",
        "image": "img/elgyem.png"
    },
    {
        "name": 'Beheeyem',
        "value": "beheeyem",
        "image": "img/beheeyem.png"
    },
    {
        "name": 'Litwick',
        "value": "litwick",
        "image": "img/litwick.png"
    },
    {
        "name": 'Lampent',
        "value": "lampent",
        "image": "img/lampent.png"
    },
    {
        "name": 'Chandelure',
        "value": "chandelure",
        "image": "img/chandelure.png"
    },
    {
        "name": 'Axew',
        "value": "axew",
        "image": "img/axew.png"
    },
    {
        "name": 'Fraxure',
        "value": "fraxure",
        "image": "img/fraxure.png"
    },
    {
        "name": 'Haxorus',
        "value": "haxorus",
        "image": "img/haxorus.png"
    },
    {
        "name": 'Cubchoo',
        "value": "cubchoo",
        "image": "img/cubchoo.png"
    },
    {
        "name": 'Beartic',
        "value": "beartic",
        "image": "img/beartic.png"
    },
    {
        "name": 'Cryogonal',
        "value": "cryogonal",
        "image": "img/cryogonal.png"
    },
    {
        "name": 'Shelmet',
        "value": "shelmet",
        "image": "img/shelmet.png"
    },
    {
        "name": 'Accelgor',
        "value": "accelgor",
        "image": "img/accelgor.png"
    },
    {
        "name": 'Stunfisk',
        "value": "stunfisk",
        "image": "img/stunfisk.png"
    },
    {
        "name": 'Mienfoo',
        "value": "mienfoo",
        "image": "img/mienfoo.png"
    },
    {
        "name": 'Mienshao',
        "value": "mienshao",
        "image": "img/mienshao.png"
    },
    {
        "name": 'Druddigon',
        "value": "druddigon",
        "image": "img/druddigon.png"
    },
    {
        "name": 'Golett',
        "value": "golett",
        "image": "img/golett.png"
    },
    {
        "name": 'Golurk',
        "value": "golurk",
        "image": "img/golurk.png"
    },
    {
        "name": 'Pawniard',
        "value": "pawniard",
        "image": "img/pawniard.png"
    },
    {
        "name": 'Bisharp',
        "value": "bisharp",
        "image": "img/bisharp.png"
    },
    {
        "name": 'Bouffalant',
        "value": "bouffalant",
        "image": "img/bouffalant.png"
    },
    {
        "name": 'Rufflet',
        "value": "rufflet",
        "image": "img/rufflet.png"
    },
    {
        "name": 'Braviary',
        "value": "braviary",
        "image": "img/braviary.png"
    },
    {
        "name": 'Vullaby',
        "value": "vullaby",
        "image": "img/vullaby.png"
    },
    {
        "name": 'Mandibuzz',
        "value": "mandibuzz",
        "image": "img/mandibuzz.png"
    },
    {
        "name": 'Heatmor',
        "value": "heatmor",
        "image": "img/heatmor.png"
    },
    {
        "name": 'Durant',
        "value": "durant",
        "image": "img/durant.png"
    },
    {
        "name": 'Deino',
        "value": "deino",
        "image": "img/deino.png"
    },
    {
        "name": 'Zweilous',
        "value": "zweilous",
        "image": "img/zweilous.png"
    },
    {
        "name": 'Hydreigon',
        "value": "hydreigon",
        "image": "img/hydreigon.png"
    },
    {
        "name": 'Larvesta',
        "value": "larvesta",
        "image": "img/larvesta.png"
    },
    {
        "name": 'Volcarona',
        "value": "volcarona",
        "image": "img/volcarona.png"
    },
    {
        "name": 'Cobalion',
        "value": "cobalion",
        "image": "img/cobalion.png"
    },
    {
        "name": 'Terrakion',
        "value": "terrakion",
        "image": "img/terrakion.png"
    },
    {
        "name": 'Virizion',
        "value": "virizion",
        "image": "img/virizion.png"
    },
    {
        "name": 'Tornadus',
        "value": "tornadus",
        "image": "img/tornadus.png"
    },
    {
        "name": 'Thundurus',
        "value": "thundurus",
        "image": "img/thundurus.png"
    },
    {
        "name": 'Reshiram',
        "value": "reshiram",
        "image": "img/reshiram.png"
    },
    {
        "name": 'Zekrom',
        "value": "zekrom",
        "image": "img/zekrom.png"
    },
    {
        "name": 'Landorus',
        "value": "landorus",
        "image": "img/landorus.png"
    },
    {
        "name": 'Kyurem',
        "value": "kyurem",
        "image": "img/kyurem.png"
    },
    {
        "name": 'Keldeo',
        "value": "keldeo",
        "image": "img/keldeo.png"
    },
    {
        "name": 'Meloetta',
        "value": "meloetta",
        "image": "img/meloetta.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Genesect',
        "value": "genesect",
        "image": "img/genesect.png"
    },
    {
        "name": 'Chespin',
        "value": "chespin",
        "image": "img/chespin.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Quilladin',
        "value": "quilladin",
        "image": "img/quilladin.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Chesnaught',
        "value": "chesnaught",
        "image": "img/chesnaught.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Fennekin',
        "value": "fennekin",
        "image": "img/fennekin.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Braixen',
        "value": "braixen",
        "image": "img/braixen.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Delphox',
        "value": "delphox",
        "image": "img/delphox.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Froakie',
        "value": "froakie",
        "image": "img/froakie.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Frogadier',
        "value": "frogadier",
        "image": "img/frogadier.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Greninja',
        "value": "greninja",
        "image": "img/greninja.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Bunnelby',
        "value": "bunnelby",
        "image": "img/bunnelby.png"
    },
    {
        "name": 'Diggersby',
        "value": "diggersby",
        "image": "img/diggersby.png"
    },
    {
        "name": 'Fletchling',
        "value": "fletchling",
        "image": "img/fletchling.png"
    },
    {
        "name": 'Fletchinder',
        "value": "fletchinder",
        "image": "img/fletchinder.png"
    },
    {
        "name": 'Talonflame',
        "value": "talonflame",
        "image": "img/talonflame.png"
    },
    {
        "name": 'Scatterbug',
        "value": "scatterbug",
        "image": "img/scatterbug.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Spewpa',
        "value": "spewpa",
        "image": "img/spewpa.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Vivillon',
        "value": "vivillon",
        "image": "img/vivillon.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Litleo',
        "value": "litleo",
        "image": "img/litleo.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Pyroar',
        "value": "pyroar",
        "image": "img/pyroar.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Flabébé',
        "value": "flabebe",
        "image": "img/flabebe.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Floette',
        "value": "floette",
        "image": "img/floette.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Florges',
        "value": "florges",
        "image": "img/florges.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Skiddo',
        "value": "skiddo",
        "image": "img/skiddo.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Gogoat',
        "value": "gogoat",
        "image": "img/gogoat.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Pancham',
        "value": "pancham",
        "image": "img/pancham.png"
    },
    {
        "name": 'Pangoro',
        "value": "pangoro",
        "image": "img/pangoro.png"
    },
    {
        "name": 'Furfrou',
        "value": "furfrou",
        "image": "img/furfrou.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Espurr',
        "value": "espurr",
        "image": "img/espurr.png"
    },
    {
        "name": 'Meowstic',
        "value": "meowstic",
        "image": "img/meowstic.png"
    },
    {
        "name": 'Honedge',
        "value": "honedge",
        "image": "img/honedge.png"
    },
    {
        "name": 'Doublade',
        "value": "doublade",
        "image": "img/doublade.png"
    },
    {
        "name": 'Aegislash',
        "value": "aegislash",
        "image": "img/aegislash.png"
    },
    {
        "name": 'Spritzee',
        "value": "spritzee",
        "image": "img/spritzee.png"
    },
    {
        "name": 'Aromatisse',
        "value": "aromatisse",
        "image": "img/aromatisse.png"
    },
    {
        "name": 'Swirlix',
        "value": "swirlix",
        "image": "img/swirlix.png"
    },
    {
        "name": 'Slurpuff',
        "value": "slurpuff",
        "image": "img/slurpuff.png"
    },
    {
        "name": 'Inkay',
        "value": "inkay",
        "image": "img/inkay.png"
    },
    {
        "name": 'Malamar',
        "value": "malamar",
        "image": "img/malamar.png"
    },
    {
        "name": 'Binacle',
        "value": "binacle",
        "image": "img/binacle.png"
    },
    {
        "name": 'Barbaracle',
        "value": "barbaracle",
        "image": "img/barbaracle.png"
    },
    {
        "name": 'Skrelp',
        "value": "skrelp",
        "image": "img/skrelp.png"
    },
    {
        "name": 'Dragalge',
        "value": "dragalge",
        "image": "img/dragalge.png"
    },
    {
        "name": 'Clauncher',
        "value": "clauncher",
        "image": "img/clauncher.png"
    },
    {
        "name": 'Clawitzer',
        "value": "clawitzer",
        "image": "img/clawitzer.png"
    },
    {
        "name": 'Helioptile',
        "value": "helioptile",
        "image": "img/helioptile.png"
    },
    {
        "name": 'Heliolisk',
        "value": "heliolisk",
        "image": "img/heliolisk.png"
    },
    {
        "name": 'Tyrunt',
        "value": "tyrunt",
        "image": "img/tyrunt.png"
    },
    {
        "name": 'Tyrantrum',
        "value": "tyrantrum",
        "image": "img/tyrantrum.png"
    },
    {
        "name": 'Amaura',
        "value": "amaura",
        "image": "img/amaura.png"
    },
    {
        "name": 'Aurorus',
        "value": "aurorus",
        "image": "img/aurorus.png"
    },
    {
        "name": 'Sylveon',
        "value": "sylveon",
        "image": "img/sylveon.png"
    },
    {
        "name": 'Hawlucha',
        "value": "hawlucha",
        "image": "img/hawlucha.png"
    },
    {
        "name": 'Dedenne',
        "value": "dedenne",
        "image": "img/dedenne.png"
    },
    {
        "name": 'Carbink',
        "value": "carbink",
        "image": "img/carbink.png"
    },
    {
        "name": 'Goomy',
        "value": "goomy",
        "image": "img/goomy.png"
    },
    {
        "name": 'Sliggoo',
        "value": "sliggoo",
        "image": "img/sliggoo.png"
    },
    {
        "name": 'Goodra',
        "value": "goodra",
        "image": "img/goodra.png"
    },
    {
        "name": 'Klefki',
        "value": "klefki",
        "image": "img/klefki.png"
    },
    {
        "name": 'Phantump',
        "value": "phantump",
        "image": "img/phantump.png"
    },
    {
        "name": 'Trevenant',
        "value": "trevenant",
        "image": "img/trevenant.png"
    },
    {
        "name": 'Pumpkaboo',
        "value": "pumpkaboo",
        "image": "img/pumpkaboo.png"
    },
    {
        "name": 'Gourgeist',
        "value": "gourgeist",
        "image": "img/gourgeist.png"
    },
    {
        "name": 'Bergmite',
        "value": "bergmite",
        "image": "img/bergmite.png"
    },
    {
        "name": 'Avalugg',
        "value": "avalugg",
        "image": "img/avalugg.png"
    },
    {
        "name": 'Noibat',
        "value": "noibat",
        "image": "img/noibat.png"
    },
    {
        "name": 'Noivern',
        "value": "noivern",
        "image": "img/noivern.png"
    },
    {
        "name": 'Xerneas',
        "value": "xerneas",
        "image": "img/xerneas.png"
    },
    {
        "name": 'Yveltal',
        "value": "yveltal",
        "image": "img/yveltal.png"
    },
    {
        "name": 'Zygarde',
        "value": "zygarde",
        "image": "img/zygarde.png"
    },
    {
        "name": 'Diancie',
        "value": "diancie",
        "image": "img/diancie.png"
    },
    {
        "name": 'Hoopa',
        "value": "hoopa",
        "image": "img/hoopa.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Volcanion',
        "value": "volcanion",
        "image": "img/volcanion.png"
    },
    {
        "name": 'Rowlet',
        "value": "rowlet",
        "image": "img/rowlet.png"
    },
    {
        "name": 'Dartrix',
        "value": "dartrix",
        "image": "img/dartrix.png"
    },
    {
        "name": 'Decidueye',
        "value": "decidueye",
        "image": "img/decidueye.png"
    },
    {
        "name": 'Litten',
        "value": "litten",
        "image": "img/litten.png"
    },
    {
        "name": 'Torracat',
        "value": "torracat",
        "image": "img/torracat.png"
    },
    {
        "name": 'Incineroar',
        "value": "incineroar",
        "image": "img/incineroar.png"
    },
    {
        "name": 'Popplio',
        "value": "popplio",
        "image": "img/popplio.png"
    },
    {
        "name": 'Brionne',
        "value": "brionne",
        "image": "img/brionne.png"
    },
    {
        "name": 'Primarina',
        "value": "primarina",
        "image": "img/primarina.png"
    },
    {
        "name": 'Pikipek',
        "value": "pikipek",
        "image": "img/pikipek.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Trumbeak',
        "value": "trumbeak",
        "image": "img/trumbeak.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Toucannon',
        "value": "toucannon",
        "image": "img/toucannon.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Yungoos',
        "value": "yungoos",
        "image": "img/yungoos.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Gumshoos',
        "value": "gumshoos",
        "image": "img/gumshoos.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Grubbin',
        "value": "grubbin",
        "image": "img/grubbin.png"
    },
    {
        "name": 'Charjabug',
        "value": "charjabug",
        "image": "img/charjabug.png"
    },
    {
        "name": 'Vikavolt',
        "value": "vikavolt",
        "image": "img/vikavolt.png"
    },
    {
        "name": 'Crabrawler',
        "value": "crabrawler",
        "image": "img/crabrawler.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Crabominable',
        "value": "crabominable",
        "image": "img/crabominable.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Oricorio',
        "value": "oricorio",
        "image": "img/oricorio.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Cutiefly',
        "value": "cutiefly",
        "image": "img/cutiefly.png"
    },
    {
        "name": 'Ribombee',
        "value": "ribombee",
        "image": "img/ribombee.png"
    },
    {
        "name": 'Rockruff',
        "value": "rockruff",
        "image": "img/rockruff.png"
    },
    {
        "name": 'Lycanroc',
        "value": "lycanroc",
        "image": "img/lycanroc.png"
    },
    {
        "name": 'Wishiwashi',
        "value": "wishiwashi",
        "image": "img/wishiwashi.png"
    },
    {
        "name": 'Mareanie',
        "value": "mareanie",
        "image": "img/mareanie.png"
    },
    {
        "name": 'Toxapex',
        "value": "toxapex",
        "image": "img/toxapex.png"
    },
    {
        "name": 'Mudbray',
        "value": "mudbray",
        "image": "img/mudbray.png"
    },
    {
        "name": 'Mudsdale',
        "value": "mudsdale",
        "image": "img/mudsdale.png"
    },
    {
        "name": 'Dewpider',
        "value": "dewpider",
        "image": "img/dewpider.png"
    },
    {
        "name": 'Araquanid',
        "value": "araquanid",
        "image": "img/araquanid.png"
    },
    {
        "name": 'Fomantis',
        "value": "fomantis",
        "image": "img/fomantis.png"
    },
    {
        "name": 'Lurantis',
        "value": "lurantis",
        "image": "img/lurantis.png"
    },
    {
        "name": 'Morelull',
        "value": "morelull",
        "image": "img/morelull.png"
    },
    {
        "name": 'Shiinotic',
        "value": "shiinotic",
        "image": "img/shiinotic.png"
    },
    {
        "name": 'Salandit',
        "value": "salandit",
        "image": "img/salandit.png"
    },
    {
        "name": 'Salazzle',
        "value": "salazzle",
        "image": "img/salazzle.png"
    },
    {
        "name": 'Stufful',
        "value": "stufful",
        "image": "img/stufful.png"
    },
    {
        "name": 'Bewear',
        "value": "bewear",
        "image": "img/bewear.png"
    },
    {
        "name": 'Bounsweet',
        "value": "bounsweet",
        "image": "img/bounsweet.png"
    },
    {
        "name": 'Steenee',
        "value": "steenee",
        "image": "img/steenee.png"
    },
    {
        "name": 'Tsareena',
        "value": "tsareena",
        "image": "img/tsareena.png"
    },
    {
        "name": 'Comfey',
        "value": "comfey",
        "image": "img/comfey.png"
    },
    {
        "name": 'Oranguru',
        "value": "oranguru",
        "image": "img/oranguru.png"
    },
    {
        "name": 'Passimian',
        "value": "passimian",
        "image": "img/passimian.png"
    },
    {
        "name": 'Wimpod',
        "value": "wimpod",
        "image": "img/wimpod.png"
    },
    {
        "name": 'Golisopod',
        "value": "golisopod",
        "image": "img/golisopod.png"
    },
    {
        "name": 'Sandygast',
        "value": "sandygast",
        "image": "img/sandygast.png"
    },
    {
        "name": 'Palossand',
        "value": "palossand",
        "image": "img/palossand.png"
    },
    {
        "name": 'Pyukumuku',
        "value": "pyukumuku",
        "image": "img/pyukumuku.png"
    },
    {
        "name": 'Type: Null',
        "value": "type-null",
        "image": "img/type-null.png"
    },
    {
        "name": 'Silvally',
        "value": "silvally",
        "image": "img/silvally.png"
    },
    {
        "name": 'Minior',
        "value": "minior",
        "image": "img/minior.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Komala',
        "value": "komala",
        "image": "img/komala.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Turtonator',
        "value": "turtonator",
        "image": "img/turtonator.png"
    },
    {
        "name": 'Togedemaru',
        "value": "togedemaru",
        "image": "img/togedemaru.png"
    },
    {
        "name": 'Mimikyu',
        "value": "mimikyu",
        "image": "img/mimikyu.png"
    },
    {
        "name": 'Bruxish',
        "value": "bruxish",
        "image": "img/bruxish.png",
        "exclude": ['swsh']
    },
    {
        "name": 'Drampa',
        "value": "drampa",
        "image": "img/drampa.png"
    },
    {
        "name": 'Dhelmise',
        "value": "dhelmise",
        "image": "img/dhelmise.png"
    },
    {
        "name": 'Jangmo-o',
        "value": "jangmo-o",
        "image": "img/jangmo-o.png"
    },
    {
        "name": 'Hakamo-o',
        "value": "hakamo-o",
        "image": "img/hakamo-o.png"
    },
    {
        "name": 'Kommo-o',
        "value": "kommo-o",
        "image": "img/kommo-o.png"
    },
    {
        "name": 'Tapu Koko',
        "value": "tapu-koko",
        "image": "img/tapu-koko.png"
    },
    {
        "name": 'Tapu Lele',
        "value": "tapu-lele",
        "image": "img/tapu-lele.png"
    },
    {
        "name": 'Tapu Bulu',
        "value": "tapu-bulu",
        "image": "img/tapu-bulu.png"
    },
    {
        "name": 'Tapu Fini',
        "value": "tapu-fini",
        "image": "img/tapu-fini.png"
    },
    {
        "name": 'Cosmog',
        "value": "cosmog",
        "image": "img/cosmog.png"
    },
    {
        "name": 'Cosmoem',
        "value": "cosmoem",
        "image": "img/cosmoem.png"
    },
    {
        "name": 'Solgaleo',
        "value": "solgaleo",
        "image": "img/solgaleo.png"
    },
    {
        "name": 'Lunala',
        "value": "lunala",
        "image": "img/lunala.png"
    },
    {
        "name": 'Nihilego',
        "value": "nihilego",
        "image": "img/nihilego.png"
    },
    {
        "name": 'Buzzwole',
        "value": "buzzwole",
        "image": "img/buzzwole.png"
    },
    {
        "name": 'Pheromosa',
        "value": "pheromosa",
        "image": "img/pheromosa.png"
    },
    {
        "name": 'Xurkitree',
        "value": "xurkitree",
        "image": "img/xurkitree.png"
    },
    {
        "name": 'Celesteela',
        "value": "celesteela",
        "image": "img/celesteela.png"
    },
    {
        "name": 'Kartana',
        "value": "kartana",
        "image": "img/kartana.png"
    },
    {
        "name": 'Guzzlord',
        "value": "guzzlord",
        "image": "img/guzzlord.png"
    },
    {
        "name": 'Necrozma',
        "value": "necrozma",
        "image": "img/necrozma.png"
    },
    {
        "name": 'Magearna',
        "value": "magearna",
        "image": "img/magearna.png"
    },
    {
        "name": 'Marshadow',
        "value": "marshadow",
        "image": "img/marshadow.png"
    },
    {
        "name": 'Poipole',
        "value": "poipole",
        "image": "img/poipole.png"
    },
    {
        "name": 'Naganadel',
        "value": "naganadel",
        "image": "img/naganadel.png"
    },
    {
        "name": 'Stakataka',
        "value": "stakataka",
        "image": "img/stakataka.png"
    },
    {
        "name": 'Blacephalon',
        "value": "blacephalon",
        "image": "img/blacephalon.png"
    },
    {
        "name": 'Zeraora',
        "value": "zeraora",
        "image": "img/zeraora.png"
    },
    {
        "name": 'Meltan',
        "value": "meltan",
        "image": "img/meltan.png"
    },
    {
        "name": 'Melmetal',
        "value": "melmetal",
        "image": "img/melmetal.png"
    },
    {
        "name": 'Grookey',
        "value": "grookey",
        "image": "img/grookey.png"
    },
    {
        "name": 'Thwackey',
        "value": "thwackey",
        "image": "img/thwackey.png"
    },
    {
        "name": 'Rillaboom',
        "value": "rillaboom",
        "image": "img/rillaboom.png"
    },
    {
        "name": 'Scorbunny',
        "value": "scorbunny",
        "image": "img/scorbunny.png"
    },
    {
        "name": 'Raboot',
        "value": "raboot",
        "image": "img/raboot.png"
    },
    {
        "name": 'Cinderace',
        "value": "cinderace",
        "image": "img/cinderace.png"
    },
    {
        "name": 'Sobble',
        "value": "sobble",
        "image": "img/sobble.png"
    },
    {
        "name": 'Drizzile',
        "value": "drizzile",
        "image": "img/drizzile.png"
    },
    {
        "name": 'Inteleon',
        "value": "inteleon",
        "image": "img/inteleon.png"
    },
    {
        "name": 'Skwovet',
        "value": "skwovet",
        "image": "img/skwovet.png"
    },
    {
        "name": 'Greedent',
        "value": "greedent",
        "image": "img/greedent.png"
    },
    {
        "name": 'Rookidee',
        "value": "rookidee",
        "image": "img/rookidee.png"
    },
    {
        "name": 'Corvisquire',
        "value": "corvisquire",
        "image": "img/corvisquire.png"
    },
    {
        "name": 'Corviknight',
        "value": "corviknight",
        "image": "img/corviknight.png"
    },
    {
        "name": 'Blipbug',
        "value": "blipbug",
        "image": "img/blipbug.png"
    },
    {
        "name": 'Dottler',
        "value": "dottler",
        "image": "img/dottler.png"
    },
    {
        "name": 'Orbeetle',
        "value": "orbeetle",
        "image": "img/orbeetle.png"
    },
    {
        "name": 'Nickit',
        "value": "nickit",
        "image": "img/nickit.png"
    },
    {
        "name": 'Thievul',
        "value": "thievul",
        "image": "img/thievul.png"
    },
    {
        "name": 'Gossifleur',
        "value": "gossifleur",
        "image": "img/gossifleur.png"
    },
    {
        "name": 'Eldegoss',
        "value": "eldegoss",
        "image": "img/eldegoss.png"
    },
    {
        "name": 'Wooloo',
        "value": "wooloo",
        "image": "img/wooloo.png"
    },
    {
        "name": 'Dubwool',
        "value": "dubwool",
        "image": "img/dubwool.png"
    },
    {
        "name": 'Chewtle',
        "value": "chewtle",
        "image": "img/chewtle.png"
    },
    {
        "name": 'Drednaw',
        "value": "drednaw",
        "image": "img/drednaw.png"
    },
    {
        "name": 'Yamper',
        "value": "yamper",
        "image": "img/yamper.png"
    },
    {
        "name": 'Boltund',
        "value": "boltund",
        "image": "img/boltund.png"
    },
    {
        "name": 'Rolycoly',
        "value": "rolycoly",
        "image": "img/rolycoly.png"
    },
    {
        "name": 'Carkol',
        "value": "carkol",
        "image": "img/carkol.png"
    },
    {
        "name": 'Coalossal',
        "value": "coalossal",
        "image": "img/coalossal.png"
    },
    {
        "name": 'Applin',
        "value": "applin",
        "image": "img/applin.png"
    },
    {
        "name": 'Flapple',
        "value": "flapple",
        "image": "img/flapple.png"
    },
    {
        "name": 'Appletun',
        "value": "appletun",
        "image": "img/appletun.png"
    },
    {
        "name": 'Silicobra',
        "value": "silicobra",
        "image": "img/silicobra.png"
    },
    {
        "name": 'Sandaconda',
        "value": "sandaconda",
        "image": "img/sandaconda.png"
    },
    {
        "name": 'Cramorant',
        "value": "cramorant",
        "image": "img/cramorant.png"
    },
    {
        "name": 'Arrokuda',
        "value": "arrokuda",
        "image": "img/arrokuda.png"
    },
    {
        "name": 'Barraskewda',
        "value": "barraskewda",
        "image": "img/barraskewda.png"
    },
    {
        "name": 'Toxel',
        "value": "toxel",
        "image": "img/toxel.png"
    },
    {
        "name": 'Toxtricity',
        "value": "toxtricity",
        "image": "img/toxtricity.png"
    },
    {
        "name": 'Sizzlipede',
        "value": "sizzlipede",
        "image": "img/sizzlipede.png"
    },
    {
        "name": 'Centiskorch',
        "value": "centiskorch",
        "image": "img/centiskorch.png"
    },
    {
        "name": 'Clobbopus',
        "value": "clobbopus",
        "image": "img/clobbopus.png"
    },
    {
        "name": 'Grapploct',
        "value": "grapploct",
        "image": "img/grapploct.png"
    },
    {
        "name": 'Sinistea',
        "value": "sinistea",
        "image": "img/sinistea.png"
    },
    {
        "name": 'Polteageist',
        "value": "polteageist",
        "image": "img/polteageist.png"
    },
    {
        "name": 'Hatenna',
        "value": "hatenna",
        "image": "img/hatenna.png"
    },
    {
        "name": 'Hattrem',
        "value": "hattrem",
        "image": "img/hattrem.png"
    },
    {
        "name": 'Hatterene',
        "value": "hatterene",
        "image": "img/hatterene.png"
    },
    {
        "name": 'Impidimp',
        "value": "impidimp",
        "image": "img/impidimp.png"
    },
    {
        "name": 'Morgrem',
        "value": "morgrem",
        "image": "img/morgrem.png"
    },
    {
        "name": 'Grimmsnarl',
        "value": "grimmsnarl",
        "image": "img/grimmsnarl.png"
    },
    {
        "name": 'Obstagoon',
        "value": "obstagoon",
        "image": "img/obstagoon.png"
    },
    {
        "name": 'Perrserker',
        "value": "perrserker",
        "image": "img/perrserker.png"
    },
    {
        "name": 'Cursola',
        "value": "cursola",
        "image": "img/cursola.png"
    },
    {
        "name": 'Sirfetch\'d',
        "value": "sirfetchd",
        "image": "img/sirfetchd.png"
    },
    {
        "name": 'Mr. Rime',
        "value": "mr-rime",
        "image": "img/mr-rime.png"
    },
    {
        "name": 'Runerigus',
        "value": "runerigus",
        "image": "img/runerigus.png"
    },
    {
        "name": 'Milcery',
        "value": "milcery",
        "image": "img/milcery.png"
    },
    {
        "name": 'Alcremie',
        "value": "alcremie",
        "image": "img/alcremie.png"
    },
    {
        "name": 'Falinks',
        "value": "falinks",
        "image": "img/falinks.png"
    },
    {
        "name": 'Pincurchin',
        "value": "pincurchin",
        "image": "img/pincurchin.png"
    },
    {
        "name": 'Snom',
        "value": "snom",
        "image": "img/snom.png"
    },
    {
        "name": 'Frosmoth',
        "value": "frosmoth",
        "image": "img/frosmoth.png"
    },
    {
        "name": 'Stonjourner',
        "value": "stonjourner",
        "image": "img/stonjourner.png"
    },
    {
        "name": 'Eiscue',
        "value": "eiscue",
        "image": "img/eiscue.png"
    },
    {
        "name": 'Indeedee',
        "value": "indeedee",
        "image": "img/indeedee.png"
    },
    {
        "name": 'Morpeko',
        "value": "morpeko",
        "image": "img/morpeko.png"
    },
    {
        "name": 'Cufant',
        "value": "cufant",
        "image": "img/cufant.png"
    },
    {
        "name": 'Copperajah',
        "value": "copperajah",
        "image": "img/copperajah.png"
    },
    {
        "name": 'Dracozolt',
        "value": "dracozolt",
        "image": "img/dracozolt.png"
    },
    {
        "name": 'Arctozolt',
        "value": "arctozolt",
        "image": "img/arctozolt.png"
    },
    {
        "name": 'Dracovish',
        "value": "dracovish",
        "image": "img/dracovish.png"
    },
    {
        "name": 'Arctovish',
        "value": "arctovish",
        "image": "img/arctovish.png"
    },
    {
        "name": 'Duraludon',
        "value": "duraludon",
        "image": "img/duraludon.png"
    },
    {
        "name": 'Dreepy',
        "value": "dreepy",
        "image": "img/dreepy.png"
    },
    {
        "name": 'Drakloak',
        "value": "drakloak",
        "image": "img/drakloak.png"
    },
    {
        "name": 'Dragapult',
        "value": "dragapult",
        "image": "img/dragapult.png"
    },
    {
        "name": 'Zacian',
        "value": "zacian",
        "image": "img/zacian.png"
    },
    {
        "name": 'Zamazenta',
        "value": "zamazenta",
        "image": "img/zamazenta.png"
    },
    {
        "name": 'Eternatus',
        "value": "eternatus",
        "image": "img/eternatus.png"
    },
    {
        "name": 'Kubfu',
        "value": "kubfu",
        "image": "img/kubfu.png"
    },
    {
        "name": 'Urshifu',
        "value": "urshifu",
        "image": "img/urshifu.png"
    },
    {
        "name": 'Zarude',
        "value": "zarude",
        "image": "img/zarude.png"
    },
    {
        "name": 'Regieleki',
        "value": "regieleki",
        "image": "img/regieleki.png"
    },
    {
        "name": 'Regidrago',
        "value": "regidrago",
        "image": "img/regidrago.png"
    },
    {
        "name": 'Glastrier',
        "value": "glastrier",
        "image": "img/glastrier.png"
    },
    {
        "name": 'Spectrier',
        "value": "spectrier",
        "image": "img/spectrier.png"
    },
    {
        "name": 'Calyrex',
        "value": "calyrex",
        "image": "img/calyrex.png"
    }
]

overwrites = []
for i, pkmn in enumerate(pkmnData):
    print(pkmn['name'], " --> ", end='')
    pokeapi = pb.pokemon_species(pkmn['value'])
    try:
        for name in pokeapi.names:
            if str(name.language) == 'de':
                print(name.name)
                overwrites.append((i, name.name))
    except AttributeError as e:
        print(pkmn['name']+"[NAME?]")
        overwrites.append((i,pkmn['name']+"[NAME?]"))

for ow in overwrites:
    pkmnData[ow[0]]['name'] = ow[1]

pprint(pkmnData)
