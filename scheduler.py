import sys
import time

from patient import Patient
from clinician import Clinician

start = time.time() * 1000

patient1 = Patient('Bob', 'Smith')
print(patient1.name)

clinician1 = Clinician('Matt', 'Ford', 'Surgeon', '12345')
print(clinician1.all)

clinician2 = Clinician('Mandy', 'Jones', 'Charge Nurse', '12340')
print(clinician2.all)

end = time.time() * 1000
print(end - start)
