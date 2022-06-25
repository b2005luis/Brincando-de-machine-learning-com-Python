var jogos = [
   [12, 18, 26, 46, 52, 55],
   [2, 11, 12, 18, 39, 55],
   [7, 12, 13, 26, 39, 53],
   [13, 24, 28, 29, 51, 52],
   [2, 3, 24, 29, 47, 55],
   [7, 21, 24, 28, 39, 53],
   [12, 26, 28, 30, 51, 53]
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
