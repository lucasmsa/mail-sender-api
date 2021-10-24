def template_message(name: str, flash_cards_for_the_day: int) -> str:
    return (
        f"Dear, {name.capitalize()}\n"
        f"You have {flash_cards_for_the_day} flash cards to do today\n\n" 
        f"From Dolphin Cards"
    )