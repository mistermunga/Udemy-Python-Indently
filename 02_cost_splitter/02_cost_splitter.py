from typing import List


def get_user_input(prompt: str, valid_options: List[str]) -> str:
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input, please enter one of {valid_options}.")


def get_people_list() -> List[str]:
    # Validate the number of people
    while True:
        try:
            num = int(input("How many people? "))
            if num <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number greater than zero.")

    # Collect names with validation for non-empty names
    people_list = []
    for i in range(num):
        while True:
            user_input = input(f"Enter person number {i + 1}: ").strip()
            if user_input:
                people_list.append(user_input)
                break
            else:
                print("Name cannot be empty. Please enter a valid name.")

    return people_list


def cost_splitter(list_of_people: List[str]) -> List[float]:
    number_of_people = len(list_of_people)
    if number_of_people < 1:
        raise ValueError("Number of people must be greater than one")

    even_flag = get_user_input("Do you want to split evenly? (y/n) ", ['y', 'n'])
    ratios = []

    if even_flag == 'y':
        ratios = [100 / number_of_people] * number_of_people
    else:
        percentage_left = 100
        for person in list_of_people:
            while True:
                try:
                    percentage = float(input(f"Enter the percentage for {person}: "))
                    if 0 <= percentage <= percentage_left:
                        ratios.append(percentage)
                        percentage_left -= percentage
                        break
                    else:
                        print(f"Please enter a value between 0 and {percentage_left}")
                except ValueError:
                    print("Please enter a valid number.")

    if sum(ratios) < 100:
        remainder_flag = get_user_input("Some percentage is left over. Do you want to split it evenly? (y/n) ",
                                        ['y', 'n'])
        if remainder_flag == 'y':
            surplus = 100 - sum(ratios)
            for i in range(len(ratios)):
                ratios[i] += surplus / number_of_people
        else:
            print("Who should receive the surplus?")
            for idx, person in enumerate(list_of_people, start=1):
                print(f"{idx}: {person}")
            while True:
                try:
                    choice = int(input("Enter their number: ")) - 1
                    if 0 <= choice < number_of_people:
                        ratios[choice] += 100 - sum(ratios)
                        break
                    else:
                        print(f"Please enter a number between 1 and {number_of_people}")
                except ValueError:
                    print(f"Please enter a number between 1 and {number_of_people}")

    return ratios


def calc(callback, total_amount: float) -> List[float]:
    ratios = callback()
    return [ratio * total_amount / 100 for ratio in ratios]


if __name__ == "__main__":
    people = get_people_list()
    bucks = (calc(lambda: cost_splitter(people), 10000))
    for i in range(len(bucks)):
        print(f"{people[i]}: {bucks[i]}")
