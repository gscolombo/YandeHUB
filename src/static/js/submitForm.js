document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const submit = document.querySelector(".submit-button");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        if (submit.disabled) {
            return;
        }
        console.log("Form submitted successfully!");

        const formData = new FormData(form);
        fetch(form.action, {
            method: form.method,
            body: formData,
        })
        .then(response => {
            response.json()
        })
        .then(json => {
            console.log(json);
        })
    });
});