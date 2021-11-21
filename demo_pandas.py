import os, pandas, pathlib
from pandas.core.frame import DataFrame


def read_data_file(path: str) -> DataFrame:
    if not os.path.exists(path):
        return None
    data_file = open(path, 'rb')
    if ".csv" in path:
        data = pandas.read_csv(data_file)
    elif ".xlsx" in path:
        data = pandas.read_excel(data_file, sheet_name='excel_file')
    elif ".json" in path:
        data = pandas.read_json(data_file)
    else:
        return None
    print(data)
    return data

def main():
    root_file = pathlib.Path(__file__).parent.resolve()
    path = os.path.join(root_file, "statics/excel_file.csv")

    # DataFrame creation
    data_frame1 = DataFrame(
        {
            "colonne_1": [1, 2, 3, 4, 5, 6],
            "colonne_2": ["a", "b", "c", "d", "e", "f"],
            "colonne_3": [11, 22, 33, 44, 55, 66]
        }
    )
    print(data_frame1)
    # DataFrame with ligne number change in 'A1', 'A2', 'A3', ...
    data_frame2 = DataFrame(
        {
            "colonne_1": [1, 2, 3, 4, 5, 6],
            "colonne_2": ["a", "b", "c", "d", "e", "f"],
            "colonne_3": [11, 22, 33, 44, 55, 66]
        },
        index = ["A1", "A2", "A3", "A4", "A5", "A6"]
    )
    print(data_frame2)

    # Get colomns average
    average = data_frame1.mean(axis=0, numeric_only=True)
    print(average)
    # Get rows average
    average = data_frame1.mean(axis=1, numeric_only=True)
    print(average)

    # Add 'colonne_1' to 'colonne_3'
    result = data_frame1["colonne_1"].add(data_frame1["colonne_3"])
    print(result)
    # Add the new 'colonne_4' (result of 'colonne_1' + 'colonne_3') at
    # the end of the DataFrame
    data_frame1["colonne_4"] = result
    print(data_frame1)

    # Multiple 'colonne_4' with 'colonne_1'
    result = data_frame1["colonne_4"].mul(data_frame1["colonne_1"])
    print(result)
    # Add the new 'colonne_5' (result of 'colonne_4' * 'colonne_1') at
    # the end of the DataFrame
    data_frame1["colonne_5"] = result
    print(data_frame1)

    # Sum of 'colonne_5'
    colonne_5_sum = data_frame1["colonne_5"].sum()
    print(colonne_5_sum)
    # Sum of 'colonne_4'
    colonne_4_sum = data_frame1["colonne_4"].sum()
    print(colonne_4_sum)
    # Sum of 'colonne_5' and 'colonne_4'
    colonne_5_and_4_sum = colonne_5_sum + colonne_4_sum
    print(colonne_5_and_4_sum)

    value4 = data_frame1["colonne_5"][4]
    print(value4)
    value5 = data_frame1["colonne_5"][5]
    print(value5)

    colomn_5_max = data_frame1["colonne_5"].max()
    print(colomn_5_max)
    colomn_5_min = data_frame1["colonne_5"].min()
    print(colomn_5_min)

    colomn5_values_greater_than_100 = data_frame1["colonne_5"].gt(100)
    print(colomn5_values_greater_than_100)
    colomn5_values_lower_than_100 = data_frame1["colonne_5"].lt(100)
    print(colomn5_values_lower_than_100)

    return data_frame1
    """
    data = read_data_file("./statics/excel_file.csv")
    print("--- Your data file ---")
    print(f"Data types:\n{data.dtypes}\n")
    print(f"File's info:\n{data.info()}\n")
    print(f"{data.count()}\n")
    print(f"Columns:\n{data.columns}\n")
    print(f"{data.to_json()}\n")
    print(f"{data.to_html()}\n")
    print(f"{data.to_dict()}\n")

    temp_df = data[["clientid"]].copy()
    print(temp_df)
    temp_df["clientid"] = temp_df["clientid"].apply(lambda x: x ** 2)
    print(temp_df)
    data["clientid"] = temp_df["clientid"]

    # Write an Excel file with the updated values
    data.to_excel("./demo_excel.xlsx")"""

if __name__ == "__main__":
    main()