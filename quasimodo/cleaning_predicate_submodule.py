from .submodule_interface import SubmoduleInterface
import logging

dirty_words = ["so", "also"]
forbidden_predicate = ["xbox", "xo", "youtube", "here",
                       "there", "yahoo", "wikipedia", "quora", "how", "why"]


class CleaningPredicateSubmodule(SubmoduleInterface):

    def __init__(self, module_reference):
        super().__init__()
        self._module_reference = module_reference
        self._name = "Cleaning predicate"

    def process(self, input_interface):
        logging.info("Start cleaning predicates")
        new_generated_facts = []
        for generated_fact in input_interface.get_generated_facts():
            predicate = generated_fact.get_predicate().get()
            if predicate in forbidden_predicate:
                continue
            predicate_parts = predicate.split(" ")
            new_predicate_parts = []
            for p in predicate_parts:
                if p not in dirty_words:
                    new_predicate_parts.append(p)
            if len(predicate_parts) != len(new_predicate_parts):
                generated_fact = generated_fact.change_predicate(" ".join(new_predicate_parts).strip())
            new_generated_facts.append(generated_fact)
        return input_interface.replace_generated_facts(new_generated_facts)