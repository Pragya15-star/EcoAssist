from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI, RateLimitError

app = FastAPI(title="EcoAssist API")

client = OpenAI()

# Allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Home route
@app.get("/")
def home():
    return {
        "message": "EcoAssist backend is running successfully! 🌱"
    }


# Health check
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# Question-answer endpoint
@app.post("/ask")
def ask_question(data: dict):
    question = data.get("question", "").strip()

    if not question:
        return {
            "answer": "Please enter a question."
        }

    question_lower = question.lower()

    # Sustainability
    if "sustainability" in question_lower:
        answer = (
            "Sustainability means using natural resources responsibly "
            "so that people today can meet their needs without harming "
            "future generations. 🌱"
        )

    # Water
    elif "water" in question_lower:
        answer = (
            "You can save water by fixing leaks, turning off the tap "
            "while brushing, taking shorter showers, and reusing water "
            "where appropriate. 💧"
        )

    # Recycling
    elif "recycle" in question_lower or "recycling" in question_lower:
        answer = (
            "Recycling helps reduce waste and conserve resources. "
            "Separate recyclable materials according to local recycling rules. ♻️"
        )

    # Climate change
    elif (
        "climate change" in question_lower
        or "global warming" in question_lower
    ):
        answer = (
            "Climate change is the long-term change in Earth's climate. "
            "We can help by saving energy, reducing waste, and choosing "
            "cleaner transportation where possible. 🌍"
        )

    # Renewable energy
    elif (
        "renewable energy" in question_lower
        or "solar energy" in question_lower
        or "wind energy" in question_lower
    ):
        answer = (
            "Renewable energy comes from naturally replenished sources "
            "such as sunlight, wind, and flowing water. It can help reduce "
            "dependence on fossil fuels. ☀️"
        )

    # Electricity and energy
    elif (
        "electricity" in question_lower
        or "save energy" in question_lower
        or "save power" in question_lower
        or "reduce electricity" in question_lower
        or "reduce power" in question_lower
        or "energy consumption" in question_lower
    ):
        answer = (
            "You can save electricity by switching off unused lights "
            "and devices, using energy-efficient appliances, and making "
            "good use of natural light. 💡"
        )

    # Pollution
    elif "pollution" in question_lower:
        answer = (
            "Pollution is the introduction of harmful substances into "
            "the environment. Reducing waste and using cleaner "
            "transportation can help reduce pollution. 🌿"
        )

    # Waste management
    elif (
        "waste management" in question_lower
        or "reduce waste" in question_lower
        or "waste" in question_lower
    ):
        answer = (
            "Good waste management means reducing the waste we create, "
            "reusing items when possible, and recycling materials correctly. "
            "Composting suitable food and garden waste can also help. ♻️"
        )

    # Default response
    else:
        try:
            response = client.responses.create(
                model="gpt-5-mini",
                instructions=(
                    "You are EcoAssist, a helpful environmental assistant. "
                    "Answer questions clearly and accurately. "
                    "Keep answers concise and suitable for a general audience."
                ),
                input=question
            )

            answer = response.output_text

        except RateLimitError:
            answer = (
                "🌱 EcoAssist can currently answer questions about " 
                "sustainability , saving water , recycling , climate change ,"
                "renewable energy , saving electricity , pollution and waste management."
            )

    return {
        "answer": answer
    }
