import pandas as pd
import numpy as np

# Load dataset (Relative path so GitHub Actions can load it)
dataset = pd.read_csv(r"iris.csv")

# --------- Tests Boolean ---------
cols = dataset.columns.tolist()
feature_check_bool = all(dataset.columns.isin(cols))

# Range tests
sepal_length_test_bool = dataset['sepal length (cm)'].between(4,7).all()
sepal_width_test_bool = dataset['sepal width (cm)'].between(2,5).all()
petal_length_test_bool = dataset['petal length (cm)'].between(1,6).all()
petal_width_test_bool = dataset['petal width (cm)'].between(0,3).all()

# Convert to Pass/Fail messages
feature_check = ["Passed ✔️" if feature_check_bool else "Failed ❌"]
sepal_length_test = ["Passed ✔️" if sepal_length_test_bool else "Failed ❌"]
sepal_width_test = ["Passed ✔️" if sepal_width_test_bool else "Failed ❌"]
petal_length_test = ["Passed ✔️" if petal_length_test_bool else "Failed ❌"]
petal_width_test = ["Passed ✔️" if petal_width_test_bool else "Failed ❌"]

# --------- Schema Test ---------
expected_columns = 4

def test_check_schema():
    actual_columns = dataset.shape[1]
    assert actual_columns == expected_columns, \
        f"Schema Test Failed! Expected {expected_columns} columns, got {actual_columns}"

# Run schema test manually (not pytest)
try:
    test_check_schema()
    schema_result = "Passed ✔️"
except AssertionError as e:
    schema_result = "Failed ❌"

# --------- Write report to test.txt ---------
with open("test.txt", "w", encoding="utf-8") as outfile:
    outfile.write("Feature Test: %s\n" % feature_check[0])
    outfile.write("Sepal Length Test: %s\n" % sepal_length_test[0])
    outfile.write("Sepal Width Test: %s\n" % sepal_width_test[0])
    outfile.write("Petal Length Test: %s\n" % petal_length_test[0])
    outfile.write("Petal Width Test: %s\n" % petal_width_test[0])
    outfile.write("\n")
    outfile.write("Schema Test: %s\n" % schema_result)

