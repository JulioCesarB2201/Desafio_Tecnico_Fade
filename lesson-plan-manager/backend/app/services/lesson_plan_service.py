from datetime import datetime
from app.repositories.lesson_plan_repository import (
    LessonPlanRepository
)

class LessonPlanService:

    @staticmethod
    def create(data):

        data["planned_date"] = datetime.strptime(
            data["planned_date"],
            "%Y-%m-%d"
        ).date()

        return LessonPlanRepository.create(data)

    @staticmethod
    def get_all():
        return LessonPlanRepository.get_all()

    @staticmethod
    def get_by_id(plan_id):
        return LessonPlanRepository.get_by_id(plan_id)
    
    @staticmethod
    def update(plan_id, data):
        lesson_plan = LessonPlanRepository.get_by_id(
            plan_id
        )

        if not lesson_plan:
            return None

        for key, value in data.items():
            setattr(
                lesson_plan,
                key,
                value
            )

        LessonPlanRepository.update()
        return lesson_plan
    
    @staticmethod
    def delete(plan_id):
        lesson_plan = LessonPlanRepository.get_by_id(
            plan_id
        )

        if not lesson_plan:
            return False

        LessonPlanRepository.delete(
            lesson_plan
        )

        return True