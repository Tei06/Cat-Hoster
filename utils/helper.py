import discord
from discord.ext.commands.errors import PrivateMessageOnly
import pymongo


mongo_url = "mongodb+srv://Tei:yeet123LMAO@shizukudb.rt4ys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["ShizukuDB"]
collection = db['new']


async def get_user(member, ctx):
    stat = collection.find_one({'_id': member})
    if stat == None:
        await ctx.send("Please make an account first by doing -start")
        return None
    elif stat != None:
        return True


async def get_member(member, ctx):
    stat = collection.find_one({'_id': member.id})
    if stat == None:
        await ctx.send(f"`{member.display_name}` does not have an account")
        return None
    elif stat != None:
        return True

shop_items = {
    "Traits": {
        "overdrive": {
            "DESCRIPTION": "__Speed Boost:__ 2 rounds to charge, gain `10` / `15` / `20` Speed.",
            "COST": 5000,
            "EMOJI": " "
        },
        "heightened awareness": {
            "DESCRIPTION": "__Evasion Boost:__ Requires 2 rounds to charge, gain `3` / `4` / `5` Evasion.",
            "COST": 5000,
            "EMOJI": " "
        },
        "voracity": {
            "DESCRIPTION": "__Attack Boost:__ Requires 2 rounds to charge, gain `20` / `30` / `40` Attack.",
            "COST": 5000,
            "EMOJI": " "
        },
        "innate bloodlust": {
            "DESCRIPTION": "__Critical Chance Boost:__ Requires 2 rounds to charge, gain `5` / `10` / `15` Critical Chance.",
            "COST": 5000,
            "EMOJI": " "
        },
        "hardened fur": {
            "DESCRIPTION": "__Defense Boost:__ Requires 2 rounds to charge, gain `25` / `35` / `45` Defense.",
            "COST": 5000,
            "EMOJI": " "
        },
        "paralyzing bite": {
            "DESCRIPTION": "__Stall:__ Requires 3 rounds to charge, has a `60%` / `70%` / `80%` to Paralyze the enemy for 1 round.",
            "COST": 5000,
            "EMOJI": " "
        },
        "poisonous breath": {
            "DESCRIPTION": "__Damage Over Time:__ Requires 2 rounds to charge, remove `7%` / `10%` / `13%` of the enemy's total Health for 3 turns.",
            "COST": 5000,
            "EMOJI": " "
        },
        "regeneration": {
            "DESCRIPTION": "__Healing:__ Requires 3 rounds to charge, recover `15%` / `20%` / `25%` of your total Health.",
            "COST": 5000,
            "EMOJI": " "
        },
        "tooth and limb": {
            "DESCRIPTION": "__Sacrificial Damage:__ Requires 3 rounds to charge, remove `12%` / `16%` / `20%` of both players total Health.",
            "COST": 5000,
            "EMOJI": " "
        },
        "cheap shot": {
            "DESCRIPTION": "__Instant Damage:__ Requires 1 round to charge, deal `15%` / `20%` / `25%` of your total Attack to the enemy.",
            "COST": 5000,
            "EMOJI": " "
        },
        "last stand": {
            "DESCRIPTION": "__Universal Stat Boost:__ Triggers when player is under `20%` / `30%` / `40%` Health, gain 30 Defense, 30 Attack, 30 Speed.",
            "COST": 5000,
            "EMOJI": " "
        }
    },
    "Potions": {
        "bastets tear": {
            "DESCRIPTION": "Heal 20% of your total HP",
            "COST": 1,
            "EMOJI": " "
        },
        "iron fur potion": {
            "DESCRIPTION": "Gain 50 Defense",
            "COST": 1,
            "EMOJI": " "
        },
        "tigers tail brew": {
            "DESCRIPTION": "Gain 20% Critical Chance",
            "COST": 1,
            "EMOJI": " "
        },
        "griffins feather": {
            "DESCRIPTION": "Gain 30 Speed",
            "COST": 1,
            "EMOJI": " "
        },
        "blessing of the sphinx": {
            "DESCRIPTION": "Gain 10 Speed, Heal 10% of your total HP",
            "COST": 1,
            "EMOJI": " "
        },
        "golden broth": {
            "DESCRIPTION": "Gain 30 Attack, 10% Critical Chance",
            "COST": 1,
            "EMOJI": " "
        }
    },
    "Chests": {
        "green chest": {
            "COST": 750,
            "DROPRATES": "50% Common, 40% uncommon, 6% rare, 3% epic, 1% legendary",
            "EMOJI": "<:GreenChest:885289025009766461>"
        },
        "blue chest": {
            "COST": 1000,
            "DROPRATES": "40% common, 30% uncommon, 22% rare, 6% epic, 2% legendary",
            "EMOJI": "<:BlueChest:885289024661647371>"
        },
        "purple chest": {
            "COST": 2000,
            "DROPRATES": "20% common, 26% uncommon, 35% rare, 15% epic, 4% legendary",
            "EMOJI": "<:PurpleChest:885289024951058434>"
        },
        "red chest": {
            "COST": 4000,
            "DROPRATES": "15% common, 15% uncommon, 30% rare, 30% epic, 10% legendary ",
            "EMOJI": "<:RedChest:885289025617952818>"
        },
        "black chest": {
            "COST": 16000,
            "DROPRATES": "50% epic, 50% legendary",
            "EMOJI": "<:BlackChest:885289030235865169>"
        }
    },
    "Miscellaneous Items": {
        "name change ticket": {
            "COST": 500,
            "EMOJI": "",
            "DESCRIPTION": "One time use, changes the name of your cat"
        },
        "profile embed colour ticket": {
            "COST": 5000,
            "EMOJI": "",
            "DESCRIPTION": "One time use, changes the colour of your profile"
        },
        "item expansion slot": {
            "COST": 5000,
            "EMOJI": "",
            "DESCRIPTION": "One time use, increases the number of equip-able items to 7 (from 6). This ticket can only be used once per cat"
        },
        "can of tuna": {
            "COST": 750,
            "EMOJI": "",
            "DESCRIPTION": "Increases XP gained by 20% for the next 24 hours "
        },
        "canned cat food": {
            "COST": 500,
            "EMOJI": "",
            "DESCRIPTION": "Gain 50 XP instantly "
        },
        "salmon mash": {
            "COST": 1000,
            "EMOJI": "",
            "DESCRIPTION": "Gain 100 XP instantly"
        }
    }
}
# update this list later
battleItems = {
    "Common Item": {
        "wooden dagger": {
            "Attack": "+10",
            "Speed": "+5",
            "Crit Chance": "+1",
            "EMOJI": "<:WoodenDagger:884862670120054855>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846271783911434/WoodenDagger.png"
        },
        "wooden shield": {
            "Defense": "+30",
            "Speed": "-5",
            "EMOJI": "<:woodenshield:884862631335325766>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846299466326076/WoodenShield.png"
        },
        "novice sword": {
            "Attack": "+25",
            "Speed": "-5",
            "EMOJI": "<:novicesword:884862824415895622>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846165449920592/novicesword.png"
        },
        "fledgling staff": {
            "Attack": "+5",
            "Speed": "+10",
            "EMOJI": "<:FledglingStaff:884862911774879764>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846081828077658/FledglingStaff.png"
        },
        "pickaxe": {
            "Attack": "+25",
            "Crit Chance": "-10",
            "EMOJI": "<:Pickaxe:884862809656156181>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846175642083358/Pickaxe.png"
        },
        "battle scythe": {
            "Attack": "+30",
            "Speed": "-10",
            "EMOJI": "<:Battle_Scythe:884863015239954483>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884845975976423445/Battle_Scythe.png"
        },
        "heavy axe": {
            "Attack": "+1",
            "EMOJI": "<:HeavyAxe:884862861397069874>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846122957426778/HeavyAxe.png"
        },
        "wax candle": {
            "Speed": "+15",
            "EMOJI": "<:Wax_Candle:884862707147366431>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846247687626752/Wax_Candle.png"
        },
        "fledgling spellbook": {
            "Crit Chance": "+15",
            "EMOJI": "<:FledglingSpellbook:884862931399999498>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846065814212658/FledglingSpellbook.png"
        },
        "fledgling necklace": {
            "Health": "+30",
            "EMOJI": "<:Fledgling_Necklace:884862965176762408>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846031752286238/Fledgling_Necklace.png"
        },
        "fledgling hat": {
            "Defense": "+5",
            "Speed": "+10",
            "EMOJI": "<:FledglingHat:884862954032492565>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846047703236669/FledglingHat.png"
        },
        "chain-mail glove": {
            "Defense": "+15",
            "Attack": "+5",
            "EMOJI": "<:Chainmail_Glove:884862996864725053>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846015897808906/Chainmail_Glove.png"
        },
        "sealed diary": {
            "Health": "+15",
            "Attack": "-10",
            "Defense": "+15",
            "EMOJI": "<:Locked_Diary:884862839548948550>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846154301460500/Locked_Diary.png"
        },
        "bronze key": {
            "Attack": "-15",
            "Speed": "+20",
            "EMOJI": "<:Rusted_Key:884862790651756604>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846190150189066/Rusted_Key.png"
        },
        "wooden bow": {
            "Attack": "+15",
            "Crit Chance": "+5",
            "Defense": "-10",
            "EMOJI": "<:woodenbow:884862691062190181>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846257934303283/woodenbow.png",
        },
        "simple fishing rod": {
            "Attack": "+5",
            "Crit Chance": "+5",
            "EMOJI": "<:simplefishingrod:884862747563659305>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846219816497232/simplefishingrod.png"
        },
        "gray orb": {
            "Health": "+15",
            "Speed": "+5",
            "EMOJI": "<:Grey_Orb:884862871165628596>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846111033016330/Grey_Orb.png"
        },
        "gambler dice": {
            "Attack": "+5",
            "Defense": "+5",
            "Speed": "+5",
            "Crit Chance": "+5",
            "Health": "-15",
            "EMOJI": "<:Gambler_Dice:884862901649829968>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846094889152572/Gambler_Dice.png"
        },
        "strange mushroom": {
            "Health": "+35",
            "Crit Chance": "-10",
            "EMOJI": "<:Strange_Mushroom:884862724578902036>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846236904063076/Strange_Mushroom.png"
        },
        "wooden flute": {
            "Attack": "+10",
            "Speed": "+10",
            "EMOJI": "<:WoodenFlute:884862651249856533>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846284576538725/WoodenFlute.png"
        },
        "brown cake": {
            "Health": "+35",
            "Speed": "-5",
            "EMOJI": "<:Brown_Cake:884863007665061888>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884845993709953074/Brown_Cake.png"
        },
        "comfortable hoodie": {
            "Health": "+5",
            "Defense": "+15",
            "EMOJI": "<:Hoodie:884862852727455754>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846139894034452/Hoodie.png"
        },
        "sharp boomerang": {
            "Attack": "+10",
            "Speed": "+5",
            "Crit Chance": "+5",
            "Defense": "-10",
            "EMOJI": "<:SharpBoomerang:884862773161508985>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846204318515231/SharpBoomerang.png"
        }
    },
    "Uncommon Item": {
        "vitality ring": {
            "Health": "+45",
            "EMOJI": "<:VitalityRing:884868142487187456>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846631617450054/Vitality_Ring.png"
        },
        "apprentice helmet": {
            "Health": "+10",
            "Defense": "+20",
            "EMOJI": "<:ApprenticeHelmet:884868141061140490>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846481796923462/ApprenticeHelmet.png"
        },
        "apprentice rapier": {
            "Attack": "+40",
            "Speed": "-5",
            "EMOJI": "<:ApprenticeRapier:884868140750741515>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846487501156373/ApprenticeRapier.png"
        },
        "battle-hardened spear": {
            "Attack": "+30",
            "EMOJI": "<:BattleHardenedSpear:884868140926918716>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846513442918400/Battle-Hardened_Spear.png"
        },
        "gem staff": {
            "Defense": "+50",
            "Speed": "-10",
            "EMOJI": "<:GemStaff:884868140918538300>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846532719935538/Gem_Staff.png"
        },
        "iron shield": {
            "Defense": "+55",
            "Speed": "-10",
            "EMOJI": "<:IronShield:884868141073723412>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846550101147748/Iron_Shield.png"
        },
        "iron armor": {
            "Defense": "+45",
            "Speed": "-5",
            "EMOJI": "<:IronArmor:884868141090488330>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846558397489152/IronArmor.png"
        },
        "proficient spelltome": {
            "Crit Chance": "+20",
            "EMOJI": "<:ProficentSpelltome:884868141342146590>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846593537372232/ProficentSpelltome.png"
        },
        "forest bow": {
            "Attack": "+30",
            "Defense": "-10",
            "Crit Chance": "+5",
            "EMOJI": "<:ForestBow:884868140767510599>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846522888491048/ForestBow.png"
        },
        "large battleaxe": {
            "Attack": "+55",
            "Speed": "-15",
            "EMOJI": "<:LargeBattleaxe:884868140905947277>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846584507007047/Large_Battleaxe.png"
        },
        "steel dagger": {
            "Attack": "+15",
            "Speed": "+10",
            "Crit Chance": "+5",
            "DESCRIPTION": " ",
            "EMOJI": "<:SteelDagger:884868140855599173>",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846611375718431/SteelDagger.png"
        },
        "ship anchor": {
            "Health": "+40",
            "Defense": "+20",
            "Speed": "-15",
            "EMOJI": "<:Anchor:884868140897538088>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846469847339038/Anchor.png"
        },
        "speed talisman": {
            "Speed": "+30",
            "Defense": "-10",
            "EMOJI": "<:SpeedTalisman:884868141040164875>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846602903232572/SpeedTalisman.png"
        },
        "iron gauntlet": {
            "Attack": "+15",
            "Defense": "+20",
            "EMOJI": "<:IronGauntlet:884868141061136394>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846566656053298/IronGauntlet.png"
        },
        "sturdy fishing rod": {
            "Attack": "+25",
            "Crit Chance": "+10",
            "EMOJI": "<:sturdyfishingrod:884868141241491496>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846620267655168/sturdyfishingrod.png"
        },
        "jade gemsphere": {
            "Health": "+35",
            "Speed": "+5",
            "EMOJI": "<:JadeGemsphere:884868141316980776>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846575409569802/Jade_Gemsphere.png"
        },
        "artisan key": {
            "Attack": "-5",
            "Speed": "+25",
            "EMOJI": "<:ArtisanKey:884868140675256373>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846497160650812/ArtisanKey.png"
        },
        "helpful spirit":{
            "Health": "+40",
            "Attack": "+1",
            "EMOJI": "<:HelpfulSpirit:884868140968865822>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846541221797888/HelpfulSpirit.png"
        },
        "baneful amulet": {
            "Attack": "+10",
            "Speed": "+10",
            "Defense": "+10",
            "Crit Chance": "+5",
            "Health": "-25",
            "EMOJI": "<:BanefulAmulet:884868141010796634>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846504349687879/Baneful_Amulet.png"
        },
        "bugle of war": {
            "Attack": "+50",
            "Health": "-25",
            "EMOJI": "<:WarBugle:884868141631565894>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846639771189328/WarBugle.png"
        }
    },
    "Rare Item": {
        "magical gaze": {
            "Crit Chance": "+25",
            "EMOJI": "<:Magical_Gaze:884890035978137710>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873996640854076/Magical_Gaze.png"
        },
        "crystal dagger": {
            "Attack": "+20",
            "Speed": "+15",
            "Crit Chance": "+5",
            "EMOJI": "<:Crystal_Dagger:884889911604441140>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873794920013824/Crystal_Dagger.png"
        },
        "golden staff": {
            "Attack": "+20",
            "Speed": "+20",
            "EMOJI": "<:Gold_Staff:884889968743444530>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873880563511296/Gold_Staff.png"
        },
        "golden fishing rod": {
            "Attack": "+40",
            "Crit Chance": "+5",
            "EMOJI": "<:Golden_Fishingrod:884889983570284564>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873911584555018/Golden_Fishingrod.png"
        },
        "ocean trident": {
            "Attack": "+50",
            "EMOJI": "<:Ocean_Trident:884890059990511646>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884874008900796446/Ocean_Trident.png"
        },
        "gold fish": {
            "Health": "+65",
            "Attack": "-10",
            "EMOJI": "<:Goldfish:884890011370127391>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873954412625950/Goldfish.png"
        },
        "crystal blade": {
            "Health": "-10",
            "Attack": "+55",
            "EMOJI": "<:Crystal_Blade:884889904218259537>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873779958923284/Crystal_Blade.png"
        },
        "golden wing": {
            "Speed": "+40",
            "Defense": "-15",
            "EMOJI": "<:goldenwing:884889995641499668>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873933382369330/goldenwing.png"
        },
        "golden apple": {
            "Health": "+50",
            "Defense": "+30",
            "Speed": "-15",
            "EMOJI": "<:Golden_Apple:884889975953453147>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873897240043571/Golden_Apple.png"
        },
        "gilded shield": {
            "Defense": "+70",
            "Speed": "-20",
            "EMOJI": "<:GildedShield:884889926561304576>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873837177618452/GildedShield.png"
        },
        "gilded battleaxe": {
            "Attack": "+65",
            "Speed": "-20",
            "EMOJI": "<:Gilded_Battleaxe:884889919175135262>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873809189023784/Gilded_Battleaxe.png"
        },
        "gold order": {
            "Attack": "+15",
            "Speed": "+10",
            "Crit Chance": "+10",
            "Defense": "+10",
            "Health": "-30",
            "EMOJI": "<:Gold_Order:884889961046896741>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873869888991262/Gold_Order.png"
        },
        "toy tiger": {
            "Speed": "+20",
            "Attack": "+15",
            "EMOJI": "<:ToyTiger:884890074859335691>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884874035069063268/ToyTiger.png"
        },
        "gold key": {
            "Health": "+50",
            "Speed": "+5",
            "Defense": "+5",
            "EMOJI": "<:Gold_Key:884889951764889632>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873860405674055/Gold_Key.png"
        },
        "veteran helmet": {
            "Defense": "+25",
            "Health": "+25",
            "Speed": "-5",
            "EMOJI": "<:Veteran_Helmet:884890084837564466>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884874046720860160/Veteran_Helmet.png"
        },
        "golden bow": {
            "Attack": "+35",
            "Crit Chance": "+10",
            "Defense": "-10",
            "EMOJI": "<:Gold_Bow:884889942189310022>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884879904510980146/Gold_Bow.png"
        },
        "glove of nature": {
            "Defense": "+30",
            "Attack": "+25",
            "EMOJI": "<:GloveofNature:884889934287241247>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873849018130452/GloveofNature.png"
        },
        "golden armor": {
            "Defense": "+55",
            "EMOJI": "<:GoldArmor:884921488682143765>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884921468138434610/Gold_Armor.png"
        }
    },
    "Epic Item": {
        "magical wonder": {
            "Crit Chance": "+35",
            "EMOJI": "<:magicalwonder:884938177524166676>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884938206674575390/magicalwonder.png"
        },
        "dagger of frost": {
            "Attack": "+30",
            "Speed": "+15",
            "Crit Chance": "+10",
            "EMOJI": "<:daggeroffrost:884937633808130088>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916193587253268/daggeroffrost.png"
        },
        "diamond fishing rod": {
            "Attack": "+65",   
            "Crit Chance": "+5",
            "EMOJI": "<:Diamondfishingrod:884937633782968380>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916259802738728/Diamondfishingrod.png"
        },
        "metallic spirit": {
            "Health": "+50",
            "Defense": "+40",
            "Speed": "-10",
            "EMOJI": "<a:MettalicSpirit:884937634781204532>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916382565826610/MetallicSpirit.gif"
        },
        "shining light": {
            "Attack": "+60",
            "Speed": "+20",
            "Defense": "-30",
            "EMOJI": "<:ShiningLight:884937633892032583>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916395677188156/ShiningLight.png"
        },
        "engulfing dark": {
            "Health": "-10",
            "Attack": "+90",
            "Speed": "-10",
            "EMOJI": "<:EngulfingDark:884937633539690567>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916280233177118/EngulfingDark.png"
        },
        "crimson bow": {
            "Attack": "+55",
            "Crit Chance": "+15",
            "Defense": "-10",
            "EMOJI": "<:CrimsonBow:884937633556467722>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916123345256478/CrimsonBow.png"
        },
        "blazing spirit": {
            "Attack": "+40",
            "Health": "+40",
            "Defense": "-10",
            "EMOJI": "<a:BurningSpirit:884937633598414919>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916107176210452/BurningSpirit.gif"
        },
        "crimson shield": {
            "Defense": "+90",
            "Speed": "-20",
            "EMOJI": "<:CrimsonShield:884937633145425971>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916155217747978/CrimsonShield.png"
        },
        "crimson spirit": {
            "Attack": "+30",
            "Speed": "+25",
            "EMOJI": "<:CrimsonSpirit:884937633619411055>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916172762533948/CrimsonSpirit.png"
        },
        "glove of frost": {
            "Health": "-10",
            "Attack": "+25",
            "Defense": "+45",
            "EMOJI": "<:GloveofFrost:884937633950744646>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916293688524860/GloveofFrost.png"
        },
        "toy dragon": {
            "Health": "+50",
            "Attack": "+20",
            "EMOJI": "<:ToyDragon:884937633929785465>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916406838243408/ToyDragon.png"
        },
        "crimson cry": {
            "Speed": "+30",
            "Health": "+20",
            "EMOJI": "<:CrimsonCry:884937633569058866>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916139002585118/CrimsonCry.png"
        },
        "dark crystal": {
            "Health": "+80",
            "Speed": "-10",
            "Defense": "+5",
            "EMOJI": "<:DarkCrystal:884937633774596156>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916217155055656/DarkCrystal.png"
        },
        "light crystal": {
            "Crit Chance": "+15",
            "Speed": "+20",
            "EMOJI": "<a:lightcrystal:884937636979044392>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916360130482247/MagicalGem.gif"
        },
        "daruma doll": {
            "Attack": "+15",
            "Crit Chance": "+15",
            "Speed": "+15",
            "EMOJI": "<:DarumaDoll:884937633925562428>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916237539352637/DarumaDoll.png"
        },
        "ancient helmet": {
            "Defense": "+35",
            "Health": "+35",
            "Speed": "-5",
            "EMOJI": "<:AncientHelmet:884937632935727125>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916069083545650/AncientHelmet.png"
        },
        "bloodstone": {
            "Attack": "+20",
            "Speed": "+20",
            "Defense": "+20",
            "Health": "-20",
            "EMOJI": "<:Bloodstone:884937633111879691>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916086477307904/Bloodstone.png"
        }
    },
    "Legendary Item": {
        "kitsune mask": {
            "Health": "+100",
            "EMOJI": "<a:KitsuneMask:885003177928319066>",
            "DESCRIPTIONS": " ",
            "URL": "https://cdn.discordapp.com/attachments/882806989539905616/885001739558875176/KitsuneMask.gif"
        }
    },
}



