import re

def correccion_fecha(date):
    if re.search(r"^[0-9][0-9]/", date):
        split_date = date.split("/")
        day = split_date[0]
        month = split_date[1]
        year = split_date[2]
        date = f"{year}-{month}-{day}"
    return date