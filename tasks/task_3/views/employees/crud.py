from dataclasses import dataclass, field
from .schemas import Employee, EmployeeCreate


@dataclass
class EmployeeStorage:
    last_id: int = 0
    employees: dict[int, Employee] = field(default_factory=dict)

    @property
    def next_id(self):
        self.last_id = self.last_id + 1
        return self.last_id

    def create_employee(self, employee_create: EmployeeCreate) -> Employee:
        employee = Employee(id=self.next_id, **employee_create.model_dump())
        self.employees[employee.id] = employee
        return employee

    def get_employees(self) -> list[Employee]:
        return list(self.employees.values())

    def get_employee_by_id(self, employee_id: int):
        return self.employees.get(employee_id)

    def delete_employee_by_id(self, employee_id: int):
        self.employees.pop(employee_id, None)


storage = EmployeeStorage()
