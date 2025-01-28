from fastapi import APIRouter, HTTPException
from app.models import Lead
from app.db import leads_collection
from uuid import uuid4
from typing import List

router = APIRouter(prefix="/leads", tags=["leads"])

@router.post("/", response_model=Lead)
def create_lead(lead: Lead):
    if leads_collection.find_one({"email": lead.email}):
        raise HTTPException(status_code=400, detail="Email already exists")
    lead.id = str(uuid4())
    leads_collection.insert_one(lead.dict())
    return lead

@router.get("/", response_model=List[Lead])
def list_leads():
    leads = list(leads_collection.find())
    for lead in leads:
        lead["id"] = str(lead["_id"])
        del lead["_id"]
    return leads

@router.get("/{lead_id}", response_model=Lead)
def get_lead(lead_id: str):
    lead = leads_collection.find_one({"_id": lead_id})
    if lead:
        lead["id"] = str(lead["_id"])
        del lead["_id"]
        return lead
    raise HTTPException(status_code=404, detail="Lead not found")

@router.put("/{lead_id}", response_model=Lead)
def update_lead(lead_id: str, updated_lead: Lead):
    result = leads_collection.update_one({"_id": lead_id}, {"$set": updated_lead.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Lead not found")
    updated_lead.id = lead_id
    return updated_lead

@router.delete("/{lead_id}")
def delete_lead(lead_id: str):
    result = leads_collection.delete_one({"_id": lead_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Lead not found")
    return {"message": "Lead deleted successfully"}
