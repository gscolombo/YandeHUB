/**
 * Handles form submission via AJAX when the DOM is fully loaded.
 * - Prevents default form submission behavior.
 * - Disables multiple submissions if the submit button is disabled.
 * - Adds a "waiting-response" class to indicate loading state.
 * - Sends form data using Fetch API to the form's action URL with the specified method.
 * - Removes the "waiting-response" class after the request completes.
 *
 * Assumes:
 * - There is a <form> element present in the DOM.
 * - There is a submit button with the class "submit-button".
 * - The form has valid "action" and "method" attributes.
 * - The server responds with JSON containing an "errors" array if there are validation issues.
 */
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
        .then(res => res.json())
        .then(data => {
            if (data.errors) {
                renderErrorList(data.errors);
            } else {
                console.log("Form submitted successfully:", data);
            }
        })
        .finally(() => {
            form.classList.remove("waiting-response");
        })
    });
});


/**
 * Renders a list of error messages in the DOM element with the class "error-list".
 * Clears any existing errors before displaying the new ones.
 *
 * @param {string[]} errors - An array of error message strings to display.
 */
function renderErrorList(errors) {
    const errorList = document.querySelector(".error-list");

    errorList.innerHTML = ""; // Clear previous errors
    errors.forEach(error => {
        const li = document.createElement("li");
        li.textContent = error;
        li.classList.add("error-item");
        errorList.appendChild(li);
    });
}