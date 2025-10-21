from sqlalchemy import SmallInteger, String, Text, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.core.database import Base
from typing import List


class CertificateType(Base):
    __tablename__ = 'certificate_types'

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(12))
    title: Mapped[str] = mapped_column(String(40))
    hours: Mapped[int] = mapped_column(SmallInteger, default=0)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    certificate_themes: Mapped[List["CertificateTheme"]] = relationship("CertificateTheme",
                                                                        back_populates="certificate_type")

    def __str__(self):
        return self.name
