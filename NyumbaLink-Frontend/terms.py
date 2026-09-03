from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

path = "NyumbaLink_Limited_Terms_and_Conditions.pdf"

doc = SimpleDocTemplate(
    path, pagesize=A4,
    rightMargin=18*mm, leftMargin=18*mm,
    topMargin=18*mm, bottomMargin=18*mm,
    title="NyumbaLink Limited – Terms and Conditions"
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TitleNL", parent=styles["Title"], alignment=TA_CENTER,
    fontSize=19, leading=23, spaceAfter=8
))
styles.add(ParagraphStyle(
    name="SubTitleNL", parent=styles["Normal"], alignment=TA_CENTER,
    fontSize=10, leading=14, textColor=colors.grey, spaceAfter=18
))
styles.add(ParagraphStyle(
    name="HeadingNL", parent=styles["Heading2"],
    fontSize=12.5, leading=16, spaceBefore=10, spaceAfter=5
))
styles.add(ParagraphStyle(
    name="BodyNL", parent=styles["BodyText"],
    fontSize=9.5, leading=14, spaceAfter=7
))

sections = [
("1. Introduction",
"""These Terms and Conditions govern your use of the NyumbaLink platform, website and related services operated by NyumbaLink Limited (“NyumbaLink”, “we”, “us” or “our”). By accessing or using the platform, you agree to comply with these Terms and Conditions. If you do not agree with them, please do not use the platform."""),
("2. About NyumbaLink",
"""NyumbaLink is a property platform designed to help people search for houses, land and other property opportunities across Kenya. The platform organizes searches by county, town and area and is intended to facilitate connections between property seekers, landlords and property sellers."""),
("3. Eligibility",
"""You must provide accurate information when creating an account or submitting a property listing. By using NyumbaLink, you confirm that you are legally capable of entering into agreements applicable to your use of the platform. Where an account is created on behalf of another person or organization, you must have authority to do so."""),
("4. Property Listings",
"""Landlords, sellers and other listing users are responsible for ensuring that all information they submit is accurate, current and not misleading. This includes property descriptions, location, rental or sale price, availability, ownership-related information, photographs and contact details."""),
("5. Verification and Accuracy",
"""NyumbaLink may review, moderate, remove or request clarification about listings, but we do not guarantee that every listing, property, landlord, seller, photograph, price, ownership claim or other information is accurate, genuine, available or legally compliant. Users should independently verify property information and ownership before making payments or entering into agreements."""),
("6. Direct Transactions",
"""NyumbaLink is intended to help property seekers connect directly with landlords and sellers. NyumbaLink is not a party to any tenancy, sale, lease, deposit, agency, management or other agreement between users unless expressly stated otherwise. Any transaction entered into by users is undertaken at their own risk and responsibility."""),
("7. Payments and Fees",
"""The standard starter property listing flow is currently free unless a different fee is clearly displayed or communicated by NyumbaLink. NyumbaLink may introduce premium listings, promotional services or other paid features in the future. Applicable charges, payment terms and refund conditions will be communicated before a paid service is used."""),
("8. User Accounts and Security",
"""Where accounts are provided, users are responsible for keeping their login information secure and for all activity conducted through their account. You should notify NyumbaLink promptly if you believe your account has been accessed without authorization. NyumbaLink may suspend or terminate accounts that violate these Terms or create risks for other users or the platform."""),
("9. Prohibited Use",
"""Users must not use NyumbaLink to publish fraudulent, deceptive, defamatory, unlawful, discriminatory or abusive content; impersonate another person; misrepresent ownership or authority over a property; upload malicious software; interfere with the operation of the platform; harvest personal information without authorization; or use the platform for any unlawful purpose."""),
("10. Communications and Contact Details",
"""Users may contact landlords or sellers using the contact information supplied in a listing. Users should exercise appropriate caution when communicating with unknown persons and should not send money or disclose sensitive information solely because a person or property appears on NyumbaLink."""),
("11. Third-Party Services and Links",
"""NyumbaLink may contain links, integrations or references to third-party websites, payment services, communication services or other resources. Such third-party services are governed by their own terms and policies. NyumbaLink is not responsible for the availability, content, security or practices of third-party services."""),
("12. Intellectual Property",
"""The NyumbaLink name, branding, logos, website design, software, text, graphics and other platform materials may be protected by intellectual property laws. Except as permitted by law or expressly authorized by NyumbaLink, users must not copy, reproduce, modify, distribute, sell or commercially exploit NyumbaLink materials."""),
("13. User-Submitted Content",
"""By submitting property photographs, descriptions or other content to NyumbaLink, you confirm that you have the necessary rights or permission to provide that content. You grant NyumbaLink a non-exclusive permission to host, display, reproduce and use the content as reasonably necessary to operate, promote and improve the platform, subject to applicable law."""),
("14. Privacy",
"""NyumbaLink may collect and process information necessary to operate the platform, including account, listing and communication information. Personal information will be handled in accordance with NyumbaLink’s applicable Privacy Policy and Kenyan data-protection requirements. Users should review the Privacy Policy for further information about collection, use, storage and disclosure of personal information."""),
("15. Disclaimer",
"""NyumbaLink provides a marketplace and information service. To the extent permitted by applicable law, we do not guarantee uninterrupted availability of the platform or the accuracy, completeness, suitability, safety or legality of any property listing or user. A listing on NyumbaLink should not be treated as a guarantee, certification, valuation, inspection, title confirmation or legal advice."""),
("16. Limitation of Liability",
"""To the maximum extent permitted by applicable law, NyumbaLink Limited will not be liable for losses arising from transactions, communications or agreements between users, fraudulent conduct by users, inaccurate listings supplied by users, inability to access a property, loss of data, service interruptions or other indirect or consequential losses arising from use of the platform. Nothing in these Terms excludes liability that cannot lawfully be excluded."""),
("17. Indemnity",
"""To the extent permitted by law, users agree to indemnify and hold NyumbaLink Limited harmless from claims, losses, liabilities, costs or expenses arising from their unlawful use of the platform, violation of these Terms, infringement of another person's rights, or inaccurate or fraudulent information submitted by them."""),
("18. Suspension and Termination",
"""NyumbaLink may remove a listing, restrict access, suspend an account or terminate platform access where reasonably necessary, including where a user violates these Terms, provides misleading information, engages in suspected fraud or creates a risk to other users or the platform."""),
("19. Changes to These Terms",
"""NyumbaLink may update these Terms and Conditions from time to time as the platform develops or legal requirements change. Updated terms will take effect when published through the platform unless a different effective date is stated. Continued use of NyumbaLink after an update constitutes acceptance of the revised terms."""),
("20. Governing Law and Disputes",
"""These Terms and Conditions are intended to be governed by the laws of Kenya. Users should first attempt to resolve disputes with NyumbaLink through good-faith communication. Where a dispute cannot be resolved informally, it may be referred to the appropriate courts or dispute-resolution mechanism with jurisdiction in Kenya, subject to applicable law."""),
("21. Contact",
"""For questions concerning these Terms and Conditions, platform use, listings or complaints, please contact NyumbaLink Limited through the official contact details published on the NyumbaLink platform."""),
]

story = [
    Paragraph("NYUMBALINK LIMITED", styles["TitleNL"]),
    Paragraph("TERMS AND CONDITIONS", styles["TitleNL"]),
    Paragraph("Effective date: 3 September 2026", styles["SubTitleNL"]),
    Paragraph(
        "<b>Important:</b> These Terms and Conditions are a general platform-use document and should be reviewed by a qualified Kenyan advocate before publication, especially for provisions concerning liability, privacy, property verification, payments and dispute resolution.",
        styles["BodyNL"]
    ),
]
for heading, body in sections:
    story.append(Paragraph(heading, styles["HeadingNL"]))
    story.append(Paragraph(body, styles["BodyNL"]))

story += [
    Spacer(1, 8),
    Paragraph("<b>End of Terms and Conditions</b>", styles["BodyNL"]),
]

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(18*mm, 10*mm, "NyumbaLink Limited — Terms and Conditions")
    canvas.drawRightString(A4[0]-18*mm, 10*mm, f"Page {doc.page}")
    canvas.restoreState()

doc.build(story, onFirstPage=footer, onLaterPages=footer)

print(path)
