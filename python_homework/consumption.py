
road_cons = int(input("Gépjármű országuti fogyasztása(/100):")) / 100
city_cons = int(input("Gépjármű városi fogyasztása(/100):")) / 100
road_km = int(input("Országúton megtett táv:"))
city_km = int(input("Városban megtett táv:"))
fuel = int(input("Benzin ára:"))

print(((road_cons) * (road_km)) + ((city_cons) * (city_km)))        # Mennyit fogyaszt az autód csak oda?
print((((road_cons) * (road_km)) + ((city_cons) * (city_km))) * 2)    # Oda-vissza









