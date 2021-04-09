import shutil
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    main_folder = Path("C:/Users/C0rbin/Documents/GitHub/BotDashboard/mouse_data__2020_12_02_updated")
    export_folder = Path("C:/Users/C0rbin/Documents/GitHub/BotDashboard/mouse_data_all3")
    if not export_folder.exists():
        export_folder.mkdir()

    sub_folder_name = "human"

    files = main_folder.glob("*.json")
    file_list = []
    for file in files:
        file_list.append([str(file)])
    print(file_list)
    df = pd.DataFrame(file_list, columns=["Path"])

    print(main_folder)
    train_df, valid_df = train_test_split(df,
                                       test_size = 0.25,
                                       random_state = 2018)
    print(train_df)
    print(valid_df)
    train_folder = Path(str(export_folder) + "/train")
    validation_folder = Path(str(export_folder) + "/validation")

    if not train_folder.exists():
        train_folder.mkdir()

    if not validation_folder.exists():
        validation_folder.mkdir()

    train_folder = train_folder / sub_folder_name
    validation_folder = validation_folder /sub_folder_name

    if not train_folder.exists():
        train_folder.mkdir()

    if not validation_folder.exists():
        validation_folder.mkdir()

    copy_files(train_df, train_folder, sub_folder_name)
    copy_files(valid_df, validation_folder, sub_folder_name)


def copy_files(df, new_path, sub_folder_name):

    for index,row in df.iterrows():
        print(row["Path"])
        fn = sub_folder_name + "_" + str(index) + ".txt"
        shutil.copy2(row["Path"],new_path/fn)


main()