const chatHistory = [];

function addToHistory(question, answer) {
    chatHistory.push({
        question: question,
        answer: answer
    });

    console.log("EcoAssist conversation:", chatHistory);
}