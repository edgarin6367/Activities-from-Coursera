def make_sandwich(bread_type:str, filling_type:str, cheese:str = "none", toasted: bool = False):
    """Make a sandwich."""
    if toasted == True and cheese != "none":
        return(f"Making a toasted {bread_type} sandwich with {filling_type} and {cheese} cheese.")
    else:
        return(f"Making a {bread_type} sandwich with {filling_type}.")

make_sandwich("wheat", "turkey", "cheddar", True)
make_sandwich("rye", "ham",)