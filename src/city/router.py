from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.dependencies import get_db

from src.city import crud, schemas


router = APIRouter()


@router.get("/cities", response_model=list[schemas.City])
async def read_cities(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_cities(db=db)


@router.get("/cities/{city_id}", response_model=schemas.CityDetailed)
async def read_city(city_id: int, db: AsyncSession = Depends(get_db)):
    print("city_id in router func: ", city_id)
    return await crud.get_city_detail(db=db, city_id=city_id)


@router.put("/cities/{city_id}", response_model=schemas.CityDetailed)
async def update_city(
        city_id: int,
        city: schemas.CityIn,
        db: AsyncSession = Depends(get_db)
):
    return await crud.update_city(db=db, city_id=city_id, city=city)


@router.delete("/cities/{city_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_city(city_id: int, db: AsyncSession = Depends(get_db)):
    await crud.delete_city(db, city_id)
    return


@router.post("/cities", response_model=schemas.City)
async def create_city(
        city: schemas.CityIn,
        db: AsyncSession = Depends(get_db)
):
    return await crud.create_city(db=db, city=city)