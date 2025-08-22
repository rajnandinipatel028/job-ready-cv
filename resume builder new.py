from reportlab.lib.pagesizes import A4 # pyright: ignore[reportMissingModuleSource]
from reportlab.pdfgen import canvas # pyright: ignore[reportMissingModuleSource]

def create_resume(data, filename="resume.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    _, height = A4
    y = height - 50  # start from top

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, data["name"])
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Email: {data['email']} | Phone: {data['phone']}")
    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Summary")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, data["summary"])
    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Education")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, data["education"])
    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Experience")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, data["experience"])
    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Skills")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, data["skills"])
    y -= 40

    c.save()
    print(f"\n✅ Resume saved as {filename}")


def main():
    print("=== Resume Creator ===")
    data = {}
    data["name"] = input("Enter your full name: ")
    data["email"] = input("Enter your email: ")
    data["phone"] = input("Enter your phone number: ")
    data["summary"] = input("Enter a short summary: ")
    data["education"] = input("Enter your education details: ")
    data["experience"] = input("Enter your work experience: ")
    data["skills"] = input("Enter your skills (comma separated): ")

    create_resume(data)


if __name__ == "__main__":
    main()
