# Utils

Questa cartella raccoglie materiale riordinato dal workspace per trovarlo piu in fretta.

Struttura:

- `utils/index/explanations/`: copie rinominate delle note e spiegazioni utili.
- `utils/index/templates/`: copie rinominate di template o script riusabili.
- `utils/templates/`: template Python generici da usare come base nelle challenge.
- `utils/scan_and_index.py`: script che scansiona il workspace e rigenera il catalogo.

Template disponibili:

- `pwn_local_remote_launcher.py`: avvio locale/remoto con pwntools.
- `http_session_helper.py`: sessione HTTP base per challenge web.
- `xor_crypto_solver.py`: helper XOR e mini brute force crypto.
- `archive_encoding_unwrapper.py`: unwrap di base64/gzip/xz annidati.
- `bruteforce_candidate_runner.py`: scaffold per brute force di stringhe.

Uso rapido:

```bash
python utils/scan_and_index.py
```

Lo script cerca file `.txt`, `.md` e `.py` nel workspace, prova a riconoscere le note esplicative e i template, e copia i risultati in `utils/index` con nomi piu leggibili.
