function googleTranslateElementInit() {
    new google.translate.TranslateElement({
        pageLanguage: 'en',
        includedLanguages: 'en,es,fr,de,hi,ml',
    }, 'google_translate_element');

    // Listen for language change events
    google.translate.addEventListener('pageLanguageChanged', function (e) {
        const selectedLanguage = e.target.getAttribute('select');
        // You can trigger translation of your content here
        // For this example, we'll just update the page language attribute
        document.documentElement.lang = selectedLanguage;
    });
}