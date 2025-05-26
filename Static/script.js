document.addEventListener("DOMContentLoaded", () => {
    // Expand/Collapse logic
    document.querySelectorAll(".expand-btn").forEach(button => {
        button.addEventListener("click", () => {
            const container = button.parentElement;
            container.classList.toggle("expanded");
            button.textContent = container.classList.contains("expanded") ? "Collapse" : "Expand";
        });
    });

    // Progress bar logic on Analyze submit
    const form = document.getElementById("uploadForm");
    form.addEventListener("submit", () => {
        const barContainer = document.getElementById("progress-bar-container");
        const bar = document.getElementById("progress-bar");

        // Reset bar
        bar.style.width = "0%";
        barContainer.style.display = "block";

        // Start bar animation
        setTimeout(() => {
            bar.style.width = "100%";
        }, 50);

        // Reveal results with animation after 4 seconds
        setTimeout(() => {
            const results = document.querySelector(".results");
            if (results) {
                results.classList.add("visible");
            }
        }, 4000);
    });
});