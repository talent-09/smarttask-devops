const form = document.getElementById("loginForm");

const message = document.getElementById("message");


form.addEventListener("submit", async function(event) {

    event.preventDefault();


    const email =
        document.getElementById("email").value;

    const password =
        document.getElementById("password").value;


    message.textContent = "Connexion en cours...";


    try {

        const response = await fetch(
            "http://localhost:5000/api/login",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    email: email,

                    password: password

                })
            }
        );


        const data = await response.json();


        if (response.ok) {

            message.textContent =
                data.message;

        } else {

            message.textContent =
                data.message;
        }


    } catch (error) {

        console.error(error);

        message.textContent =
            "Impossible de contacter le backend.";
    }

});
