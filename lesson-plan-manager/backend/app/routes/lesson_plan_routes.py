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

    try:
        data = request.get_json()
        lesson_plan = LessonPlanService.create(
            data
        )

        return jsonify(
            lesson_plan.to_dict()
        ), 201

    except ValueError as e:

        return jsonify({
            "error": str(e)
        }), 400
        
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@lesson_plan_bp.route(
    "/plans",
    methods=["GET"]
)
def get_all_plans():

    page = request.args.get(
        "page",
        default=1,
        type=int
    )

    per_page = request.args.get(
        "per_page",
        default=10,
        type=int
    )

    pagination = LessonPlanService.get_all(
        page,
        per_page
    )

    return jsonify({
        "items": [
            plan.to_dict()
            for plan in pagination.items
        ],
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.page
    })
    
@lesson_plan_bp.route(
    "/plans/<int:plan_id>",
    methods=["GET"]
)

def get_plan_by_id(plan_id):

    lesson_plan = LessonPlanService.get_by_id(
        plan_id
    )

    if not lesson_plan:

        return jsonify({
            "error": "Lesson plan not found"
        }), 404

    return jsonify(
        lesson_plan.to_dict()
    )
    
@lesson_plan_bp.route(
    "/plans/<int:plan_id>",
    methods=["PUT"]
)

def update_plan(plan_id):

    data = request.get_json()
    updated_plan = LessonPlanService.update(
        plan_id,
        data
    )

    if not updated_plan:
        return jsonify({
            "error": "Lesson plan not found"
        }), 404

    return jsonify(
        updated_plan.to_dict()
    )
    
@lesson_plan_bp.route(
    "/plans/<int:plan_id>",
    methods=["DELETE"]
)

def delete_plan(plan_id):
    deleted = LessonPlanService.delete(
        plan_id
    )

    if not deleted:
        return jsonify({
            "error": "Lesson plan not found"
        }), 404

    return jsonify({
        "message": "Lesson plan deleted"
    })