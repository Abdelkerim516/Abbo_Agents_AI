class EmailReaderTool:
    """
    Fake email reader for prototype.
    Replace with real IMAP/Office API later.
    """
    def read_email(self, text):
        return f"Email content captured: {text}"
