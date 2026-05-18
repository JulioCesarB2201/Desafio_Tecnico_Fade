from flask import Blueprint
from flask import jsonify
from flask import request

from app.services.lesson_plan_service import (
    LessonPlanService
)

lesson_plan_bp = Blueprint(
    "lesson_plan_bp",
    __name__
)


@lesson_plan_bp.route(
    "/plans",
    methods=["POST"]
)

def create_plan():

    data = request.get_json()
    lesson_plan = LessonPlanService.create(data)

    return jsonify(
        lesson_plan.to_dict()
    ), 201


@lesson_plan_bp.route(
    "/plans",
    methods=["GET"]
)
def get_all_plans():

    lesson_plans = LessonPlanService.get_all()

    return jsonify([
        plan.to_dict()
        for plan in lesson_plans
    ])