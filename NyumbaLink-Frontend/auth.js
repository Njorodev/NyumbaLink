//const API_BASE = "http://127.0.0.1:8000";
const API_BASE = "https://nyumbalink-backend.vercel.app";

/*
|--------------------------------------------------------------------------
| Utility functions
|--------------------------------------------------------------------------
*/

function showMessage(form, type, message) {
  const messageElement = form.querySelector(`.${type}`);

  if (!messageElement) {
    console[type === "error" ? "error" : "log"](message);
    return;
  }

  messageElement.textContent = message;
  messageElement.classList.add("show");
}

function hideMessage(form, type) {
  const messageElement = form.querySelector(`.${type}`);

  if (messageElement) {
    messageElement.textContent = "";
    messageElement.classList.remove("show");
  }
}

function setSubmitState(button, isLoading, defaultText) {
  if (!button) return;

  button.disabled = isLoading;
  button.textContent = isLoading
    ? "Please wait..."
    : defaultText;
}

/*
|--------------------------------------------------------------------------
| Password visibility toggle
|--------------------------------------------------------------------------
*/

document.querySelectorAll(".toggle-password").forEach(button => {
  button.addEventListener("click", () => {
    const targetId = button.dataset.target;
    const input = document.getElementById(targetId);

    if (!input) {
      console.warn(`Password input not found: ${targetId}`);
      return;
    }

    const isVisible = input.type === "text";

    input.type = isVisible ? "password" : "text";
    button.textContent = isVisible ? "Show" : "Hide";
    button.setAttribute(
      "aria-label",
      isVisible ? "Show password" : "Hide password"
    );
  });
});

/*
|--------------------------------------------------------------------------
| Authentication forms
|--------------------------------------------------------------------------
*/

document.querySelectorAll(".auth-form").forEach(form => {
  form.addEventListener("submit", async event => {
    event.preventDefault();

    const data = new FormData(form);

    /*
     * These values come from the HTML form:
     *
     * Login:
     * data-mode="login"
     *
     * Signup:
     * data-mode="signup"
     *
     * Role:
     * data-role="landlord"
     * data-role="seeker"
     */
    const mode = form.dataset.mode;
    const role = form.dataset.role;

    if (mode !== "login" && mode !== "signup") {
      showMessage(
        form,
        "error",
        "Form configuration error: data-mode must be login or signup."
      );

      console.error(
        "Missing or invalid data-mode on form:",
        mode
      );

      return;
    }

    if (!role || !["landlord", "seeker"].includes(role)) {
      showMessage(
        form,
        "error",
        "Form configuration error: invalid account role."
      );

      console.error(
        "Missing or invalid data-role on form:",
        role
      );

      return;
    }

    hideMessage(form, "success");
    hideMessage(form, "error");

    let endpoint;
    let payload;

    /*
    |--------------------------------------------------------------------------
    | Signup request
    |--------------------------------------------------------------------------
    */

    if (mode === "signup") {
      const firstName = data.get("first_name");
      const lastName = data.get("last_name");
      const email = data.get("email");
      const phone = data.get("phone");
      const password = data.get("password");
      const confirmPassword = data.get("confirm_password");

      if (!firstName || !lastName || !email || !phone || !password) {
        showMessage(
          form,
          "error",
          "Please complete all required fields."
        );
        return;
      }

      if (!confirmPassword) {
        showMessage(
          form,
          "error",
          "Please confirm your password."
        );
        return;
      }

      if (password !== confirmPassword) {
        showMessage(
          form,
          "error",
          "Passwords do not match."
        );
        return;
      }

      if (password.length < 8) {
        showMessage(
          form,
          "error",
          "Password must be at least 8 characters long."
        );
        return;
      }

      endpoint = `${API_BASE}/api/auth/signup`;

      payload = {
        first_name: firstName.trim(),
        last_name: lastName.trim(),
        email: email.trim().toLowerCase(),
        phone: phone.trim(),
        password: password,
        role: role
      };
    }

    /*
    |--------------------------------------------------------------------------
    | Login request
    |--------------------------------------------------------------------------
    */

    if (mode === "login") {
      const email = data.get("email");
      const password = data.get("password");

      if (!email || !password) {
        showMessage(
          form,
          "error",
          "Please enter your email and password."
        );
        return;
      }

      endpoint = `${API_BASE}/api/auth/login`;

      payload = {
        email: email.trim().toLowerCase(),
        password: password
      };
    }

    const submitButton = form.querySelector(
      'button[type="submit"], .auth-btn'
    );

    const originalButtonText = submitButton
      ? submitButton.textContent
      : "Submit";

    try {
      setSubmitState(
        submitButton,
        true,
        originalButtonText
      );

      console.log("Submitting to:", endpoint);
      console.log("Request mode:", mode);
      console.log("Account role:", role);

      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify(payload)
      });

      let result;

      try {
        result = await response.json();
      } catch {
        throw new Error(
          `Server returned an invalid response. HTTP status: ${response.status}`
        );
      }

      if (!response.ok) {
        let errorMessage = "Authentication request failed.";

        if (typeof result.detail === "string") {
          errorMessage = result.detail;
        } else if (Array.isArray(result.detail)) {
          errorMessage = result.detail
            .map(error => error.msg)
            .join(", ");
        }

        throw new Error(errorMessage);
      }

      if (!result.access_token) {
        throw new Error(
          "Login succeeded, but the server did not return an access token."
        );
      }

      /*
      |--------------------------------------------------------------------------
      | Save authentication data
      |--------------------------------------------------------------------------
      |
      | Store only the raw JWT.
      | Do not store "Bearer " together with the token.
      |
      */

      localStorage.setItem(
        "nyumbalink_token",
        result.access_token
      );

      if (result.user) {
        localStorage.setItem(
          "nyumbalink_user",
          JSON.stringify(result.user)
        );
      }

      const successMessage =
        mode === "signup"
          ? `${role === "landlord" ? "Landlord" : "Seeker"} account created successfully.`
          : "Signed in successfully.";

      showMessage(form, "success", successMessage);

      /*
      |--------------------------------------------------------------------------
      | Redirect after successful authentication
      |--------------------------------------------------------------------------
      */

      setTimeout(() => {
        window.location.href = "index.html";
      }, 800);

    } catch (error) {
      console.error("Authentication error:", error);

      let message = error.message;

      if (
        error instanceof TypeError &&
        error.message.toLowerCase().includes("fetch")
      ) {
        message =
          "Unable to connect to the backend. Check that FastAPI is running and CORS is configured.";
      }

      showMessage(form, "error", message);

    } finally {
      setSubmitState(
        submitButton,
        false,
        originalButtonText
      );
    }
  });
});
