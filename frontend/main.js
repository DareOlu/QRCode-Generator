function generateQRCode() {
	var d = document.getElementById("data").value
	eel.generateQRCode(d)(setImage)
}

function setImage(base64) {
	document.getElementById("qr").src = base64
}