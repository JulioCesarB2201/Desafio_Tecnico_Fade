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
    def get_all(
        page=1,
        per_page=10,
        discipline=None,
        title=None,
        sort=None
    ):

        query = LessonPlan.query

        if discipline:

            query = query.filter(
                LessonPlan.discipline.ilike(
                    f"%{discipline}%"
                )
            )

        if title:

            query = query.filter(
                LessonPlan.title.ilike(
                    f"%{title}%"
                )
            )

        if sort:

            allowed_sorts = [
                "planned_date",
                "created_at",
                "title"
            ]

            if sort in allowed_sorts:

                query = query.order_by(
                    getattr(
                        LessonPlan,
                        sort
                    )
                )

        pagination = query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        return pagination

    @staticmethod
    def get_by_id(plan_id):
        return db.session.get(
            LessonPlan,
            plan_id
        )

    @staticmethod
    def delete(lesson_plan):
        db.session.delete(lesson_plan)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()