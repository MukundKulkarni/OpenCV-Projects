import pandas as pd
import numpy as np

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Side, PatternFill, Font


def create_test_data_citizens_syn(size):
    values = {"final_assessment_flag": ["N", "Y", "U"],
              "final_assessment_level": ["0", "1", "U"],
              "authorized_user_velocity": ["N", "U"],
              "id_discrepency_flag": ["N", "Y", "U"],
              "number_of_authorized_users": ["U", "0", "7", "10"],
              "number_of_terminated_users": ["U", "0", "2", "49"],
              "id_confirmation_behavior_flag": ["N", "Y", "U"],
              "ssn_verified_flag": ["N", "Y", "U"],
              "invalid_ssn_flag": ["N", "Y", "U"],
              "shared_address_flag": ["N", "Y", "U"],
              "identity_confirmation_flag_1": ["N", "Y", "U"],
              "identity_confirmation_flag_2": ["N", "Y", "U"],
              "inquiry_flag": ["N", "Y", "U"],
              "death_master_hit_flag": ["N", "U"]
              }

    df = pd.DataFrame()

    columns = [key for key in values.keys()]
    print(columns)

    for column in values.keys():
        df[column] = np.random.choice(values[column], size)

    return df


def proc_frequency(input_df, attribute, percent=True, cumulative_freq=True, cumulative_percent=True):

    freq_df = pd.DataFrame(input_df[attribute].value_counts().sort_index())
    freq_df.rename(columns={"count": 'Frequency'}, inplace=True)
    freq_df.index.name = attribute

    if percent:
        freq_df['Percent'] = round(
            (freq_df["Frequency"]/freq_df["Frequency"].sum())*100, 6)
    if cumulative_freq:
        freq_df['Cumulative Frequency'] = freq_df['Frequency'].cumsum()
    if cumulative_percent:
        freq_df['Cumulative Percent'] = freq_df['Percent'].cumsum()

    return freq_df


# This Function will write the input_df to the output xlsx file at the given
# start column and row

def print_table(xlsxwriter, input_df, output_path, start_col, start_row, sheet_name):
    pass


def create_xlsx_report(file_path, file_name):
    return pd.ExcelWriter(file_path + file_name, engine='xlsxwriter')


if __name__ == "__main__":
    np.random.seed(42)

    test_df = create_test_data_citizens_syn(1000000)

    output_path = "/home/mukund/Work/SAS_To_Py/"
    output_file = "Citizens_Bank_Syn_Flag_Report.xlsx"

    sheet_name = "Citizens_Bank_Syn_Flag"
    project_name = "TEST PROJECT NAME"
    project_number = "A1B2345"

    report1 = create_xlsx_report(output_path, output_file)
    workbook1 = report1.book
    worksheet1 = workbook1.add_worksheet(sheet_name)

    # Add a text format.
    text_format = workbook1.add_format({'text_wrap': True})
    # Add a text format.
    text_format_1 = workbook1.add_format({'text_wrap': True, 'border' : 1})
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

    text_format = workbook1.add_format({'text_wrap': True, 'border': 2})
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

    # set a border around a specific range of cells
    rrange_border = Border(left=Side(style='thin'),
                           right=Side(style='thin'),
                           top=Side(style='thin'),
                           bottom=Side(style='thin'))

    input_df = test_df[['final_assessment_flag', 'final_assessment_level', 'authorized_user_velocity',
                        'id_discrepency_flag', 'number_of_authorized_users', 'number_of_terminated_users',
                        'id_confirmation_behavior_flag', 'ssn_verified_flag', 'invalid_ssn_flag', 'shared_address_flag',
                        'identity_confirmation_flag_1', 'identity_confirmation_flag_2', 'inquiry_flag', 'death_master_hit_flag']]

    columns = input_df.columns

    startrow = 6
    startcol = 0

    worksheet1.set_column(0, 5, 15, cell_format)

    worksheet1.write(0, 0, "PROJECT NAME : " + project_name, title_format)
    worksheet1.write(1, 0, "PROJECT NUMBER : " + project_number, title_format)

    for column in columns:
        freq_df = proc_frequency(input_df, column)
        for col_num, value in enumerate(freq_df.columns.values):
            worksheet1.write(startrow - 1, col_num + 1, value, header_format)

        worksheet1.write(startrow - 1, 0, column, header_format)
        worksheet1.merge_range(startrow - 2, 0, startrow - 2, 4, column, table_title_format)

        start_row = startrow

        for index in freq_df.index.values.tolist():
            worksheet1.write(start_row, 0, index, table_title_format)
            start_row += 1

        start_col = startcol
        for col in freq_df.columns:

            start_row = startrow
            for value in freq_df[col]:
                worksheet1.write(start_row, start_col + 1, value, text_format_1)
                start_row += 1
            start_col += 1




        startrow += freq_df.shape[0] + 3

    report1.close()
