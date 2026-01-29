import socket

# அழகான பேனர்
print("""
*************************************************
*          Pr3mG_Sec_heck CCTV GUARD            *
*       Building Cyber Security in SL 🇱🇰        *
*************************************************
""")

target = input("Enter Target IP: ")

# CCTV மற்றும் சர்வர்களுக்கான முக்கியமான 10 போர்ட்கள்
ports = [21, 22, 23, 80, 443, 554, 1935, 8000, 8080, 8443]

print(f"\n[+] Scanning {target}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[!] PORT {port} IS OPEN (Alert!)")
    else:
        print(f"[-] Port {port}: Closed")
    s.close()

print("\nScan Completed!")
input("Press Enter to Exit...")