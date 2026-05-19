from flask import Blueprint
from flask import jsonify
from flask import request
from flasgger import swag_from

from app.services.lesson_plan_service import (
    LessonPlanService
)

lesson_plan_bp = Blueprint(
    "lesson_plan_bp",
    __name__
)

@swag_from({
    "tags": ["Lesson Plans"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "example": "OSPF Básico"
                    },
                    "objective": {
                        "type": "string",
                        "example": "Aprender OSPF"
                    },
                    "summary": {
                        "type": "string",
                        "example": "Introdução ao protocolo"
                    },
                    "planned_date": {
                        "type": "string",
                        "example": "2026-05-20"
                    },
                    "discipline": {
                        "type": "string",
                        "example": "Redes"
                    },
                    "contents": {
                        "type": "string",
                        "example": "OSPF, LSAs"
                    },
                    "support_resources": {
                        "type": "string",
                        "example": "Packet Tracer"
                    },
                    "tags": {
                        "type": "string",
                        "example": "redes,ospf"
                    }
                }
            }
        }
    ],
    "responses": {
        201: {
            "description": "Lesson plan created successfully"
        }
    }
})

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


@swag_from({
    "tags": ["Lesson Plans"],
    "parameters": [
        {
            "name": "page",
            "in": "query",
            "type": "integer",
            "required": False,
            "default": 1
        },
        {
            "name": "per_page",
            "in": "query",
            "type": "integer",
            "required": False,
            "default": 10
        },
        {
            "name": "discipline",
            "in": "query",
            "type": "string",
            "required": False
        },
        {
            "name": "title",
            "in": "query",
            "type": "string",
            "required": False
        },
        {
            "name": "sort",
            "in": "query",
            "type": "string",
            "required": False
        }
    ],
    "responses": {
        200: {
            "description": "List of lesson plans"
        }
    }
})

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

    discipline = request.args.get(
        "discipline"
    )

    title = request.args.get(
        "title"
    )
    
    sort = request.args.get(
        "sort"
    )

    pagination = LessonPlanService.get_all(
        page,
        per_page,
        discipline,
        title,
        sort
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

@swag_from({
    "tags": ["Lesson Plans"],
    "parameters": [
        {
            "name": "plan_id",
            "in": "path",
            "type": "integer",
            "required": True
        }
    ],
    "responses": {
        200: {
            "description": "Lesson plan found"
        },
        404: {
            "description": "Lesson plan not found"
        }
    }
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

@swag_from({
    "tags": ["Lesson Plans"],
    "parameters": [
        {
            "name": "plan_id",
            "in": "path",
            "type": "integer",
            "required": True
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "example": "Plano Atualizado"
                    }
                }
            }
        }
    ],
    "responses": {
        200: {
            "description": "Lesson plan updated successfully"
        },
        404: {
            "description": "Lesson plan not found"
        }
    }
})
    
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

@swag_from({
    "tags": ["Lesson Plans"],
    "parameters": [
        {
            "name": "plan_id",
            "in": "path",
            "type": "integer",
            "required": True
        }
    ],
    "responses": {
        200: {
            "description": "Lesson plan deleted successfully"
        },
        404: {
            "description": "Lesson plan not found"
        }
    }
})
    
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