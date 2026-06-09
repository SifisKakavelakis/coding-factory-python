def get_formatted_date(day: int  = 1, month: int = 1, year: int = 2000) -> str:
    """Returns a sdtring representing a date in the format ""dd/mm/yyyy""
      Args:
        day (int, optional): The day of the month. Defaults to 1.
        month (int, optional): The month of the year. Defaults to 1.
        year (int, optional): The year. Defaults to 2000.
        
        Returns:
            str: The formatted date string.
        """
    return f"{day:02d}/{month:02d}/{year}"

def main():
    print(get_formatted_date())  # "01/01/2000"
    print(get_formatted_date(10))  # "10/01/2000"
    print(get_formatted_date(14, 5))  # "14/05/2000"
    print(get_formatted_date(12, 7, 2010))  # "12/07/2010"
    print(get_formatted_date(year = 2026)) # "01/01/2026"
    print(get_formatted_date(day=10, month=12, year=2025)) # "10/12/2025"
    
    get_formatted_date()

if __name__ == "__main__":
    main()