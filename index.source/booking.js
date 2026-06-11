document.addEventListener('DOMContentLoaded', () => {
    const timeSlots = document.querySelectorAll('td.available');
    const messageDiv = document.getElementById('message');
    const bookingModal = document.getElementById('bookingModal');
    const closeButton = document.querySelector('.close-button');
    const bookingForm = document.getElementById('bookingForm');
    const modalDaySpan = document.getElementById('modalDay');
    const modalTimeSpan = document.getElementById('modalTime');
    const emailInput = document.getElementById('email');
    const serviceInput = document.getElementById('service');

    let currentSelectedSlot = null; // Speichert den aktuell ausgewählten Slot

    timeSlots.forEach(slot => {
        slot.addEventListener('click', (event) => {
            const clickedSlot = event.currentTarget;
            
            if (clickedSlot.classList.contains('available')) {
                const time = clickedSlot.dataset.time;
                const day = clickedSlot.dataset.day;

                // Informationen im Modal anzeigen
                modalDaySpan.textContent = day;
                modalTimeSpan.textContent = time;
                emailInput.value = ''; // E-Mail-Feld leeren
                serviceInput.value = ''; // Leistungs-Feld leeren
                currentSelectedSlot = clickedSlot; // Den Slot speichern

                // Modal anzeigen
                bookingModal.classList.add('show-modal');
            } else if (clickedSlot.classList.contains('booked')) {
                showMessage('Dieser Termin ist bereits gebucht.', 'error');
            }
        });
    });

    // Modal schließen, wenn der Schließen-Button geklickt wird
    closeButton.addEventListener('click', () => {
        bookingModal.classList.remove('show-modal');
    });

    // Modal schließen, wenn außerhalb des Modal-Inhalts geklickt wird
    window.addEventListener('click', (event) => {
        if (event.target === bookingModal) {
            bookingModal.classList.remove('show-modal');
        }
    });

    // Formular abschicken
    bookingForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Standard-Formularversand verhindern

        const email = emailInput.value;
        const time = modalTimeSpan.textContent;
        const day = modalDaySpan.textContent;
        const service = serviceInput.value;

        if (email && service && currentSelectedSlot) {
            // Hier würde die eigentliche Buchungslogik an ein Backend gesendet werden
            // In diesem Beispiel simulieren wir die Buchung
            
            // "Buchen" des Slots im Timetable
            currentSelectedSlot.classList.remove('available');
            currentSelectedSlot.classList.add('booked');
            currentSelectedSlot.textContent = 'Gebucht';
            currentSelectedSlot.style.cursor = 'not-allowed';

            // Modal schließen
            bookingModal.classList.remove('show-modal');

            // Erfolgsmeldung anzeigen
            showMessage(`Ihr Termin für ${service} am ${day} um ${time} Uhr wurde erfolgreich gebucht. Eine Bestätigung geht an ${email}.`, 'success');

            currentSelectedSlot = null; // Referenz zurücksetzen
        } else {
            showMessage('Bitte geben Sie eine gültige E-Mail-Adresse ein und wählen Sie eine Leistung aus.', 'error');
        }
    });


    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = ''; 
        messageDiv.classList.add('show');

        if (type === 'success') {
            messageDiv.style.backgroundColor = '#dff0d8';
            messageDiv.style.color = '#3c763d';
            messageDiv.style.border = '1px solid #d6e9c6';
        } else if (type === 'error') {
            messageDiv.style.backgroundColor = '#f2dede';
            messageDiv.style.color = '#a94442';
            messageDiv.style.border = '1px solid #ebccd1';
        }

        setTimeout(() => {
            messageDiv.classList.remove('show');
        }, 5000);
    }
});