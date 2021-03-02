from unittest import TestCase

from cleetcode.taskFactory.make_dataset_text import AllProb


class TestAllProb(TestCase):
    def test_init_data(self):
        ap = AllProb("../cleetcode/taskFactory/problems.json")

        with open("all.json", "w") as f:
            ap.dump(f)


class TestAllProb01(TestCase):
    def test_generator_one_frequency_exclude(self):
        ap = AllProb()
        with open("/root/progs/leetcode2021/cleetcode/taskFactory/problems_middleware.json", "r") as f:
            ap.load(f)
        print(ap)
        ap.generator_one_frequency_exclude()

        for i in ap.generator_one_frequency_exclude(0,2,2):
            print([j.level for j in i])
            # print(len(i))