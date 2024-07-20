# break : if we want break iteration(for/while loop) then we will use break keyword
# continue(skip): if we want to skip iteration then we will use continue
# pass : will be used to write syntactically correct code when we don't have logic

source = None
target = 10
for i in range(1,11):
    if i == 7:
        break
    print(i)
#
print("*"*40)
for i in range(1,5):
    if i == 2:
        continue
    print(i)
#
# source = None
# Target = None
#
# source1 = 10
# target1 = 11
#
# for i in range(1,5):
#     if source is None or Target is None:
#         continue

for i in range(1,10):
    pass

for j in range(1,11):
    pass

def azure_sql_db(connection_str):
    pass
