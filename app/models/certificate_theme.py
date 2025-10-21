from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class CertificateTheme(Base):

    __tablename__ = 'certificate_themes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40))
    description: Mapped[str] = mapped_column(Text, nullable=True)
    certificate_type_id: Mapped[int] = mapped_column(ForeignKey("certificate_types.id"))
    certificate_type: Mapped["CertificateType"] = relationship("CertificateType", back_populates="certificate_themes")