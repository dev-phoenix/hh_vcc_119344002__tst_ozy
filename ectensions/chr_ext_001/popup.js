document.getElementById("countButton").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript(
            {
                target: { tabId: tabs[0].id },
                func: countWords,
            },
            (results) => {
                document.getElementById("count").innerText = `Words: ${results[0].result}`;
            }
        );
    });
});

function countWords() {
    const selection = window.getSelection().toString().trim();
    const text = selection || document.body.innerText;
    console.log('text',text)
    const wordCount = text.match(/\b\w+\b/g)?.length || 0;
    return wordCount;
}