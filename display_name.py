"""
scrivere un programma che visualizzi sullo schermo 
il vostro nome all'interno di un rettangolo
come nel seguente esempio:
+------+
¦ Dave ¦
+------+
"""

def display_name(name):
    corner = "+"
    horizontal_frame = "-" * (len(name) + 2)
    vertical_frane = "¦"
    print(corner + horizontal_frame + corner)
    print(vertical_frane + " " + name.capitalize() + " " + vertical_frane)
    print(corner + horizontal_frame + corner)

display_name("carmine")

display_name("VANESSA")