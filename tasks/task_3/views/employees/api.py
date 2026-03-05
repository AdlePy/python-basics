from fastapi import APIRouter, HTTPException, status
from .crud import storage
from .schemas import Employee, EmployeeCreate


router = APIRouter(prefix="employees", tags=["employees"])


@router.get("/", response_model=list[Employee])
async def get_employee_list() -> list[Employee]:
    return storage.get_employees()


@router.get("/{employee_id}", response_model=Employee)
async def get_employee_by_id(employee_id: int) -> Employee:
    employee = storage.get_employee_by_id(employee_id=employee_id)

    if employee is not None:
        return employee

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"could not found employee #{employee_id}",
    )


@router.post("/", response_model=Employee)
async def create_employee(employee_create: EmployeeCreate) -> Employee:
    return storage.create_employee(employee_create=employee_create)


@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee_by_id(employee_id: int) -> None:
    storage.delete_employee_by_id(employee_id=employee_id)
