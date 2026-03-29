from app import create_app, db
from app.models.user import User
from dotenv import load_dotenv

load_dotenv()

app = create_app()


def seed_users():
    users = [
        User(
            first_name="Admin",
            last_name="User",
            email="admin@example.com",
            is_admin=True,
        ),
        User(
            first_name="Alice",
            last_name="Nguyen",
            email="alice.nguyen@example.com",
        ),
        User(
            first_name="Marcus",
            last_name="Torres",
            email="marcus.torres@example.com",
        ),
        User(
            first_name="Priya",
            last_name="Patel",
            email="priya.patel@example.com",
        ),
        User(
            first_name="Jordan",
            last_name="Kim",
            email="jordan.kim@example.com",
        ),
    ]

    db.session.add_all(users)
    db.session.commit()
    print("Seeded users!")


if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_users()