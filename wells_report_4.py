import pandas as pd
import numpy as np
import random

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Side, PatternFill, Font


def create_test_data_citizens_syn(size):
    values = {"SCORE_PSPS5206": [str(n).zfill(5) for n in range(88, 100)] + [" "],
              "NEW_CUSTOM_ATTR2": [" ", "94"],
              "FRAUD_VICTIM_FLAG": [" ", "N", "Q", "R", "T", "W", "X"],
              "NEW_CUSTOM_ATTR1": [" ", "A", "B", "1", "2", "3", "4"],
              "ACCEPT_DROP_TAG": ["A", "P", "X", "Z"]
              }

    df = pd.DataFrame()

    columns = [key for key in values.keys()]
    print(columns)

    for column in values.keys():
        if column == "NEW_CUSTOM_ATTR2":
            print(True)
            df[column] = np.random.choice(a = values[column], p=[0.9, 0.1], size = size)
        else:
            df[column] = np.random.choice(a = values[column], size = size)

    return df

def proc_frequency(input_df, attribute1, attribute2 = None, percent = True, cumulative_freq = True, cumulative_percent = True):

    if attribute2:

        two_way_df = pd.crosstab(input_df[attribute1], input_df[attribute2])

        columns = two_way_df.columns

        for col in columns:
            two_way_df[col + "_percent"] = round((two_way_df[col]/input_df.shape[0])*100, 6)

        two_way_df["Total_Count"] = two_way_df[[col for col in columns]].sum(axis=1)
        two_way_df["Total_percent"] = two_way_df[[col + "_percent" for col in columns]].sum(axis=1)

        return two_way_df

    else:

        freq_df = pd.DataFrame(input_df[attribute1].value_counts().sort_index())
        freq_df.rename(columns={"count": 'Frequency'}, inplace=True)
        freq_df.index.name = attribute1

        if percent:
            freq_df['Percent'] = round(
                (freq_df["Frequency"]/freq_df["Frequency"].sum())*100, 6)
        if cumulative_freq:
            freq_df['Cumulative Frequency'] = freq_df['Frequency'].cumsum()
        if cumulative_percent:
            freq_df['Cumulative Percent'] = freq_df['Percent'].cumsum()

        return freq_df

def create_xlsx_report(file_path, file_name):
    return pd.ExcelWriter(file_path + file_name, engine='xlsxwriter')

def two_way_freq_to_excel(report, input_df, start_row, start_col, attribute1, attribute2, headers):

     # Add a text format.
    text_format_1 = workbook1.add_format({'text_wrap': True, 'top': True, 'right': True, 'left': True})
    text_format_2 = workbook1.add_format({'text_wrap': True, 'bottom': True, 'right': True, 'left': True})

    # Add a header format.
    header_format = workbook1.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'align': 'center',
        'fg_color': '#d6eaf8',
        'border': 1})

    # Add a header format.
    cell_format = workbook1.add_format({'text_wrap': True})

    # Add a header format.
    table_title_format = workbook1.add_format({
        'bold': True,
        'text_wrap': True,
        'align': 'center',
        'fg_color': '#d6eaf8',
        'border': 1})

    title_format = workbook1.add_format({
        'bold': True,
        'align': 'left',
        'fg_color': '#d6eaf8',
        'border': 1})

    startrow = start_row
    startcol = start_col

    headers = sorted(list(headers)) + ["Total"]

    worksheet1.merge_range(startrow, startcol, startrow, startcol + len(headers), "Table of {} by {}".format(attribute1, attribute2), table_title_format)
    worksheet1.merge_range(startrow + 1, startcol, startrow + 2, startcol, attribute1 , table_title_format)
    worksheet1.merge_range(startrow + 1, startcol + 1, startrow + 1,  startcol + len(headers), attribute2, table_title_format)

    startrow = start_row + 2
    startcol = start_col + 1

    for header in headers:
        print(header)
        worksheet1.write(startrow, startcol, header, header_format)
        startcol += 1

    startrow = start_row + 3
    startcol = start_col

    print("------->", startrow)

    for index in input_df.index.values.tolist():
        worksheet1.merge_range(startrow, startcol, startrow + 1, startcol, index, table_title_format)
        startrow += 2

    worksheet1.merge_range(startrow, startcol, startrow + 1, startcol, "Total", table_title_format)


    startcol = start_col + 1
    for header in headers:
        print(header)
        startrow = start_row + 3

        if header != "Total":
            for cnt1, percent in zip(two_way_freq[header], two_way_freq[header + "_percent"]):
                worksheet1.write(startrow, startcol, cnt1, text_format_1)
                worksheet1.write(startrow + 1, startcol, percent, text_format_2)
                startrow += 2

            total_cnt = two_way_freq[header].sum()
            total_percent = two_way_freq[header + "_percent"].sum()
            worksheet1.write(startrow, startcol, total_cnt, text_format_1)
            worksheet1.write(startrow + 1, startcol, total_percent, text_format_2)

            startcol += 1
        else:
            for cnt1, percent in zip(two_way_freq["Total_Count"], two_way_freq["Total_percent"]):
                worksheet1.write(startrow, startcol, cnt1, text_format_1)
                worksheet1.write(startrow + 1, startcol, percent, text_format_2)
                startrow += 2

            total_cnt = two_way_freq["Total_Count"].sum()
            total_percent = two_way_freq["Total_percent"].sum()
            worksheet1.write(startrow, startcol, total_cnt, text_format_1)
            worksheet1.write(startrow + 1, startcol, total_percent, text_format_2)

            startcol += 1

