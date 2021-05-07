from django.db.models import Max

from django.test import TestCase,Client
 
from .models import Airport, Flight, Passenger

# Create your tests here.
class FlightTestCase(TestCase):

    def setUp(self):

        #Create Airports
        a1 = Airport.objects.create(code= "AAA",city="City A")
        a2 = Airport.objects.create(code = "BBB", city= "City B")

        #Create Flights
        f1 = Flight.objects.create(origin=a1, destination= a2, duration= 200)
        f2 = Flight.objects.create(origin=a1, destination= a1, duration= 200)
        f3 = Flight.objects.create(origin=a1, destination= a2, duration= -200)

    def test_departure_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(),3)
    
    def tes_arrivals_count(self):
        a = Airport.objects.get(code= "AAA")
        self.assertEqual(a.arrivals.count(), 1)

    def test_valid_flight(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1,destination=a2,duration=200)
        self.assertTrue(f.is_valid_flight())
    
    def test_invalid_flight_destination(self):
        a1 = Airport.objects.get(code= "AAA")
        f = Flight.objects.get(origin=a1,destination=a1)
        self.assertFalse(f.is_valid_flight())
        
    def test_invalid_flight_duration(self):
        a1 = Airport.objects.get(code= "AAA")
        a2 = Airport.objects.get(code = "BBB")
        f = Flight.objects.get(origin=a1,destination=a2, duration= -200 )
        self.assertFalse(f.is_valid_flight())

    def test_index(self):
        c = Client()
        response = c.get("/hello/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["Flights"].count(), 3)
    
    def test_valid_flight_page(self):
        a1 = Airport.objects.get(code= "AAA")
        f = Flight.objects.get(origin=a1, destination= a1)

        c = Client()
        response = c.get(f"/hello/{f.id}")
        self.assertEqual(response.status_code, 200)

    # def test_invalid_flight_page(self):
    #     max_id = Flight.objects.all().aggregate(Max("id"))["id__max"]
        
    #     c = Client()
    #     response = c.get(f"/hello/{max_id + 1}")
    #     self.assertEqual(response.status_code, 404)

    def test_flight_page_passsengers(self):
        f = Flight.objects.get(pk=1)
        p = Passenger.objects.create(first="Habib", last= "Ur Rehman")
        f.passengers.add(p)

        c = Client()
        response = c.get(f"/hello/{f.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["passengers"].count(), 1)
        
    def test_flight_page_non_passsengers(self):
        f = Flight.objects.get(pk=1)
        p = Passenger.objects.create(first="Habib", last= "Ur Rehman")

        c = Client()
        response = c.get(f"/hello/{f.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["non_passengers"].count(), 1)
