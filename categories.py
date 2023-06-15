import json

categories = {
    "Augļi un dārzeņi" : {
        "Augļi un ogas" : {
            "Āboli un bumbieri" : [],
            "Banāni" : [],
            "Citrusaugļi" : [],
            "Eksotiskie augļi" : [],
            "Melones un arbūzi" : [],
            "Kauliņaugļi" : [],
            "Ogas" : []
        },
        "Dārzeņi un sēnes" : {
            "Ķirbji un kabačveidīgie" : [],
            "Bietes un citi sakņaugi" : [],
            "Gurķi un tomāti" : [],
            "Kartupeļi un burkāni" : [],
            "Pākšaugi, kukurūza un sparģeļi" : [],
            "Paprika un pipari" : [],
            "Pārstrādātie dārzeņi" : [],
            "Kāposti un salāti" : [],
            "Sīpoli, puravi un ķiploki" : [],
            "Garšaugi" : [],
            "Sēnes" : []
        }
    },
    "Vegāniem un veģetāriešiem" : {
        "Deserti" : [],
        "Siers" : [],
        "Krēms un majonēze" : [],
        "Sviesta alternatīvas" : [],
        "Augu dzērieni" : [],
        "Gaļas alternatīvas" : [],
        "Saldēti ēdieni" : [],
        "Sojas produkti" : []
    },
    "Gaļa, zivis un gatavā kulinārija" : {
        "Gatavā kulinārija" : {
            "Gaļas un zivju kulinārija" : [],
            "Pankūkas" : [],
            "Pastas un picas" : [],
            "Piedevas un mērces" : [],
            "Salāti" : [],
            "Sviestmaizes" : [],
            "Uzkodas, plates" : [],
            "Gatavas maltīes" : [],
            "Deserti" : []
        },
        "Svaiga gaļa" : {
            "Cūkgaļa" : [],
            "Liellopa un teļa gaļa" : [],
            "Svaigas gaļas subprodukti" : [],
            "Tītara un pīles gaļa" : [],
            "Vistas gaļa" : [],
            "Dažādu veidu maltā gaļa" : [],
            "Truša gaļa" : []
        },
        "Marinēta gaļa" : {
            "Mājputnu gaļa" : [],
            "Cūkgaļa" : [],
            "Liellopu gaļa" : []
        },
        "Pārstrādāta gaļa" : {
            "Auksti kūpinātā gaļa" : [],
            "Karsti kūpinātā gaļa" : [],
            "Vārīta un cepta gaļa" : [],
            "Vītinātās gaļas produkti" : []
        },
        "Desas un pastētes" : {
            "Auksti kūpinātās desas" : [],
            "Karsti kūpinātās desas" : [],
            "Vārītās desas" : [],
            "Pastēte, aknu desas" : []
        },
        "Cīsiņi, sardeles" : {
            "Cīsiņi un sardeles" : [],
            "Grila desiņas" : []
        },
        "Gaļas maltītes un uzkodas" : {
            "Galerti, gaļa želejā" : [],
            "Gaļas bumbiņas, nageti" : [],
            "Lēni pagatavotas gaļas maltītes" : [],
            "Uzkodas" : [],
            "RIMI kulinārija" : []
        },
        "Svaigās zivis un jūrasveltes" : {
            "Veselas zivis" : [],
            "Zivju filejas" : [],
            "Svaigās jūras veltes" : []
        },
        "Pārstrādātās zivis" : {
            "Auksti kūpinātas zivis" : [],
            "Karsti kūpinātas zivis" : [],
            "Krabju nūjiņas" : [],
            "Sālītas, marinētas zivis, zivis eļļā" : [],
            "Vītinātas zivis" : [],
            "Zivju un ikru pastētes" : [],
            "Zivju salāti un maltītes" : [],
            "Nēģi" : []
        },
        "Pārstrādāti jūras produkti un ikri" : {
            "Ikri" : [],
            "Jūras kāposti" : [],
            "Pārstrādātas jūras veltes" : []
        },
        "Zivju un gaļas konservi" : {
            "Citas konservētas zivis" : [],
            "Konservētas jūras veltes" : [],
            "Konservētas šprotes" : [],
            "Konservēts tuncis" : [],
            "Gaļas konservi" : []
        }
    },
    "Piena produkti un olas" : {
        "Jogurti un deserti" : [],
        "Piens" : [],
        "Kefīrs un skābpiena produkti" : [],
        "Krējums" : [],
        "Majonēze" : [],
        "Siers" : [],
        "Sviests un margarīns" : [],
        "Biezpiens" : [],
        "Olas" : [],
    },
    "Maize un konditoreja" : [],
    "Saldētie ēdieni" : {
        "Saldētie ēdieni un konditorejas izstrādājumi" : [],
        "Saldētas zivis un jūras veltes" : [],
        "Saldēti dārzeņi, augļi un sēnes" : [],
        "Saldējums un ledus" : []
    },
    "Iepakotā pārtika" : {
        "Speciālā pārtika un galetes" : [],
        "Sporta uzturs" : [],
        "Kafija un kakao" : [],
        "Tēja" : [],
        "Graudaugi un putraimi" : [],
        "Makaroni" : [],
        "Pākšaugi" : [],
        "Milti un miltu maisījumi" : [],
        "Graudaugu pārslas" : [],
        "Brokastu pārslas un musli" : [],
        "Konservēti produkti" : [],
        "Mērces, kečupi, sinepes, mārrutki" : [],
        "Eļļas un etiķi" : [],
        "Garšvielas" : [],
        "Saldās garšvielas" : [],
        "Pasaules virtuve" : [],
        "Ātri pagatavojami ēdieni": [],
    },
    "Saldumi un uzkodas" : [],
    "Dzērieni" : {
        "Sporta un funkcionālie dzērieni" : [],
        "Ūdens" : [],
        "Limonādes" : [],
        "Sulas un sulu dzērieni" : [],
        "Svaigas sulas un smūtīji" : [],
        "Sīrupi" : [],
        "Bezalkoholiskais alus, sidri un vīni" : [],
        "Dzirkstošie bezalkoholosiskie dzērieni" : [],
        "Enerģijas dzērieni" : []
    },
    "Alkoholiskie dzērieni" : [],
    "Skaistumkopšana un higiēnai" : [],
    "Zīdaiņiem un bērniem" : [],
    "Sadzīves ķīmija" : [],
    "Mājdzīvniekiem" : {
        "Barība" : [],
        "Smiltis un aksesuāri" : []
    },
    "Mājai, dārzam un atpūtai" : {
        "Sveces" : [],
        "Dārzam" : [],
        "Grilam" : [],
        "Preces mašīnai" : [],
        "Sadzīves tehnika un elektronika" : [],
        "Tavai mājai" : [],
        "Mājas tekstils" : [],
        "Vienreizējās lietošanas preces" : [],
        "Virtuvei" : [],
        "Aktīvai atpūtai" : [],
        "Preses izdevumi" : [],
        "Kancelejas preces" : [],
        "Ziedi" : [],
        "Suvenīri" : []
    },
    
    ### CUSTOM CATEGORIES ###
    "Vietējās izcelsmes pārtikas produkti" : [],
    "Augu izcelsmes produkti" : [],
    "Iepakojumi" : [],
    "Depozīts" : []
}
