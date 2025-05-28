document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const submit = document.querySelector(".submit-button");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        if (submit.disabled) {
            return;
        }
        
        form.classList.add("waiting-response");
        const formData = new FormData(form);
        fetch(form.action, {
            method: form.method,
            body: formData,
        })
        .then(res => {
            if (!res.ok) {
                form.classList.add("error");
            }
        })
        .finally(() => {
            form.classList.remove("waiting-response");
        })
    });
});