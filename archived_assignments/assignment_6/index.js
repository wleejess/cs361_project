'use strict';

const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.static('public'));

app.use(express.urlencoded({
    extended: true
}));


app.post("/results", (req, res) => {
    const msg = req.body.comments;
    res.send(`
      <h3>Your message is:</h3>
      <p>${msg}</p>
    `);
}); 

app.use(express.static('public'));
  
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}...`);
});

