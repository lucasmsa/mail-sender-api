def validate_request_body(request_body_json):
    if not all (field in request_body_json.keys() for field in ("name", "email", "flash_cards_for_the_day")):
        raise Exception("Missing required fields, which are [name, email, flash_cards_for_the_day]")
    for field, value in request_body_json.items():
        if not len(field):
            raise Exception(f"{field} field should not be blank")

        if field == "flash_cards_for_the_day" and type(value) != int:
            raise Exception(f"{field} field should be an integer")