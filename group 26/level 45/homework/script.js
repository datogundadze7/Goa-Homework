function is_empirical(n) {
    if (n <= 0) return false;
    let power = 0;
    while (Math.pow(2, power) < n) {
        power += 1;
    }
    return Math.pow(2, power) === n;
}

function checkEmpirical() {
    const input = document.getElementById('numberInput').value;
    const resultDiv = document.getElementById('result');
    const number = parseInt(input, 10);
    resultDiv.innerHTML = is_empirical(number) ? `${number} არის 2-ის ძალა.` : `${number} არ არის 2-ის ძალა.`;
}
