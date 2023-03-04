import numpy as np

class MonsterDiagnosisAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    def convertToNumericNumpyArray(self, symptoms):
        numeric_array = np.array([1 if v == '+' else -1 if v == '-' else 0 for v in symptoms.values()])
        return numeric_array

    def convertToDiseaseDictionary(self, np_symptoms):
        disease_dict = {chr(65+i): '+' if n > 0 else ('0' if n == 0 else '-') for i, n in enumerate(np_symptoms)}
        return disease_dict

    def convertToDiseaseList(self, np_disease_list, diseases):
        disease_list = []
        for array in np_disease_list:
            disease_dict = self.convertToDiseaseDictionary(array)
            for key, value in diseases.items():
                if value == disease_dict:
                    disease_list.append(key)
                    break
        return disease_list


    def recursiveDiagnostic(self, diseases, patient, range):
        if np.all(np.sign(np.sum(diseases[:range], axis=0)) == np.sign(patient)):
            return diseases[:range]
        elif range >= len(diseases):
            return None
        else:
            return self.recursiveDiagnostic(diseases, patient, range+1)

    def diagnoseMonster(self, diseases, patient):
        patient_np_array = self.convertToNumericNumpyArray(patient)
        diseases_np_arrays = []
        for disease in diseases.values():
            diseases_np_arrays.append(self.convertToNumericNumpyArray(disease))
        lists_of_diagnoses = []
        for n in range(len(diseases_np_arrays)):
            # index_start = np.where(diseases_np_arrays == disease)[0][0]
            lists_of_diagnoses.append(self.recursiveDiagnostic(diseases_np_arrays[n:], patient_np_array, 1))
        lists_of_diagnoses = [x for x in lists_of_diagnoses if x is not None]
        simplest_np_diagnosis = min(lists_of_diagnoses, key=len)
        diagnosis = self.convertToDiseaseList(simplest_np_diagnosis, diseases)
        return diagnosis

    def solve(self, diseases, patient):
        return self.diagnoseMonster(diseases, patient)

