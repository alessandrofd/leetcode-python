"""
Your music player contains num_songs different songs. You want to listen to 
length_playlist songs (not necessarily different) during your trip. To avoid 
boredom, you
will create a playlist so that:

    Every song is played at least once.

    A song can only be played again only if num_lead_songs other songs have been 
    played.
    OBS: This is unclear to the point of being misleading... it should really 
    say "A song can only appear in the playlist once every num_lead_songs songs".


Given num_songs, length_playlist, and num_lead_songs, return the number of 
possible playlists that you can create. Since the answer can be very large, 
return it modulo 10^9 + 7.

Constraints:
    0 <= num_lead_songs < num_songs <= lenght_playlist <= 100
"""


class Solution:
    def numMusicPlaylists(
        self, num_songs: int, length_playlist: int, num_lead_songs: int
    ) -> int:
        """
        * Programação dinâmica
        * Dimensões: comprimento da playlist e número de canções
        * Casos base:
        *    Playlist de comprimento 0 e número de canções 0 só tem uma
        *    possibilidade de playlist - playlist vazia => dp[0][0] = 1.
        *
        *    Se o número de canções for maior que a comprimento de playlist, uma das
        *    condições do problema não pode ser respeitada (todas as canções devem
        *    tocar ao menos uma vez) e, portanto, não haverá playlist possível =>
        *    dp[i][j] = 0 se j > i
        *
        * Transições:
        *    Podemos acrescentar tanto uma canção inédita quanto uma repetida, desde
        *    que seja respeitado a quantidade mínima de canções inéditas antes de
        *    repeti-las.
        *
        *    Se acrescentarmos uma canção inédita, teremos que adicionar a dp[i][j],
        *    onde i é o comprimento da playlist e j a quantidade de canções, a
        *    quantidade de playlists com comprimento uma unidade menor (i-1) e com uma
        *    canção a menos (j-1) multiplicado pela quantidade de canções inéditas
        *    disponíveis para serem adicionadas. Como (j-1) canções já foram escolhidas,
        *    o número de alternativas será igual a numSongs - (j-1)
        *    => dp[i][j] += dp[i-1][j-1] * (numSongs - (j-1))
        *
        *    Para acrescentarmos uma canção repetida é necessário que haja na playlist
        *    um número canções distintas da canção a ser repetida (numLeadSongs). Logo,
        *    só poderemos repetir canções quando j > numLeadSongs. Neste caso, devemos
        *    adicionar a dp[i][j], a quantidade de playlists com comprimento uma
        *    unidade menor (i-1) e o mesmo número de canções (j) multiplicada pela
        *    quantidade de canções possíveis de serem repetidas. Neste ponto, o
        *    enunciado do problema é confuso. A princípio ele dá a enteder que assim
        *    que numLeadSongs distintas estiverem na playlist, qualquer canção pode ser
        *    repetida. No entanto, os exemplos (especialmente o terceiro) demonstram
        *    que na verdada a intenção é permitir repetição apenas se numLeadSongs
        *    canções distintas precederam imediatamente a canção a ser repetida.
        *    Assim o número de canções que podem ser repetidas será igual a (j - numLeadSongs).
        *    => dp[i][j] = dp[i-1][j] * (j - numLeadSongs)
        """

        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().numMusicPlaylists,
    ]

    # fmt: off
    data = [
        (3, 3, 1, 6),
        (2, 3, 0, 6),
        (2, 3, 1, 2),
    ]
    # fmt: on
    for num_songs, length_playlist, num_lead_songs, expected in data:
        for func in funcs:
            assert func(num_songs, length_playlist, num_lead_songs) == expected


if __name__ == "__main__":
    pass
