from suncraft_parsing import list_groups_as_string

all_list = ['Toilet Accessories', 'Kitchen & Accessories', 'Tub Accessories', 'Various Items', 'Glass Vessels', 'Tub Spout', 'Glass Vessel Accessories', 'Bathroom Sink Accessories', 'Tools', 'Special', 'Shower Heads', 'Bathroom Sink Drains', 'Shower Accessories', 'Tub Drains', 'Overflow Faceplate', 'Grid Drain', 'Various Items', 'Kit', 'Hose', 'Facet Pull Out Sprayer', 'Push & Lock', 'Rinse Spray', 'Aerator', 'Shower Arm', 'Escutcheon', 'One Piece', 'Vessel Mount', 'Mount', 'Facet Washer', 'Faucet', 'Clicker Style', 'Tailpiece', 'Strainer Assembly', 'Parts', 'Lever', 'Filler', 'Washer', 'Diverter', 'Facet Washer Bibb Chest', 'Shower Supply Elbow', 'Flange', 'Wrench', 'Rain', 'Pop Up', 'Drop In', 'Vacuum breaker', 'Adjustable Spray', 'Flow Control', 'Pipe Cutter', 'Single Function', 'Lift and Turn', 'Hose Connection', 'Hand Held', 'Drinking faucet', '2.5 GPM', 'No Diverter', 'Massage', '1.75"D', '1/2" IPS', 'Three Piece', 'Cartridge Puller', 'Two Piece', '2 Holes', 'Telescoping Adjustable Feature', 'U Shape', 'Square', '59-80" hose', 'Stainless Steel', 'Slip Fit 5/8" OD', 'Spin and Seal', 'Copper Pipe', 'Rear Mount', 'Water Saving', 'Flush Mount', 'S Shape', 'nose mount', 'Bracket', 'Tapered', 'Grid Drain', 'Kit', '1 1/2" (Coarse Thread)', 'Duplex', 'Adjustable', 'Jr Duo', 'Pop Up Assembly', 'Sillcock Key', 'Button', 'Parts', '1.75 GPM', 'Clicker Stopper', '1.5 GPM', '2.2 GPM', 'Step', 'Spray Head', '8"', 'Nut Wrench', 'Nipple Extractor', '3/4" IPS', '2.0 GPM', 'Economy', 'PVC', 'Clog Resistant', 'Hose Guide', '1.2 GPM', 'Industrial', 'Hose Connection', 'Half & Half', 'No Overflow', 'Plastic', 'Stopper', '7"D', 'Deep Cup', 'Hook', 'Zinc', '1 1/4" (Fine Thread)', 'Wide', 'Socket Wrench', 'Convert', 'Plug Wrench', 'Dome', 'Basket', 'Pop Up', 'Adjustable Spray', 'De-burring Tool', 'Jet', 'Carded', 'Jewel Series', 'pliers', 'Front Diverter', 'Hose', '®Mixet Style 4', 'Round', 'Arm Mount', '1 hole', 'Flat', 'All Brass', 'Straight', 'Strap Wrench', 'Escutchon', '1-4-All Universal Fit', 'Beveled', 'Free Rotateing Connector Nut', 'Jaws', '4.5"D', 'Spud Chuck', 'L Shape', 'Swivel Connector', 'Flow Control', '10 Sizes', 'Faucet Seat', 'Single Function', '1.8 GPM', 'Basin Wrench', '6"D', 'Strainer Wrench', 'Rear Diverter', 'With Overflow', 'Wall Mount', '5 Function']
suncraft_database_file = "SClist_2023_08_08_02:42PM.json"

looking_for = all_list # Spelling and case sensitive at least at the moment, must be a list

type_of_group = "Categories" # Abrevations accepted "cat, sub, tag"



# List of catagories, subcategoreis, and tags
"""
Catagories:
-----------
Tools
Shower Accessories
Tub Spout
Bathroom Sink Drains
Shower Heads
Glass Vessel Accessories
Special
Kitchen & Accessories
Toilet Accessories
Various Items
Bathroom Sink Accessories
Tub Accessories
Tub Drains


Subcatagories:
--------------
Lever
Push & Lock
Adjustable Spray
Vacuum breaker
Diverter
Tailpiece
Filler
Pop Up
Pipe Cutter
Escutcheon
Lift and Turn
Various Items
Aerator
Rinse Spray
Flow Control
Facet Washer
Grid Drain
Flange
Overflow Faceplate
Clicker Style
Mount
One Piece
Kit
Parts
Facet Washer Bibb Chest
Faucet
Facet Pull Out Sprayer
Drinking faucet
Hose
Shower Arm
Washer
Single Function
Rain
Drop In
Shower Supply Elbow
Vessel Mount
Hose Connection
Hand Held
Wrench
Strainer Assembly


Tags:
-----
Nipple Extractor
Escutchon
2.0 GPM
2 Holes
Square
Plug Wrench
Deep Cup
Jaws
7"D
Jr Duo
Pop Up
Duplex
Economy
pliers
nose mount
Nut Wrench
Grid Drain
Basin Wrench
Basket
Water Saving
Carded
Parts
6"D
Clog Resistant
Strap Wrench
3/4" IPS
Tapered
Jewel Series
Flush Mount
Straight
1-4-All Universal Fit
1 1/2" (Coarse Thread)
U Shape
Button
Copper Pipe
Dome
2.5 GPM
Swivel Connector
1.8 GPM
Rear Diverter
Clicker Stopper
No Overflow
Sillcock Key
1 hole
Adjustable
Stainless Steel
Socket Wrench
Pop Up Assembly
Hose
1 1/4" (Fine Thread)
Single Function
Hose Guide
4.5"D
Arm Mount
®Mixet Style 4
Hook
Adjustable Spray
De-burring Tool
Step
Convert
1/2" IPS
L Shape
All Brass
2.2 GPM
Flow Control
Massage
No Diverter
Kit
Spray Head
Spud Chuck
Rear Mount
Two Piece
Free Rotateing Connector Nut
Front Diverter
With Overflow
Wide
S Shape
Spin and Seal
Stopper
1.75"D
Three Piece
Round
Half & Half
59-80" hose
Flat
1.2 GPM
Plastic
5 Function
Bracket
8"
Wall Mount
10 Sizes
Jet
Beveled
1.5 GPM
Zinc
Slip Fit 5/8" OD
Cartridge Puller
1.75 GPM
Telescoping Adjustable Feature
Hose Connection
Faucet Seat
Strainer Wrench
PVC
Industrial
"""