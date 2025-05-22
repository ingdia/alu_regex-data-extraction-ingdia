import re

class PatternTypes:
    """This class contains different regex patterns for certain data."""
    def __init__(self):
        # Email pattern
        self.email_typ = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        # Phone number pattern
        self.phone_typ = r'(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]?\d{4}'
        # Hashtag pattern
        self.hashtag_typ = r'#[a-zA-Z0-9_]+'
        # HTML tag pattern
        self.htmltag_typ = import re

class PatternTypes:
    """This class contains different regex patterns for certain data."""
    def __init__(self):
        # Email pattern
        self.email_typ = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        # Phone number pattern
        self.phone_typ = r'(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]?\d{4}'
        # Hashtag pattern
        self.hashtag_typ = r'#[a-zA-Z0-9_]+'
        # HTML tag pattern
        self.htmltag_typ = r'<[^>]+>'
        # Currency (USD) pattern
        self.currency_typ = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'


class Extractor:
    """This class extracts data using regular expressions."""
    def __init__(self):
        self.patterns = PatternTypes()
    # function to extract email
    def emails_extractor(self, text):
        return re.findall(self.patterns.email_typ, text)
    # function to extract phone number
    def phone_extractor(self, text):
        return re.findall(self.patterns.phone_typ, text)
    # function to extract  hashtag
    def hashtag_extractor(self, text):
        return re.findall(self.patterns.hashtag_typ, text)
    # function to extract html tags 
    def htmltag_extractor(self, text):
        return re.findall(self.patterns.htmltag_typ, text)
    # function to extract  currency 
    def currency_extractor(self, text):
        return re.findall(self.patterns.currency_typ, text)
    # function to keep them together
    def extract_all(self, text):
        """Extract all data types from the sample text."""
        return {
            "Emails": self.emails_extractor(text),
            "Phone Numbers": self.phone_extractor(text),
            "Hashtags": self.hashtag_extractor(text),
            "HTML Tags": self.htmltag_extractor(text),
            "Currency Amounts": self.currency_extractor(text)
        }

# display function that help to have an user friendly format
def display_results(results):
    print("Here are the extracted results:")
    for key, values in results.items():
        print(f"\n{key}:")
        if values:
            for value in values:
                print(f"  {value}")
        else:
            print("  (none)")


def main():
    # Sample text
    my_sample_text = """
    Contact us at user@example.com or firstname.lastname@company.co.uk
    Here is our phone number: (123) 456-7890 or 123-456-7890 or 123.456.7890
    Use #ThisIsAHashtag and #happyshop for social media.
    Here's a tag: <h1 class='main'>Welcome to Our website</h1></br>
    Products being sold at $19.99 or premium packages for $1,234.56
    """
    # instant of a class Extractor
    my_extractor = Extractor()
    results = my_extractor.extract_all(my_sample_text)
    display_results(results)


if __name__ == "__main__":
    main()

        # Currency (USD) pattern
        self.currency_typ = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'


class Extractor:
    """This class extracts data using regular expressions."""
    def __init__(self):
        self.patterns = PatternTypes()
    # function to extract email
    def emails_extractor(self, text):
        return re.findall(self.patterns.email_typ, text)
    # function to extract phone number
    def phone_extractor(self, text):
        return re.findall(self.patterns.phone_typ, text)
    # function to extract  hashtag
    def hashtag_extractor(self, text):
        return re.findall(self.patterns.hashtag_typ, text)
    # function to extract html tags 
    def htmltag_extractor(self, text):
        return re.findall(self.patterns.htmltag_typ, text)
    # function to extract  currency 
    def currency_extractor(self, text):
        return re.findall(self.patterns.currency_typ, text)
    # function to keep them together
    def extract_all(self, text):
        """Extract all data types from the sample text."""
        return {
            "Emails": self.emails_extractor(text),
            "Phone Numbers": self.phone_extractor(text),
            "Hashtags": self.hashtag_extractor(text),
            "HTML Tags": self.htmltag_extractor(text),
            "Currency Amounts": self.currency_extractor(text)
        }

# display function that help to have an user friendly format
def display_results(results):
    print("Here are the extracted results:")
    for key, values in results.items():
        print(f"\n{key}:")
        if values:
            for value in values:
                print(f"  {value}")
        else:
            print("  (none)")


def main():
    # Sample text
    my_sample_text = """
    Contact us at user@example.com or firstname.lastname@company.co.uk
    Here is our phone number: (123) 456-7890 or 123-456-7890 or 123.456.7890
    Use #ThisIsAHashtag and #happyshop for social media.
    Here's a tag: <h1 class='main'>Welcome to Our website</h1></br>
    Products being sold at $19.99 or premium packages for $1,234.56
    """
    # instant of a class Extractor
    my_extractor = Extractor()
    results = my_extractor.extract_all(my_sample_text)
    display_results(results)


if __name__ == "__main__":
    main()
