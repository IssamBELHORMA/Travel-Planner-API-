ACTIVITIES_DB = {
    "paris": [
        "Visit the Eiffel Tower",
        "Explore the Louvre Museum",
        "Stroll along the Seine River"
    ],
    "london": [
        "Tour the British Museum",
        "Walk through Hyde Park",
        "See Buckingham Palace"
    ],
    "tokyo": [
        "Visit Senso-ji Temple",
        "Wander through Shibuya Crossing",
        "Try ramen in Omoide Yokocho"
    ],
    "new york": [
        "Walk through Central Park",
        "Visit the Statue of Liberty",
        "See a Broadway show"
    ],
    "rome": [
        "Explore the Colosseum",
        "Throw a coin in the Trevi Fountain",
        "Visit the Vatican Museums"
    ],
    "barcelona": [
        "Admire the Sagrada Familia",
        "Stroll down Las Ramblas",
        "Relax at Barceloneta Beach"
    ],
    "kyoto": [
        "Walk through Fushimi Inari Shrine",
        "Explore the Arashiyama Bamboo Grove",
        "Visit the Kinkaku-ji (Golden Pavilion)"
    ],
    "sydney": [
        "Take photos of the Sydney Opera House",
        "Walk from Bondi to Coogee coastal path",
        "Cross the Sydney Harbour Bridge"
    ],
    "cairo": [
        "Marvel at the Pyramids of Giza",
        "Explore the Grand Egyptian Museum",
        "Shop at Khan el-Khalili bazaar"
    ],
    "rio de janeiro": [
        "Visit the Christ the Redeemer statue",
        "Take the cable car up Sugarloaf Mountain",
        "Relax on Copacabana Beach"
    ],
    "amsterdam": [
        "Take a canal cruise",
        "Visit the Van Gogh Museum",
        "Explore the Rijksmuseum"
    ],
    "dubai": [
        "Go to the top of Burj Khalifa",
        "Shop at the Dubai Mall",
        "Experience a desert safari"
    ],
    "bangkok": [
        "Visit the Grand Palace",
        "Explore Wat Arun (Temple of Dawn)",
        "Shop at Chatuchak Weekend Market"
    ],
    "cape town": [
        "Hike or take the cableway up Table Mountain",
        "Visit Robben Island",
        "Drive along Chapman's Peak"
    ],
    "berlin": [
        "See the Berlin Wall at the East Side Gallery",
        "Walk through the Brandenburg Gate",
        "Visit the Museum Island"
    ],
    "toronto": [
        "Go up the CN Tower",
        "Take a ferry to the Toronto Islands",
        "Explore the Royal Ontario Museum"
    ],
    "singapore": [
        "Explore Gardens by the Bay",
        "Walk around Marina Bay Sands",
        "Visit the Singapore Botanic Gardens"
    ],
    "marrakesh": [
        "Wander through Jemaa el-Fnaa square",
        "Visit the Jardin Majorelle",
        "Explore the Bahia Palace"
    ],
    "san francisco": [
        "Walk or bike across the Golden Gate Bridge",
        "Take a boat tour to Alcatraz Island",
        "Ride the historic cable cars"
    ],
    "reykjavik": [
        "Relax in the Blue Lagoon",
        "See the Hallgrimskirkja church",
        "Take a Golden Circle day tour"
    ],
    "default": [
        "Visit the main historical museum",
        "Explore the city centre on foot",
        "Try a local food tour"
    ]
}

def get_activities(city: str) -> list:
    key = city.strip().lower()
    return ACTIVITIES_DB.get(key, ACTIVITIES_DB["default"])