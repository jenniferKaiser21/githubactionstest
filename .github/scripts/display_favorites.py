import argparse

def main():
    parser = argparse.ArgumentParser(description='Display favorite food and drink.')
    parser.add_argument('favorite_food', type=str, help='Your favorite food')
    parser.add_argument('favorite_drink', type=str, help='Your favorite drink')
    args = parser.parse_args()

    favorite_food = args.favorite_food
    favorite_drink = args.favorite_drink

    print(f"My favorite food is: {favorite_food}")
    print(f"My favorite drink is: {favorite_drink}")

if __name__ == "__main__":
    main()