from app.repositories.lesson_plan_repository import (
    LessonPlanRepository
)

class LessonPlanService:

    @staticmethod
    def create(data):
        return LessonPlanRepository.create(data)

    @staticmethod
    def get_all():
        return LessonPlanRepository.get_all()

    @staticmethod
    def get_by_id(plan_id):
        return LessonPlanRepository.get_by_id(plan_id)