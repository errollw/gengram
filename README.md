# gengram

A __lightweight n-gram random text generator__ written in Python. It was developed for automating [Happy Hour](http://www.cl.cam.ac.uk/misc/localarea/catering.html#happyhour) weekly reminder emails at the [Cambridge Computer Lab](http://www.cl.cam.ac.uk/).

An _n-gram_ is a contiguous sequence of symbols. For the text,

> The cat sat on the mat.

The _bigrams_ (2-long n-grams) are:
`The cat`, `cat sat`, `sat on`, `on the`, `the mat`, `mat .`

### How it works

We arrange n-grams in a table of `symbol_sequence : (next_symbol, frequency)` to record which sequences are most common. From a given `symbol_sequence` we can make a _random weighted choice_ for the `next_symbol`.

An excerpt from the example Happy Hour corpus (trigrams):

|  symbol sequence  |  next symbol  |  frequency  |
| ------------------| ------------- | ----------- |
| `yet another`     | `conference`  | 1           |
|                   | `paper`       | 1           |
|                   | `friday`      | 1           |
|                   | `happy`       | 2           |
| `have a`          | `keg`         | 6           |
|                   | `recent`      | 1           |
|                   | `nice`        | 1           |
|...                | ...           | ...         |

So if we have a symbol sequence that currently ends with `have a`, we are more likely to choose `keg` as the next symbol to output, rather than `recent` or `nice`. By iterating this we can generate long sequences of symbols.

Once we output a punctuation symbol from `. ! ?`, we record that at sentence has been generated.

### Usage

1. Place source text corpus into `corpus.txt`
2. Run the `gengram.py` script

This _preprocess_ the text, normalizing whitespace and characters, and then calls the main method `gengram_sentence`. Its arguments are:

  * `corpus` - preprocessed text corpus
  * `N` - how long the n-grams are (default: 3)
  * `sentence_count` - how many sentences to generate (default: 5)
  * `start_seq` - seed start sequence (default: None)

If no seed `start_seq` is given, gengram chooses a random one. After sentence symbol sequences are generated, they are _postprocessed_ to correct whitespace and capitalization.

### Sample output

`start_seq = "Join us"`
> Join us for the happy hour. We have a recent repeat. Cyclops. Rawr! We apologize for the usual collection of snacks.

`start_seq = "Once again"`
> Once again we invite you to our usual selection of soft drinks, bottled ales, and a keg of sparta, crisps, dips, bins, napkins, paper plates and chopping boards. Now is our keg filled with sparta 4.3%; our packets of nuts for the happy hour! Join us for the crisp eaters, there will be crisps, dips, bins, napkins, paper plates and chopping boards. Now is our keg filled with sparta 4.3%; our packets of crisps. What more could you want? Join us for the usual selection of snacks, juice, snacks, juice, snacks, beer, snacks, beer, a keg of beer!

`start_seq = "There will"`
> There will be a keg of justinian 3.9%, bottled ales, lagers, ales, lagers, ales, lagers, ales, lagers, ciders, a selection of soft drinks and snacks available. Our usual selection. Roses are red, happy hour. We considered having happy hour and replacing the keg, lots of lagers, crisps, bottled beers and cider, and the usual. Join us at 5pm this afternoon.

### Dependencies

  * [Python 2.7](http://www.python.org/download/releases/2.7/)