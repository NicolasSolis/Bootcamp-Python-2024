from persona import Persona, Supervisor, SupervisorZona
print("******")
supervisorzona1 = SupervisorZona('Juan', 'Pérez', 123456, 'Sur', 8,
25, 123)
supervisor1 = Supervisor('Pedro', 'Carrillo', 123456, 'Norte')
print("supervisorzona1")
# Es instancia supervisorzona1 de Persona
print(isinstance(supervisorzona1, Persona))
# Es instancia supervisorzona1 de Supervisor
print(isinstance(supervisorzona1, Supervisor))
# Es instancia supervisorzona1 de SupervisorZona
print(isinstance(supervisorzona1, SupervisorZona))
print("supervisor")
# Es instancia supervisor de Persona
print(isinstance(supervisor1, Persona))
# Es instancia supervisor de Supervisor
print(isinstance(supervisor1, Supervisor))
# Es instancia supervisor de SupervisorZona
print(isinstance(supervisor1, SupervisorZona))