class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f'distance: {self.distance}')
        print(f'rate per km: {self.rate_per_km}')
        print(f'total: {self.fare}')



def main():
    ride=TaxiRide(4)
    ride.calculate_fare(7)
    ride.print_receipt()

    print()

    ride2=TaxiRide(8)
    ride2.calculate_fare(10)
    ride2.print_receipt()

    

if __name__ == "__main__":
    main()