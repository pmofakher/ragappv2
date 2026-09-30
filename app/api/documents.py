from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.user import User
from app.models.document import Document
from app.core.dependencies import get_current_user
from app.services.document_processor import process_document

from app.services.documents import (
    get_user_documents,
    get_user_document,
    delete_document,
)
import os


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


UPLOAD_DIR = "uploads"


os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    filepath = f"{UPLOAD_DIR}/{file.filename}"


    content = await file.read()


    with open(filepath, "wb") as f:
        f.write(content)


    document = Document(
        filename=file.filename,
        filepath=filepath,
        user_id=current_user.id
    )


    db.add(document)

    await db.commit()

    await db.refresh(document)

    result = await process_document(
    filepath=document.filepath,
    document_id=document.id,
    user_id=current_user.id,
    filename=document.filename
)

    return {
    "id": document.id,
    "filename": document.filename,
    "chunks": result["chunks"]
}

@router.get("/")
async def list_documents(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    documents = await get_user_documents(
        db,
        current_user.id
    )

    return [
        {
            "id": document.id,
            "filename": document.filename,
            "filepath": document.filepath,
        }
        for document in documents
    ]


@router.get("/{document_id}")
async def get_document(
    document_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    document = await get_user_document(
        db,
        document_id,
        current_user.id
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return {
        "id": document.id,
        "filename": document.filename,
        "filepath": document.filepath,
    }


@router.delete("/{document_id}")
async def remove_document(
    document_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    document = await get_user_document(
        db,
        document_id,
        current_user.id
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    await delete_document(
        db,
        document
    )

    return {
        "message": "Document deleted successfully"
    }