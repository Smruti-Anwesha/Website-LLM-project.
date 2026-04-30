def plan_website(user_prompt):
    user_prompt = user_prompt.lower()

    if "restaurant" in user_prompt:
        return {
            "type": "restaurant",
            "sections": ["hero", "menu", "gallery", "contact"]
        }

    elif "portfolio" in user_prompt:
        return {
            "type": "portfolio",
            "sections": ["hero", "projects", "skills", "contact"]
        }

    elif "bakery" in user_prompt:
        return {
            "type": "bakery",
            "sections": ["hero", "gallery", "contact"]
        }

    elif "startup" in user_prompt or "business" in user_prompt:
        return {
            "type": "startup",
            "sections": ["hero", "features", "projects", "contact"]
        }

    else:
        return {
            "type": "general",
            "sections": ["hero", "about", "contact"]
        }