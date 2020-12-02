names=["a","b","c","d","e","f"]
passed=["a","b","c"]
name_set=set(names)
passed_set=set(passed)
failed_set=name_set-passed_set
print(failed_set)