# funkcja wyświetla urodziny osób z kontaktów w następnych 7 dniach
def show_upcoming_birthday(adressbook):
    info = "Upcoming birthdays:"
    is_upcoming_birthday = False
    for day, records in adressbook.records_with_upcoming_birthday().items():
        if records: # jeśli lista z danego dnia nie jest pusta
            names = []
            for record in records:
                names.append(record.name.value)    
            info += "\n{:>10}, {:<18}: {:<60}".format(day.strftime('%A'), day.strftime('%d %B %Y'), '; '.join(names))
            is_upcoming_birthday = True
    if is_upcoming_birthday:
        return info
    return "No upcoming birthdays in the next 7 days."


