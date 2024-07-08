document.getElementById('queryForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    alert(`Query submitted!\nEmail: ${email}\nMessage: ${message}`);
    document.getElementById('queryForm').reset();
});

function openCalculator() {
    document.getElementById('calculatorPopup').style.display = 'block';
}

function closeCalculator() {
    document.getElementById('calculatorPopup').style.display = 'none';
}

function appendCalc(value) {
    const calcInput = document.getElementById('calcInput');
    calcInput.value += value;
}

function calculate() {
    const calcInput = document.getElementById('calcInput');
    try {
        calcInput.value = eval(calcInput.value);
    } catch (e) {
        alert('Invalid calculation');
    }
}

function clearCalc() {
    document.getElementById('calcInput').value = '';
}
