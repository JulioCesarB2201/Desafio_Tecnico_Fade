from datetime import datetime
from app.database.db import db

class LessonPlan(db.Model):

    __tablename__ = "lesson_plans"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    objective = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    planned_date = db.Column(db.Date, nullable=False)
    discipline = db.Column(db.String(100), nullable=False)
    contents = db.Column(db.Text)
    support_resources = db.Column(db.Text)
    tags = db.Column(db.String(255))
    
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "objective": self.objective,
            "summary": self.summary,
            "planned_date": self.planned_date.isoformat(),
            "discipline": self.discipline,
            "contents": self.contents,
            "support_resources": self.support_resources,
            "tags": self.tags,
            "created_at": self.created_at.isoformat()
        }