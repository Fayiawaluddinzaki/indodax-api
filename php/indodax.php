<?php

class Indodax {
    private $base_url;

    public function __construct () {
        $this->base_url = 'https://indodax.com';        
    }

    public function external_rates_summaries () {
        $resp = $this->get($this->base_url . '/api/external_rates_summaries');

        if (empty($resp)) {
            return FALSE;
        }

        return $resp;
    }

    protected function req ($method, $url, array $data = array()) {
        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);

        switch (strtolower($method)) {
        default:
            break;
        case 'POST':
            curl_setopt($ch, CURLOPT_POST, TRUE);
            break;
        }

        $resp = curl_exec($ch);

        curl_close($ch);

        if (!empty($resp)) {
            return @json_decode($resp);
        }

        return FALSE;
    }

    protected function get ($url, array $data = array()) {
        return $this->req('GET', $url, $data);
    }
}