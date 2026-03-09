<?php
// 1. La tua chiave segreta (tienila al sicuro, non condividerla!)
// In produzione, useresti getenv('SECRET') o un file di config
$secret_key = "eWFw7Li8jKImzw";

// 2. Il dato che vuoi "firmare" (nel tuo caso l'URL dell'immagine)
$data_to_sign = "https://127.0.0.1/get_flag.php";

// 3. Generazione dell'HMAC
// Parametri: (algoritmo, messaggio, chiave)
$hmac = hash_hmac('md5', $data_to_sign, $secret_key);

// 4. Risultato
echo "Dato originale: " . $data_to_sign . "\n";
echo "HMAC generato: " . $hmac . "\n";

// --- ESEMPIO DI VERIFICA ---
// Quando il server riceve una richiesta, rifà il calcolo:
$received_hmac = $hmac; // Supponiamo che arrivi da $_GET['hmac']

$check = hash_hmac('md5', $data_to_sign, $secret_key);

if (hash_equals($check, $received_hmac)) {
    echo "✅ La firma è valida! Il dato non è stato manomesso.";
} else {
    echo "❌ Firma NON valida! Attacco rilevato.";
}
?>