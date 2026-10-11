## SUDS - Suspicious URL Detection System

| Parameters | Valid       | Invalid                         |
| ---------- | ----------- | ------------------------------- |
| Hostname   | google.com  | qweasdfzqwrqwar.com             |
| Protocl    | https       | http                            |
| Port       | example.com | example.com:1010                |
| Query      | /?q=book    | /?q=<script>alert(123)</script> |
| Fragment   | #users      | #<script>alert(123)</script>    |
