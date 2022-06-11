let RGB = [0, 0, 0];
const redslider= document.getElementById('red');
const greenslider= document.getElementById('green');
let blueslider= document.getElementById('blue');

const output = document.getElementById('output');
console.log("innit")
console.log(typeof blueslider);

redslider.oninput = update;
greenslider.oninput = update;
blueslider.oninput = update;

console.log(RGB);
fetch("http://192.168.0.99:5000/").then(response => response.json()).then(data => 
{
redslider.value = data.RGB[0];
greenslider.value = data.RGB[1];
blueslider.value = data.RGB[2];
});

output.textContent = RGB.join(', ');
fetch("http://192.168.0.99:5000/").then(response => response.json()).then(data => console.log(data.RGB));
function update() {
  console.log(RGB);
    RGB[0] = redslider.value;
    RGB[1] = greenslider.value;
    RGB[2] = blueslider.value;
    output.textContent = RGB.join(', ');
    fetch("http://192.168.0.99:5000/",{
        method: "POST",
        headers: {
          'Access-Control-Allow-Origin': '*',
          "Content-Type": "application/json"
        },
        body: JSON.stringify({"RGB": RGB})
      })
}
