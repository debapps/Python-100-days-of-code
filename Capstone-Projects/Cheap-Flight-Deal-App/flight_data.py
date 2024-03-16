class FlightData:
    # This class is responsible for structuring the flight data.
    
    def __init__(self, price, origin_city, origin_city_code, destination_city, destination_city_code, outbound_date, inbound_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_city_code = origin_city_code
        self.destination_city = destination_city
        self.destination_city_code = destination_city_code
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date

    def get_price(self):
        return self.price
    
    def get_org_city(self):
        return self.origin_city
    
    def get_org_code(self):
        return self.origin_city_code
    
    def get_dest_city(self):
        return self.destination_city
    
    def get_dest_code(self):
        return self.destination_city_code
    
    def get_out_date(self):
        return self.outbound_date

    def get_in_date(self):
        return self.inbound_date


    

