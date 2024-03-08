import sys
import time

from patient import Patient

start = round(time.time() * 1000)

patient1 = Patient('Bob', 'Smith')
print(patient1.last_name)
print(patient1.full_name)
print(patient1.name)

end = round(time.time() * 1000)
print(end - start)
