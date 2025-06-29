# Web-related functions and HTML templates for Gas Detector
import crypto  # Import crypto module for DES encryption

# DES encryption key (sama dengan di boot.py)
DES_KEY = "Sliterin"

def get_timestamp():
    """Get current timestamp in formatted string"""
    from time import localtime
    t = localtime()
    return f"{t[0]}-{t[1]:02d}-{t[2]:02d} {t[3]:02d}:{t[4]:02d}:{t[5]:02d}"

def get_html_template():
    """Return the modern HTML template for the web interface (no gradient, green for normal, gray for empty history)"""
    return """<!DOCTYPE html>
<html>
<head>
    <title>Gas Detector Pro</title>
    <meta http-equiv='refresh' content='5'>
    <meta charset='utf-8'>
    <style>
        body {{
            min-height: 100vh;
            background: #f5f5f5;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Arial, sans-serif;
        }}
        .container {{
            background: #fff;
            max-width: 480px;
            margin: 40px auto 24px auto;
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(80, 80, 160, 0.15);
            padding: 32px 24px 24px 24px;
        }}
        h1 {{
            text-align: center;
            font-size: 2.2rem;
            margin-bottom: 0.2em;
        }}
        .subtitle {{
            text-align: center;
            color: #666;
            font-size: 1.05rem;
            margin-bottom: 1.2em;
        }}
        .group-box {{
            background: linear-gradient(90deg, #7f7fd5 0%, #86a8e7 100%);
            color: #fff;
            border-radius: 8px;
            padding: 12px 0 8px 0;
            text-align: center;
            margin-bottom: 18px;
        }}
        .group-box strong {{
            display: block;
            font-size: 1.1rem;
            margin-bottom: 2px;
        }}
        .status-box {{
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
            font-size: 1.2rem;
            padding: 10px 0 10px 0;
            margin-bottom: 18px;
            letter-spacing: 1px;
        }}
        .status-box.normal {{
            background: #e8f5e9;
            color: #43a047;
            border: 2px solid #43a047;
        }}
        .status-box.alert {{
            background: #ffebee;
            color: #c62828;
            border: 2px solid #ef5350;
        }}
        .info-grid {{
            display: flex;
            gap: 12px;
            margin-bottom: 18px;
        }}
        .info-card {{
            flex: 1;
            background: #f8f9fa;
            border-radius: 8px;
            padding: 14px 8px 10px 8px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(80,80,160,0.04);
        }}
        .info-card h3 {{
            margin: 0 0 6px 0;
            font-size: 1.05rem;
            color: #495057;
            font-weight: 600;
        }}
        .info-card .main {{
            font-size: 1.5rem;
            font-weight: bold;
            color: #212529;
        }}
        .info-card .encrypted {{
            font-size: 0.85rem;
            color: #888;
            margin-top: 2px;
            word-break: break-all;
        }}
        .reference-box {{
            background: #f8f9fa;
            border-radius: 8px;
            padding: 10px 8px 8px 8px;
            text-align: center;
            margin-bottom: 18px;
            box-shadow: 0 2px 8px rgba(80,80,160,0.04);
        }}
        .reference-box h3 {{
            margin: 0 0 6px 0;
            font-size: 1.05rem;
            color: #495057;
            font-weight: 600;
        }}
        .reference-box .main {{
            font-size: 1.2rem;
            font-weight: bold;
            color: #212529;
        }}
        .reference-box .encrypted {{
            font-size: 0.85rem;
            color: #888;
            margin-top: 2px;
            word-break: break-all;
        }}
        .alert-history {{
            margin-bottom: 18px;
        }}
        .alert-history-title {{
            font-weight: bold;
            margin-bottom: 6px;
            color: #c62828;
        }}
        .alert-log {{
            background: #ffe0e0;
            border-radius: 6px;
            padding: 8px 10px 4px 10px;
            margin-bottom: 8px;
            color: #c62828;
            font-size: 0.98rem;
            box-shadow: 0 1px 4px rgba(200,0,0,0.04);
        }}
        .alert-log .encrypted {{
            font-size: 0.8rem;
            color: #888;
            margin-top: 2px;
            word-break: break-all;
        }}
        .alert-log.empty {{
            background: #f0f0f0;
            color: #888;
            box-shadow: none;
            text-align: center;
        }}
        .footer {{
            text-align: center;
            color: #888;
            font-size: 0.95rem;
            margin-top: 18px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Gas Leak Detector</h1>
        <div class="subtitle">Real-time Gas Leak Monitoring System</div>
        <div class="group-box">
            <strong>Kelompok 16</strong>
            Alghifari Rasyid Zola (105220206)<br>
            Raihan Akira Rahmaputra (105222040)
        </div>
        <div class="status-box {status_class}">{status}</div>
        <div class="info-grid">
            <div class="info-card">
                <h3>Current Reading</h3>
                <div class="main">{gas_level}</div>
                <div class="encrypted">Encrypted: {gas_enc_hex}</div>
            </div>
            <div class="info-card">
                <h3>Threshold</h3>
                <div class="main">{threshold}</div>
                <div class="encrypted">Encrypted: {threshold_enc_hex}</div>
            </div>
        </div>
        <div class="reference-box">
            <h3>Reference</h3>
            <div class="main">{reference}</div>
            <div class="encrypted">Encrypted: {ref_enc_hex}</div>
        </div>
        <div class="alert-history">
            <div class="alert-history-title">Alert History</div>
            {logs}
        </div>
        <div class="footer">
            Last update: {timestamp} | Gas Detector Pro - Kelompok 16
        </div>
    </div>
</body>
</html>"""

