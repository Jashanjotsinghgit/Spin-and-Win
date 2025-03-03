function sendOTP() {
    let phone = document.getElementById("phone").value;
    fetch("http://localhost:8000/send-otp/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ phone_number: phone })
    }).then(response => response.json())
    .then(data => alert("OTP Sent!"))
    .then(() => window.location.href = "verify.html");
}

function verifyOTP() {
    let otp = document.getElementById("otp").value;
    fetch("http://localhost:8000/verify-otp/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ otp: otp })
    }).then(response => response.json())
    .then(data => alert("Verified!"))
    .then(() => window.location.href = "spin.html");
}

function spinWheel() {
    fetch("http://localhost:8000/spinwheel/spin/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: 1 })
    }).then(response => response.json())
    .then(data => document.getElementById("result").innerText = data.message)
    .catch(() => alert("Already Spun!"));
}