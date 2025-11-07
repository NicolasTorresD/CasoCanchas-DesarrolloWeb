from fastapi import APIRouter, Depends, HTTPException
from app.schemas.cancha import CanchaCreate, CanchaResponse
from app.services.cancha_service import CanchaService
from app.core.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=CanchaResponse)
async def create_cancha(cancha: CanchaCreate, current_user: str = Depends(get_current_user)):
    return await CanchaService.create_cancha(cancha, current_user)

@router.get("/{cancha_id}", response_model=CanchaResponse)
async def read_cancha(cancha_id: int, current_user: str = Depends(get_current_user)):
    cancha = await CanchaService.get_cancha(cancha_id)
    if not cancha:
        raise HTTPException(status_code=404, detail="Cancha not found")
    return cancha

@router.get("/", response_model=list[CanchaResponse])
async def read_canchas(current_user: str = Depends(get_current_user)):
    return await CanchaService.get_all_canchas()

@router.put("/{cancha_id}", response_model=CanchaResponse)
async def update_cancha(cancha_id: int, cancha: CanchaCreate, current_user: str = Depends(get_current_user)):
    updated_cancha = await CanchaService.update_cancha(cancha_id, cancha)
    if not updated_cancha:
        raise HTTPException(status_code=404, detail="Cancha not found")
    return updated_cancha

@router.delete("/{cancha_id}", response_model=dict)
async def delete_cancha(cancha_id: int, current_user: str = Depends(get_current_user)):
    result = await CanchaService.delete_cancha(cancha_id)
    if not result:
        raise HTTPException(status_code=404, detail="Cancha not found")
    return {"detail": "Cancha deleted successfully"}