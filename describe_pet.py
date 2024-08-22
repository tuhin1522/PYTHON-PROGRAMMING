def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


if __name__ == "__main__":
    describe_pet(pet_name="harry", animal_type="hamster")
