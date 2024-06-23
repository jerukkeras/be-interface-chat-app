import os
from supabase import create_client, Client

url: str = "https://offzcyobhczqgiccxxrl.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9mZnpjeW9iaGN6cWdpY2N4eHJsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTgzOTI5NDEsImV4cCI6MjAzMzk2ODk0MX0.nkn46wyD3Vj_CRUIXNnjvfrmA8mzNVFjf3xgPqgH2Ho"
supabase: Client = create_client(url, key)