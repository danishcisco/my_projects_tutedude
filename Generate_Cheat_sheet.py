from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch

def create_cheat_sheet():
    filename = "Network_Troubleshooting_Cheat_Sheet.pdf"
    doc = SimpleDocTemplate(filename, pagesize=LETTER, topMargin=0.5*inch, bottomMargin=0.5*inch)
    elements = []
    styles = getSampleStyleSheet()

    # --- Header ---
    title_style = ParagraphStyle('Title', parent=styles['Heading1'], alignment=1, fontSize=18, spaceAfter=12)
    elements.append(Paragraph("Network Operations Troubleshooting Cheat Sheet", title_style))
    elements.append(Paragraph("<b>Focus:</b> Switching (L2) & IPv4 Addressing (L3)", styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))

    # --- Section 1: The Golden Workflow ---
    elements.append(Paragraph("1. The Golden Workflow (Check in Order)", styles['Heading2']))
    workflow_data = [
        ["Step", "Layer", "What to Check", "Success Indicator"],
        ["1", "Physical (L1)", "Cables, Link Lights, SFPs", "Link LED is Solid Green"],
        ["2", "Data Link (L2)", "Port Status, VLAN, MAC Table", "Switch sees Device MAC address"],
        ["3", "Network (L3)", "IP, Subnet Mask, Gateway", "Valid IP (Not 169.254.x.x)"],
        ["4", "Reachability", "Ping Gateway -> Internet -> DNS", "Reply from 8.8.8.8 & google.com"]
    ]
    t1 = Table(workflow_data, colWidths=[0.5*inch, 1.2*inch, 2.5*inch, 2.5*inch])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.navy),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,1), (-1,1), colors.whitesmoke),
        ('BACKGROUND', (0,3), (-1,3), colors.whitesmoke),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(t1)
    elements.append(Spacer(1, 0.2*inch))

    # --- Section 2: Quick Decision Logic ---
    elements.append(Paragraph("2. Rapid Decision Logic: Switch vs. IP?", styles['Heading2']))
    decision_data = [
        ["Symptom", "Link Light", "IP Status", "Ping Gateway", "Likely Root Cause"],
        ["Dead Air", "OFF / Dark", "N/A", "Fails", "Physical (L1) - Cable/Power"],
        ["Blocked", "Green/Amber", "169.254.x.x", "Fails", "Switching (L2) - VLAN/DHCP Snooping"],
        ["Isolated", "Green", "Valid IP", "Fails", "Routing (L3) - Gateway/Mask Issue"],
        ["Lost", "Green", "Valid IP", "Success", "DNS / Application Layer"]
    ]
    t2 = Table(decision_data, colWidths=[1.0*inch, 1.0*inch, 1.2*inch, 1.2*inch, 2.3*inch])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.darkgreen),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(t2)
    elements.append(Spacer(1, 0.2*inch))

    # --- Section 3: Essential Commands ---
    elements.append(Paragraph("3. Essential Command Reference", styles['Heading2']))
    cmd_data = [
        ["Goal", "Windows Command", "Cisco IOS Command"],
        ["Check IP Config", "ipconfig /all", "show ip int brief"],
        ["Test Connectivity", "ping -t [IP_Address]", "ping [IP_Address]"],
        ["Trace Path", "tracert -d [IP_Address]", "traceroute [IP_Address]"],
        ["See Neighbors (L2)", "arp -a", "show mac address-table int [ID]"],
        ["Check Interface Errors", "netstat -e", "show int [ID] status"],
        ["Check VLANs", "N/A", "show vlan brief"]
    ]
    t3 = Table(cmd_data, colWidths=[2.0*inch, 2.0*inch, 2.7*inch])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTNAME', (1,1), (-1,-1), 'Courier'), # Monospace for commands
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,1), (-1,-1), colors.aliceblue),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(t3)
    elements.append(Spacer(1, 0.2*inch))

    # --- Section 4: Escalation Checklist ---
    elements.append(Paragraph("4. Before You Escalate (The 'Golden Ticket' Data)", styles['Heading2']))
    elements.append(Paragraph("<i>Do not escalate a ticket without these 5 items:</i>", styles['Normal']))
    
    escalation_style = ParagraphStyle('Escalation', parent=styles['Normal'], leftIndent=20, leading=14)
    bullets = [
        "1. <b>Source IP & MAC Address:</b> (From ipconfig /all)",
        "2. <b>Switch Name & Port Number:</b> (e.g., SW-FLOOR1 Port Gi1/0/24)",
        "3. <b>Scope:</b> Is it one user, one row, or the whole building?",
        "4. <b>Time:</b> When did it start? (Did it happen after a change?)",
        "5. <b>Test Results:</b> 'I can ping the Gateway but cannot ping 8.8.8.8'"
    ]
    
    for b in bullets:
        elements.append(Paragraph(b, escalation_style))

    # Build PDF
    doc.build(elements)
    print(f"PDF Generated Successfully: {filename}")

if __name__ == "__main__":
    create_cheat_sheet()