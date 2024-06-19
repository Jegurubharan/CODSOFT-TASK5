import tkinter as tk
from tkinter import ttk, messagebox
class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        # Initialize an empty list to store contacts
        self.contacts = []
        # Frame for contact list and details
        self.contacts_frame = ttk.Frame(self.root, padding="20")
        self.contacts_frame.grid(row=0, column=0, sticky="nsew")
        # Contact List
        self.contact_listbox = tk.Listbox(self.contacts_frame, width=40, height=10)
        self.contact_listbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        # Scrollbar for contact list
        self.scrollbar = ttk.Scrollbar(self.contacts_frame, orient=tk.VERTICAL, command=self.contact_listbox.yview)
        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        # Label and Entry for adding new contact
        self.name_label = ttk.Label(self.contacts_frame, text="Name:")
        self.name_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.name_entry = ttk.Entry(self.contacts_frame, width=30)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.phone_label = ttk.Label(self.contacts_frame, text="Phone:")
        self.phone_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.phone_entry = ttk.Entry(self.contacts_frame, width=30)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5)
        self.email_label = ttk.Label(self.contacts_frame, text="Email:")
        self.email_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.email_entry = ttk.Entry(self.contacts_frame, width=30)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)
        self.address_label = ttk.Label(self.contacts_frame, text="Address:")
        self.address_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.address_entry = ttk.Entry(self.contacts_frame, width=30)
        self.address_entry.grid(row=4, column=1, padx=10, pady=5)
        # Label to display total number of contacts
        self.total_label = ttk.Label(self.contacts_frame, text="")
        self.total_label.grid(row=5, column=0, columnspan=2, pady=10)
        # Buttons for actions
        self.add_button = ttk.Button(self.contacts_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.view_button = ttk.Button(self.contacts_frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.search_label = ttk.Label(self.contacts_frame, text="Search:")
        self.search_label.grid(row=8, column=0, sticky="w", padx=10, pady=5)
        self.search_entry = ttk.Entry(self.contacts_frame, width=30)
        self.search_entry.grid(row=8, column=1, padx=10, pady=5)
        self.search_button = ttk.Button(self.contacts_frame, text="Search", command=self.search_contact)
        self.search_button.grid(row=9, column=0, columnspan=2, pady=10)
        self.update_button = ttk.Button(self.contacts_frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=10, column=0, columnspan=2, pady=10)
        self.delete_button = ttk.Button(self.contacts_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=11, column=0, columnspan=2, pady=10)
        # Configure grid weights
        self.contacts_frame.grid_rowconfigure(0, weight=1)
        self.contacts_frame.grid_columnconfigure(0, weight=1)
    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()
        if name and phone:  # Ensure name and phone are provided
            contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
            self.contacts.append(contact)
            self.update_contact_list()
            self.clear_entries()
            self.update_total_label()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Name and Phone number are required.")
    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
        self.update_total_label()
    def search_contact(self):
        query = self.search_entry.get().strip().lower()
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if query in contact['name'].lower() or query in contact['phone']:
                self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
        self.update_total_label()
    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            updated_name = self.name_entry.get().strip()
            updated_phone = self.phone_entry.get().strip()
            updated_email = self.email_entry.get().strip()
            updated_address = self.address_entry.get().strip()
            if updated_name and updated_phone:
                self.contacts[index] = {
                    'name': updated_name,
                    'phone': updated_phone,
                    'email': updated_email,
                    'address': updated_address
                }
                self.update_contact_list()
                self.clear_entries()
                self.update_total_label()
                messagebox.showinfo("Success", "Contact updated successfully.")
            else:
                messagebox.showerror("Error", "Name and Phone number are required.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")
    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.update_contact_list()
            self.clear_entries()
            self.update_total_label()
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")
    def update_contact_list(self):
        self.view_contacts()  # Simply refreshes the contact list
    def update_total_label(self):
        total_contacts = len(self.contacts)
        self.total_label.config(text=f"Total Contacts: {total_contacts}")
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()