import pandas as pd
import os
print(os.listdir('W:/Workforce Monthly Reports/Monthly_Reports/Oct-19 Snapshot/'))
df = pd.read_excel('W:/Workforce Monthly Reports/Monthly_Reports/Oct-19 Snapshot/GGC Balanced Scorecard - Oct-19.xls',
                   sheet_name='Department')
print(df.columns)
df = df[df['Sector/Directorate/HSCP'] == 'West Dunbartonshire HSCP']

dir1 = {'Addictions - Hscp West Dun':'Mental Health, Learning Disability & Addictions',
        'Adult Community Services':'', #TODO fix this
       'Change Fund Hscp - West Dun':'Community Health & Care',
       'Child Services - Community - West Dun':'Child Health and Criminal Justice',
       'Health & Community Care - Hscp West Dun':'Community Health & Care',
       'Learning Disabilities - Hscp West Dun':'Mental Health, Learning Disability & Addictions',
       'Mental Health Adult Comm Services - Hscp West Dun':'Mental Health, Learning Disability & Addictions',
       'Mental Health Elderly Services - Hscp West Dun':'Mental Health, Learning Disability & Addictions',
       'Msk Physiotherapy-hosted Serv':'Msk Physiotherapy',
       'Planning & Health Improvement - Hscp West Dun':'Strategy, Planning & Health Improvement',
       'Retinal Screening':'Retinal Screening',
       'Wst Dun Administration + Management':'Community Health & Care'}

dir2 = {'Drug Treat & Test Orders':'Mental Health, Learning Disability & Addictions',
        'Wst Dun: Cats':'Mental Health, Learning Disability & Addictions',
        'Effective Care At Time of Tran':'Community Health & Care',
        'Hospital & Care Homes':'Community Health & Care',
        'Preventative & Anticipatory Care':'Community Health & Care',
        'Proactive Care & Support At Home':'Mental Health, Learning Disability & Addictions',
        "Health Visiting - Childrens' Services 1":'Child Health and Criminal Justice',
        'Parenting Strategy':'Child Health and Criminal Justice',
        "School Nursing - Childrens' Services 1":'Child Health and Criminal Justice',
        "Senior Nursing - Childrens' Services":'Child Health and Criminal Justice',
        'Specialist Children Services Wst Dun':'Child Health and Criminal Justice',
        'Young Families Support':'Child Health and Criminal Justice',
        'Diabetes Pp - Health & Comm Care 2':'Community Health & Care',
        'District Nursing - Hlth & Community Care 3':'Community Health & Care',
        'Older People Rehabilitation Services':'Community Health & Care',
        'Out of Hours Nursing - Hlth & Comm Care 2':'Community Health & Care',
        'Treatment Room Nursing':'Community Health & Care',
        'Wst Dun: Management Hlth & Cc':'Senior Management Team',
        'Wst Dun: Oth Comm Nursing':'Community Health & Care',
        'Wst Dun: Youth Enablement':'Community Health & Care',
        'Hscp-Wdc: Learning Disab':'Mental Health, Learning Disability & Addictions',
        'Amh Crisis Service':'Mental Health, Learning Disability & Addictions',
        'Amh Other Community Services':'Mental Health, Learning Disability & Addictions',
        'Management Mental Health':'Mental Health, Learning Disability & Addictions',
        'Primary Care Mental Health':'Mental Health, Learning Disability & Addictions',
        'Wst Dun: Adult Community Mh':'Mental Health, Learning Disability & Addictions',
        'Wdn Transfer from Glenkirk':'Mental Health, Learning Disability & Addictions',
        'Wst Dun: Elderly Community Mental Health':'Mental Health, Learning Disability & Addictions',
        'Wst.Dun : Elderly Mh Inpatient':'Mental Health, Learning Disability & Addictions',
        'Msk Physiotherapy-hosted Serv':'Msk Physiotherapy',
        'Health Improvement - Planning 3':'Strategy, Planning & Health Improvement',
        'West Dunbartonshire Planning':'Strategy, Planning & Health Improvement',
        'Wst Dun: Management Plan & Hi':'Senior Management Team',
        'Retinal Screening':'Retinal Screening',
        'Wst Dun Accommodation':'a', #TODO FIX THESE when Fiona replies
        'Wst Dun Other':'a',
        'Chp-Wdc: Nursing General':'a',
        'Other Nursing':'a',
        'Wst Dun Other Admin Staff':'a'
        }
df['West_Dun_Name_dir1'] = df['Sub-Directorate 1'].map(dir1)
df['West_Dun_Name_dir2'] = df['Sub-Directorate 2'].map(dir2)
df.to_csv('W:/West Dunbartonshire HSCP/test.csv', index=False)

piv = pd.pivot_table(df, values='WTE')
#df = df[df['']]