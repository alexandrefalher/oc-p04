from kview.data_model.data_model import DataModel
from typing import List


class ErrorPatialView:
    @staticmethod
    def generate(model: DataModel) -> str:
        view: str = ""
        errors: List[str] = model.get("errors")
        if errors is not None:
            view += "    .    " + "\n"\
                    "   / \\  " + "\n"\
                    "  / ! \\ " + "\n"\
                    " /_____\\" + "\n"
            for error in errors:
                view += "{0} \n".format(error)
            view += "------------------ \n"
        return view
