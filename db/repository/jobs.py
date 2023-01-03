from sqlalchemy.orm import Session
from db.schemas.jobs import JobCreate
from db.models.jobs import Job


def create_new_job(job: JobCreate, db: Session, owner_id: int):
    job = Job(**job.dict(), owner_id=owner_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def retreive_job(id: int, db: Session):
    # item = db.query(Job).filter(Job.id == id).first()
    item = db.query(Job).get(id)
    return item


def list_jobs(db: Session):
    items = db.query(Job).all()
    return items


def update_job_by_id(id: int, job: JobCreate, db: Session, owner_id):
    # existing_job = db.query(Job).get(id)
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0
    job.__dict__.update(owner_id=owner_id)
    existing_job.update(job.__dict__)
    db.commit()
    return 1


def delete_job_by_id(id: int, db: Session, owner_id):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0
    existing_job.delete(synchronize_session=False)
    db.commit()
    return 1



