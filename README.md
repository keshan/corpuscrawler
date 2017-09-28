# Corpus Crawler

_Corpus Crawler_ is a tool for [Corpus
Linguistics](https://en.wikipedia.org/wiki/Corpus_linguistics).

Modern linguistic research works by analyzing corpora, which are large
samples of “real world” text. This crawler helps to build corpora: it
follows links to web pages that are known to be written in a certain
language; it removes boilerplate and HTML markup; finally, it writes
its output into plaintext files.  The crawler adheres to the [Robots
Exclusion
Standard](https://en.wikipedia.org/wiki/Robots_exclusion_standard) and
is intentionally slow, so it does not cause much load on the crawled
web sites.

This is not an official Google product. But if you’re a linguist or
plan to write software for spell checking or other language processing,
you might find _Corpus Crawler_ useful.


## Supported Languages

| IETF BCP47 Code     | Language                     |  Tokens |
| :------------------ | :--------------------------- | ------: |
| `am`                | Amharic                      |         |
| `bg`                | Bulgarian                    |         |
| `bm`                | Bambara                      |     30K |
| `bn`                | Bangla                       |         |
| `ccp`               | Chakma                       |    120K |
| `fa`                | Persian                      |         |
| `fa-AF`             | Dari                         |         |
| `fo`                | Faroese                      |    870K |
| `fuv`               | Nigerian Fulfulde            |     13K |
| `gsw-u-sd-chag`     | Swiss German (Aargau)        |    102K |
| `gsw-u-sd-chbe`     | Swiss German (Bern)          |     73K |
| `gsw-u-sd-chfr`     | Swiss German (Fribourg)      |     42K |
| `gv`                | Manx Gaelic                  |    149K |
| `ha`                | Hausa                        |  1,780K |
| `hi`                | Hindi                        |         |
| `id`                | Indonesian                   |         |
| `ig`                | Igbo                         |     12K |
| `kj`                | Kuanyama                     |  1,506K |
| `ky`                | Kyrgyz                       |    507K |
| `mnw`               | Mon                          |    475K |
| `mk`                | Macedonian                   |         |
| `mt`                | Maltese                      |         |
| `my`                | Burmese                      |    486K |
| `my-t-d0-zawgyi`    | Burmese (Zawgyi encoding)    |    153K |
| `ps`                | Pashto                       |         |
| `rm-puter`          | Romansh (Puter)              |  1,230K |
| `rm-rumgr`          | Romansh (Grischun)           |  5,605K |
| `rm-surmiran`       | Romansh (Surmiran)           |  3,287K |
| `rm-sursilv`        | Romansh (Sursilvan)          | 13,552K |
| `rm-sutsilv`        | Romansh (Sutsilvan)          |  1,230K |
| `rm-vallader`       | Romansh (Vallader)           |  6,347K |
| `rw`                | Kinyarwanda                  |    616K |
| `shn`               | Shan                         |    440K |
| `so`                | Somali                       |    878K |
| `sq`                | Albanian                     |         |
| `sw`                | Swahili                      |  1,285K |
| `ta`                | Tamil                        |  1,568K |
| `taq`               | Tamasheq                     |     63K |
| `ur`                | Urdu                         |  4,163K |
| `yo`                | Yoruba                       |     79K |

You’re very welcome to join the project, for example to add another language.
Please read the [contribution guidelines](./CONTRIBUTING.md) and send [pull
requests](https://help.github.com/categories/collaborating-with-issues-and-pull-requests/).


## Running the Crawler

```sh
./corpuscrawler --language=rm --output=./corpus
```
