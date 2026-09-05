import ctypes
import sys
import os
import tkinter as tk
from tkinter import messagebox

def force_bsod():
    """
    Forces a Blue Screen of Death using NtRaiseHardError.
    """
    # Check if running as admin
    if not ctypes.windll.shell32.IsUserAnAdmin():
        messagebox.showerror("Admin Required", "Please run this script as Administrator.")
        sys.exit(1)

    try:
        ntdll = ctypes.windll.ntdll
        
        # Parameters for NtRaiseHardError
        # ErrorStatus: 0xC0000005 (Access Violation)
        # NumberOfParameters: 0
        # ValidResponseOptions: 1 (Force the response)
        # Response: 7 (BugCheck/BSOD)
        
        response = ctypes.c_ulong(7)
        
        result = ntdll.NtRaiseHardError(
            ctypes.c_long(0xC0000005),  # STATUS_ACCESS_VIOLATION
            ctypes.c_ulong(0),          # No extra parameters
            ctypes.c_ulong(0),          # Validity offset
            None,                       # Parameters buffer
            ctypes.c_ulong(1),          # Force response
            ctypes.byref(response)
        )
        
        if result != 0:
            messagebox.showerror("BSOD Failed", f"NtRaiseHardError failed with code: {hex(result)}")
        else:
            messagebox.showinfo("Success", "BSOD Triggered! System will crash now.")
            
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def confirm_bsod():
    """
    Second window: "Are you sure?"
    """
    root2 = tk.Toplevel()
    root2.title("Are you sure?")
    root2.geometry("300x150")
    root2.resizable(False, False)
    
    label = tk.Label(root2, text="Are you sure you want to crash your system?", font=("Arial", 12))
    label.pack(pady=20)
    
    def on_yes():
        root2.destroy()
        force_bsod()
        # Give a tiny delay for the window to close before the system crashes
        import time
        time.sleep(0.5) 

    def on_no():
        root2.destroy()
        root.destroy()

    btn_frame = tk.Frame(root2)
    btn_frame.pack(pady=10)
    
    btn_yes = tk.Button(btn_frame, text="Yes", command=on_yes, width=10, font=("Arial", 10))
    btn_yes.pack(side=tk.LEFT, padx=10)
    
    btn_no = tk.Button(btn_frame, text="No", command=on_no, width=10, font=("Arial", 10))
    btn_no.pack(side=tk.LEFT, padx=10)

def ask_run():
    """
    First window: "Do you want to run this?"
    """
    root = tk.Tk()
    root.title("BSOD Forcer")
    root.geometry("300x150")
    root.resizable(False, False)
    
    label = tk.Label(root, text="Do you want to run this?", font=("Arial", 12))
    label.pack(pady=20)
    
    def on_yes():
        root.destroy()
        confirm_bsod()

    def on_no():
        root.destroy()

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)
    
    btn_yes = tk.Button(btn_frame, text="Yes", command=on_yes, width=10, font=("Arial", 10))
    btn_yes.pack(side=tk.LEFT, padx=10)
    
    btn_no = tk.Button(btn_frame, text="No", command=on_no, width=10, font=("Arial", 10))
    btn_no.pack(side=tk.LEFT, padx=10)
    
    root.mainloop()

if __name__ == "__main__":
    ask_run()