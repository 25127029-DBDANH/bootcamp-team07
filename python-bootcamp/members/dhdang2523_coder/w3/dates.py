from datetime import date, timedelta

def parse_due(text: str, today: date) -> date:
    text = text.lower().strip()
    
    if text == "tomorrow":
        return today + timedelta(days=1)
        
    if text.startswith("in ") and text.endswith(" days"):
        try:
            days = int(text[3:-5].strip())
            return today + timedelta(days=days)
        except ValueError:
            pass
            
    try:
        return date.fromisoformat(text)
    except ValueError:
        pass
        
    weekdays = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6}
    for day_str, day_num in weekdays.items():
        if text.startswith(day_str):
            days_ahead = day_num - today.weekday()
            if days_ahead <= 0:
                days_ahead += 7
            return today + timedelta(days=days_ahead)

    raise ValueError(f"Cannot parse date from: {text}")