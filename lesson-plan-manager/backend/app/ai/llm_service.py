import os
import json
import requests


OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)


def generate_mock_plan(topic):

    return {
        "title": f"Introdução a {topic}",
        "objective":
            f"Compreender os conceitos de {topic}",

        "summary":
            f"Plano introdutório sobre {topic}",

        "planned_date": "2026-06-01",

        "discipline": "Redes",

        "contents":
            f"Fundamentos de {topic}",

        "support_resources":
            "Slides, Packet Tracer",

        "tags":
            f"{topic.lower()},redes"
    }


def generate_lesson_plan(topic):

    prompt = f"""
    Create a lesson plan in JSON format.

    Topic:
    {topic}

    Return ONLY valid JSON.
    """

    try:

        response = requests.post(
            url=
            "https://openrouter.ai/api/v1/chat/completions",

            headers={
                "Authorization":
                    f"Bearer {OPENROUTER_API_KEY}",

                "Content-Type":
                    "application/json"
            },

            json={
                "model":
                    "openai/gpt-3.5-turbo",

                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        )

        data = response.json()

        print(data)

        if "choices" not in data:

            print(
                "LLM unavailable. Using mock."
            )

            return generate_mock_plan(
                topic
            )

        content = (
            data["choices"][0]
            ["message"]
            ["content"]
        )

        content = content.replace(
            "```json",
            ""
        )

        content = content.replace(
            "```",
            ""
        )

        content = content.strip()

        return json.loads(content)

    except Exception as e:

        print(
            f"LLM exception: {e}"
        )

        return generate_mock_plan(
            topic
        )