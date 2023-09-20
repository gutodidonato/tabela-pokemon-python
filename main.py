from prettytable.colortable import ColorTable, Themes

table = ColorTable(theme=Themes.OCEAN)


table.field_names = ["Pokemon", "Tipo", "Região Inicial", "Poder"]
table.add_row(["Magikarp", "Água", "Kanto", 99999])
table.add_row(["Mewtwo", "Psíquico", "Kanto", 30])
table.add_row(["Trecko", "Planta", "Hoen", 3000])
table.add_row(["Pikachu", "Elétrico", "Johto", 999])
table.add_row(["Charizard", "Fogo/Voador", "Kanto", 2000])
table.add_row(["Gengar", "Fantasma/Veneno", "Johto", 500])
table.add_row(["Bulbasaur", "Planta/Veneno", "Kanto", 3000])
table.add_row(["Squirtle", "Água", "Kanto", 300])
table.add_row(["Jigglypuff", "Normal/Fada", "Kanto", 200])

table.align = "c"

print(table)