def one_way_freq_to_excel(report, input_df, start_row, start_col, attribute1):

     # Add a text format.
    text_format_1 = workbook1.add_format({'text_wrap': True, 'top': True, 'right': True, 'left': True, 'bottom' : True})
    text_format_2 = workbook1.add_format({'text_wrap': True, 'bottom': True, 'right': True, 'left': True})

    # Add a header format.
    header_format = workbook1.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'align': 'center',
        'fg_color': '#d6eaf8',
        'border': 1})

    # Add a header format.
    cell_format = workbook1.add_format({'text_wrap': True})

    # Add a header format.
    table_title_format = workbook1.add_format({
        'bold': True,
        'text_wrap': True,
        'align': 'center',
        'fg_color': '#d6eaf8',
        'border': 1})

    title_format = workbook1.add_format({
        'bold': True,
        'align': 'left',
        'fg_color': '#d6eaf8',
        'border': 1})


    startrow = start_row
    startcol = start_col

    for col_num, value in enumerate(input_df.columns.values):
        worksheet1.write(startrow + 1, startcol + col_num + 1, value, header_format)

    worksheet1.write(startrow + 1 , startcol, attribute1, header_format)
    worksheet1.merge_range(startrow, startcol, startrow, startcol + input_df.shape[1], attribute1, table_title_format)

    startrow = start_row

    for index in input_df.index.values.tolist():
        worksheet1.write(startrow + 2, startcol, index, table_title_format)
        startrow += 1

    startcol = start_col + 1
    for col in input_df.columns:
        startrow = start_row + 2
        for value in input_df[col]:
            worksheet1.write(startrow, startcol, value, text_format_1)
            startrow += 1
        startcol += 1


if __name__ == "__main__":
    np.random.seed(42)

    test_df = create_test_data_citizens_syn(1000)

    output_path = "/home/mukund/Work/SAS_To_Py/"
    output_file = "Wells_Report_4.xlsx"

    sheet_name = "QC_Report"
    project_name = "TEST PROJECT NAME"
    project_number = "A1B2345"

    report1 = create_xlsx_report(output_path, output_file)
    workbook1 = report1.book
    worksheet1 = workbook1.add_worksheet(sheet_name)

    # Add a header format.
    cell_format = workbook1.add_format({'text_wrap': True})
    title_format = workbook1.add_format({
        'bold': True,
        'align': 'left',
        'fg_color': '#d6eaf8',
        'border': 1})

    input_df = test_df[["SCORE_PSPS5206", "NEW_CUSTOM_ATTR2", "FRAUD_VICTIM_FLAG", "NEW_CUSTOM_ATTR1", "ACCEPT_DROP_TAG"]]

    columns = input_df.columns

    worksheet1.set_column(0, 10, 10, cell_format)

    # two_way_freq = proc_frequency(input_df, "SCORE_PSPS5206", "NEW_CUSTOM_ATTR2")
    # headers = input_df["NEW_CUSTOM_ATTR2"].unique()
    # two_waf_freq_to_excel(report1, two_way_freq, 6, 0, "SCORE_PSPS5206", "NEW_CUSTOM_ATTR2", headers)
    #
    # two_way_freq = proc_frequency(input_df, "FRAUD_VICTIM_FLAG", "NEW_CUSTOM_ATTR1")
    # headers = input_df["NEW_CUSTOM_ATTR1"].unique()
    # two_waf_freq_to_excel(report1, two_way_freq, 39, 0, "FRAUD_VICTIM_FLAG", "NEW_CUSTOM_ATTR1", headers)

    one_way_freq = proc_frequency(input_df, "ACCEPT_DROP_TAG")
    print(one_way_freq)
    one_way_freq_to_excel(report1, one_way_freq, 6, 0, "ACCEPT_DROP_TAG")

    one_way_freq = proc_frequency(input_df, "FRAUD_VICTIM_FLAG")
    print(one_way_freq)
    one_way_freq_to_excel(report1, one_way_freq, 20, 0, "FRAUD_VICTIM_FLAG")

    report1.close()