def generate_html_response(gas_detected, current_analog_val, threshold, ref_avg, gas_alert_log):
    """Generate complete HTML response with current data (show decrypted-from-encrypted values)"""
    try:
        # Prepare data for encryption (8 karakter)
        gas_data = f"{int(current_analog_val):08d}"  # Pad to 8 digits
        threshold_data = f"{int(threshold):08d}"  # Pad to 8 digits
        ref_data = f"{int(ref_avg):08d}"  # Pad to 8 digits
        
        # Encrypt data using DES
        gas_encrypted = crypto.des_encrypt(gas_data, DES_KEY)
        threshold_encrypted = crypto.des_encrypt(threshold_data, DES_KEY)
        ref_encrypted = crypto.des_encrypt(ref_data, DES_KEY)
        
        # Decrypt the encrypted data
        gas_decrypted = crypto.des_decrypt(gas_encrypted, DES_KEY)
        threshold_decrypted = crypto.des_decrypt(threshold_encrypted, DES_KEY)
        ref_decrypted = crypto.des_decrypt(ref_encrypted, DES_KEY)
        
        # Remove padding (leading zeros)
        gas_display = str(int(gas_decrypted))
        threshold_display = str(int(threshold_decrypted))
        ref_display = str(int(ref_decrypted))
        
        # Convert encrypted data to hex for display
        gas_enc_hex = crypto.bytes_to_hex(gas_encrypted)
        threshold_enc_hex = crypto.bytes_to_hex(threshold_encrypted)
        ref_enc_hex = crypto.bytes_to_hex(ref_encrypted)
        
        # Prepare status data
        status = "GAS DETECTED!" if gas_detected else "NORMAL"
        status_class = "alert" if gas_detected else "normal"
        
        # Prepare logs (with encrypted value)
        logs_html = ""
        if gas_alert_log:
            for log in gas_alert_log[-5:][::-1]:  # 5 terakhir, terbaru di atas
                try:
                    value = log.split('Gas: ')[1]
                    value_padded = f"{int(value):08d}"
                    value_enc = crypto.des_encrypt(value_padded, DES_KEY)
                    value_dec = crypto.des_decrypt(value_enc, DES_KEY)
                    value_dec_clean = str(int(value_dec))
                    value_enc_hex = crypto.bytes_to_hex(value_enc)
                except Exception:
                    value_enc_hex = "-"
                    value_dec_clean = "-"
                logs_html += f'<div class="alert-log">{log}<div class="encrypted">Encrypted: {value_enc_hex} | Decrypted: {value_dec_clean}</div></div>'
        else:
            logs_html = '<div class="alert-log empty">No alerts yet</div>'
        
        # Generate HTML
        html = get_html_template().format(
            status=status,
            status_class=status_class,
            gas_level=gas_display,
            gas_enc_hex=gas_enc_hex,
            threshold=threshold_display,
            threshold_enc_hex=threshold_enc_hex,
            reference=ref_display,
            ref_enc_hex=ref_enc_hex,
            logs=logs_html,
            timestamp=get_timestamp()
        )
        return html
    except Exception as e:
        print(f"Error generating HTML: {e}")
        return f"<html><body><h1>Error</h1><p>{e}</p></body></html>"

def handle_web_request(client_socket, gas_detected, current_analog_val, threshold, ref_avg, gas_alert_log):
    """Handle web request dengan error handling yang lebih baik"""
    try:
        # Baca request
        request = client_socket.recv(1024).decode('utf-8')
        
        # Generate HTML response
        html = generate_html_response(gas_detected, current_analog_val, threshold, ref_avg, gas_alert_log)
        
        # Kirim response dengan header yang lebih lengkap
        response_headers = [
            "HTTP/1.1 200 OK",
            "Content-Type: text/html; charset=utf-8",
            "Connection: close",
            "Cache-Control: no-cache",
            "",
            ""
        ]
        
        response = "\r\n".join(response_headers) + html
        client_socket.send(response.encode('utf-8'))
        
    except UnicodeDecodeError as e:
        print(f"Unicode decode error: {e}")
        try:
            error_html = """<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>Error</h1>
    <p>Encoding error occurred</p>
</body>
</html>"""
            error_response = "HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/html; charset=utf-8\r\n\r\n" + error_html
            client_socket.send(error_response.encode('utf-8'))
        except:
            pass
    except Exception as e:
        print(f"Error handling web request: {e}")
        try:
            error_html = """<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>Error</h1>
    <p>Server error occurred</p>
</body>
</html>"""
            error_response = "HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/html; charset=utf-8\r\n\r\n" + error_html
            client_socket.send(error_response.encode('utf-8'))
        except:
            pass
    finally:
        try:
            client_socket.close()
        except:
            pass

def setup_web_server():
    """Setup web server sederhana"""
    import socket
    
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('', 80))
        server.listen(1)
        server.settimeout(1.0)
        print("✅ Web server aktif di port 80")
        return server, True
    except Exception as e:
        print(f"❌ Web server gagal: {e}")
        try:
            # Coba port 8080
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(('', 8080))
            server.listen(1)
            server.settimeout(1.0)
            print("✅ Web server aktif di port 8080")
            return server, True
        except Exception as e2:
            print(f"❌ Web server gagal di port 8080: {e2}")
            return None, False 
