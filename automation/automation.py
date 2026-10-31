
from openpyxl import load_workbook
import win32com.client
import os
from datetime import datetime

os.system('cls' if os.name == 'nt' else 'clear')

# Word

folder = os.getcwd()

template_path = os.path.join(folder, 'Template.docx')
result_path = os.path.join(folder, 'Household Data.docx')

word = win32com.client.Dispatch('Word.Application')

for doc in word.Documents:
    if os.path.abspath(doc.FullName) == os.path.abspath(result_path):
        doc.Close(SaveChanges=False)
        break

if os.path.exists(result_path):
    os.remove(result_path)
    print('The old file was closed and deleted.')
else:
    print('The file does not exist.')



template = word.Documents.Open(template_path)

word.Visible = True

template.Content.Copy()

doc = template
doc.SaveAs2(result_path)

def page_break():
    doc.Range(
        Start=doc.Content.End - 1,
        End=doc.Content.End - 1
    ).InsertBreak(7)

def paste_template():
    doc.Range(
        Start=doc.Content.End - 1,
        End=doc.Content.End - 1,
    ).Paste()



def replace(placeholder, value):
    last_page_number = doc.ComputeStatistics(2)

    last_page_start = doc.GoTo(
        What=1,
        Which=1,
        Count=last_page_number
    ).Start

    search_range = doc.Range(
        Start=last_page_start,
        End=doc.Content.End
    )

    find = search_range.Find
    find.Text = placeholder

    # while find.Execute():
    #     search_range.Text = str(value)

    if find.Execute():
        search_range.Text = str(value)

def run_replace(dictionary):
    for placeholder, value in dictionary.items():
        replace(placeholder, value)
# Excel
excel = load_workbook('Household Data.xlsx')

sheet = excel['Household Data']

headers = [cell.value for cell in sheet[1]]

column = {name: i for i, name in enumerate(headers)}

hh_ids = []

for row in sheet.iter_rows(min_row=2, values_only=True):
    hh_ids.append(row[column['HH ID']])

hh_ids = list(set(hh_ids))

households = {h: [] for h in hh_ids}

for row in sheet.iter_rows(min_row=2, values_only=True):
    hh_id = row[column['HH ID']]
    households[hh_id].append(row)

# households = {}
# 
# for row in sheet.iter_rows(min_row=2, values_only=True):
#     hh_id = row[column['HH ID']]
#     households.setdefault(hh_id, []).append(row)

today = datetime.today().strftime("%d/%m/%Y")

# surveyor = input('Enter Surveyor Name: ')
surveyor = 'Layt Lar Mal - IT Team'

def member(i, row):

    member = {
        'no': i + 1,
        'name': row[column['Name']],
        'id': row[column['ID']],
        'gender': row[column['Gender']],
        'age': row[column['Age']],
        'dateOfBirth': row[column['Date of Birth']].strftime('%d/%m/%Y'),
        'role': row[column['Role']],
        'occupation': row[column['Occupation']],
        'phone': row[column['Phone']],
    }

    return member

def fill_cell(new_row, data):

    new_row.Cells(1).Range.Text = str(data['no'])
    new_row.Cells(2).Range.Text = str(data['name'])
    new_row.Cells(3).Range.Text = str(data['id'])
    new_row.Cells(4).Range.Text = str(data['gender'])
    new_row.Cells(5).Range.Text = str(data['age'])
    new_row.Cells(6).Range.Text = str(data['dateOfBirth'])
    new_row.Cells(7).Range.Text = str(data['role'])
    new_row.Cells(8).Range.Text = str(data['occupation'])
    new_row.Cells(9).Range.Text = str(data['phone'])

def fill_row(table, rows):
    for i, row in enumerate(rows):
            data = member(i, row)
            fill_cell(table.Rows(i + 2), data)

def go_to_last_page():
    last_page = doc.ComputeStatistics(2)

    word.Selection.GoTo(
        What=1,
        Which=1,
        Count=last_page
    )

def sumcol(rows, col, value):
    return sum(1 for row in rows if row[column[col]] == value)

def age_r_sum(rows, start, end=None):
    return sum(
        1 for row in rows
        if int(row[column['Age']]) >= start
        and (end is None or int(row[column['Age']]) <= end)
    )

