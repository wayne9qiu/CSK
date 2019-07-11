import unittest

from quasimodo import OpenIEFactGeneratorSubmodule, Inputs, PatternGoogle
from quasimodo.are_transformation_submodule import AreTransformationSubmodule
from quasimodo.referencable_interface import ReferencableInterface


class TestAreTransformation(unittest.TestCase):

    def setUp(self) -> None:
        dummy_reference = ReferencableInterface("Dummy reference")
        self.openie_fact_generator = OpenIEFactGeneratorSubmodule(dummy_reference)
        self.openie_fact_generator._name = "OPENIE"  # Dummy name only useful for testing
        self.empty_input = Inputs()
        self.are_transformation = AreTransformationSubmodule(None)

    def test_color(self):
        suggestion = ("why are pandas black", 1.0, None, "panda")
        new_gfs = self.openie_fact_generator.get_generated_facts([suggestion])
        inputs = self.empty_input.add_generated_facts(new_gfs)
        inputs = self.are_transformation.process(inputs)
        self.assertEqual(1, len(inputs.get_generated_facts()))
        self.assertEqual(inputs.get_generated_facts()[0].get_predicate(), "has_color")

    def test_color1(self):
        suggestion = ("why are pandas white", 1.0, None, "panda")
        new_gfs = self.openie_fact_generator.get_generated_facts([suggestion])
        inputs = self.empty_input.add_generated_facts(new_gfs)
        inputs = self.are_transformation.process(inputs)
        self.assertEqual(1, len(inputs.get_generated_facts()))
        self.assertEqual(inputs.get_generated_facts()[0].get_predicate(), "has_color")

    def test_body(self):
        suggestion = ("why do pandas have hands", 1.0, None, "panda")
        new_gfs = self.openie_fact_generator.get_generated_facts([suggestion])
        inputs = self.empty_input.add_generated_facts(new_gfs)
        inputs = self.are_transformation.process(inputs)
        self.assertEqual(1, len(inputs.get_generated_facts()))
        self.assertEqual(inputs.get_generated_facts()[0].get_predicate(), "has_body_part")

    def test_trait(self):
        suggestion = ("why are pandas nice", 1.0, PatternGoogle("why are", "has_property", 1.0), "panda")
        new_gfs = self.openie_fact_generator.get_generated_facts([suggestion])
        inputs = self.empty_input.add_generated_facts(new_gfs)
        inputs = self.are_transformation.process(inputs)
        self.assertEqual(1, len(inputs.get_generated_facts()))
        self.assertEqual(inputs.get_generated_facts()[0].get_predicate(), "has_trait")

    def test_property(self):
        suggestion = ("why are pandas dead", 1.0, PatternGoogle("why are", "has_property", 1.0), "panda")
        new_gfs = self.openie_fact_generator.get_generated_facts([suggestion])
        inputs = self.empty_input.add_generated_facts(new_gfs)
        inputs = self.are_transformation.process(inputs)
        self.assertEqual(1, len(inputs.get_generated_facts()))
        self.assertEqual(inputs.get_generated_facts()[0].get_predicate(), "has_property")

    def test_property_no_relation(self):
        suggestion = ("why are pandas dead", 1.0, PatternGoogle("why are"), "panda")
        new_gfs = self.openie_fact_generator.get_generated_facts([suggestion])
        inputs = self.empty_input.add_generated_facts(new_gfs)
        inputs = self.are_transformation.process(inputs)
        self.assertEqual(1, len(inputs.get_generated_facts()))
        self.assertEqual(inputs.get_generated_facts()[0].get_predicate(), "are")

    def test_quick(self):
        suggestion = ("why are pandas quick", 1.0, PatternGoogle("why are", "has_property", 1.0), "panda")
        new_gfs = self.openie_fact_generator.get_generated_facts([suggestion])
        inputs = self.empty_input.add_generated_facts(new_gfs)
        inputs = self.are_transformation.process(inputs)
        self.assertEqual(1, len(inputs.get_generated_facts()))
        self.assertEqual(inputs.get_generated_facts()[0].get_predicate(), "has_movement")

    def test_ignore(self):
        suggestion = ("why do pandas eat bamboo", 1.0, PatternGoogle("why do", "has_property", 1.0), "panda")
        new_gfs = self.openie_fact_generator.get_generated_facts([suggestion])
        inputs = self.empty_input.add_generated_facts(new_gfs)
        inputs = self.are_transformation.process(inputs)
        self.assertEqual(1, len(inputs.get_generated_facts()))
        self.assertEqual(inputs.get_generated_facts()[0].get_predicate(), "eat")


if __name__ == '__main__':
    unittest.main()
