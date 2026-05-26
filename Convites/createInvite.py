import os

# =========================================
# GUEST LIST
# You can have 1, 2, 3, or more guests
# =========================================

guests = [
  # Helo
    (["Rita", "Fábio"], "2 de Agosto de 2026"),
    (["Emilly"], "2 de Agosto de 2026"),
    (["Letícia", "Wilye"], "2 de Agosto de 2026"),
    (["Sarah", "Pedro"], "2 de Agosto de 2026"),
    (["Mariana"], "2 de Agosto de 2026"),
    (["Beatriz Dias"], "2 de Agosto de 2026"),
    (["Beatriz","Ricardo","Helena"], "2 de Agosto de 2026"),
    (["Silke"], "2 de Agosto de 2026")
  #Luis
]

# =========================================
# FUNCTION TO FORMAT NAMES
# =========================================

def format_guest_names(names):

    if len(names) == 1:
        return names[0]

    elif len(names) == 2:
        return f"{names[0]} e {names[1]}"

    else:
        return ", ".join(names[:-1]) + f" e {names[-1]}"


# =========================================
# TEMPLATE 1 (COVER)
# =========================================

cover_template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Wedding Invitation</title>

<style>
  body {{
    margin: 0;
    height: 100vh;
    background-color: #f8f5f1;

    display: flex;
    justify-content: center;
    align-items: center;

    overflow: hidden;
    font-family: Arial, sans-serif;
  }}

  .invite-container {{
    position: relative;
    transform: scale(1.3);
    transform-origin: center;
  }}

  .invite {{
    max-height: 95vh;
    display: block;

    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    border-radius: 12px;
  }}

  /* Button */
  .open-btn {{
    position: absolute;

    /* adjust position */
    bottom: 35%;
    left: 50%;
    transform: translateX(-50%);

    padding: 8px 18px;
    border: none;
    border-radius: 30px;

   background-color: #a08678; /* marrom claro */
   color: #ffffff;

    font-size: 10px;
    cursor: pointer;

    box-shadow: 0 4px 15px rgba(0,0,0,0.2);

    transition: 0.3s;
  }}

  .open-btn:hover {{
    background: white;
    transform: translateX(-50%) scale(1.05);
  }}

  /* Mobile */
  @media (max-width: 768px) {{
    .invite-container {{
      transform: scale(1);
    }}

    .invite {{
      max-width: 95vw;
      height: auto;
    }}

    .open-btn {{
      font-size: 16px;
      padding: 12px 22px;
      bottom: 32%;
    }}
  }}
</style>
</head>

<body>

  <div class="invite-container">

    <img class="invite" src="Convite1.png" alt="Wedding Invitation">

    <!-- Button -->
    <button class="open-btn"
      onclick="window.location.href='c_{code}.html'">
      Clique aqui para abrir
    </button>

  </div>

</body>
</html>
"""


# =========================================
# TEMPLATE 2 (INVITATION)
# =========================================

invite_template = """

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="../style.css">

<title>Invitation</title>

<style>
  body {{
    margin: 0;
    height: 100vh;
    background-color: #f8f5f1;

    display: flex;
    justify-content: center;
    align-items: center;

    overflow: hidden;
    font-family: Arial, sans-serif;
  }}

  .invite-container {{
    position: relative;
    transform: scale(1.3);
    transform-origin: center;
  }}

  .invite {{
    max-height: 95vh;
    display: block;

    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    border-radius: 12px;
  }}

  /* Text on top of image */
  .invite-text {{
    position: absolute;

    top: 55%;
    left: 50%;
    transform: translate(-50%, -50%);

    width: 80%;

    text-align: center;
    color: #6b4f3f;

    font-size: 20px;
    line-height: 1.2;
  }}

  .invite-text h1 {{
    margin-bottom: 0px;
    font-size: 35px;
    font-weight: 400;
    letter-spacing: 2px;
    line-height: 1.2;
    color: #7c7e50;
  }}

  .invite-text nav {{
  margin-bottom: 0px;
  font-size: 15px;
  letter-spacing: 0.3px;
  line-height: 1.2;
  color: #6b4f3f;
  }}

  .bold-text {{
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.3px;
    line-height: 1.2;
    color: #6b4f3f;
  }}

  .invite-text nav.small-note {{
    font-size: 12px;
    letter-spacing: 0.3px;
    color: #7a5c4d;
    line-height: 1.2;
  }}


  /* Button */
  .open-btn {{
  margin-top: 18px;

  padding: 8px 18px;
  border: none;
  border-radius: 30px;

  background-color: #a08678; /* marrom claro */
  color: #ffffff;

  font-size: 10px;
  cursor: pointer;

  transition: 0.3s;
  }}

  .open-btn:hover {{
    background: white;
    transform: scale(1.05);
  }}

  /* Mobile */
  @media (max-width: 768px) {{

    .invite-container {{
      transform: scale(1);
    }}

    .invite {{
      transform: scale(1.08);
      transform-origin: center;
      max-width: 95vw;
      height: auto;
    }}

    .invite-text {{
      width: 85%;
    }}

    .invite-text h1 {{
      font-size: 28px;
    }}

    .invite-text nav {{
      font-size: 14px;
    }}

    .invite-text .bold-text {{
      font-size: 15px;
    }}

    .invite-text .small-note {{
      font-size: 12px;
    }}

    .open-btn {{
      font-size: 12px;
      padding: 8px 16px;
    }}
  }}

</style>
</head>

<body>

  <div class="invite-container">

    <img class="invite" src="Convite2.png" alt="Wedding Invitation">

    <div class="invite-text">
      <h1>Heloisa & Luis</h1>

      <nav>
        convidam <strong>{guest_text}</strong> para o seu casamento dia
      </nav>

      <nav class="bold-text">
        21 de Fevereiro de 2027 às 11:00 h
      </nav>

      <nav class="small-note">
        Av. Angélica, 2278 - Consolação, São Paulo - SP, Brasil
      </nav>

    <!-- Button -->
    <button class="open-btn"
    onclick="window.location.href='../index.html'">
    Clique para Confirmar Presença
    </button>

    <nav class="small-note">
      Confirmar até dia {date}
    </nav>

    </div>

  </div>

</body>
</html>
"""


# =========================================
# CREATE FILES
# =========================================

for names, date in guests:

    code = "".join(name.replace(" ", "") for name in names)

    guest_text = format_guest_names(names)

    cover_filename = f"{code}.html"
    invite_filename = f"c_{code}.html"

    with open(cover_filename, "w", encoding="utf-8") as f:
        f.write(
            cover_template.format(code=code)
        )

    with open(invite_filename, "w", encoding="utf-8") as f:
        f.write(
            invite_template.format(
                guest_text=guest_text,
                date=date
            )
        )

    print(f"Created: {cover_filename}")
    print(f"Created: {invite_filename}")