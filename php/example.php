<?php

require_once('indodax.php');

$idx = new Indodax();

echo json_encode($idx->external_rates_summaries(), JSON_PRETTY_PRINT);
