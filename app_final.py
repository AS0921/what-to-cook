import csv
from pathlib import Path

from fastapi import FastAPI, HTTPException

APP_VERSION = "0.1.1"
RECIPES_FILE = Path(__file__).parent / "recipes.csv"

def load_recipes():
    recipes = []
    with open(RECIPES_FILE, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            recipes.append({
                "id": int(row["id"]),
                "name": row["name"].strip(),
                "ingredients": [item.strip().lower() for item in row["ingredients"].split(";")],
            })
    return recipes


RECIPES = load_recipes()


app = FastAPI(title="Что приготовить")

@app.get("/")
def root():
    return {"message": "Сервис подбора блюд работает"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": APP_VERSION}

@app.get("/recipes")
def list_recipes():
    return RECIPES

@app.get("/recipes/{recipe_id}")
def get_recipe(recipe_id: int):
    for recipe in RECIPES:
        if recipe["id"] == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail="Блюдо не найдено")