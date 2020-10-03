const path = require("path");
const express = require("express");
const app = express();

const PORT = 3000;

app.use(express.static(__dirname + "/public"));

app.get("/", (req, res, next) => {
	res.sendFile(path.join(__dirname + "/model.html"));
});

app.listen(PORT, () => {
	console.log(`Server is listening on port: ${PORT}`);
})
