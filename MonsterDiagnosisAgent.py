import numpy as np
from itertools import combinations
class MonsterDiagnosisAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    @staticmethod
    def convertToNumericNumpyArray(symptoms):
        numeric_array = np.array([1 if v == '+' else -1 if v == '-' else 0 for v in symptoms.values()])
        return numeric_array

    @staticmethod
    def convertToDiseaseDictionary(np_symptoms):
        disease_dict = {chr(65+i): '+' if v > 0 else ('0' if v == 0 else '-') for i, v in enumerate(np_symptoms)}
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

    @staticmethod
    def diagnosisBruteForce(diseases, patient):
        array_count = len(diseases)
        for i in range(1, array_count + 1):
            for disease_combination in combinations(diseases, i):
                if np.all(np.sign(np.sum(disease_combination, axis=0)) == np.sign(patient)):
                    return disease_combination
        return []

    def diagnoseMonster(self, diseases, patient):
        patient_np_array = self.convertToNumericNumpyArray(patient)
        diseases_np_arrays = []
        for disease in diseases.values():
            diseases_np_arrays.append(self.convertToNumericNumpyArray(disease))
        np_diagnosis = self.diagnosisBruteForce(diseases_np_arrays, patient_np_array)
        diagnosis = self.convertToDiseaseList(np_diagnosis, diseases)
        return diagnosis

    def solve(self, diseases, patient):
        return self.diagnoseMonster(diseases, patient)

