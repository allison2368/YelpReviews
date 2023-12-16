import folium

# Create a map.
m_LA = folium.Map(location=[34.075090, -118.252810], zoom_start=9)
m_SF = folium.Map(location=[37.79701, -122.399886], zoom_start=12)
m_LA_yelp = folium.Map(location=[34.075090, -118.252810], zoom_start=12)
# List of restaurant data
restaurants_LA = [
    {"name": "El Compadre", "location": [34.075090, -118.252810]},
    {"name": "Bubba Gump Shrimp Co.", "location": [34.138290, -118.359420]},
    {"name": "n/naka", "location": [34.025108, -118.412193]},
    {"name": "Raffaello Ristorante", "location": [33.740501, -118.287857]},
    {"name": "Providence", "location": [34.083649, -118.330200]},
    {"name": "Brent's Deli Northridge", "location": [34.2288696, -118.560294]},
    {"name": "Langer's", "location": [34.0561715, -118.2768127]},
    {"name": "Maccheroni Republic", "location": [34.0500863, -118.2484718]},
    {"name": "Café Gratitude Venice", "location": [33.9979925, -118.4734043]},
    {"name": "Angelini Osteria", "location": [34.0764233, -118.3491153]},
    {"name": "Sushi Gen", "location": [34.0466822, -118.238663]},
    {"name": "Pampas Grill", "location": [34.0717709, -118.3603109]},
    {"name": "Russell's", "location": [34.1464711, -118.1502487]},
    {"name": "The Luggage Room Pizzeria", "location": [34.1413522, -118.148518]},
    {"name": "Din Tai Fung", "location": [34.1454865, -118.2599065]},
    {"name": "Toast Bakery Cafe", "location": [34.072709, -118.3687647]},
    {"name": "Lemonade", "location": [33.989343, -118.4626508]},
    {"name": "Craft Los Angeles", "location": [34.0590401, -118.4146931]},
    {"name": "BOA Steakhouse", "location": [34.089796, -118.392704]},
    {"name": "Bea Bea's", "location": [34.1558966, -118.3462235]}
]
restaurants_SF = [
    {"name": "Mersea Restaurant & Bar", "location": [37.8225343, -122.3756693]},
    {"name": "Fogo de Chão Brazilian Steakhouse", "location": [37.7850502, -122.3998171]},
    {"name": "Luisa's Restaurant Wine Bar Since 1959", "location": [37.8016453, -122.4123444]},
    {"name": "L'ardoise Bistro", "location": [37.766587, -122.4331557]},
    {"name": "Seven Hills", "location": [37.798122, -122.41857]},
    {"name": "Blue Mermaid Restaurant", "location": [37.8075356, -122.4200793]},
    {"name": "Eight Am", "location": [37.806252, -122.419208]},
    {"name": "Lapisara Eatery", "location": [37.7875459, -122.4131381]},
    {"name": "Mo's Grill", "location": [37.7991868, -122.4071897]},
    {"name": "Kokkari Estiatorio", "location": [37.79701, -122.399886]},
    {"name": "Quince", "location": [37.7975151, -122.4032498]},
    {"name": "Piccolo Forno", "location": [37.8013592, -122.4119709]},
    {"name": "Surisan", "location": [37.8067912, -122.4175639]},
    {"name": "Anchor Oyster Bar", "location": [37.7596437, -122.4346403]},
    {"name": "Sweet Maple", "location": [37.7857147, -122.4351313]},
    {"name": "Fred's Coffee Shop", "location": [37.861799, -122.494681]},
    {"name": "Betty Lou's Seafood and Grill", "location": [37.7982667, -122.4069722]},
    {"name": "Fino Bar & Ristorante", "location": [37.787984, -122.412286]},
    {"name": "Frascati", "location": [37.79836, -122.419105]},
    {"name": "Za Pizza", "location": [37.7985461, -122.4191479]}
]
restaurants_LA_yelp = [
    {"name": "Republique", "location": [34.062963, -118.343390]},
    {"name": "L’Antica Pizzeria Da Michele", "location": [34.098415, -118.328194]},
    {"name": "GRANVILLE", "location": [34.078870, -118.370112]},
    {"name": "Running Goose", "location": [34.099440, -118.329137]},
    {"name": "Met Him At A Bar", "location": [34.057446, -118.344537]},
    {"name": "Ka’teen", "location": [34.101261, -118.338396]},
    {"name": "Bacari Silverlake", "location": [34.088170, -118.266123]},
    {"name": "Great White", "location": [34.077902, -118.323404]},
    {"name": "Beauty & Essex", "location": [34.099922, -118.329967]},
    {"name": "Mother Tongue", "location": [34.090394, -118.341245]},
    {"name": "Olivia", "location": [34.072066, -118.291726]},
    {"name": "Joseon", "location": [34.090823, -118.281648]},
    {"name": "Perch", "location": [34.051737, -118.251227]},
    {"name": "Jinsol Gukbap 8th", "location": [34.060102, -118.299229]},
    {"name": "OSTE", "location": [34.073152, -118.364752]},
    {"name": "The Front Yard", "location": [34.150893, -118.374671]},
    {"name": "Toca Madera - Los Angeles", "location": [34.073694, -118.373234]},
    {"name": "Bestia", "location": [34.033772, -118.229161]},
    {"name": "Morrison Atwater Village", "location": [34.113676, -118.261461]},
]
restaurants_SF_yelp = [
    {"name": "Savor", "location": [37.763651, -122.465630]},
    {"name": "Memento SF", "location": [37.751431, -122.436493]},
    {"name": "The Snug", "location": [37.792540, -122.434755]},
    {"name": "Bottega", "location": [37.753308, -122.420692]},
    {"name": "Pearl", "location": [37.784686, -122.482352]},
    {"name": "Yakitori Edomasa", "location": [37.786888, -122.430804]},
    {"name": "Marufuku Ramen", "location": [37.786620, -122.430647]},
    {"name": "The Tailor’s Son", "location": [37.789675, -122.434176]},
    {"name": "Dumpling Story", "location": [37.789704, -122.434051]},
    {"name": "Dumpling Home", "location": [37.774632, -122.422871]},
    {"name": "Lily", "location": [37.782778, -122.464571]},
    {"name": "Kothai Republic", "location": [37.765980, -122.466267]},
    {"name": "7 Adams", "location": [37.753308, -122.420692]},
    {"name": "Dalida", "location": [37.799708, -122.448219]},
    {"name": "Bistro Ember", "location": [37.751216, -122.429652]},
    {"name": "Barberio Osteria", "location": [37.762436, -122.421477]},
    {"name": "The Tailor’s Son", "location": [37.789675, -122.434176]},
    {"name": "Bansang", "location": [37.783155, -122.432621]},
    {"name": "Otra", "location": [37.771632, -122.432367]},
    {"name": "Noodle in a Haystack", "location": [37.780834, -122.472216]},
]

# Add markers for each restaurant
for restaurant in restaurants_SF_yelp:
    folium.Marker(
        location=restaurant["location"],
        tooltip="Click me!",
        popup=restaurant["name"],
        icon=folium.Icon(icon="cutlery"),
    ).add_to(m_SF)

# chante the the map name to saving file name
m_SF.save("restaurant_map_SF_yelp.html")
