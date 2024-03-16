from datetime import timedelta
from datetime import datetime


class Hotel():
    def __init__(self, name, address):
        self.hotel_name = name
        self.hotel_address = address

    def __str__(self):
        return "Hotel Name: " + self.hotel_name + " Address: " + str(self.hotel_address)


class Driver():
    def __init__(self, name, vehno):
        self.driver_name = name
        self.driver_number = vehno

    def set_driver_number(self, vehno):
        self.driver_number = vehno

    def __str__(self):
        return "Driver Name: " + self.driver_name + " Vehicle Number: " + str(self.driver_number)


class Booking(Hotel, Driver):
    def __init__(self, datetimeOfPickup, fromAirport, name, address, numPassengers):
        super().__init__(name, address)
        self.date = datetimeOfPickup
        self.Fromhotel = fromAirport
        self.hotel = Hotel
        self.numPassengers = numPassengers
        self.driver = Driver

    def datetimeOfPickup(self):
        date_string = datetime.strptime(self.date, "%d %b %Y %H:%M %p")
        datetimeOfPickup = date_string - timedelta(hours=1)
        return datetimeOfPickup

    def __str__(self):
        return "Date/Time: " + str(
            self.date) + self.Fromhotel + "\n" + "Hotel Name: " + self.hotel_name + " Address: " + str(
            self.hotel_address) + " Number of Pax: " + str(self.numPassengers)


class TransportServices():
    _hotels = [['Zenite', '1,Road']]
    _drivers = [['Alan', 'A11111']]
    _bookings = [['01 Jan 2019 11:45', 'To Airport', 'Zenite', '5', 'No']]

    def get_driver_name(self):
        return TransportServices._drivers

    def get_date(self):
        return TransportServices._bookings

    def get_hotel_name(self):
        return TransportServices._hotels

    def searchHotel(self, name):
        for sublist in TransportServices.get_hotel_name(self):
            if sublist[0] == name:
                obj2 = Hotel(sublist[0], sublist[1])
                print(obj2)
            else:
                print("No Hotel Found!")

    def searchDriver(self, name, vehicle_number):
        for sublist in TransportServices.get_driver_name(self):
            if sublist[0] == name or sublist[1] == vehicle_number:
                obj2 = Driver(sublist[0], sublist[1])
                print(obj2)
            else:
                print("No Driver Found!")

    def searchBooking(self, datetimeOfPickup, fromAirport, name):
        for sublist in TransportServices.get_date(self):
            if sublist[0] == datetimeOfPickup and sublist[1] == fromAirport and sublist[2] == name:
                for HotelList in TransportServices._hotels:
                    obj2 = Booking(sublist[0], sublist[1], HotelList[0], HotelList[1], sublist[3])
                    print(obj2)
                for DriverList in TransportServices._drivers:
                    if sublist[4] in DriverList:
                        print("Assigned: " + Driver(DriverList[0], DriverList[1]))
                        continue
                    else:
                        print("Assigned: " + sublist[4])
                        continue
            else:
                print("No Booking Found!")

    def hotelStr(self):
        obj1 = Hotel(sublist[0], sublist[1])
        print(obj1)

    def driverStr(self):
        obj1 = Driver(sublist[0], sublist[1])
        print(obj1)

    def bookingStr(self):
        for HotelList in TransportServices._hotels:
            obj1 = Booking(sublist[0], sublist[1], HotelList[0], HotelList[1], sublist[3])
            print(obj1)
        for DriverList in TransportServices._drivers:
            if sublist[4] in DriverList:
                print("Assigned: " + Driver(DriverList[0], DriverList[1]))
                continue
            else:
                print("Assigned: " + sublist[4])
                continue

    def addHotel(self):
        self.get_hotel_name().append(x1)

    def addDriver(self):
        self.get_driver_name().append(x2)

    def addBooking(self):
        self.get_date().append(x3)

    def removeDriver(self):
        self.get_driver_name().remove(x4)

    def removeBooking(self):
        self.get_date().remove(x5)

    def removeBookingwithDriver(self):
        self.get_date().remove(x6)

    def assignDriver(self):
        self.get_date().remove(x7)
        self.get_date().append(x9)


obj1 = TransportServices()

