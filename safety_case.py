import datetime

class AISafetyCase:
    def __init__(self, organization_name, website=None):
        self.organization_name = organization_name
        self.website = website
        self.sms_document = None
        self.incident_history = []
        self.hazards = []
        self.contractor_management = None
        self.global_warming_impacts = []

    def provide_sms(self):
        """Prompt user to enter SMS details interactively."""
        self.sms_document = input("Enter a brief summary of your Safety Management System (SMS): ")

    def add_incident(self):
        """Prompt user to enter incident details."""
        description = input("Describe a past incident: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        impact = input("Describe the impact: ")

        # Validate date format
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")
            return

        self.incident_history.append({"description": description, "date": date, "impact": impact})

    def add_hazard(self):
        """Prompt user to enter hazard details."""
        hazard_name = input("Enter the name of the hazard: ")
        potential_risk = input("Describe the potential risk: ")
        existing_control = input("What control measures are in place?: ")

        self.hazards.append({"hazard": hazard_name, "risk": potential_risk, "control": existing_control})

    def set_contractor_management(self):
        """Prompt user to describe contractor safety policy."""
        self.contractor_management = input("Describe your contractor safety policies: ")

    def add_global_warming_factor(self):
        """Prompt user to enter climate-related risks."""
        factor = input("Enter a climate-related risk (e.g., extreme heat, flooding): ")
        impact = input("Describe its impact on operations: ")

        self.global_warming_impacts.append({"factor": factor, "impact": impact})

    def generate_safety_case(self):
        """Compile and return the safety case report."""
        if not self.sms_document:
            return "Error: SMS document required for analysis."

        safety_case = f"Safety Case for {self.organization_name}\n\n"
        safety_case += "1. Organization Overview:\n" + (self.website if self.website else "No website provided") + "\n\n"
        safety_case += "2. Safety Management System (SMS) Overview:\n" + str(self.sms_document) + "\n\n"

        if self.incident_history:
            safety_case += "3. Past Incident Analysis:\n"
            for incident in self.incident_history:
                safety_case += f" - {incident['date']}: {incident['description']} (Impact: {incident['impact']})\n"
        else:
            safety_case += "3. No past incidents recorded.\n\n"

        if self.hazards:
            safety_case += "4. Identified Hazards and Controls:\n"
            for hazard in self.hazards:
                safety_case += f" - {hazard['hazard']}: {hazard['risk']} (Control: {hazard['control']})\n"
        else:
            safety_case += "4. No hazards documented.\n\n"

        if self.contractor_management:
            safety_case += f"5. Contractor Management Approach:\n {self.contractor_management}\n\n"
        else:
            safety_case += "5. No contractor management policy provided.\n\n"

        if self.global_warming_impacts:
            safety_case += "6. Global Warming Considerations:\n"
            for impact in self.global_warming_impacts:
                safety_case += f" - {impact['factor']}: {impact['impact']}\n"
        else:
            safety_case += "6. No climate-related hazard impacts documented.\n\n"

        safety_case += "7. AI Recommendations:\n" + \
            "- AI suggests reviewing hazard control measures for improvements.\n" + \
            "- Consider additional contractor risk management strategies.\n" + \
            "- AI advises monitoring extreme weather risks as part of future safety planning.\n"

        return safety_case

    def save_to_file(self, filename="safety_case_report.txt"):
        """Save the generated safety case to a text file."""
        report = self.generate_safety_case()
        with open(filename, "w") as file:
            file.write(report)
        print(f"\n✅ Safety case saved as {filename}")


# Example Usage
if __name__ == "__main__":
    company_name = input("Enter your company name: ")
    website = input("Enter your company website (or leave blank if none): ")

    organization = AISafetyCase(company_name, website)

    # Collecting Safety Case Data
    organization.provide_sms()

    add_more_incidents = True
    while add_more_incidents:
        organization.add_incident()
        add_more_incidents = input("Would you like to add another incident? (yes/no): ").strip().lower() == "yes"

    add_more_hazards = True
    while add_more_hazards:
        organization.add_hazard()
        add_more_hazards = input("Would you like to add another hazard? (yes/no): ").strip().lower() == "yes"

    organization.set_contractor_management()
    
    add_more_global_warming = True
    while add_more_global_warming:
        organization.add_global_warming_factor()
        add_more_global_warming = input("Would you like to add another global warming risk? (yes/no): ").strip().lower() == "yes"

    # Generating and Saving the Safety Case Report
    print("\n📄 Generating Safety Case Report...\n")
    print(organization.generate_safety_case())
    organization.save_to_file()
