var jogos = [
   [19, 21, 35, 50, 52, 53],
   [1, 7, 44, 47, 49, 55],
   [7, 8, 12, 20, 39, 41],
   [20, 22, 25, 26, 28, 39],
   [5, 12, 15, 16, 20, 32],
   [9, 21, 44, 45, 49, 59],
   [2, 4, 19, 49, 54, 56]
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
