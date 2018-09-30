import requests
import json

drug_name = str(input("Введите название препарата (Например Placebo): "))
phase = str(input("Введите фазу испытаний в формате I: "))
params = {
            'arms.interventions.intervention_type': 'Drug',
            'arms.interventions.intervention_name': drug_name,
            'phase.phase': phase}
url = 'https://clinicaltrialsapi.cancer.gov/v1/clinical-trials'
r = requests.get(url, params=params)
json_data = json.loads(r.text)
for i in range(10):
    NCTID = json_data["trials"][i]["nct_id"]
    print(str(NCTID))
