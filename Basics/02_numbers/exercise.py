# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
football_field_length = 92
football_field_width = 48.8
# 1. Calculate the area of a football field in square meters.
football_field_area = round(football_field_length * football_field_width, 2)
print("Football field area in square meters:", football_field_area)

#2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
chips_packet_price = 1.49
total_chips_packets = 9
total_chips_cost = chips_packet_price * total_chips_packets
money_given_to_shopkeeper = 20
money_received_back = money_given_to_shopkeeper - total_chips_cost
print("Money received back from shopkeeper:", money_received_back)

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
tile_length = 5.5
tile_area = tile_length ** 2
tile_cost_per_square = 500
total_cost_tiles_replacement = tile_area * tile_cost_per_square
print("Total cost of tiles replacement:", total_cost_tiles_replacement)

# 4. Print binary representation of number 17
print(format(17,'b')) # 4 bytes (or 32 bits), visual of binary presentation








