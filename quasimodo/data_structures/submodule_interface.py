from .submodule_reference_interface import SubmoduleReferenceInterface
from .process_interface import ProcessInterface


class SubmoduleInterface(SubmoduleReferenceInterface, ProcessInterface):
    """SubmoduleInterface
    Represents a submodule
    """

    def __init__(self):
        self._module_reference = None # ModuleReferenceInterface

    def __str__(self):
        return "----> SUBMODULE: " + self.get_name()

    def clean(self):
        pass
