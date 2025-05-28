document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const submit = document.querySelector(".submit-button");
    let inputs = form.querySelectorAll("input");
    submit.disabled = Array.from(inputs).map(input => input.value.trim() === "").includes(true);

    form.addEventListener("input", function(event) {
        for (let input of inputs) {
            if (input.value.trim() === "") {
                submit.disabled = true;
                return;
            }
        }
        submit.disabled = false;
    })
});