UserAns=True
while UserAns:
    print("""
                1. Search Hotel
                2. Search Driver
                3. Search Booking
                4. List Hotels
                5. List Drivers
                6. List Bookings
                7. Add Hotel
                8. Add Driver
                9. Add Booking
                10. Remove Driver
                11. Remove Booking
                12. Assign Driver to Booking
                """)
    UserAns=input('Enter choice: ')
    if UserAns=="1":
        UserHotel = input('Enter Hotel Name: ')
        obj1.searchHotel(UserHotel)
    if UserAns=="2":
        UserDriver = input('Enter Driver Name: ')
        UserDriverNumber = input('Enter Driver Vehicle Number: ')
        obj1.searchDriver(UserDriver,UserDriverNumber)
    if UserAns=="3":
        UserTime = input('Enter Pickup Date/Time (eg: 01 Jan 2019 11:45):' )
        UserFrom_To = input('Enter To Airport/Hotel: ')
        UserBookingHotel = input ('Enter Hotel Name: ')
        obj1.searchBooking(UserTime,UserFrom_To,UserBookingHotel)
    if UserAns=="4":
        for sublist in obj1.get_hotel_name():
            obj1.hotelStr()
    if UserAns=="5":
        for sublist in obj1.get_driver_name():
            obj1.driverStr()
    if UserAns=="6":
        for sublist in obj1.get_date():
            obj1.bookingStr()
    if UserAns=="7":
        addhotel = input ('Enter Hotel Name: ')
        addhoteladdress = input('Enter Hotel Address: ')
        x1=[addhotel,addhoteladdress]
        if x1 not in (obj1.get_hotel_name()):
            obj1.addHotel()
        else:
            print("Hotel Name Already Exist!")
            continue
    if UserAns=="8":
        add_driver = input('Enter Driver Name: ')
        add_driver_number = input('Enter Driver Vehicle Number: ')
        x2=[add_driver,add_driver_number]
        if x2 not in (obj1.get_driver_name()):
            obj1.addDriver()
        else:
            print("Driver Already Exist!")
            continue
    if UserAns=="9":
        add_date = input('Enter Pickup Date/Time (eg: 01 Jan 2019 11:45):')
        add_From_To = input('Enter To Airport/Hotel: ')
        add_bookinghotel = input('Enter Hotel Name: ')
        add_passenger = input ('Enter No. of Passenger: ')
        x3=[add_date,add_From_To,add_bookinghotel,add_passenger,'No']

        if x3 not in (obj1.get_date()):
            obj1.addBooking()
        else:
            print("Booking Already Exist!")
            continue
    if UserAns=="10":
        remove_driver = input('Enter Driver Name: ')
        remove_driver_number = input('Enter Driver Vehicle Number: ')
        x4=[remove_driver,remove_driver_number]
        if x4 in (obj1.get_driver_name()):
            obj1.removeDriver()
        else:
            print("Driver Does not Exist!")
            continue
    if UserAns=="11":
        remove_date = input('Enter Pickup Date/Time (eg: 01 Jan 2019 11:45):')
        remove_From_To = input('Enter To Airport/Hotel: ')
        remove_bookinghotel = input('Enter Hotel Name: ')
        remove_passenger = input('Enter No. of Passenger: ')
        remove_assigneddriver = input('Is Driver Assigned? Y/N: ')
        if remove_assigneddriver == 'N':
            x5=[remove_date,remove_From_To,remove_bookinghotel,remove_passenger,'No']
            if x5 in (obj1.get_date()):
                obj1.removeBooking()
            else:
                print ("Booking Does not Exist!")
                continue
        elif remove_assigneddriver == 'Y':
            remove_assigneddriver_Name = input('Enter Driver Name: ')
            remove_assigneddriver_Number = input('Enter Driver Number: ')
            x6= [remove_date,remove_From_To,remove_bookinghotel,remove_passenger,remove_assigneddriver_Name,remove_assigneddriver_Number]
            if x6 in (obj1.get_date()):
                obj1.removeBookingwithDriver()
            else:
                print("Booking Does not Exist!")
                continue
    if UserAns=="12":
        add_booking_date = input('Enter Pickup Date/Time (eg: 01 Jan 2019 11:45):')
        add_booking_From_To = input('Enter To Airport/Hotel: ')
        add_hotelname = input('Enter Hotel Name: ')
        add_bookingpassenger = input('Enter No. of Passenger: ')
        add_bookingDriver = input('Enter Driver Name: ')
        add_bookingDriverNumber = input('Enter Driver Number: ')
        x7 = [add_booking_date,add_booking_From_To,add_hotelname,add_bookingpassenger,'No']
        x8 = [add_bookingDriver,add_bookingDriverNumber]
        x9 = [add_booking_date,add_booking_From_To,add_hotelname,add_bookingpassenger,add_bookingDriver,add_bookingDriverNumber]
        if x7 in (obj1.get_date()) and x8 in (obj1.get_driver_name()):
            obj1.assignDriver()
        else:
            print ("Booking/Driver Does not Exist!")
            continue
