from manager.password import Encryptor


def main():
    try:
        encryptor = Encryptor()
        print("Successfully imported encryptor.")
    except Exception as e:
        print(f"An error occurred: {e}.")


if __name__ == "__main__":
    main()