def add_table_row(table, rows):
    for i, row in enumerate(rows):
        if i != 0:
            table.Rows.Add()

def gen_info_phs(head_row, welfare_list):
    residence_status = head_row[column['Residence Status']]
    housing_type = head_row[column['Housing Type']]

    main_house_occupation = head_row[column['Occupation']]
    hh_issues_note = head_row[column['Household Issues Note']]

    info_phs = {
        '{Owner}': '☑' if residence_status == 'Owner' else '☐',
        '{Renter}': '☑' if residence_status == 'Renter' else '☐',
        '{IOccupancy}': '☑' if residence_status == 'Informal occupancy' else '☐',
        '{LWRelatives}': '☑' if residence_status == 'Live with relatives' else '☐',

        '{WHouse}': '☑' if housing_type == 'Wooden house' else '☐',
        '{TShelter}': '☑' if housing_type == 'Temporary shelter' else '☐',
        '{Apartment}': '☑' if housing_type == 'Apartment' else '☐',
        '{CHouse}': '☑' if housing_type == 'Concrete house' else '☐',
        '{MMHouse}': '☑' if housing_type == 'Mixed-material house' else '☐',

        '{CSGrant}': '☑' if 'Child support grant' in welfare_list else '☐',
        '{MBenefits}': '☑' if 'Multiple benefits' in welfare_list else '☐',
        '{OPAllowance}': '☑' if 'Older-person allowance' in welfare_list else '☐',
        '{DAllowance}': '☑' if 'Disability allowance' in welfare_list else '☐',
        '{LIAssistance}': '☑' if 'Low-income assistance' in welfare_list else '☐',
        '{HCSupport}': '☑' if 'Health coverage support' in welfare_list else '☐',

        '{HHMOccupation}': main_house_occupation,

        '{HHINote}': hh_issues_note
    }

    return info_phs

total_household = len(households)

def re_run_control():
    print('Invalid Range')
    return run_control()

def run_control():
    print('e.g range 5 or 7 or 10 or full')
    value = input('Enter specific range for Run: ')

    if value.isdigit():
        return int(value) - 1
    elif value.lower() == 'full':
        return value
    else:
        return re_run_control()

def run():

    value = run_control()

    for household_index, (hh_id, rows) in enumerate(households.items()):

        head_row = next(row for row in rows if row[column['Role']] == 'Head')

        table = doc.Tables(doc.Tables.Count - 2)

        title_phs = {
            '{SurveyDate}': today,
            '{HouseNo}': head_row[column['House No']],
            '{HeadName}': head_row[column['Name']],
            '{HHPhone}': head_row[column['Phone']]
        }

        male = sumcol(rows, 'Gender', 'Male')
        female = sumcol(rows, 'Gender', 'Female')
        age_0_14 = age_r_sum(rows, 0, 14)
        age_15_59 = age_r_sum(rows, 15, 59)
        age_60_plus = age_r_sum(rows, 60)
        disable = sumcol(rows, 'Vulnerability', 'Disable')
        bedridden = sumcol(rows, 'Vulnerability', 'Bedridden')

        summary_phs = {
            '{Total}': len(rows),
            '{Male}': male,
            '{Female}': female,
            '{Age0-14}': age_0_14,
            '{Age15-59}': age_15_59,
            '{Age60+}': age_60_plus,
            '{Disable}': disable,
            '{Bedridden}': bedridden
        }

        welfare_list = [row[column['Welfare Benefits']] for row in rows]

        info_phs = gen_info_phs(head_row, welfare_list)

        hs_phs = {
            '{HeadName}': head_row[column['Name']],
            '{Surveyor}': surveyor,
        }

        run_replace(title_phs)

        add_table_row(table, rows)

        fill_row(table, rows)

        run_replace(summary_phs)

        run_replace(info_phs)
        
        run_replace(hs_phs)

        progress = ((household_index + 1) / total_household) * 100

        print(f'Processing {progress: 0f}% / 100%')

        if value != 'full':
            if household_index == value:
                break
        
        if household_index < len(households) - 1:
            page_break()
            go_to_last_page()
            paste_template()


run()

# 