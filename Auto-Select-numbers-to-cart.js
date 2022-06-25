var jogos = [
    [13, 22, 29, 55, 77],
   [1, 13, 19, 25, 64],
   [10, 29, 61, 70, 77],
   [22, 47, 58, 70, 80],
   [1, 18, 32, 37, 64],
   [1, 22, 52, 59, 77],
   [7, 8, 32, 41, 58],
   [13, 17, 31, 51, 58],
   [1, 7, 27, 73, 77],
   [8, 10, 17, 27, 40]
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
