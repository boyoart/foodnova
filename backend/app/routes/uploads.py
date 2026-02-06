from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from ..core.config import settings

router = APIRouter(prefix="/uploads", tags=["Uploads"])


@router.get("/{filename}")
async def get_uploaded_file(filename: str):
    file_path = Path(settings.UPLOAD_DIR) / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(file_path)
