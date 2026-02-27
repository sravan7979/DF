import socket
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread


def scan_ports():
    target = entry_ip.get()
    start_port = int(entry_start.get())
    end_port = int(entry_end.get())

    result_box.delete(1.0, tk.END)

    def run_scan():
        result_box.insert(tk.END, f"Scanning {target}\n")

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((target, port))

            if result == 0:
                result_box.insert(
                    tk.END,
                    f"Port {port} : OPEN\n"
                )

            sock.close()

        result_box.insert(tk.END, "\nScan Completed")

    Thread(target=run_scan).start()


# GUI Window
root = tk.Tk()
root.title("IP & Port Scanner")
root.geometry("500x450")

# IP input
tk.Label(root, text="Target IP").pack()
entry_ip = tk.Entry(root, width=40)
entry_ip.pack()

# Start port
tk.Label(root, text="Start Port").pack()
entry_start = tk.Entry(root)
entry_start.pack()

# End port
tk.Label(root, text="End Port").pack()
entry_end = tk.Entry(root)
entry_end.pack()

# Scan Button
tk.Button(root, text="Start Scan",
          command=scan_ports).pack(pady=10)

# Output box
result_box = scrolledtext.ScrolledText(
    root,
    width=60,
    height=15
)
result_box.pack()

root.mainloop()
