from json import load
from read_it_all import read_it_all

imported_dict = load(open("test_input_file.json"))

def test_everything():
    t = read_it_all(imported_dict)

    assert "------------------------------\n"+\
"Name: SS Clad Top Plastic Popup No Overflow\n"+\
"------------------------------\n"+\
"   Categories: Bathroom Sink Drains\n"+\
"subcategories: Pop Up\n"+\
"         tags: No Overflow, Plastic\n"+\
"------------------------------\n"+\
"Description: Plastic Sink Drain single piece Pop-Up Drain without Overflow Easy Assembly with  with Stainless Steel clad waste seat and plunger, comes complete with lift rod and linkage.\n"+\
"------------------------------\n"+\
"| UPC |  Part|  Info\n"+\
"------------------------------\n"+\
"|10000| 600S2| Plastic with Stainless Steel Clad Top & Plunger\n\n"+\
"Categories: Bathroom Sink Drains\n"+\
"Subcategories: Pop Up\n"+\
"Tags: No Overflow, Plastic\n" == t
    