items = {
    "Common Item": {
        "wooden dagger": {
            "Attack": "+10",
            "Speed": "+5",
            "Crit Chance": "+1",
            "EMOJI": "<:WoodenDagger:884862670120054855>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846271783911434/WoodenDagger.png"
        },
        "wooden shield": {
            "Defense": "+30",
            "Speed": "-5",
            "EMOJI": "<:woodenshield:884862631335325766>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846299466326076/WoodenShield.png"
        },
        "novice sword": {
            "Attack": "+25",
            "Speed": "-5",
            "EMOJI": "<:novicesword:884862824415895622>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846165449920592/novicesword.png"
        },
        "fledgling staff": {
            "Attack": "+5",
            "Speed": "+10",
            "EMOJI": "<:FledglingStaff:884862911774879764>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846081828077658/FledglingStaff.png"
        },
        "pickaxe": {
            "Attack": "+25",
            "Crit Chance": "-10",
            "EMOJI": "<:Pickaxe:884862809656156181>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846175642083358/Pickaxe.png"
        },
        "battle scythe": {
            "Attack": "+30",
            "Speed": "-10",
            "EMOJI": "<:Battle_Scythe:884863015239954483>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884845975976423445/Battle_Scythe.png"
        },
        "heavy axe": {
            "Attack": "+1",
            "EMOJI": "<:HeavyAxe:884862861397069874>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846122957426778/HeavyAxe.png"
        },
        "wax candle": {
            "Speed": "+15",
            "EMOJI": "<:Wax_Candle:884862707147366431>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846247687626752/Wax_Candle.png"
        },
        "fledgling spellbook": {
            "Crit Chance": "+15",
            "EMOJI": "<:FledglingSpellbook:884862931399999498>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846065814212658/FledglingSpellbook.png"
        },
        "fledgling necklace": {
            "Health": "+30",
            "EMOJI": "<:Fledgling_Necklace:884862965176762408>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846031752286238/Fledgling_Necklace.png"
        },
        "fledgling hat": {
            "Defense": "+5",
            "Speed": "+10",
            "EMOJI": "<:FledglingHat:884862954032492565>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846047703236669/FledglingHat.png"
        },
        "chain-mail glove": {
            "Defense": "+15",
            "Attack": "+5",
            "EMOJI": "<:Chainmail_Glove:884862996864725053>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846015897808906/Chainmail_Glove.png"
        },
        "sealed diary": {
            "Health": "+15",
            "Attack": "-10",
            "Defense": "+15",
            "EMOJI": "<:Locked_Diary:884862839548948550>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846154301460500/Locked_Diary.png"
        },
        "bronze key": {
            "Attack": "-15",
            "Speed": "+20",
            "EMOJI": "<:Rusted_Key:884862790651756604>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846190150189066/Rusted_Key.png"
        },
        "wooden bow": {
            "Attack": "+15",
            "Crit Chance": "+5",
            "Defense": "-10",
            "EMOJI": "<:woodenbow:884862691062190181>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846257934303283/woodenbow.png",
        },
        "simple fishing rod": {
            "Attack": "+5",
            "Crit Chance": "+5",
            "EMOJI": "<:simplefishingrod:884862747563659305>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846219816497232/simplefishingrod.png"
        },
        "gray orb": {
            "Health": "+15",
            "Speed": "+5",
            "EMOJI": "<:Grey_Orb:884862871165628596>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846111033016330/Grey_Orb.png"
        },
        "gambler dice": {
            "Attack": "+5",
            "Defense": "+5",
            "Speed": "+5",
            "Crit Chance": "+5",
            "Health": "-15",
            "EMOJI": "<:Gambler_Dice:884862901649829968>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846094889152572/Gambler_Dice.png"
        },
        "strange mushroom": {
            "Health": "+35",
            "Crit Chance": "-10",
            "EMOJI": "<:Strange_Mushroom:884862724578902036>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846236904063076/Strange_Mushroom.png"
        },
        "wooden flute": {
            "Attack": "+10",
            "Speed": "+10",
            "EMOJI": "<:WoodenFlute:884862651249856533>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846284576538725/WoodenFlute.png"
        },
        "brown cake": {
            "Health": "+35",
            "Speed": "-5",
            "EMOJI": "<:Brown_Cake:884863007665061888>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884845993709953074/Brown_Cake.png"
        },
        "comfortable hoodie": {
            "Health": "+5",
            "Defense": "+15",
            "EMOJI": "<:Hoodie:884862852727455754>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846139894034452/Hoodie.png"
        },
        "sharp boomerang": {
            "Attack": "+10",
            "Speed": "+5",
            "Crit Chance": "+5",
            "Defense": "-10",
            "EMOJI": "<:SharpBoomerang:884862773161508985>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219160375214090/884846204318515231/SharpBoomerang.png"
        }
    },
    "Uncommon Item": {
        "vitality ring": {
            "Health": "+45",
            "EMOJI": "<:VitalityRing:884868142487187456>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846631617450054/Vitality_Ring.png"
        },
        "apprentice helmet": {
            "Health": "+10",
            "Defense": "+20",
            "EMOJI": "<:ApprenticeHelmet:884868141061140490>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846481796923462/ApprenticeHelmet.png"
        },
        "apprentice rapier": {
            "Attack": "+40",
            "Speed": "-5",
            "EMOJI": "<:ApprenticeRapier:884868140750741515>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846487501156373/ApprenticeRapier.png"
        },
        "battle-hardened spear": {
            "Attack": "+30",
            "EMOJI": "<:BattleHardenedSpear:884868140926918716>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846513442918400/Battle-Hardened_Spear.png"
        },
        "gem staff": {
            "Defense": "+50",
            "Speed": "-10",
            "EMOJI": "<:GemStaff:884868140918538300>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846532719935538/Gem_Staff.png"
        },
        "iron shield": {
            "Defense": "+55",
            "Speed": "-10",
            "EMOJI": "<:IronShield:884868141073723412>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846550101147748/Iron_Shield.png"
        },
        "iron armor": {
            "Defense": "+45",
            "Speed": "-5",
            "EMOJI": "<:IronArmor:884868141090488330>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846558397489152/IronArmor.png"
        },
        "proficient spelltome": {
            "Crit Chance": "+20",
            "EMOJI": "<:ProficentSpelltome:884868141342146590>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846593537372232/ProficentSpelltome.png"
        },
        "forest bow": {
            "Attack": "+30",
            "Defense": "-10",
            "Crit Chance": "+5",
            "EMOJI": "<:ForestBow:884868140767510599>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846522888491048/ForestBow.png"
        },
        "large battleaxe": {
            "Attack": "+55",
            "Speed": "-15",
            "EMOJI": "<:LargeBattleaxe:884868140905947277>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846584507007047/Large_Battleaxe.png"
        },
        "steel dagger": {
            "Attack": "+15",
            "Speed": "+10",
            "Crit Chance": "+5",
            "EMOJI": "<:SteelDagger:884868140855599173>",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846611375718431/SteelDagger.png"
        },
        "ship anchor": {
            "Health": "+40",
            "Defense": "+20",
            "Speed": "-15",
            "EMOJI": "<:Anchor:884868140897538088>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846469847339038/Anchor.png"
        },
        "speed talisman": {
            "Speed": "+30",
            "Defense": "-10",
            "EMOJI": "<:SpeedTalisman:884868141040164875>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846602903232572/SpeedTalisman.png"
        },
        "iron gauntlet": {
            "Attack": "+15",
            "Defense": "+20",
            "EMOJI": "<:IronGauntlet:884868141061136394>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846566656053298/IronGauntlet.png"
        },
        "sturdy fishing rod": {
            "Attack": "+25",
            "Crit Chance": "+10",
            "EMOJI": "<:sturdyfishingrod:884868141241491496>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846620267655168/sturdyfishingrod.png"
        },
        "jade gemsphere": {
            "Health": "+35",
            "Speed": "+5",
            "EMOJI": "<:JadeGemsphere:884868141316980776>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846575409569802/Jade_Gemsphere.png"
        },
        "artisan key": {
            "Attack": "-5",
            "Speed": "+25",
            "EMOJI": "<:ArtisanKey:884868140675256373>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846497160650812/ArtisanKey.png"
        },
        "helpful spirit":{
            "Health": "+40",
            "Attack": "+1",
            "EMOJI": "<:HelpfulSpirit:884868140968865822>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846541221797888/HelpfulSpirit.png"
        },
        "baneful amulet": {
            "Attack": "+10",
            "Speed": "+10",
            "Defense": "+10",
            "Crit Chance": "+5",
            "Health": "-25",
            "EMOJI": "<:BanefulAmulet:884868141010796634>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846504349687879/Baneful_Amulet.png"
        },
        "bugle of war": {
            "Attack": "+50",
            "Health": "-25",
            "EMOJI": "<:WarBugle:884868141631565894>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219178058403861/884846639771189328/WarBugle.png"
        }
    },
    "Rare Item": {
        "magical gaze": {
            "Crit Chance": "+25",
            "EMOJI": "<:Magical_Gaze:884890035978137710>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873996640854076/Magical_Gaze.png"
        },
        "crystal dagger": {
            "Attack": "+20",
            "Speed": "+15",
            "Crit Chance": "+5",
            "EMOJI": "<:Crystal_Dagger:884889911604441140>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873794920013824/Crystal_Dagger.png"
        },
        "golden staff": {
            "Attack": "+20",
            "Speed": "+20",
            "EMOJI": "<:Gold_Staff:884889968743444530>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873880563511296/Gold_Staff.png"
        },
        "golden fishing rod": {
            "Attack": "+40",
            "Crit Chance": "+5",
            "EMOJI": "<:Golden_Fishingrod:884889983570284564>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873911584555018/Golden_Fishingrod.png"
        },
        "ocean trident": {
            "Attack": "+50",
            "EMOJI": "<:Ocean_Trident:884890059990511646>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884874008900796446/Ocean_Trident.png"
        },
        "gold fish": {
            "Health": "+65",
            "Attack": "-10",
            "EMOJI": "<:Goldfish:884890011370127391>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873954412625950/Goldfish.png"
        },
        "crystal blade": {
            "Health": "-10",
            "Attack": "+55",
            "EMOJI": "<:Crystal_Blade:884889904218259537>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873779958923284/Crystal_Blade.png"
        },
        "golden wing": {
            "Speed": "+40",
            "Defense": "-15",
            "EMOJI": "<:goldenwing:884889995641499668>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873933382369330/goldenwing.png"
        },
        "golden apple": {
            "Health": "+50",
            "Defense": "+30",
            "Speed": "-15",
            "EMOJI": "<:Golden_Apple:884889975953453147>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873897240043571/Golden_Apple.png"
        },
        "gilded shield": {
            "Defense": "+70",
            "Speed": "-20",
            "EMOJI": "<:GildedShield:884889926561304576>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873837177618452/GildedShield.png"
        },
        "gilded battleaxe": {
            "Attack": "+65",
            "Speed": "-20",
            "EMOJI": "<:Gilded_Battleaxe:884889919175135262>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873809189023784/Gilded_Battleaxe.png"
        },
        "gold order": {
            "Attack": "+15",
            "Speed": "+10",
            "Crit Chance": "+10",
            "Defense": "+10",
            "Health": "-30",
            "EMOJI": "<:Gold_Order:884889961046896741>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873869888991262/Gold_Order.png"
        },
        "toy tiger": {
            "Speed": "+20",
            "Attack": "+15",
            "EMOJI": "<:ToyTiger:884890074859335691>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884874035069063268/ToyTiger.png"
        },
        "gold key": {
            "Health": "+50",
            "Speed": "+5",
            "Defense": "+5",
            "EMOJI": "<:Gold_Key:884889951764889632>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873860405674055/Gold_Key.png"
        },
        "veteran helmet": {
            "Defense": "+25",
            "Health": "+25",
            "Speed": "-5",
            "EMOJI": "<:Veteran_Helmet:884890084837564466>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884874046720860160/Veteran_Helmet.png"
        },
        "golden bow": {
            "Attack": "+35",
            "Crit Chance": "+10",
            "Defense": "-10",
            "EMOJI": "<:Gold_Bow:884889942189310022>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884879904510980146/Gold_Bow.png"
        },
        "glove of nature": {
            "Defense": "+30",
            "Attack": "+25",
            "EMOJI": "<:GloveofNature:884889934287241247>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884873849018130452/GloveofNature.png"
        },
        "golden armor": {
            "Defense": "+55",
            "EMOJI": "<:GoldArmor:884921488682143765>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219191702482984/884921468138434610/Gold_Armor.png"
        }
    },
    "Epic Item": {
        "magical wonder": {
            "Crit Chance": "+35",
            "EMOJI": "<:magicalwonder:884938177524166676>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884938206674575390/magicalwonder.png"
        },
        "dagger of frost": {
            "Attack": "+30",
            "Speed": "+15",
            "Crit Chance": "+10",
            "EMOJI": "<:daggeroffrost:884937633808130088>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916193587253268/daggeroffrost.png"
        },
        "diamond fishing rod": {
            "Attack": "+65",   
            "Crit Chance": "+5",
            "EMOJI": "<:Diamondfishingrod:884937633782968380>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916259802738728/Diamondfishingrod.png"
        },
        "metallic spirit": {
            "Health": "+50",
            "Defense": "+40",
            "Speed": "-10",
            "EMOJI": "<a:MettalicSpirit:884937634781204532>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916382565826610/MetallicSpirit.gif"
        },
        "shining light": {
            "Attack": "+60",
            "Speed": "+20",
            "Defense": "-30",
            "EMOJI": "<:ShiningLight:884937633892032583>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916395677188156/ShiningLight.png"
        },
        "engulfing dark": {
            "Health": "-10",
            "Attack": "+90",
            "Speed": "-10",
            "EMOJI": "<:EngulfingDark:884937633539690567>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916280233177118/EngulfingDark.png"
        },
        "crimson bow": {
            "Attack": "+55",
            "Crit Chance": "+15",
            "Defense": "-10",
            "EMOJI": "<:CrimsonBow:884937633556467722>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916123345256478/CrimsonBow.png"
        },
        "blazing spirit": {
            "Attack": "+40",
            "Health": "+40",
            "Defense": "-10",
            "EMOJI": "<a:BurningSpirit:884937633598414919>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916107176210452/BurningSpirit.gif"
        },
        "crimson shield": {
            "Defense": "+90",
            "Speed": "-20",
            "EMOJI": "<:CrimsonShield:884937633145425971>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916155217747978/CrimsonShield.png"
        },
        "crimson spirit": {
            "Attack": "+30",
            "Speed": "+25",
            "EMOJI": "<:CrimsonSpirit:884937633619411055>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916172762533948/CrimsonSpirit.png"
        },
        "glove of frost": {
            "Health": "-10",
            "Attack": "+25",
            "Defense": "+45",
            "EMOJI": "<:GloveofFrost:884937633950744646>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916293688524860/GloveofFrost.png"
        },
        "toy dragon": {
            "Health": "+50",
            "Attack": "+20",
            "EMOJI": "<:ToyDragon:884937633929785465>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916406838243408/ToyDragon.png"
        },
        "crimson cry": {
            "Speed": "+30",
            "Health": "+20",
            "EMOJI": "<:CrimsonCry:884937633569058866>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916139002585118/CrimsonCry.png"
        },
        "dark crystal": {
            "Health": "+80",
            "Speed": "-10",
            "Defense": "+5",
            "EMOJI": "<:DarkCrystal:884937633774596156>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916217155055656/DarkCrystal.png"
        },
        "light crystal": {
            "Crit Chance": "+15",
            "Speed": "+20",
            "EMOJI": "<a:lightcrystal:884937636979044392>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916360130482247/MagicalGem.gif"
        },
        "daruma doll": {
            "Attack": "+15",
            "Crit Chance": "+15",
            "Speed": "+15",
            "EMOJI": "<:DarumaDoll:884937633925562428>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916237539352637/DarumaDoll.png"
        },
        "ancient helmet": {
            "Defense": "+35",
            "Health": "+35",
            "Speed": "-5",
            "EMOJI": "<:AncientHelmet:884937632935727125>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916069083545650/AncientHelmet.png"
        },
        "bloodstone": {
            "Attack": "+20",
            "Speed": "+20",
            "Defense": "+20",
            "Health": "-20",
            "EMOJI": "<:Bloodstone:884937633111879691>",
            "DESCRIPTION": " ",
            "URL": "https://cdn.discordapp.com/attachments/884219204964868167/884916086477307904/Bloodstone.png"
        }
    },
    "Legendary Item": {
        "kitsune mask": {
            "Health": "+100",
            "EMOJI": "<a:KitsuneMask:885003177928319066>",
            "DESCRIPTIONS": " ",
            "URL": "https://cdn.discordapp.com/attachments/882806989539905616/885001739558875176/KitsuneMask.gif"
        }
    },
    "Traits": {
        "overdrive": {
            "DESCRIPTION": "__Speed Boost:__ 2 rounds to charge, gain `10` / `15` / `20` Speed.",
            "COST": 5000,
            "EMOJI": " "
        },
        "heightened awareness": {
            "DESCRIPTION": "__Evasion Boost:__ Requires 2 rounds to charge, gain `3` / `4` / `5` Evasion.",
            "COST": 5000,
            "EMOJI": " "
        },
        "voracity": {
            "DESCRIPTION": "__Attack Boost:__ Requires 2 rounds to charge, gain `20` / `30` / `40` Attack.",
            "COST": 5000,
            "EMOJI": " "
        },
        "innate bloodlust": {
            "DESCRIPTION": "__Critical Chance Boost:__ Requires 2 rounds to charge, gain `5` / `10` / `15` Critical Chance.",
            "COST": 5000,
            "EMOJI": " "
        },
        "hardened fur": {
            "DESCRIPTION": "__Defense Boost:__ Requires 2 rounds to charge, gain `25` / `35` / `45` Defense.",
            "COST": 5000,
            "EMOJI": " "
        },
        "paralyzing bite": {
            "DESCRIPTION": "__Stall:__ Requires 3 rounds to charge, has a `60%` / `70%` / `80%` to Paralyze the enemy for 1 round.",
            "COST": 5000,
            "EMOJI": " "
        },
        "poisonous breath": {
            "DESCRIPTION": "__Damage Over Time:__ Requires 2 rounds to charge, remove `7%` / `10%` / `13%` of the enemy's total Health for 3 turns.",
            "COST": 5000,
            "EMOJI": " "
        },
        "regeneration": {
            "DESCRIPTION": "__Healing:__ Requires 3 rounds to charge, recover `15%` / `20%` / `25%` of your total Health.",
            "COST": 5000,
            "EMOJI": " "
        },
        "tooth and limb": {
            "DESCRIPTION": "__Sacrificial Damage:__ Requires 3 rounds to charge, remove `12%` / `16%` / `20%` of both players total Health.",
            "COST": 5000,
            "EMOJI": " "
        },
        "cheap shot": {
            "DESCRIPTION": "__Instant Damage:__ Requires 1 round to charge, deal `15%` / `20%` / `25%` of your total Attack to the enemy.",
            "COST": 5000,
            "EMOJI": " "
        },
        "last stand": {
            "DESCRIPTION": "__Universal Stat Boost:__ Triggers when player is under `20%` / `30%` / `40%` Health, gain 30 Defense, 30 Attack, 30 Speed.",
            "COST": 5000,
            "EMOJI": " "
        }
    },
    "Potions": {
        "bastets tear": {
            "DESCRIPTION": "Heal 20% of your total HP",
            "COST": 1,
            "EMOJI": " "
        },
        "iron fur potion": {
            "DESCRIPTION": "Gain 50 Defense",
            "COST": 1,
            "EMOJI": " "
        },
        "tigers tail brew": {
            "DESCRIPTION": "Gain 20% Critical Chance",
            "COST": 1,
            "EMOJI": " "
        },
        "griffins feather": {
            "DESCRIPTION": "Gain 30 Speed",
            "COST": 1,
            "EMOJI": " "
        },
        "blessing of the sphinx": {
            "DESCRIPTION": "Gain 10 Speed, Heal 10% of your total HP",
            "COST": 1,
            "EMOJI": " "
        },
        "golden broth": {
            "DESCRIPTION": "Gain 30 Attack, 10% Critical Chance",
            "COST": 1,
            "EMOJI": " "
        }
    },
    "Chests": {
        "green chest": {
            "COST": 750,
            "DROPRATES": "50% Common, 40% uncommon, 6% rare, 3% epic, 1% legendary",
            "EMOJI": "<:GreenChest:885289025009766461>"
        },
        "blue chest": {
            "COST": 1000,
            "DROPRATES": "40% common, 30% uncommon, 22% rare, 6% epic, 2% legendary",
            "EMOJI": "<:BlueChest:885289024661647371>"
        },
        "purple chest": {
            "COST": 2000,
            "DROPRATES": "20% common, 26% uncommon, 35% rare, 15% epic, 4% legendary",
            "EMOJI": "<:PurpleChest:885289024951058434>"
        },
        "red chest": {
            "COST": 4000,
            "DROPRATES": "15% common, 15% uncommon, 30% rare, 30% epic, 10% legendary ",
            "EMOJI": "<:RedChest:885289025617952818>"
        },
        "black chest": {
            "COST": 16000,
            "DROPRATES": "50% epic, 50% legendary",
            "EMOJI": "<:BlackChest:885289030235865169>"
        }
    },
    "Miscellaneous Items": {
        "name change ticket": {
            "COST": 500,
            "EMOJI": "",
            "DESCRIPTION": "One time use, changes the name of your cat"
        },
        "profile embed colour ticket": {
            "COST": 5000,
            "EMOJI": "",
            "DESCRIPTION": "One time use, changes the colour of your profile"
        },
        "item expansion slot": {
            "COST": 5000,
            "EMOJI": "",
            "DESCRIPTION": "One time use, increases the number of equip-able items to 7 (from 6). This ticket can only be used once per cat"
        },
        "can of tuna": {
            "COST": 750,
            "EMOJI": "",
            "DESCRIPTION": "Increases XP gained by 20% for the next 24 hours "
        },
        "canned cat food": {
            "COST": 500,
            "EMOJI": "",
            "DESCRIPTION": "Gain 50 XP instantly "
        },
        "salmon mash": {
            "COST": 1000,
            "EMOJI": "",
            "DESCRIPTION": "Gain 100 XP instantly"
        }
    }
}
