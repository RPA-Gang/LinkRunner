import os

from CustomClasses import Command, Dict
from Dependencies import DataHelper, DictHelper, StringHelper, VMHelper

from rich import print

os.system("cls")
# noinspection SpellCheckingInspection
url: str = r"file://melcorpsmb.apac.linkgroup.corp/BluePrism/SmartAuto/Process%20On%20Demand/Data/RPAVMLinks.html"
vital_prefix: str = "vmrc"


# ---------------------- Start of Helper Functions ----------------------
def view(virtual_machines: dict, target=None) -> bool:
    """VMHelper.view() prints the virtual_machines parameter in either a PrettyTable or pandas DataFrame."""
    if target is None:
        print("/* Behold: Tabulated data!\n")
        VMHelper.tabulate_dict(machines=virtual_machines)
    else:
        print("/* I cannot yet view specific targets!\n")
    return True


def connect(virtual_machines: dict, _target=None) -> bool:
    """VMHelper's search_connect() function wrapped in a while loop."""
    print("\n/* Initiating remote connection routine...")
    connection_attempt: bool = False
    while connection_attempt is False:
        connection_attempt = VMHelper.search_connect(machines=virtual_machines, target=_target)
        _target = None
    else:
        return True


# ----------------------- End of Helper Functions -----------------------


def startup() -> Dict:
    """Function runs on startup; retrieves, cleans and returns necessary data."""
    print("/* Welcome to LinkRunner 2049 - Fetching links...")
    hyperlinks: dict = DataHelper.retrieve_links(url=url)
    hyperlinks_clean_keys: dict = DictHelper.dict_cleanup(data=hyperlinks,
                                                          target=r"LG | VB")
    offensive_values: list = []

    for v in hyperlinks_clean_keys.values():
        if v is None or not str(v).startswith(vital_prefix):
            offensive_values.append(v)
        else:
            continue

    hyperlinks_filtered: Dict = Dict(DictHelper.filter_values(data=hyperlinks_clean_keys,
                                                              values=offensive_values))
    print("/* Data aggregation complete!\n")
    return hyperlinks_filtered


def main() -> None:
    vm_links: Dict = startup()
    commands: Command = Command(
        cmd_list=Dict({
            "view": view,  # Keys can be customized, altering the options available to the user.
            "run": connect,  # Values are to be function names. For simplicity, all functions take the same argument.
        })
    )

    print("/* What would you like to do?\n\t"
          "'view': View a list of available Virtual Machines.\n\t"
          "'run': Connect to a specific Virtual Machine.\n")
    while True:
        try:
            user_input: str = input("> ")
            user_input: list = StringHelper.part_filter(user_string=user_input)
            if user_input[0] != "quit":
                commands.cmd_list[user_input[0].lower()](vm_links, user_input[1])
            else:
                print("\n/* Terminating...")
                break
        except KeyError:
            print("/* You can choose from the following:\t",
                  *commands.cmd_list.keys(), sep="\n\t")


if __name__ == "__main__":
    main()
