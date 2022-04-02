var jogos = [
    [10, 11, 22, 47, 50, 52],
    [3, 16, 23, 24, 26, 34],
    [21, 30, 33, 50, 53, 54],
    [2, 18, 24, 31, 39, 55],
    [6, 9, 15, 19, 58, 59],
    [17, 25, 36, 39, 55, 58],
    [26, 27, 30, 46, 49, 55]
];

jogos.map(function (jogo) {
    marcarJogo(jogo);
});

function marcarJogo(jogo) {

    jogo.map(function (n) {
        n = (n < 10) ? ("#n0" + n) : ("#n" + n);
        document.querySelector(n).click();
    });

    document.querySelector("#colocarnocarrinho").click();

}
