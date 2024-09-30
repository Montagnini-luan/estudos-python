import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

emailoutlook = outlook.CreateItem(0)

emailoutlook.to = "luanmontagnini60@gmail.com"
emailoutlook.Subject = "Meu primeiro email usando Python e Outlook"
emailoutlook.HTMLBody = """
<p>Boa noite Luan </p>
<p>Esse e apenas um email de teste </p>
<p>Atencionsamente.</p>
"""

emailoutlook.save()