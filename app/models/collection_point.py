class WasteCollectionLocation:
    def __init__(self, id, nome, endereco, lat, lng, tipo):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.lat = lat
        self.lng = lng
        self.tipo = tipo

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "endereco": self.endereco,
            "lat": self.lat,
            "lng": self.lng,
            "tipo": self.tipo
        }