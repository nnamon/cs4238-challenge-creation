<html>
<head>
<title>BabyWeb</title>
</head>
<body>
<div align="center">
<h1>BabyWeb</h1>
<p>Quotes from your favourite books!</p>
<hr>
<div>
<em>
<?php

chdir("includes");

if (!isset($_GET["page"])) {
    $quote = "Please select a book.";
}

include($_GET["page"] . ".php");

echo($quote);

?>
</em>
</div>
<a href="?page=harry">Harry Potter</a>
<a href="?page=twilight">Twilight</a>
<a href="?page=tiffanys">Breakfast at Tiffany's</a>
<a href="?page=iliad">The Iliad</a>
<hr>
<em>The flag is in flag.php</em>
</div>
</body>
</html>
