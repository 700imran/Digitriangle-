from urllib.parse import quote
TO="info@gtckuwait.com"
# role -> (what to describe, documents to attach)
R={
"A/B Seaman":("your sea service on vessels and boats, watchkeeping and deck duties","seaman's book, STCW / safety certificates and sea-service record"),
"Accountant":("your experience in bookkeeping, reconciliations, month-end close and reporting","degree or professional certificate (e.g. CPA/ACCA if held) and accounting software skills"),
"Administrative Assistant":("your experience in office administration, scheduling, filing and correspondence","education certificates and a note of your Arabic/English skills"),
"Architect":("the building types you have designed, your drawing and BIM/CAD tools, and site coordination experience","architecture degree, portfolio and professional registration (if held)"),
"Agriculturist":("your experience in crop or landscape management, irrigation and plant health in arid conditions","agriculture degree or diploma and any project references"),
"Auto Technician":("your experience diagnosing and repairing light and heavy vehicles","trade certificates, brands/systems worked on and driving licence"),
"Boat Mechanic":("your experience servicing marine engines, outboards and boat systems","trade or marine engineering certificates and engine makes worked on"),
"Camp Supervisor":("your experience running remote camps: accommodation, housekeeping, catering coordination and staff supervision","supervisory certificates, camp/site references and number of staff led"),
"Chemical Engineer":("your process, plant or lab experience and the standards and software you work with","engineering degree, professional registration (if held) and project list"),
"Chemist":("your laboratory experience, analytical methods and instruments you operate","chemistry degree, lab certifications and list of methods/standards used"),
"Civil Engineer":("the projects you have delivered, site supervision experience and codes you work to","engineering degree, KSE or other registration (if held) and project list"),
"Clerk":("your experience in data entry, filing, record keeping and basic office software","education certificates and typing/computer skills"),
"Customer Service Officer":("your experience handling client enquiries, complaints and follow-up in person, by phone and by email","education certificates and languages spoken"),
"Diesel Mechanic":("your experience overhauling and repairing diesel engines, generators and heavy equipment","trade certificates and equipment/engine makes worked on"),
"Electrician":("your experience in wiring, installation, fault-finding and maintenance, and the voltages you work with","trade certificates, electrical licence (if held) and project references"),
"Electrical Engineer":("your design, installation or maintenance experience and the standards and software you work with","engineering degree, professional registration (if held) and project list"),
"Finance Manager":("your experience leading budgeting, financial reporting, controls and a finance team","professional qualification (e.g. CPA/ACCA/CMA), ERP experience and leadership scope"),
"Heavy Duty Driver":("your experience driving heavy trucks and trailers, including long-distance and site work","valid heavy-vehicle driving licence and clean driving record"),
"Heavy Equipment Operator":("the equipment you operate (excavator, loader, crane, etc.) and your site experience","operator licences/certificates and equipment list"),
"HSE Engineer":("your experience in site safety audits, risk assessment, incident investigation and HSE training","HSE certifications (e.g. NEBOSH/IOSH), engineering degree and project list"),
"Industrial Engineer":("your experience in process improvement, planning, productivity and operations analysis","engineering degree, Lean/Six Sigma certificates (if held) and project examples"),
"Information Technologist (I.T)":("your experience in networks, systems support, security and user helpdesk","IT degree or certifications (e.g. CCNA, Microsoft) and tools/platforms managed"),
"Laundry Supervisor":("your experience supervising commercial laundry operations, hygiene standards and staff scheduling","supervisory references and equipment/process experience"),
"Lawyer":("your areas of practice, Kuwait/GCC legal experience and contract or corporate work","law degree, bar registration (if held) and languages of practice"),
"Maintenance Fitter":("your experience in mechanical fitting, preventive maintenance and breakdown repairs","trade certificates and equipment types maintained"),
"Marketing Officer":("your experience in campaigns, digital and social media, events and brand material","degree, portfolio or campaign results and tools you use"),
"Mechanical Engineer":("your design, installation or maintenance experience (HVAC, plant, equipment) and the standards you work to","engineering degree, professional registration (if held) and project list"),
"Nurse":("your clinical experience, ward or care settings and patient-care specialisms","nursing degree/diploma, nursing licence and MOH or equivalent registration"),
"Operations Coordinator":("your experience coordinating teams, schedules, suppliers and daily operations reporting","education certificates and examples of operations you coordinated"),
"Orderly":("your experience supporting patients, hospital or care-facility hygiene and patient transport","relevant training certificates and care-setting references"),
"Painter":("your experience in interior and exterior painting, surface preparation and finishing","trade certificates and project/site references"),
"Pharmacist":("your experience in dispensing, medication safety and pharmacy operations","pharmacy degree, licence and MOH or equivalent registration"),
"Procurement Officer":("your experience in sourcing, vendor negotiation, purchase orders and supplier follow-up","education certificates, ERP/procurement tools and categories you have bought"),
"Public Relations Officer":("your experience with government transactions, visas, licences and liaison with ministries","Civil ID copy (if in Kuwait), education certificates and Arabic/English skills"),
"Quality Control Officer":("your experience in inspections, quality audits, food-safety or ISO systems","quality/ISO/HACCP certificates and sectors audited"),
"Safety Officer":("your experience in site safety, inspections, toolbox talks and incident reporting","safety certifications (e.g. NEBOSH/IOSH/OSHA) and site references"),
"Sales Associate":("your experience in selling, client relationships and meeting targets","education certificates and sales results/references"),
"Security Officer":("your experience in guarding, access control, patrols and incident reporting","security training certificates, police clearance (if available) and references"),
"Teacher":("the subjects and age groups you teach, curriculum experience and classroom results","teaching degree/licence, subject certificates and references"),
"Translator":("your language pairs, subject areas and translation/interpretation experience","degree or translation certificates and 1-2 work samples"),
"Welder":("the welding processes you hold (MIG, TIG, arc), positions and materials you weld","welding certificates (e.g. 6G/AWS or equivalent) and project references"),
}
EXTRA={
"Engineering":"Willing to work on site / shift basis: [Yes / No]",
"Corporate":"Expected salary (KWD): [amount]",
"Field & Care":"Willing to work on site / camp / shift basis: [Yes / No]",
}
def apply_href(role,category):
    what,docs=R[role]
    subj=f"Application: {role} - [Your Full Name]"
    body=f"""Dear GTC Human Capital Team,

I would like to apply for the position of {role} ({category}, Kuwait) listed on your careers page.

Key experience for this role - please describe {what}:
[Write 2-3 lines here]

My details:
Full name: [Your name]
Nationality: [Nationality]
Current location: [City, Country]
Phone / WhatsApp: [Number]
Years of experience as {role}: [Years]
Current or last employer: [Company]
Notice period / available from: [Date]
Civil ID / transferable residency (if in Kuwait): [Yes / No]
{EXTRA[category]}

Attached: my CV, plus {docs}.

Thank you for your time. I would welcome the chance to discuss how I can contribute to GTC.

Kind regards,
[Your name]
"""
    return f"mailto:{TO}?subject={quote(subj)}&body={quote(body.replace(chr(10),chr(13)+chr(10)))}"
