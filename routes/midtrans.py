from fastapi import APIRouter
from service.midtrans_service import MidtransService
from domain.requests.midtrans.create import MidtransRequest

midtransrouter = APIRouter(prefix="/midtrans", tags=["Midtrans"])


@midtransrouter.post("/transaction")
def create_transaction(dto: MidtransRequest):
    return MidtransService.createTransaction(dto=dto)
