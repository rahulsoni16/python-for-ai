def calculate_total(quantity, price):
    "Calculate total for single line"
    return f"{quantity*price:,.1f}"

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"