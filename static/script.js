function predict() {
    const fileInput = document.getElementById("imageInput");
    const output = document.getElementById("output");

    if (fileInput.files.length === 0) {
        output.innerText = "Please upload a thermal image.";
        return;
    }

    output.innerText = "Processing image...";

    const formData = new FormData();
    formData.append("image", fileInput.files[0]);

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        output.innerHTML =
            `<strong>Status:</strong> ${data.message}<br>
             <strong>Temporal Input Shape:</strong> ${data.temporal_input_shape}<br>
             <strong>Note:</strong> ${data.status}`;
    })
    .catch(() => {
        output.innerText = "Server error. Please try again.";
    });
}
