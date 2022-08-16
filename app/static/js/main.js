const preloader = document.querySelector(".page-preloader"),
	bootstrapColors = [
		"primary",
		"warning",
		"info",
		"secondary",
		"danger",
		"dark",
		"light",
		"success",
	],
	ShowPasswordToggle = document.querySelectorAll("[type='password']"),
	form = document.querySelector("form"),
	fileInput = document.querySelector("input[type=file]");

preloader
	.querySelector(".spinner-border")
	.classList.add(`text-${bootstrapColors[Math.ceil(Math.random() * 8)]}`);

document.addEventListener("DOMContentLoaded", function (e) {
	setTimeout(() => {
		preloader.style.setProperty("display", "none");
	}, 600);
});

form.addEventListener("submit", async function (e) {
	e.preventDefault();

	// Preloader on

	preloader.style.setProperty("display", "flex");

	const formData = new FormData(e.target),
		url = `${window.origin}`,
		body = {
			message: formData.get("message"),
			template: formData.get("template") ? "True" : "False",
			file: formData.getAll("file"),
		};

	const response = await fetch(url, {
		method: "post",
		headers: {
			"content-type": "application/json",
		},
		body: JSON.stringify(body),
	});

	// Preloader off

	preloader.style.setProperty("display", "none");

	if (response.ok) {
		e.target.reset();
		alert(await response.json());
	}
});

// Password field

ShowPasswordToggle.forEach((el) => {
	el.onclick = function () {
		el.classList.add("input-password");
		const togglePasswordButton = el.nextElementSibling;
		togglePasswordButton.classList.remove("d-none");
		togglePasswordButton.addEventListener("click", togglePassword);
		function togglePassword() {
			if (el.type === "password") {
				el.type = "text";
				togglePasswordButton.setAttribute("aria-label", "Hide password.");
			} else {
				el.type = "password";
				togglePasswordButton.setAttribute(
					"aria-label",
					"Show password as plain text. " +
						"Warning: this will display your password on the screen."
				);
			}
		}
	};
});

// --------------
