from datetime import datetime
from app.repositories.lesson_plan_repository import (
    LessonPlanRepository
)

class LessonPlanService:
    REQUIRED_FIELDS = [
        "title",
        "objective",
        "summary",
        "planned_date",
        "discipline",
        "contents"
    ]

    @staticmethod
    def validate(data):

        missing_fields = []

        for field in LessonPlanService.REQUIRED_FIELDS:

            if field not in data or not data[field]:

                missing_fields.append(field)

        if missing_fields:

            raise ValueError(
                f"Missing required fields: {missing_fields}"
            )
            
    @staticmethod
    def create(data):

        LessonPlanService.validate(data)
        
        data["planned_date"] = datetime.strptime(
            data["planned_date"],
            "%Y-%m-%d"
        ).date()

        return LessonPlanRepository.create(data)

    @staticmethod
    def get_all(
        page,
        per_page,
        discipline=None,
        title=None,
        sort=None
    ):

        return LessonPlanRepository.get_all(
            page,
            per_page,
            discipline,
            title,
            sort
        )

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