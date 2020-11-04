function sendMail(contactForm) {
    emailjs.send("gmail", "Data-Planner", {
        "from_email": contactForm.email.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;
}

