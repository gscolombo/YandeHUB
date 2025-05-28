/**
 * Enables or disables the submit button of a form based on the completion of all input fields.
 *
 * - Disables the submit button if any input field is empty on page load.
 * - Listens for input events on the form and enables the submit button only when all input fields are filled.
 *
 * Assumptions:
 * - The form is the first <form> element in the DOM.
 * - The submit button has the class "submit-button".
 * - Only <input> elements inside the form are considered for validation.
 */
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const submit = form.querySelector(".submit-button");
    let inputs = form.querySelectorAll("input");
    submit.disabled = Array.from(inputs).map(input => input.value.trim() === "").includes(true);

    form.addEventListener("input", function() {
        for (let input of inputs) {
            if (input.value.trim() === "") {
                submit.disabled = true;
                return;
            }
        }
        submit.disabled = false;
    })
});