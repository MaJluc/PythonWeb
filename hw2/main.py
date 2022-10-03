from cli_interface import CLI, DATA_MODULE
from address_book import AddressBook
from notes import Notes


def main():
    try:
        DATA_MODULE["address_book"] = AddressBook()
        DATA_MODULE["note_book"] = Notes()

        cli = CLI()
        cli.run()
    finally:
        del DATA_MODULE["address_book"]
        del DATA_MODULE["note_book"]
        del cli


if __name__ == '__main__':
    main()
