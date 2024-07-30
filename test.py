# class Father():
#     def __init__(self):
#         print("this is constuctor")
#
#     def property(self):
#         print("this is father parent and ready to construct")
#
#
# class child(Father):
#     def property2(self):
#         print("Father has not built any building lets starts building")
#         print("costructions started")
#         print("construction has been completed")
#
# class child2(Father):
#     def property(self):
#         print("Father has not built any building lets keep this property as is")
#
#
# child1 = child()
#
# child1.property()
#
# child2 = child2()
#
# child2.property()
#
#
#
#
#
#
#
# # class Character:
# #     def __init__(self, name, health):
# #         self.name = name
# #         self.health = health
# #
# #     def attack(self):
# #         print("parent class")
# #
# # class Hero(Character):
# #     def attack(self):
# #         print(f"{self.name} attacks with a sword!")
# #
# # class Villain(Character):
# #     def attack(self):
# #         print(f"{self.name} attacks with dark magic!")
# #
# # obj = Villain(name='Sreeni', health='nice')
# #
# # obj.attack()
#
#
#
#
class ETLTest:
    def __init__(self, name):
        self.name = name
        print("parent constructor")


    def run(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def validate(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def execute(self):
        self.run()
        self.validate()




class CountVerificationTest(ETLTest):
    def __init__(self, name, source_count, target_count):
        super().__init__(name)
        self.source_count = source_count
        self.target_count = target_count

    def run(self):
        print(f"Running count verification for test: {self.name}")
        print(f"Source count: {self.source_count}, Target count: {self.target_count}")

    def validate(self):
        print(f"Validating count for test: {self.name}")
        if self.source_count == self.target_count:
            print("Count verification passed: Record counts match.")
        else:
            print("Count verification failed: Record counts do not match.")


source_count = 1000
target_count = 1000

# Creating and executing a count verification test
count_test = CountVerificationTest("Customer Data Count Verification", source_count, target_count)
count_test.execute()


class Test:
    def __init__(self):
        print("parent constructor")

    def method(self):
        print("parent method")

class Test2(Test):
    def __init__(self):
        print("child cons")
    def method(self):
        print("child method")

Test2()
