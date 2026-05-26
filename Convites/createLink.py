import pandas as pd

guests = [
    # Helo
    (["Rita", "Fábio"], "2 de Agosto de 2026"),
    (["Emilly"], "2 de Agosto de 2026"),
    (["Letícia", "Wilye"], "2 de Agosto de 2026"),
    (["Sarah", "Pedro"], "2 de Agosto de 2026"),
    (["Mariana"], "2 de Agosto de 2026"),
    (["Beatriz Dias"], "2 de Agosto de 2026"),
    (["Beatriz", "Ricardo", "Helena"], "2 de Agosto de 2026"),
    (["Silke"], "2 de Agosto de 2026")
]

base_url = "https://casamento-hl.github.io/HeloLuis/Convites/"

rows = []

for names, date in guests:
    filename = "".join(name.replace(" ", "") for name in names)
    link = f"{base_url}{filename}.html"

    rows.append({
        "Guests": ", ".join(names),
        "Date": date,
        "Link": link
    })

# Create DataFrame
df = pd.DataFrame(rows)

# Save to Excel
df.to_excel("guest_links.xlsx", index=False)

print("Excel file saved as guest_links.xlsx")