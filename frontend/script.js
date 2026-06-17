
async function askAI() {
    const question = document.getElementById("question").value;
    const answerBox = document.getElementById("answer");

    answerBox.innerText = "🤖 Thinking...\n";

    const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question })
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    let result = "";

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        result += chunk;

        answerBox.innerText = result;  // 🔥 live update
    }
}
