 
# ==============
#  Pretty Title
# ==============

def pretty_title(name = "ENTER A NAME", fancy_bit = "=", closing_bit = "", opening_bit = ""):
    
    fancy_line = fancy_bit * int(len(name) / len(fancy_bit) + 2) + closing_bit
    
    title = "\n" +\
        fancy_line + "\n" +\
        " " * (len(fancy_bit) + len(opening_bit)) + name + "\n" +\
        fancy_line + "\n"

    return title



# o==[===============>
#     Sword Title
# <===============]==o

def sword_title(name = "ENTER A NAME", blade_segment = "="):

    handle_r = "o==["
    point_r = ">"

    handle_l = "]==o"
    point_l = "<"

    sword_r = handle_r + blade_segment * int(len(name + handle_r)  / len(blade_segment)) + point_r
    sword_l = point_l + blade_segment * int(len(name + handle_l) / len(blade_segment)) + handle_l

    title = ( "\n" + \
            sword_r + "\n" + \
            (" " * len(handle_r)) + name + "\n" + \
            sword_l + "\n")
   
    return title


# ======
#  Under Line
# ======

def underline(name = "ENTER A NAME", fancy_bit = "-", closing_bit = "", opening_bit = ""):
    
    fancy_line = fancy_bit * int(len(name) / len(fancy_bit)) + closing_bit
    
    title = " " * len(opening_bit) + name + "\n" +\
        fancy_line + "\n"

    return title

# ======
#  over Line
# ======

def overline(name = "ENTER A NAME", fancy_bit = "-", closing_bit = "", opening_bit = ""):
    
    fancy_line = fancy_bit * int(len(name) / len(fancy_bit) + 2) + closing_bit
    
    title = "\n" +\
        fancy_line + "\n" +\
        " " * (len(fancy_bit) + len(opening_bit)) + name + "\n"

    return title