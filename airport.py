class Airport:
    def __init__(self, code, name, city, country, lat, long, rate) -> None:
        self.code = code
        self.name = name
        self.city = city
        self.country = country
        self.lat = float(lat)
        self.lon = float(long)
        self.rate = float(rate)
    
    def __repr__(self) -> str:
        return f'Airport: {self.name}, In: {self.country}, Lat: {self.lat}, Long: {self.long}, Rate: {self.rate}'