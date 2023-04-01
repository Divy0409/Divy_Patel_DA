vehicle = {'2 wheeler': {'gear': 1.18, 'non-gear': 1.21},
           '4 wheeler': {'gear': 1.28, 'non-gear': 1.32}}
Short_Listed_vehicles = {1: {'vehicle_id': 1001, 'vehicle': '2 wheeler', 'gear-type': 'gear', 'Showroom price': 70000, 'On-road price': 96000},
                         2: {'vehicle_id': 1002, 'vehicle': '4 wheeler', 'gear-type': 'non-gear', 'Showroom price': 50000, 'On-road price': 66000}}


class on_road_price:
    def Cal_Price(self, Showroom_Price, Wheeler_Type, Gear_Type):
        A_P = (vehicle[Wheeler_Type][Gear_Type]*Showroom_Price)
        return A_P


menu = """
    Press 1 for calculating costs.
    Press 2 for checking previously calculated vehicle costs.
    Press 3 for exit.

"""

status = True
P_status = True
while(status):
    print(menu)
    choice = int(input("Enter your choice: "))
    if choice == 1:

        menu_102 = """
                 Press a for 2 wheeler and b for 4 wheeler
        """
        print(menu_102)
        choice_102 = input("Enter your choice: ")

        menu_103 = """
                 Press a for gear and b for non-gear
        """
        print(menu_103)
        choice_103 = input("Enter your choice: ")

        while P_status:
            Listed_Vehicles = {}
            index = 1
            vehicle_id = 1001

            if choice_102 == 'a':
                Wheeler_Type = '2 wheeler'
            elif choice_102 == 'b':
                Wheeler_Type = '4 wheeler'

            if choice_103 == 'a':
                Gear_Type = 'gear'
            elif choice_103 == 'b':
                Gear_Type = 'non-gear'
            Showroom_Price = int(input("Enter showroom price of vehicle: "))

            A_Price = on_road_price()
            O_Price = A_Price.Cal_Price(
                Showroom_Price, Wheeler_Type, Gear_Type)
            print("On road price of vehicle: ", O_Price)

            for i in range(1, len(Short_Listed_vehicles)+1):
                Listed_Vehicles['vehicle_id'] = vehicle_id
                Listed_Vehicles['vehicle'] = Wheeler_Type
                Listed_Vehicles['gear-type'] = Gear_Type
                Listed_Vehicles['Showroom price'] = Showroom_Price
                Listed_Vehicles['On-road price'] = O_Price
                index += 1
                vehicle_id += 1

            Short_Listed_vehicles[index] = Listed_Vehicles
            print(Short_Listed_vehicles)

            choice_1 = input(
                "Do you want to calculate more vehicle costs(y/n): ")
            if choice_1 == 'n':
                P_status = False

    elif choice == 2:

        menu_101 = """
                 Press 1 for accessing listed vehicle using its Wheeler type
                 Press 2 for accessing listed vehicle using its Gear type
                 Press 3 for accessing listed vehicle using its Showroom price  
        
        """
        print(menu_101)
        choice_101 = int(input("Enter your choice: "))

        menu_102 = """
                 Press a for 2 wheeler and b for 4 wheeler
        """

        menu_103 = """
                 Press a for gear and b for non-gear
        """

        L_vehicles = {}

        if choice_101 == 1:
            print(menu_102)
            choice_102 = input("Enter your choice: ")
            if choice_102 == 'a':
                Wheeler_Type = '2 wheeler'
            elif choice_102 == 'b':
                Wheeler_Type = '4 wheeler'
            L_vehicles['vehicle'] = Wheeler_Type
            instance_found = 0
            for i in Short_Listed_vehicles.values():
                if i['vehicle'] == L_vehicles['vehicle']:
                    instance_found += 1
            instance_done = 0
            if instance_found == 0:
                print("No match found..")
            else:
                for i in range(1, len(Short_Listed_vehicles)+1):
                    if L_vehicles['vehicle'] == Short_Listed_vehicles[i]['vehicle']:
                        print(
                            f" On road price of vehicle no.{Short_Listed_vehicles[i]['vehicle_id']} {Short_Listed_vehicles[i]['vehicle']} {Short_Listed_vehicles[i]['gear-type']} vehicle prior to given details is  {Short_Listed_vehicles[i]['On-road price']} rs.")
                    instance_done += 1

                    if instance_done == instance_found:
                        break

        elif choice_101 == 2:
            print(menu_103)
            choice_103 = input("Enter your choice: ")
            if choice_103 == 'a':
                Gear_Type = 'gear'
            elif choice_103 == 'b':
                Gear_Type = 'non-gear'
            L_vehicles['gear-type'] = Gear_Type
            instance_found = 0
            for i in Short_Listed_vehicles.values():
                if i['gear-type'] == L_vehicles['gear-type']:
                    instance_found += 1
            instance_done = 0
            if instance_found == 0:
                print("No match found..")
            else:
                for i in range(1, len(Short_Listed_vehicles)+1):
                    if L_vehicles['gear-type'] == Short_Listed_vehicles[i]['gear-type']:
                        print(
                            f" On road price of vehicle no.{Short_Listed_vehicles[i]['vehicle_id']} {Short_Listed_vehicles[i]['vehicle']} {Short_Listed_vehicles[i]['gear-type']} vehicle prior to given details is  {Short_Listed_vehicles[i]['On-road price']} rs.")
                        instance_done += 1

                    if instance_done == instance_found:
                        break

        elif choice_101 == 3:
            Showroom_Price = int(input("Enter Showroom Price of vehicle: "))
            L_vehicles['Showroom price'] = Showroom_Price
            instance_found = 0
            for i in Short_Listed_vehicles.values():
                if i['Showroom price'] == L_vehicles['Showroom price']:
                    instance_found += 1
            instance_done = 0
            if instance_found == 0:
                print("No match found..")
            else:
                for i in range(1, len(Short_Listed_vehicles)+1):
                    if L_vehicles['Showroom price'] == Short_Listed_vehicles[i]['Showroom price']:
                        print(
                            f" On road price of vehicle no.{Short_Listed_vehicles[i]['vehicle_id']} {Short_Listed_vehicles[i]['vehicle']} {Short_Listed_vehicles[i]['gear-type']} vehicle prior to given details is  {Short_Listed_vehicles[i]['On-road price']} rs.")
                        instance_done += 1

                    if instance_done == instance_found:
                        break

    else:
        status = False
