var jogos = [
    [20, 28, 30, 40, 43, 48],
    [2, 8, 16, 28, 34, 43],
    [8, 12, 22, 27, 30, 35],
    [18, 29, 30, 36, 51, 59],
    [14, 18, 22, 36, 39, 41],
    [4, 16, 20, 48, 57, 59],
    [8, 22, 31, 41, 51, 59]
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
