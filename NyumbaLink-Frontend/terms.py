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
    (
        "1. Introduction and Acceptance",
        """These Terms and Conditions ("Terms") constitute a legally binding agreement between you ("User", "you", or "your") and NyumbaLink Limited ("NyumbaLink", "we", "us", or "our"), a company incorporated under the Companies Act, 2015 of the Laws of Kenya. These Terms govern your access to and use of the NyumbaLink web application, mobile applications, APIs, and associated services (collectively, the "Platform"). By accessing, browsing, registering, or listing on the Platform, you acknowledge that you have read, understood, and agreed to be bound by these Terms and our Privacy Policy. If you do not agree to these Terms, you must immediately cease all use of the Platform.""",
    ),
    (
        "2. Platform Scope and Regulatory Disclosures",
        """NyumbaLink operates exclusively as an online listing aggregator and information exchange platform connecting property seekers, landlords, real estate agents, property managers, and property sellers across Kenya. 

In accordance with the Consumer Protection Act, 2012 (No. 46 of 2012):
(a) NyumbaLink is NOT a licensed real estate agency, property management firm, land valuer, conveyancer, or financial institution under Kenyan law.
(b) NyumbaLink does not hold legal title to, leasehold interest in, or custody of any properties displayed on the Platform.
(c) The display of a property listing on the Platform does not constitute an endorsement, official verification, valuation, or structural guarantee by NyumbaLink Limited.""",
    ),
    (
        "3. Eligibility and Legal Capacity",
        """By creating an account or interacting with the Platform, you represent and warrant that:
(a) You are at least eighteen (18) years of age and possess full legal capacity to enter into binding contracts under the Law of Contract Act (Cap 23, Laws of Kenya).
(b) If registering or acting on behalf of a corporate body, partnership, or trust, you hold express legal authority to bind that entity to these Terms.
(c) Your use of the Platform does not violate any applicable Kenyan laws, regulations, or third-party rights.""",
    ),
    (
        "4. Property Listings and Representation Warranties",
        """Landlords, sellers, agents, and listing agents ("Publishers") bear sole, strict legal responsibility for the truthfulness and accuracy of all submitted listings. Every Publisher expressly warrants that:
(a) They possess verified legal title, power of attorney, valid agency authorization, or tenancy management mandates required under the Land Act, 2012 and Land Registration Act, 2012 to list, market, lease, or sell the specified property.
(b) All property details—including but not limited to rent/sale prices, location data, total/available units, amenities, square footage, encumbrances, and photographic representations—are current, exact, and not deceptive or fraudulent.
(c) Property images uploaded are true, unmanipulated representations of the actual physical premises.""",
    ),
    (
        "5. Independent Due Diligence and Verification Disclaimer",
        """While NyumbaLink reserves the right to review, moderate, request proof of title/mandate, or take down non-compliant listings, we perform no formal conveyancing, official registry searches (Ministry of Lands / ArdhiSaasa), or physical structural inspections. 

Property seekers are strictly advised to independently conduct all standard legal due diligence prior to executing agreements or transferring funds, including:
(a) Inspecting official green cards/search certificates at the relevant Land Registry or via ArdhiSaasa.
(b) Conducting physical site visits to verify unit availability and structural safety.
(c) Verifying the identity and legitimacy of the landlord, seller, or registered estate agent.""",
    ),
    (
        "6. Direct Transactions and Disclaimer of Agency",
        """All lease agreements, tenancy contracts, sale agreements, booking deposits, or monetary transactions negotiated via the Platform occur strictly and directly between the respective users. 

(a) NyumbaLink is not a party to, third-party beneficiary of, or guarantor for any transaction or dispute arising out of interactions initiated on the Platform.
(b) NyumbaLink strictly disclaims liability for any advance payments, holding deposits, agency fees, or rental sums paid directly to Publishers or third parties.""",
    ),
    (
        "7. Fees, Paid Features, and Financial Terms",
        """(a) Standard browsing and basic property listing submission flows are provided free of charge or at fees clearly indicated on the Platform.
(b) NyumbaLink reserves the right to introduce optional premium services, featured placement fees, or subscription tiers. All fees, billing structures, and non-refundable terms will be explicitly disclosed to you prior to authorization.
(c) All payments processed through integrated payment gateways (e.g., M-PESA, credit/debit cards) are governed by the respective payment processor’s terms.""",
    ),
    (
        "8. User Accounts, Credentials, and Security",
        """(a) You are responsible for maintaining the strict confidentiality of your login credentials, phone numbers, and authentication tokens.
(b) You assume total legal responsibility for all activities, messages, and listings originated under your account.
(c) You agree to notify NyumbaLink immediately via official channels upon detecting any unauthorized access, breach, or compromise of your account.""",
    ),
    (
        "9. Prohibited Conduct and System Integrity",
        """Pursuant to the Computer Misuse and Cybercrimes Act, 2018 (No. 5 of 2018), users strictly agree NOT to:
(a) Publish false, fraudulent, misleading, deceptive, defamatory, or unlawful property listings.
(b) Misrepresent identity, impersonate third parties, or fake land/property ownership or agency mandates.
(c) Scrape, harvest, extract, or mine data, phone numbers, images, or user details automatically or manually without prior written consent.
(d) Introduce viruses, Trojans, malware, or execute denial-of-service attacks against the Platform infrastructure.
(e) Bypassing authentication or probing system vulnerabilities.""",
    ),
    (
        "10. Communication Guidelines and Risk Warnings",
        """(a) Contact features (direct phone calls, emails, or WhatsApp shortcuts) are supplied to facilitate genuine real estate inquiries.
(b) Users must exercise caution when communicating with unknown persons and should never remit funds (e.g., viewing fees, reservation deposits) prior to physical verification and execution of formal legal documentation.
(c) NyumbaLink accepts no responsibility for off-platform communications or fraudulent solicitations conducted via third-party messaging apps.""",
    ),
    (
        "11. Third-Party Integrations and External Links",
        """The Platform may embed links, maps, communications links, or external tools (such as WhatsApp, Google Maps, or payment gateways). Such integrations are operated by independent third parties under their respective terms. NyumbaLink exerts no operational control over, and expressly disclaims liability for, the availability, privacy practices, accuracy, or safety of external services.""",
    ),
    (
        "12. Intellectual Property Rights",
        """All software code, database design, user interfaces, branding, domain names, service marks, copy, graphics, and visual elements on the Platform are the exclusive intellectual property of NyumbaLink Limited, protected under the Copyright Act (Cap 130, Laws of Kenya) and the Trade Marks Act (Cap 506, Laws of Kenya). Unauthorized reproduction, extraction, reverse engineering, or commercial exploitation is strictly prohibited.""",
    ),
    (
        "13. User-Submitted Content and Licensing",
        """By submitting property photos, text descriptions, media, or listings to NyumbaLink:
(a) You grant NyumbaLink Limited a perpetual, royalty-free, worldwide, non-exclusive license to host, index, display, resize, distribute, format, and re-transmit such content for platform operation, syndication, and marketing purposes.
(b) You confirm that you possess all necessary copyright licenses and property consent releases for media uploaded.""",
    ),
    (
        "14. Privacy and Data Protection Compliance",
        """NyumbaLink processes personal data in strict compliance with the Data Protection Act, 2019 (No. 24 of 2019) and the Data Protection (General) Regulations, 2021.
(a) By using the Platform, you consent to the collection, processing, and lawful disclosure of your personal data (such as contact info, listing metadata) necessary for real estate connectivity.
(b) Details regarding your rights as a data subject (access, correction, erasure, objection) are set out in our Privacy Policy.""",
    ),
    (
        "15. Service Availability and Operational Disclaimers",
        """The Platform is provided on an "AS IS" and "AS AVAILABLE" basis without warranties of any kind, express or implied. NyumbaLink does not guarantee that access to the site will be uninterrupted, error-free, timely, secure, or free from server outages, maintenance downtime, or cyber-attacks.""",
    ),
    (
        "16. Limitation of Liability",
        """To the maximum extent permitted by Kenyan law, NyumbaLink Limited, its directors, officers, employees, agents, and affiliates shall NOT be liable for any direct, indirect, incidental, punitive, special, or consequential damages, including but not limited to:
(a) Loss of money, deposits, rental sums, or purchase funds paid to fraudulent landlords/sellers.
(b) Inaccuracies, typographical errors, or misrepresentations in property listings.
(c) Physical injuries, trespass claims, or contractual disputes occurring during property visits or tenancies.
(d) Loss of data, server downtime, or cyber breaches beyond our reasonable control.""",
    ),
    (
        "17. Indemnification",
        """You agree to defend, indemnify, and hold harmless NyumbaLink Limited, its directors, employees, and agents from and against all legal claims, liabilities, costs, losses, damages, or expenses (including legal fees) arising from:
(a) Your breach of these Terms or applicable laws.
(b) Misleading, unlawful, or fraudulent content submitted by you.
(c) Disputes between you and any landlord, seller, tenant, or buyer.""",
    ),
    (
        "18. Account Suspension, Listing Removal, and Termination",
        """NyumbaLink reserves the absolute right, without prior notice or liability, to edit, decline, flag, suspend, or permanently remove any property listing, user account, or platform access if we suspect:
(a) Fraudulent activity, false advertising, or identity misrepresentation.
(b) Violation of the Data Protection Act, 2019 or Cybercrimes Act, 2018.
(c) Repeated user complaints or breach of these Terms.""",
    ),
    (
        "19. Amendments to Terms",
        """NyumbaLink Limited reserves the right to modify or revise these Terms at any time. Updated versions will be published on the Platform with a updated "Effective Date". Your continued use of the Platform after such changes constitute binding acceptance of the modified Terms.""",
    ),
    (
        "20. Governing Law, Dispute Resolution, and Jurisdiction",
        """(a) Governing Law: These Terms are governed by and construed in accordance with the Laws of the Republic of Kenya.
(b) Informal Resolution: In the event of any dispute or claim arising out of these Terms, parties shall first endeavor in good faith to resolve the matter informally through written negotiation.
(c) Formal Proceedings: Where informal negotiations fail within thirty (30) days, the dispute shall be submitted to the exclusive jurisdiction of the competent courts of the Republic of Kenya.""",
    ),
    (
        "21. Contact Information and Complaints",
        """For notices, legal inquiries, data protection requests, or listing reporting complaints, please reach out to NyumbaLink Limited through our official support desk:

NyumbaLink Limited
Nairobi, Kenya
Email: support@nyumbalink.co.ke / legal@nyumbalink.co.ke""",
    ),
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
