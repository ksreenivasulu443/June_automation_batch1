class ETLTest:
    def __init__(self, name):
        self.name = name
        #print("parent constructor")


    def run(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def validate(self):
        print("this parent validate method")

    def execute(self):
        self.run()
        self.validate()




class CountVerificationTest(ETLTest):
    def __init__(self, name, source_count, target_count):
        super().__init__(name)
        #self.name=name
        self.source_count = source_count
        self.target_count = target_count

    def run(self):
        print(f"Running count verification for test: {self.name}")
        print(f"Source count: {self.source_count}, Target count: {self.target_count}")

    # def validate(self):
    #     print(f"Validating count for test: {self.name}")
    #     if self.source_count == self.target_count:
    #         print("Count verification passed: Record counts match.")
    #     else:
    #         print("Count verification failed: Record counts do not match.")


source_count = 1000
target_count = 1000

# Creating and executing a count verification test
count_test = CountVerificationTest("Customer Data Count Verification", source_count, target_count)
count_test.execute()