def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    numero = coordinate[0]
    letra = coordinate[1]

    return (numero, letra)


def create_record(azara_record, rui_record):
    a, b = azara_record
    c, d = rui_record
    numero = b[0]
    letra = b[1]
    ca = (numero, letra)

    if ca == d:
        final = azara_record + rui_record
    else:
        final = "not a match"

    return final
