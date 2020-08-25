// STRIPE - Accept one-time payments

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: "#000",
        fontFamily: 'Ubuntu Condensed, sans-serif',
        fontSmoothing: "antialiased",
        "::placeholder": {
            color: "#aab7c4"
        }
    },
    invalid: {
        fontFamily: 'Ubuntu Condensed, sans-serif',
        color: "#b71c1c",
        iconColor: "#b71c1c"
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.on("change", function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span role="alert">
                <i class="material-icons left">error</i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Stripe Javascript to confirm credit card payment on form submit

var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    // First disable card and submit button to avoid multiple form submits
    card.update({ 'disabled': true });
    $('#checkout-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            // Show error to your customer (e.g., insufficient funds)
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span role="alert">
                    <i class="material-icons left">error</i>
                </span>
                <span>${result.error.message}</span>
            `;
            $(errorDiv).html(html);
            // Enable form submit button for customer to correct mistakes
            card.update({ 'disabled': false });
            $('#submit-button').attr('disabled', false);
        } else {
            // The payment has been processed!
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});