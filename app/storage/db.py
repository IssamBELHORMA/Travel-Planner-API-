import os
from datetime import datetime, timezone
import uuid
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# 1. Chargement des variables d'environnement du fichier .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "votre_mot_de_passe_ici")
DB_NAME = os.getenv("DB_NAME", "travel_planner")
DB_PORT = os.getenv("DB_PORT", "3306")

# Construction de l'URL de connexion MySQL avec le driver pymysql
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 2. Initialisation de SQLAlchemy
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# 3. Définition des Modèles SQLAlchemy
class UserModel(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)


class ActivityModel(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(100), nullable=False, index=True)
    activity_name = Column(String(255), nullable=False)


# 4. Dépendance FastAPI pour obtenir une session de base de données propre
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 5. Fonctions d'interaction avec la base de données (Users)
def list_users(db) -> list:
    """Retourne la liste de tous les utilisateurs sous forme de dictionnaires."""
    users = db.query(UserModel).all()
    return [
        {
            "id": u.id,
            "email": u.email,
            "hashed_password": u.hashed_password,
            "created_at": u.created_at.isoformat()
        } for u in users
    ]

def find_user_by_email(db, email: str):
    """Cherche un utilisateur par son email (insensible à la casse)."""
    user = db.query(UserModel).filter(UserModel.email.ilike(email)).first()
    if user:
        return {
            "id": user.id,
            "email": user.email,
            "hashed_password": user.hashed_password,
            "created_at": user.created_at.isoformat()
        }
    return None

def create_user(db, email: str, hashed_password: str) -> dict:
    """Crée et enregistre un nouvel utilisateur en base de données."""
    new_user = UserModel(
        id=str(uuid.uuid4()),
        email=email.lower(),
        hashed_password=hashed_password,
        created_at=datetime.now(timezone.utc)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "id": new_user.id,
        "email": new_user.email,
        "hashed_password": new_user.hashed_password,
        "created_at": new_user.created_at.isoformat()
    }


# 6. Fonctions d'interaction avec la base de données (Activities)
def get_activities_by_city(db, city: str) -> list:
    """Récupère les activités d'une ville depuis MySQL. Renvoie le défaut si vide."""
    key = city.strip().lower()
    
    # 1. On cherche les activités pour la ville demandée
    results = db.query(ActivityModel.activity_name).filter(ActivityModel.city == key).all()
    
    if results:
        # On extrait la chaîne de caractères du tuple renvoyé par SQLAlchemy
        return [r[0] for r in results]
        
    # 2. Si aucune activité n'est trouvée, on renvoie les activités par défaut
    default_results = db.query(ActivityModel.activity_name).filter(ActivityModel.city == "default").all()
    return [r[0] for r in default_results]


# Crée les tables si elles n'existent pas (utile en développement)
Base.metadata.create_all(bind=engine)