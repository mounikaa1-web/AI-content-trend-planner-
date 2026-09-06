from flask import Flask, render_template, request
import random

app = Flask(__name__)

content_ideas = {
    "ai": ["AI Tools", "Machine Learning", "Chatbots", "Generative AI", "AI Automation"],
    "technology": ["Smart Home Devices", "VR Headsets", "Blockchain", "5G Technology", "Cybersecurity"],
    "python": ["Flask Projects", "Automation Scripts", "Data Science", "Web Development"],
    "cybersecurity": ["Ethical Hacking", "Network Security", "Malware Analysis", "Zero Trust", "Cloud Security"],
    "blockchain": ["Crypto Wallets", "Smart Contracts", "Web3", "NFT Platforms", "DeFi"]
}

hashtags = {
    "ai": ["#AI", "#MachineLearning", "#TechTrends"],
    "technology": ["#Technology", "#Innovation", "#FutureTech"],
    "python": ["#Python", "#Coding", "#Flask"],
    "cybersecurity": ["#CyberSecurity", "#EthicalHacking", "#InfoSec"],
    "blockchain": ["#Blockchain", "#Web3", "#Crypto"]
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        topic = request.form["topic"].lower().strip()
        trend_data = [random.randint(50, 100) for _ in range(12)]

        if topic in content_ideas:
            result = {
                "topic": topic.upper(),
                "trend_score": random.randint(75, 95),
                "ideas": content_ideas[topic],
                "hashtags": hashtags[topic],
                "best_time": random.choice(["9 AM", "1 PM", "6 PM", "8 PM"]),
                "trend_data": trend_data
            }
        else:
            generated_ideas = [
                f"{topic.title()} Basics",
                f"{topic.title()} Future Trends",
                f"{topic.title()} Tools",
                f"{topic.title()} Tips",
                f"{topic.title()} Latest Innovations"
            ]
            generated_tags = [
                f"#{topic}",
                f"#{topic}Trends",
                f"#{topic}Tips"
            ]

            result = {
                "topic": topic.upper(),
                "trend_score": random.randint(60, 90),
                "ideas": generated_ideas,
                "hashtags": generated_tags,
                "best_time": random.choice(["9 AM", "1 PM", "6 PM", "8 PM"]),
                "trend_data": trend_data
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
