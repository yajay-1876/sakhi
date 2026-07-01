from sqlalchemy import Column, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
import datetime

Base = declarative_base()

def _now_utc():
    return datetime.datetime.now(datetime.timezone.utc)

# ==========================================
# PARENT CLASS
# ==========================================
class Organization(Base):
    __tablename__ = "corp_registry"  # <-- DB Table Name

    id         = Column(Text, primary_key=True)
    name       = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=_now_utc)

    # Relationship setup
    roster = relationship(
        "Worker",                       # 1. Targets the CHILD CLASS NAME
        back_populates="employer",      # 2. Targets the attribute inside the Child Class
        order_by="Worker.joined_date",  # 3. Uses CHILD CLASS NAME . attribute
        cascade="all, delete-orphan",
    )

# ==========================================
# CHILD CLASS
# ==========================================
class Worker(Base):
    __tablename__ = "payroll_staff"  # <-- DB Table Name

    id          = Column(Text, primary_key=True)
    name        = Column(Text, nullable=False)
    joined_date = Column(DateTime(timezone=True), nullable=False, default=_now_utc)
    
    # ForeignKey links directly to the PARENT DB TABLE NAME and its column
    firm_id = Column(Text, ForeignKey("corp_registry.id"), nullable=False)

    # Relationship setup
    employer = relationship(
        "Organization",                 # 1. Targets the PARENT CLASS NAME
        back_populates="roster"         # 2. Targets the attribute inside the Parent Class
    )

# Fetching an organization instance
my_org = session.query(Organization).first()

# 1. Accessing the list
print(my_org.roster)  
# Output: [<Worker id=1>, <Worker id=2>]

# 2. It's a standard list, so you can loop through it
for worker in my_org.roster:
    print(worker.name)

# 3. You can modify the relationship by using standard list methods
new_worker = Worker(id="W3", name="Alice")
my_org.roster.append(new_worker)  # SQLAlchemy automatically handles the foreign key behind the scenes!