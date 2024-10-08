# Standard Deck Shuffler
#### This library's primary use is for the mechanics involved with keeping a mathematically accurate deck of cards. Some of these features are a WIP.

### Overview/Features:

- It creates and shuffles both single and double decks, and emulates common dealer shuffling practices such as the [**Riffle Shuffle**](https://en.wikipedia.org/wiki/Riffle_shuffle_permutation) and different variations of [**Cuts**](https://en.wikipedia.org/wiki/Cut_(cards))

- Washes are emulated by performing impossible or inconvenient shuffles(Inverse Ripple Shuffle) and cuts(Scarne's Cut) that would typically be against the rules in a standard card game.

- Ability to both deal, [second deal](https://en.wikipedia.org/wiki/Second_dealing), and [bottom deal](https://en.wikipedia.org/wiki/Bottom_dealing) from the deck

- Top and Bottom Peeking of Cards

- Single and Double decks are supported (52 or 104)

- Functional game mechanics, such as Discard Piles and [Community Cards](https://en.wikipedia.org/wiki/Community_card_poker)


### Functions:

[x] Create_Deck()

[x] Create_Double_Deck()

[x] Delete_Deck()

[x] Shuffle()

[x] In_Perfect_Riffle_Shuffle()

[x] Out_Perfect_Riffle_Shuffle()

[x] In_Imperfect_Riffle_Shuffle()

[x] Out_Imperfect_Riffle_Shuffle()

[x] Cut()

[x] Perfect_Cut()

[x] Top_Third_Cut()

[x] Bottom_Third_Cut()

[ ] Peek_Top()

[ ] Peek_Bottom()

[ ] Deal()

[ ] Second_Deal()

[ ] Bottom_Deal()

[ ] Add_Player()

[ ] Delete_Player()

[ ] Discard_Card()

[ ] Discard_Hand()

[ ] Add_Community_Pile()

[ ] Add_Discard_Pile()

[ ] Delete_Community_Pile()

[ ] Delete_Discard_Pile()

