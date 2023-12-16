# Creates a default template where properties field is empty
# This function is called by the fill_template function and returns an incomplete template
def create_template():
    return {
        "standard": "arc69",
        "mime_type": "image/jpg",
        "properties": {}
    }

# Calls the create_template function and fills in the empty properties dictionary key value from arguments
# Returns a complete template for metadata which is passed into the note field of the asset creation transaction
def fill_template(name, description, type, strength, health, level, exp):
    template = create_template()
    template["properties"] = {
        "Name": name,
        "Description": description,
        "Type": type,
        "Strength": strength,
        "Health": health,
        "Level": level,
        "Experience": exp
    }
    return template

# Example Usage
name = 'AshMaker'
description = 'Covered in Ashes and Flaming Hot!'
type = 'Fire'
strength = 5
health = 20
level = 1
exp = 0

complete_template = fill_template(name, description, type, strength, health, level, exp)
