from .models import Movie, Onscreen


def create_data():
    movies = [
        {"name": "K.G.F. Chapter 2", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Runway 34", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Maa", "year": 2022, "pincode": [110001, 400001]},
        {
            "name": "Doctor Strange: In the Multiverse of Madness",
            "year": 2022,
            "pincode": [110001, 400001],
        },
        {"name": "RRR", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Heropanti 2", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Top Gun: Maverick", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Mere Desh Ki Dharti", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Jersey", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Ni Main Sass Kuttni", "year": 2022, "pincode": [110001, 400001]},
        {"name": "CBI 5: The Brain", "year": 2022, "pincode": [110001, 400001]},
        {
            "name": "Fantastic Beasts: The Secrets of Dambledore",
            "year": 2022,
            "pincode": [110001, 400001],
        },
        {"name": "Jana Gana Mana", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Sonic: The Hedgehog 2", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Thnking of Him", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Spider-Man: No Way Home", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Acharya", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Makal", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Sarkaru Vaari Paata", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Adrushya", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Don", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Jayeshbhai Jordaar", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Jo & Jo", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Meri Awas Suno", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Pathaam Valavu", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Ranga", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Saunkan Saunkne", "year": 2022, "pincode": [110001, 400001]},
        {"name": "X=Prem", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Bhool Bhulaiyaa 2", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Dhaakad", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Hit: The First Case", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Kokka", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Mrs Chatterjee Vs Norway", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Shekar", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Anek", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Bat Ji Kuttange", "year": 2022, "pincode": [110001, 400001]},
        {"name": "F3: Fun And Frustration", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Kuttavum  Shikshayum", "year": 2022, "pincode": [110001, 400001]},
        {"name": "The Conversion", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Thinking Of Him", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Memory", "year": 2022, "pincode": [110001, 400001]},
        {
            "name": "Kaathuvaakula Rendu Kaadhal",
            "year": 2022,
            "pincode": [110001, 400001],
        },
        {
            "name": "The Unbearable Weight Of Massive Talent",
            "year": 2022,
            "pincode": [110001, 400001],
        },
        {"name": "The Batman", "year": 2022, "pincode": [110001, 400001]},
        {"name": "Sooryavanshi", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Antim: The Final Truth", "year": 2021, "pincode": [110001, 400001]},
        {"name": "83", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Bell Bottom", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Chandigarh Kare Aashiqui", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Tadap", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Roohi", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Mumbai Saga", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Bunty Aur Babli 2", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Radhe", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Pushpa", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Waah Zindagi", "year": 2021, "pincode": [110001, 400001]},
        {
            "name": "Murder at Teesri Manzil 302",
            "year": 2021,
            "pincode": [110001, 400001],
        },
        {"name": "Atrangi Re", "year": 2021, "pincode": [110001, 400001]},
        {"name": "420 IPC", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Code Name Abdul", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Velle", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Bob Biswas", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Chhorii", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Satyameva Jayate 2", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Ye Mard Bechara", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Cash  ", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Dhamaka", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Squad", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Hum Do Hamare Do", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Dybbuk", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Bekhudi", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Aafat-E-Ishq", "year": 2021, "pincode": [110001, 400001]},
        {
            "name": "Shang-Chi and the Legend of the Ten Rings",
            "year": 2021,
            "pincode": [110001, 400001],
        },
        {
            "name": "Venom: Let There Be Carnage",
            "year": 2021,
            "pincode": [110001, 400001],
        },
        {"name": "Black Widow", "year": 2021, "pincode": [110001, 400001]},
        {"name": "F9", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Eternals", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Sing 2", "year": 2021, "pincode": [110001, 400001]},
        {"name": "No Time to Die", "year": 2021, "pincode": [110001, 400001]},
        {"name": "A Quiet Place Part II", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Ghostbusters: Afterlife", "year": 2021, "pincode": [110001, 400001]},
        {"name": "The White Tiger", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Locked Down", "year": 2021, "pincode": [110001, 400001]},
        {"name": "No Man's Land", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Nomadland", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Son of the South", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Minari", "year": 2021, "pincode": [110001, 400001]},
        {"name": "Flora & Ulysses", "year": 2021, "pincode": [110001, 400001]},
    ]
    return movies


def create_movie_entries():
    movies = create_data()
    for movie in movies:
        movie_instance = Movie.objects.create(
            name=movie.get("name"), year=movie.get("year")
        )
        if movie_instance:
            Onscreen.objects.bulk_create(
                [
                    Onscreen(movie=movie_instance, pincode=movie.get("pincode", [])[0]),
                    Onscreen(movie=movie_instance, pincode=movie.get("pincode", [])[1]),
                ]
            )
