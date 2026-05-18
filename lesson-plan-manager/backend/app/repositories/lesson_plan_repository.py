from app.database.db import db
from app.models.lesson_plan import LessonPlan


class LessonPlanRepository:
    
    @staticmethod
    def create(data):
        lesson_plan = LessonPlan(**data)
        db.session.add(lesson_plan)
        db.session.commit()
        
        return lesson_plan

    @staticmethod
    def get_all():
        return LessonPlan.query.all()

    @staticmethod
    def get_by_id(plan_id):
        return LessonPlan.query.get(plan_id)

    @staticmethod
    def delete(lesson_plan):
        db.session.delete(lesson_plan)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()