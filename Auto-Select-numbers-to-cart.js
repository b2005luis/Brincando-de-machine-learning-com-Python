var numeros = [1, 5, 6, 7, 8, 10, 11, 13, 15, 17, 18, 19, 20, 22, 23]
numeros.map(function (n) {
    n = (n < 10) ? ("#n0" + n) : ("#n" + n);
    document.querySelector(n).click();
});
document.querySelector("#colocarnocarrinho").click();