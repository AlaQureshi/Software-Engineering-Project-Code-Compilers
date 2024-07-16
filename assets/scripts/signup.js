class Signup {
    constructor(form, fields) {
        this.form = form;
        this.fields = fields;
        this.validateonSubmit();
    }

    validateonSubmit() {
        let self = this;

        this.form.addEventListener("submit", (e) => {
            e.preventDefault();
            var error = 0;
            self.fields.forEach((field) => {
                const input = document.querySelector(`#${field}`);
                if (self.validateFields(input) === false) {
                    error++;
                }
            });
            if (error === 0) {
                // Simulate a successful sign-up
                window.location.href = "/dashboard.html"; // Redirect to dashboard on successful sign-up
            }
        });
    }

    validateFields(field) {
        if (field.value.trim() === "") {
            this.setStatus(
                field,
                `${field.previousElementSibling.innerText} cannot be blank`,
                "error"
            );
            return false;
        } else if (field.type === "email" && !this.validateEmail(field.value)) {
            this.setStatus(
                field,
                `Invalid email address`,
                "error"
            );
            return false;
        } else if (field.id === "confirm-password") {
            const passwordField = document.querySelector("#password");
            if (field.value !== passwordField.value) {
                this.setStatus(
                    field,
                    `Passwords do not match`,
                    "error"
                );
                return false;
            } else {
                this.setStatus(field, null, "success");
                return true;
            }
        } else {
            this.setStatus(field, null, "success");
            return true;
        }
    }

    validateEmail(email) {
        const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@(([^<>()[\]\.,;:\s@"]+\.[^<>()[\]\.,;:\s@"]{2,})+)$/i;
        return re.test(String(email).toLowerCase());
    }

    setStatus(field, message, status) {
        const errorMessage = field.parentElement.querySelector(".error-message");

        if (status === "success") {
            if (errorMessage) {
                errorMessage.innerText = "";
            }
            field.classList.remove("input-error");
        }

        if (status === "error") {
            errorMessage.innerText = message;
            field.classList.add("input-error");
        }
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector(".signupForm");
    if (form) {
        const fields = ["username", "email", "password", "confirm-password"];
        const validator = new Signup(form, fields);
    }
});
